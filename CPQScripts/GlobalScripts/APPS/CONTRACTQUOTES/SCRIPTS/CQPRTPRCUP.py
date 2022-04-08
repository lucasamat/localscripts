# =========================================================================================================================================
#   __script_name : CQPRTPRCUP.py
#   __script_description : THIS SCRIPT IS USED FOR CPS PART PRICING 
#   __primary_author__ : 
#   __create_date :23-10-2020
#   © BOSTON HARBOR TECHNOLOGY LLC - ALL RIGHTS RESERVED
## ==========================================================================================================================================
import Webcom.Configurator.Scripting.Test.TestProduct
import clr
#clr.AddReference("System.Net")
clr.AddReference("IronPython")
clr.AddReference("Microsoft.Scripting")
from System.Net import WebRequest
from System.Net import HttpWebResponse
from Microsoft.Scripting import SourceCodeKind
from IronPython.Hosting import Python
from IronPython import Compiler
#import Webcom.Configurator.Scripting.Test.TestProduct
import System.Net
import sys
import datetime
from System.Text.Encoding import UTF8
from System import Convert
from SYDATABASE import SQL
import time
import datetime 
import re


Sql = SQL()
QUOTE = Param.CPQ_Columns['Entries']
revision = Param.CPQ_Columns['Revision']
script_start_time = time.time()
# Log.Info("QUOTE ID---> "+str(QUOTE)+"CPS Price Script Started")
# Log.Info("------->CPI Hitting  2021")
webclient = System.Net.WebClient()
webclient.Headers[System.Net.HttpRequestHeader.ContentType] = "application/json"
webclient.Headers[System.Net.HttpRequestHeader.Authorization] = "Basic c2ItYzQwYThiMWYtYzU5NS00ZWJjLTkyYzYtYzM4ODg4ODFmMTY0IWIyNTAzfGNwc2VydmljZXMtc2VjdXJlZCFiMzkxOm9zRzgvSC9hOGtkcHVHNzl1L2JVYTJ0V0FiMD0=";
response = webclient.DownloadString("https://cpqprojdevamat.authentication.us10.hana.ondemand.com:443/oauth/token?grant_type=client_credentials")
response = eval(response)
Request_URL="https://cpservices-pricing.cfapps.us10.hana.ondemand.com/api/v1/statelesspricing"
webclient.Headers[System.Net.HttpRequestHeader.Authorization] ="Bearer "+str(response['access_token'])

# Log.Info("654 response['access_token'] --->"+str(response['access_token']))
# Log.Info("revision_CUP==>"+str(revision))
Log.Info("QUOTE_CUP==>"+str(QUOTE))

x = datetime.datetime.today()
x= str(x)
y = x.split(" ")
#partids = []
all_count = 0
loop_count = 0
#GET PRICING PROCEDURE
contract_quote_record_id = None
account_info={}
taxk1=''
pricingPro={'ZZCQAP':'ZC07','ZZCQNA':'M','ZZCQEU':'M','ZZCQEU-KONDA':'75','ZZCQNA-KONDA':'75','ZZCQAP-KONDA':'S4'}


SAQTIP_INFO = SqlHelper.GetList(""" SELECT CPQ_PARTNER_FUNCTION, PARTY_ID FROM SAQTIP (NOLOCK) WHERE QUOTE_ID='{}' AND QTEREV_RECORD_ID='{}' AND CPQ_PARTNER_FUNCTION IN ('SOLD TO','SHIP TO') """.format(QUOTE,revision))
for keyobj in SAQTIP_INFO:
	account_info[keyobj.CPQ_PARTNER_FUNCTION] = keyobj.PARTY_ID

GetPricingProcedure = Sql.GetFirst("SELECT DIVISION_ID, DISTRIBUTIONCHANNEL_ID, SALESORG_ID, DOC_CURRENCY,COUNTRY, PRICINGPROCEDURE_ID, QUOTE_RECORD_ID,EXCHANGE_RATE_TYPE, GLOBAL_CURRENCY, ACCTAXCLA_ID, PAYMENTTERM_ID, INCOTERM_ID, COMPANY_ID, DOCTYP_ID,CONTRACT_VALID_FROM FROM SAQTRV (NOLOCK) WHERE QUOTE_ID = '{}' AND QTEREV_RECORD_ID='{}' ".format(QUOTE,revision))
if GetPricingProcedure is not None:
	Trace.Write('inside----'+str(GetPricingProcedure))
	PricingProcedure = GetPricingProcedure.PRICINGPROCEDURE_ID
	curr = GetPricingProcedure.DOC_CURRENCY
	glb_curr =  GetPricingProcedure.GLOBAL_CURRENCY
	dis = GetPricingProcedure.DISTRIBUTIONCHANNEL_ID
	salesorg = GetPricingProcedure.SALESORG_ID
	div = GetPricingProcedure.DIVISION_ID
	exch = GetPricingProcedure.EXCHANGE_RATE_TYPE
	contract_quote_record_id = GetPricingProcedure.QUOTE_RECORD_ID
	country=GetPricingProcedure.COUNTRY
	taxk1 = GetPricingProcedure.ACCTAXCLA_ID
	payterm_id = GetPricingProcedure.PAYMENTTERM_ID
	incoterm_id = GetPricingProcedure.INCOTERM_ID
	company_id = GetPricingProcedure.COMPANY_ID
	doctype_id=GetPricingProcedure.DOCTYP_ID
	contract_valid_from = GetPricingProcedure.CONTRACT_VALID_FROM
	cv=str(contract_valid_from)
	(cm,cd,cy)=re.sub(r'\s+([^>]*?)$','',cv).split('/')
	cd = '0'+str(cd) if len(cd)==1 else cd
	cm = '0'+str(cm) if len(cm)==1 else cm        
	cvf = cy+cm+cd
	cvf_1 = cy+'-'+cm+'-'+cd 		
	#taxk1 = GetPricingProcedure.CUSTAXCLA_ID
	#taxk1 = "1"
account_info['docCurrency']= '{"name":"KOMK-WAERK","values":["'+str(curr)+'"]}'
account_info['globalCurrency']= '{"name":"KOMK-HWAER","values":["'+str(glb_curr)+'"]}'
#else:
#PricingProcedure = 'ZZCQAP'
#curr = 'USD'
#dis = '01'
#salesorg = '2034'
if doctype_id=='ZWK1':
	div = '56'

#GET ISOCODE 
ISOCode={}
getIsocode=SqlHelper.GetList("""SELECT DISTINCT UOM, UOM_ISO_CODE FROM MAMUOM (NOLOCK)""")
for code in getIsocode:
	ISOCode[code.UOM]=code.UOM_ISO_CODE

#UPDATE PRICING PROCEDURE TO SAQITM
getPricingProc=SqlHelper.GetFirst("""SELECT PRICINGPROCEDURE_ID FROM SASAPP (NOLOCK) WHERE DISTRIBUTIONCHANNEL_ID='{}' AND DIVISION_ID='{}' AND SALESORG_ID='{}'""".format(dis,div,salesorg))
if getPricingProc:
	PricingProcedure = getPricingProc.PRICINGPROCEDURE_ID
	if exch == '':
		exch = pricingPro[PricingProcedure]
		update_SAQTRV = "UPDATE SAQTRV  SET PRICINGPROCEDURE_ID = '{prc}', EXCHANGE_RATE_TYPE = '{EXCH}' WHERE SAQTRV.QUOTE_ID = '{quote}'".format(prc=str(PricingProcedure),EXCH=str(exch), quote=QUOTE)
		Sql.RunQuery(update_SAQTRV)
# update_SAQITM = "UPDATE SAQITM SET PRICINGPROCEDURE_ID = '{prc}' WHERE SAQITM.QUOTE_ID = '{quote}' AND SAQITM.QTEREV_RECORD_ID='{revision_rec_id}'".format(prc=str(PricingProcedure), quote=QUOTE, revision_rec_id = revision)
# Sql.RunQuery(update_SAQITM)
update_SAQIFP = "UPDATE SAQIFP SET PRICINGPROCEDURE_ID = '{prc}', TAX_PERCENTAGE = '{tax}' WHERE SAQIFP.QUOTE_ID = '{quote}'".format(prc=str(PricingProcedure),tax=str(taxk1), quote=QUOTE)
Sql.RunQuery(update_SAQIFP)

price_listtype=''
price_groupid=''

price_list = SqlHelper.GetFirst("SELECT  PRICEGROUP_ID, PRICELIST_ID FROM  SASAAC (NOLOCK) WHERE  SALESORG_ID ='"+str(salesorg)+"'AND ACCOUNT_ID='"+str(account_info['SOLD TO'])+"' AND DIVISION_ID ='"+str(div)+"'   AND DISTRIBUTIONCHANNEL_ID ='"+str(dis)+"'")

if price_list:
	price_listtype=price_list.PRICELIST_ID
	price_groupid=price_list.PRICEGROUP_ID


#currency_attribute = account_info['docCurrency']+','+account_info['globalCurrency']+','+'{"name":"KOMK-KONDA","values":["'+str(pricingPro[PricingProcedure+'-KONDA'])+'"]}'
currency_attribute = account_info['docCurrency']+','+account_info['globalCurrency']+','+'{"name":"KOMK-KONDA","values":["'+str(price_groupid)+'"]}'

today = datetime.datetime.now()
Modi_date = today.strftime("%m/%d/%Y %H:%M:%S %p")


start = 1
end = 25
L = 1

# Taxm1Qurey=Sql.GetFirst("SELECT ISNULL(SRVTAXCLA_ID,1) as SRVTAXCLA_ID FROM SAQITM (NOLOCK) WHERE QUOTE_ID ='{quote}' AND QTEREV_RECORD_ID='{revision_rec_id}'".format(quote=QUOTE, revision_rec_id = revision))
part_query = ""
ancillary_part_query =""
fpm_part_query =""
part_query = SqlHelper.GetList("SELECT DISTINCT PART_NUMBER, ANNUAL_QUANTITY FROM (SELECT PART_NUMBER, ANNUAL_QUANTITY,ROW_NUMBER() OVER(ORDER BY PART_NUMBER) AS SNO FROM SAQIFP (NOLOCK) WHERE QUOTE_ID = '"+str(QUOTE)+"' AND QTEREV_RECORD_ID = '"+str(revision)+"' AND PRICING_STATUS = 'ACQUIRING...' )A WHERE SNO>="+str(start)+" AND SNO<="+str(end)+"  ")
if not part_query:
	ancillary_part_query = Sql.GetFirst("SELECT DISTINCT PART_NUMBER, QUANTITY as ANNUAL_QUANTITY FROM (SELECT PART_NUMBER, QUANTITY,ROW_NUMBER() OVER(ORDER BY PART_NUMBER) AS SNO FROM SAQRSP (NOLOCK) WHERE QUOTE_ID = '"+str(QUOTE)+"' AND QTEREV_RECORD_ID = '"+str(revision)+"' AND INCLUDED =1 AND SERVICE_ID IN('Z0100','Z0101') AND QUANTITY >0 )A WHERE SNO>="+str(start)+" AND SNO<="+str(end)+" ")
if not part_query:
	#Log.Info("Validate FPM QUERY")
	fpm_part_query = Sql.GetFirst("SELECT DISTINCT PART_NUMBER, CUSTOMER_ANNUAL_QUANTITY as ANNUAL_QUANTITY FROM (SELECT PART_NUMBER, CUSTOMER_ANNUAL_QUANTITY,ROW_NUMBER() OVER(ORDER BY PART_NUMBER) AS SNO FROM SAQSPT (NOLOCK) WHERE QUOTE_ID = '"+str(QUOTE)+"' AND QTEREV_RECORD_ID = '"+str(revision)+"' )A WHERE SNO>="+str(start)+" AND SNO<="+str(end)+" ")
if part_query or ancillary_part_query or fpm_part_query:

	while L == 1:
		itemid = ''
		if part_query:
			get_part_query = Sql.GetList("SELECT DISTINCT PART_NUMBER, ANNUAL_QUANTITY, ODCC_FLAG,SHPACCOUNT_ID,SALESUOM_ID,SALESUOM_CONVERSION_FACTOR FROM (SELECT PART_NUMBER, ANNUAL_QUANTITY,ODCC_FLAG,SHPACCOUNT_ID,SALESUOM_ID,SALESUOM_CONVERSION_FACTOR, ROW_NUMBER() OVER(ORDER BY PART_NUMBER) AS SNO FROM SAQIFP (NOLOCK) WHERE QUOTE_ID = '"+str(QUOTE)+"' AND QTEREV_RECORD_ID = '"+str(revision)+"' AND PRICING_STATUS = 'ACQUIRING...' )A WHERE SNO>="+str(start)+" AND SNO<="+str(end)+"  ")
		if ancillary_part_query:
			get_part_query = Sql.GetList("SELECT DISTINCT PART_NUMBER, QUANTITY as ANNUAL_QUANTITY,ODCC_FLAG,SHPACCOUNT_ID,SALESUOM_ID,SALESUOM_CONVERSION_FACTOR FROM (SELECT PART_NUMBER, QUANTITY,null as ODCC_FLAG, null as SHPACCOUNT_ID,null as SALESUOM_ID,null as SALESUOM_CONVERSION_FACTOR, ROW_NUMBER() OVER(ORDER BY PART_NUMBER) AS SNO FROM SAQRSP (NOLOCK) WHERE QUOTE_ID = '"+str(QUOTE)+"' AND QTEREV_RECORD_ID = '"+str(revision)+"' AND INCLUDED = 1 AND SERVICE_ID IN('Z0100','Z0101')  AND UNIT_PRICE IS NULL )A WHERE SNO>="+str(start)+" AND SNO<="+str(end)+"  ")
		if fpm_part_query:
			get_part_query = Sql.GetList("SELECT DISTINCT PART_NUMBER, CUSTOMER_ANNUAL_QUANTITY as ANNUAL_QUANTITY,ODCC_FLAG, SHPACCOUNT_ID,SALESUOM_ID,SALESUOM_CONVERSION_FACTOR FROM (SELECT PART_NUMBER, CUSTOMER_ANNUAL_QUANTITY,ODCC_FLAG,SHPACCOUNT_ID ,SALESUOM_ID,SALESUOM_CONVERSION_FACTOR,ROW_NUMBER() OVER(ORDER BY PART_NUMBER) AS SNO FROM SAQSPT (NOLOCK) WHERE QUOTE_ID = '"+str(QUOTE)+"' AND QTEREV_RECORD_ID = '"+str(revision)+"' )A WHERE SNO>="+str(start)+" AND SNO<="+str(end)+"  ")
		
		partids = quantity = li = []
		s = ""
		shipto_details= ""
		shipto = ""
		if get_part_query:      
			partids = [p.PART_NUMBER for p in get_part_query]
			quantity = [q.ANNUAL_QUANTITY for q in get_part_query]
			try:
				odcc_flag = [r.ODCC_FLAG for r in get_part_query]
				shipto = [s.SHPACCOUNT_ID for s in get_part_query]
				salesUOM = [t.SALESUOM_ID for t in get_part_query]
				salesUOMConv = [u.SALESUOM_CONVERSION_FACTOR for u in get_part_query]
				salesUOMConvs = int(salesUOMConv[0] or 1)
				shipto_details=shipto[0] or account_info['SHIP TO']
				str_odcc_flag = odcc_flag[0]
			except:
				odcc_flag = ['' for r in get_part_query] 
				str_odcc_flag =''
			start = start + 25
			end = end + 25
			requestdata = ''
			##for currencies in ('docCurrency','globalCurrency'):
			currencies='globalCurrency'
			if len(partids) == 1:
				#Log.Info("**Single-Partids**")
				if quantity[0] == 0 or quantity[0] == '':
					quantity[0]=1
				quantity[0] = int(quantity[0])
				curr_attr = currency_attribute
				if salesUOM[0] !='':
					salesUOM[0] ='EA'
				if salesUOM[0] !='':
					salesuom_attr = '"quantity":{"value":'+str(quantity[0])+',"unit":"'+str(ISOCode[salesUOM[0]])+'"},"exchRateType":"'+str(exch)+'","exchRateDate":"'+str(y[0])+'","productDetails":{"productId":"'+str(partids[0])+'","baseUnit":"EA","alternateProductUnits": [{"alternateUnitName": "'+str(ISOCode[salesUOM[0]])+'","numerator": "'+str(salesUOMConvs)+'","denominator": "1"}]}'
				if str_odcc_flag !='':
					curr_attr += ','+'{"name":"KOMP-ZZ_ODCC_ELIGIBILITY_FLAG","values":["'+str(str_odcc_flag)+'"]}'
				itemid = str(partids[0])+";"+str(QUOTE)+";"+str(quantity[0])+";"+str(currencies)
				item_string = '{"itemId":"'+str(itemid)+'","externalId":null,'+str(salesuom_attr)+',"attributes":[{"name":"KOMK-LAND1","values":["'+str(country)+'"]},{"name":"KOMP-KPOSN","values":["10"]},{"name":"KOMV-KSCHL","values":[""]},{"name":"KOMP-ZZEXE","values":[""]},{"name":"KOMP-KZNEP","values":[""]},{"name":"KOMK-KUNNR","values":["'+account_info['SOLD TO']+'"]},{"name":"KOMK-KUNWE","values":["'+str(shipto_details)+'"]},{"name":"KOMK-SPART","values":["56"]},{"name":"KOMP-SPART","values":["56"]},{"name":"KOMP-PMATN","values":["'+str(partids[0])+'"]},{"name":"KOMP-ZZPSTR_COUNTER","values":["1"]},{"name":"KOMK-ZZSPART","values":["'+str(div)+'"]},'+str(curr_attr)+',{"name":"KOMV-KDUPL","values":[""]},{"name":"KONV-KOAID","values":["A"]},{"name":"KOMP-ZZPRREASON","values":[""]},{"name":"KOMK-AUART","values":["ZQT1"]},{"name":"KOMP-PRSFD","values":["X"]},{"name":"KOMK-ZZWFSTATUS","values":[""]},{"name":"KOMP-UEPOS","values":["0000"]},{"name":"KOMP-FAREG","values":[""]},{"name":"KOMP-EVRWR","values":["X"]},{"name":"KOMK-KURST","values":["'+str(exch)+'"]},{"name":"KOMP-MGAME","values":["1.00"]},{"name":"KOMP-TAXM1","values":["1"]},{"name":"KOMK-TAXK1","values":["'+str(taxk1)+'"]},{"name":"KOMK-ZZKTOKD","values":["KUNA"]},{"name":"KOMK-BUKRS","values":["'+str(company_id)+'"]},{"name":"KOMV-KKURS","values":["1.00"]},{"name":"KONP-KNTYP","values":["L"]},{"name":"KOMK-ZTERM","values":["'+str(payterm_id)+'"]},{"name":"KOMK-INCO1","values":["'+str(incoterm_id)+'"]},{"name":"KOMK-AUART_SD","values":["ZQT1"]},{"name":"KOMK-ALAND","values":["'+str(country)+'"]},{"name":"KOMP-WERKS","values":["8639"]},{"name":"KOMP-MWSBP","values":["0.00"]},{"name":"KOMP-PRSOK","values":["X"]},{"name":"KOMP-PSTYV","values":["ZAGN"]},{"name":"KOMP-SKTOF","values":["X"]},{"name":"KOMK-PLTYP","values":["'+str(price_listtype)+'"]},{"name":"KOMP-ZZMTLSEGMCODE","values":["A01-000"]},{"name":"KOMP-KONDM","values":["N"]},{"name":"KOMV-KNTYP","values":["G"]},{"name":"KOMK-VTWEG","values":["'+str(dis)+'"]},{"name":"KOMP-BRTWR","values":["0.0"]},{"name":"KOMP-MGLME","values":["1.0"]},{"name":"KOMV-KPEIN","values":["1.0"]},{"name":"KOMK-FKART","values":[""]},{"name":"KOMK-ERDAT","values":["'+str(cvf)+'"]},{"name":"KOMV-KNUMV","values":[""]},{"name":"KOMK-VBTYP","values":["B"]},{"name":"KOMK-VKORG","values":["'+str(salesorg)+'"]}],"accessDateList":[{"name":"KOMK-PRSDT","value":"'+str(cvf_1)+'"},{"name":"KOMK-FBUDA","value":"'+str(cvf_1)+'"}],"variantConditions":[],"statistical":true,"subItems":[]}'
				li.append(item_string)
				s = ','.join(li)	
				requestdata = '<?xml version=\"1.0\" encoding=\"UTF-8\"?><soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\">  <soapenv:Body> <cpq_columns><root> {"docCurrency":"USD","locCurrency":"'+glb_curr+'","pricingProcedure":"'+PricingProcedure+'","groupCondition":false,"itemConditionsRequired":true,"items": ['+str(s)+']} </root> <CPSToken>'+str(response['access_token'])+'</CPSToken></cpq_columns> </soapenv:Body></soapenv:Envelope>'
			else:
				#Log.Info("**Multiple-Partids**")
				for index,val in enumerate(zip(partids,quantity,odcc_flag,shipto,salesUOM,salesUOMConv)):
					p=val[0]
					q=val[1]
					r=val[2]
					s=val[3] or account_info['SHIP TO']
					salesUOMs=val[4] or 'EA'
					salesUOMConvs=int(val[5] or 1)
					if q<=0 or q=='':
						q=1
					q=int(q)
					curr_attr2 = currency_attribute
					if salesUOMs !='':
						salesuom_attr = '"quantity":{"value":'+str(q)+',"unit":"'+str(ISOCode[salesUOMs])+'"},"exchRateType":"'+str(exch)+'","exchRateDate":"'+str(y[0])+'","productDetails":{"productId":"'+str(p)+'","baseUnit":"EA","alternateProductUnits": [{"alternateUnitName": "'+str(ISOCode[salesUOMs])+'","numerator": "'+str(salesUOMConvs)+'","denominator": 1}]}'
				
					if r in ('CCM','CCO','CUM','CUO'):
						curr_attr2 += ','+'{"name":"KOMP-ZZ_ODCC_ELIGIBILITY_FLAG","values":["'+str(r)+'"]}'
					itemid = str(p)+";"+str(QUOTE)+";"+str(q)+";"+str(currencies)
					item_string = '{"itemId":"'+str(itemid)+'","externalId":null,'+str(salesuom_attr)+',"attributes":[{"name":"KOMK-LAND1","values":["'+str(country)+'"]},{"name":"KOMP-KPOSN","values":["10"]},{"name":"KOMV-KSCHL","values":[""]},{"name":"KOMP-ZZEXE","values":[""]},{"name":"KOMP-KZNEP","values":[""]},{"name":"KOMK-KUNNR","values":["'+account_info['SOLD TO']+'"]},{"name":"KOMK-KUNWE","values":["'+str(s)+'"]},{"name":"KOMK-SPART","values":["56"]},{"name":"KOMP-SPART","values":["56"]},{"name":"KOMP-PMATN","values":["'+str(p)+'"]},{"name":"KOMP-ZZPSTR_COUNTER","values":["1"]},{"name":"KOMK-ZZSPART","values":["'+str(div)+'"]},'+str(curr_attr2)+',{"name":"KOMV-KDUPL","values":[""]},{"name":"KONV-KOAID","values":["A"]},{"name":"KOMP-ZZPRREASON","values":[""]},{"name":"KOMK-AUART","values":["ZQT1"]},{"name":"KOMP-PRSFD","values":["X"]},{"name":"KOMK-ZZWFSTATUS","values":[""]},{"name":"KOMP-UEPOS","values":["0000"]},{"name":"KOMP-FAREG","values":[""]},{"name":"KOMP-EVRWR","values":["X"]},{"name":"KOMK-KURST","values":["'+str(exch)+'"]},{"name":"KOMP-MGAME","values":["1.00"]},{"name":"KOMP-TAXM1","values":["1"]},{"name":"KOMK-TAXK1","values":["'+str(taxk1)+'"]},{"name":"KOMK-ZZKTOKD","values":["KUNA"]},{"name":"KOMK-BUKRS","values":["'+str(company_id)+'"]},{"name":"KOMV-KKURS","values":["1.00"]},{"name":"KONP-KNTYP","values":["L"]},{"name":"KOMK-ZTERM","values":["'+str(payterm_id)+'"]},{"name":"KOMK-INCO1","values":["'+str(incoterm_id)+'"]},{"name":"KOMK-AUART_SD","values":["ZQT1"]},{"name":"KOMK-ALAND","values":["'+str(country)+'"]},{"name":"KOMP-WERKS","values":["8639"]},{"name":"KOMP-MWSBP","values":["0.00"]},{"name":"KOMP-PRSOK","values":["X"]},{"name":"KOMP-PSTYV","values":["ZAGN"]},{"name":"KOMP-SKTOF","values":["X"]},{"name":"KOMK-PLTYP","values":["'+str(price_listtype)+'"]},{"name":"KOMP-ZZMTLSEGMCODE","values":["A01-000"]},{"name":"KOMP-KONDM","values":["N"]},{"name":"KOMV-KNTYP","values":["G"]},{"name":"KOMK-VTWEG","values":["'+str(dis)+'"]},{"name":"KOMP-BRTWR","values":["0.0"]},{"name":"KOMP-MGLME","values":["1.0"]},{"name":"KOMV-KPEIN","values":["1.0"]},{"name":"KOMK-FKART","values":[""]},{"name":"KOMK-ERDAT","values":["'+str(cvf)+'"]},{"name":"KOMV-KNUMV","values":[""]},{"name":"KOMK-VBTYP","values":["B"]},{"name":"KOMK-VKORG","values":["'+str(salesorg)+'"]}],"accessDateList":[{"name":"KOMK-PRSDT","value":"'+str(cvf_1)+'"},{"name":"KOMK-FBUDA","value":"'+str(cvf_1)+'"}],"variantConditions":[],"statistical":true,"subItems":[]}'
					li.append(item_string)
				s = ','.join(li)
				
				start_time = time.time()
				requestdata = '<?xml version=\"1.0\" encoding=\"UTF-8\"?><soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\">  <soapenv:Body> <cpq_columns><root>  {"docCurrency":"USD","locCurrency":"'+glb_curr+'","pricingProcedure":"'+PricingProcedure+'","groupCondition":false,"itemConditionsRequired":true,"items": ['+str(s)+']} </root> <CPSToken>'+str(response['access_token'])+'</CPSToken></cpq_columns> </soapenv:Body></soapenv:Envelope>'
			Log.Info("requestdata==>"+str(requestdata))
			#response1 = webclient.UploadString(Request_URL,str(requestdata))
				
			LOGIN_CREDENTIALS = SqlHelper.GetFirst("SELECT USER_NAME as Username,Password,Domain FROM SYCONF where Domain='AMAT_TST'")
			Login_Username = str(LOGIN_CREDENTIALS.Username)
			Login_Password = str(LOGIN_CREDENTIALS.Password)
			authorization = Login_Username + ":" + Login_Password
			binaryAuthorization = UTF8.GetBytes(authorization)
			authorization = Convert.ToBase64String(binaryAuthorization)
			authorization = "Basic " + authorization
			webclient = System.Net.WebClient()
			webclient.Headers[System.Net.HttpRequestHeader.ContentType] = "application/xml"
			webclient.Headers[System.Net.HttpRequestHeader.Authorization] = authorization
			#Log.Info("Looping Count ==> ")
			
			response1 = webclient.UploadString("https://e250404-iflmap.hcisbt.us3.hana.ondemand.com/cxf/CPQ_CPS",str(requestdata))
			Log.Info("response1data==>"+str(response1))
			end_time = time.time()
			#Log.Info("QUOTE ID---> "+str(QUOTE)+"loop---"+str(loop_count)+ "---time"+str(end_time - start_time))
		else:
			L=0
else:
	Log.Info('150----to call pricing here---quote table insert----')
	'''
	price = []
	#QUOTE = ''
	account_obj = Sql.GetFirst("SELECT ACCOUNT_ID FROM SAOPQT (NOLOCK) WHERE QUOTE_ID ='{QuoteRecordId}' ".format(QuoteRecordId=QUOTE,revision_rec_id = revision))
	stp_account_id = ""
	service_obj = Sql.GetFirst("SELECT SERVICE_ID FROM SAQTSE (NOLOCK) WHERE QUOTE_ID ='{QuoteRecordId}' AND QTEREV_RECORD_ID='{revision_rec_id}'".format(QuoteRecordId=QUOTE,revision_rec_id = revision))
	serviceId = ""
	if account_obj:
		stp_account_id = str(account_obj.ACCOUNT_ID)
	if service_obj:
		serviceId = str(service_obj.SERVICE_ID)
	salesorg_obj = Sql.GetFirst("SELECT DIVISION_ID, DISTRIBUTIONCHANNEL_ID, SALESORG_ID, DOC_CURRENCY, PRICINGPROCEDURE_ID,EXCHANGE_RATE_TYPE FROM SAQTRV (NOLOCK) WHERE QUOTE_ID ='{QuoteRecordId}' AND QTEREV_RECORD_ID='{revision_rec_id}'".format(QuoteRecordId=QUOTE,revision_rec_id = revision))
	item_string = ''
	if salesorg_obj:
		Trace.Write("serviceId--22--"+str(serviceId))			
		
		exchange_rate_type = salesorg_obj.EXCHANGE_RATE_TYPE if salesorg_obj.EXCHANGE_RATE_TYPE else 'M'
		pricing_procedure_id = salesorg_obj.PRICINGPROCEDURE_ID if salesorg_obj.PRICINGPROCEDURE_ID else 'ZZNA05'
		item_string = '{"itemId":"1","externalId":null,"quantity":{"value":'+str(1)+',"unit":"EA"},"exchRateType":"'+exchange_rate_type+'","exchRateDate":"'+str(y[0])+'","productDetails":{"productId":"'+str(serviceId)+'","baseUnit":"EA","alternateProductUnits":null},"attributes":[{"name":"KOMK-ALAND","values":["'+str(country)+'"]},{"name":"KOMK-REGIO","values":["TX"]},{"name":"KOMK-KUNNR","values":["'+stp_account_id+'"]},{"name":"KOMK-KUNWE","values":["'+stp_account_id+'"]},{"name":"KOMK-SPART","values":["'+str(salesorg_obj.DIVISION_ID)+'"]},{"name":"KOMP-SPART","values":["'+str(salesorg_obj.DIVISION_ID)+'"]},{"name":"KOMP-PMATN","values":["'+str(serviceId)+'"]},{"name":"KOMK-WAERK","values":["'+str(salesorg_obj.DOC_CURRENCY)+'"]},{"name":"KOMK-HWAER","values":["'+str(salesorg_obj.DOC_CURRENCY)+'"]},{"name":"KOMP-PRSFD","values":["X"]},{"name":"KOMK-VTWEG","values":["'+str(salesorg_obj.DISTRIBUTIONCHANNEL_ID)+'"]},{"name":"KOMK-VKORG","values":["'+str(salesorg_obj.SALESORG_ID)+'"]},{"name":"KOMP-KPOSN","values":["0"]},{"name":"KOMP-KZNEP","values":[""]},{"name":"KOMP-ZZEXE","values":["true"]}],"accessDateList":[{"name":"KOMK-PRSDT","value":"'+str(y[0])+'"},{"name":"KOMK-FBUDA","value":"'+str(y[0])+'"}],"variantConditions":[{"factor":1.0,"key":"AGS_LAB_OPT6"},{"factor":13.0,"key":"AGS_LAB_OPT8"}],"statistical":true,"subItems":[]}'

	requestdata = '{"docCurrency":"'+salesorg_obj.DOC_CURRENCY+'","locCurrency":"'+salesorg_obj.DOC_CURRENCY+'","pricingProcedure":"'+pricing_procedure_id+'","groupCondition":false,"itemConditionsRequired":true,"items": ['+item_string+']}'
	#Log.Info("requestdata--171---"+str(requestdata))
	response1 = webclient.UploadString(Request_URL,str(requestdata))
	#Log.Info("res--173-------"+str(response1))
	response1 = str(response1).replace(": true", ': "true"').replace(": false", ': "false"').replace(": null",': " None"')
	response1 = eval(response1)
	#Log.Info("res--176------"+str(response1))
	for root, value in response1.items():
		if root == "items":
			#Log.Info("6666 i[u] --->"+str(list(root1[inv])))
			price = value[:]			 
			break

	#Log.Info("type condition--->")
	#price = [price]
	#Log.Info("456789 type(price) --->"+str(type(price)))
	#for i in price[0]['conditions']:		
		#Itemidinfo = str(i["itemId"])
		#Log.Info("456 Itemidinfo --->"+str(Itemidinfo))
		#QUOTE = str(Itemidinfo[1])	
	contract_quote_record_id = None		
	getuomrec_val = ''
	getservicerecord = Sql.GetFirst("select QUOTE_RECORD_ID,QUOTE_NAME,SERVICE_DESCRIPTION,SERVICE_ID,	SERVICE_RECORD_ID from SAQTSE (NOLOCK) where QUOTE_ID = '{}' AND QTEREV_RECORD_ID='{}'".format(QUOTE,revision))
	#QuoteItemList = Quote.QuoteTables["SAQICD"]
	for cond_info in price[0]['conditions']:
		#Log.Info("333 cond_info['conditionType'] --->"+str(cond_info['conditionType']))
		getuomrec = Sql.GetFirst("select UOM_RECORD_ID from MAMTRL where UNIT_OF_MEASURE = '"+str(cond_info['conditionUnit'])+"'")
		if getuomrec:
			getuomrec_val = getuomrec.UOM_RECORD_ID
		else:
			getuomrec_val = 'EA'
		#Log.Info("query start") 
		#Log.Info("sp_executesql @T=N'INSERT QT__SAQICD (CONDITION_COUNTER,CONDITION_DATA_TYPE,CONDITION_RATE,CONDITION_TYPE,CONDITIONTYPE_NAME,CONDITIONTYPE_RECORD_ID,UOM,CONDITION_VALUE,UOM_RECORD_ID,LINE,QUOTE_ID,QTEITM_RECORD_ID,QUOTE_NAME,SERVICE_DESCRIPTION,SERVICE_ID,STEP_NUMBER,SERVICE_RECORD_ID,QUOTE_RECORD_ID,CONDITION_CURRENCY,CONDITION_BASE) values (''"+str(cond_info['conditionCounter'])+"'',''"+str(cond_info['calculationType'])+"'',''"+str(cond_info['conditionRate'].strip())+"'',''"+str(cond_info['conditionType'])+ "'',''"+ str(cond_info['conditionTypeDescription'].strip())+ "'' , ''"+ str(cond_info['conditionUnitValue'])+ "'',''"+ str(cond_info['conditionUnit'])+ "'',''"+ str(cond_info['conditionValue'])+ "'',''"+ str(getuomrec_val)+ "'','''',''"+ str(getservicerecord.QUOTE_RECORD_ID)+ "'','''',''"+ str(getservicerecord.QUOTE_NAME)+ "'',''"+ str(getservicerecord.SERVICE_DESCRIPTION)+ "'',''"+ str(getservicerecord.SERVICE_ID)+ "'',''"+ str(cond_info['stepNo'])+ "'',''"+ str(getservicerecord.SERVICE_RECORD_ID)+ "'',''"+ str(QUOTE)+ "'',''"+str(cond_info['conditionCurrency'])+"'',''"+str(cond_info['conditionBase'])+"'')'")
		
		saqicd_insert = SqlHelper.GetFirst("sp_executesql @T=N'INSERT QT__SAQICD (CONDITION_COUNTER,CONDITION_DATA_TYPE,CONDITION_RATE,CONDITION_TYPE,CONDITIONTYPE_NAME,CONDITIONTYPE_RECORD_ID,UOM,CONDITION_VALUE,UOM_RECORD_ID,LINE,QUOTE_ID,QTEITM_RECORD_ID,QUOTE_NAME,SERVICE_DESCRIPTION,SERVICE_ID,STEP_NUMBER,SERVICE_RECORD_ID,QUOTE_RECORD_ID,CONDITION_CURRENCY,CONDITION_BASE) values (''"+str(cond_info['conditionCounter'])+"'',''"+str(cond_info['calculationType'])+"'',''"+str(cond_info['conditionRate'].strip())+"'',''"+str(cond_info['conditionType'])+ "'',''"+ str(cond_info['conditionTypeDescription'].strip())+ "'' , ''"+ str(cond_info['conditionUnitValue'])+ "'',''"+ str(cond_info['conditionUnit'])+ "'',''"+ str(cond_info['conditionValue'])+ "'',''"+ str(getuomrec_val)+ "'','''',''"+ str(QUOTE)+ "'','''',''"+ str(getservicerecord.QUOTE_NAME)+ "'',''"+ str(getservicerecord.SERVICE_DESCRIPTION)+ "'',''"+ str(getservicerecord.SERVICE_ID)+ "'',''"+ str(cond_info['stepNo'])+ "'',''"+ str(getservicerecord.SERVICE_RECORD_ID)+ "'',''"+ str(getservicerecord.QUOTE_RECORD_ID)+ "'',''"+str(cond_info['conditionCurrency'])+"'',''"+str(cond_info['conditionBase'])+"'')'")
		newRow = QuoteItemList.AddNewRow()
		newRow['CONDITION_COUNTER'] = cond_info['conditionCounter']
		newRow['CONDITION_DATA_TYPE'] =  cond_info['conditionType']
		newRow['CONDITION_RATE'] = cond_info['conditionRate'].strip()
		newRow['CONDITION_TYPE'] = cond_info['conditionType']
		newRow['CONDITIONTYPE_NAME'] = cond_info['conditionTypeDescription'].strip()
		newRow['UOM'] =  cond_info['conditionUnit']
		newRow['CONDITIONTYPE_RECORD_ID'] = ''
		newRow['CONDITION_VALUE'] = cond_info['conditionValue']
		newRow['UOM_RECORD_ID'] = getuomrec.UOM_RECORD_ID
		newRow['LINE'] = ''
		newRow['QTEITM_RECORD_ID'] = ''
		newRow['QUOTE_NAME'] = getservicerecord.QUOTE_NAME
		newRow['SERVICE_DESCRIPTION'] = getservicerecord.SERVICE_DESCRIPTION
		newRow['SERVICE_ID'] = getservicerecord.SERVICE_ID
		newRow['STEP_NUMBER'] = cond_info['stepNo']
		newRow['SERVICE_RECORD_ID'] = getservicerecord.SERVICE_RECORD_ID
		newRow['QUOTE_RECORD_ID'] = contract_quote_record_id
		newRow['QUOTE_ID'] = QUOTE
		QuoteItemList.Save()'''		                
today = datetime.datetime.now()
Modi_date = today.strftime("%m/%d/%Y %H:%M:%S %p")