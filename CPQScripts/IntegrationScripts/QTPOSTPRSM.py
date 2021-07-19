# =========================================================================================================================================
#   __script_name : QTPOSTPRSM.PY
#   __script_description : THIS SCRIPT IS USED TO GET SSCM DATA FROM THE QTQCAS TABLE AND RETURN IN JSON FORMAT RESULT
#   __primary_author__ : SURESH MUNIYANDI, Baji
#   __create_date :
#   © BOSTON HARBOR TECHNOLOGY LLC - ALL RIGHTS RESERVED
# ==========================================================================================================================================
import sys
import clr
import System.Net
from System.Text.Encoding import UTF8
from System import Convert
from System.Net import HttpWebRequest, NetworkCredential
from System.Net import *
from System.Net import CookieContainer
from System.Net import Cookie
from System.Net import WebRequest
from System.Net import HttpWebResponse
from System import Uri
clr.AddReference("System.Net")
from System.Net import CookieContainer, NetworkCredential, Mail
from System.Net.Mail import SmtpClient, MailAddress, Attachment, MailMessage
import time


Qt_id = [str(param_result.Value) for param_result in Param.CPQ_Columns]
try:

	Qt_id = [str(param_result.Value) for param_result in Param.CPQ_Columns]

	Log.Info("QTPOSTPRSM Start ---->"+str(Qt_id))
	
	sessionid = SqlHelper.GetFirst("SELECT NEWID() AS A")
	timestamp_sessionid = "'" + str(sessionid.A) + "'"
	
	Flag = 'False'
	
	CRMQT = SqlHelper.GetFirst("select convert(varchar(100),c4c_quote_id) as c4c_quote_id from SAQTMT(nolock) WHERE QUOTE_ID = '"+str(Qt_id[0])+"' ")
	
	SAQSCO = "SAQSCO_BKP_1"+str(CRMQT.c4c_quote_id)
	SAQIEN = "SAQIEN_BKP_1"+str(CRMQT.c4c_quote_id)
	SAQSCA = "SAQSCA_BKP_1"+str(CRMQT.c4c_quote_id)
	SAQSAP = "SAQSAP_BKP_1"+str(CRMQT.c4c_quote_id)
	
	SAQSCO_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSCO)+"'' ) BEGIN DROP TABLE "+str(SAQSCO)+" END  ' ")
	
	SAQIEN_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQIEN)+"'' ) BEGIN DROP TABLE "+str(SAQIEN)+" END  ' ")
	
	SAQSCA_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSCA)+"'' ) BEGIN DROP TABLE "+str(SAQSCA)+" END  ' ")

	SAQSAP_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSAP)+"'' ) BEGIN DROP TABLE "+str(SAQSAP)+" END  ' ")
	
	SAQSCO_SEL = SqlHelper.GetFirst("sp_executesql @T=N'select QUOTE_ID,EQUIPMENT_ID,SERVICE_ID,CONVERT(VARCHAR(100),NULL) AS COVERAGE,CONVERT(VARCHAR(100),NULL) AS TECHFORCE INTO "+str(SAQSCO)+" from SAQSCO(NOLOCK) WHERE QUOTE_ID = ''"+str(Qt_id[0])+"'' AND SERVICE_ID NOT IN (SELECT ADNPRDOFR_ID FROM MAADPR(NOLOCK))   ' ")

	start = 1
	end = 1

	Check_flag = 1
	while Check_flag == 1:

		ent_query = SqlHelper.GetFirst("SELECT DISTINCT QUOTE_ID,cpqtableentryid FROM (SELECT DISTINCT quote_id,cpqtableentryid, ROW_NUMBER()OVER(ORDER BY cpqtableentryid) AS SNO FROM SAQSCE (NOLOCK) where quote_id='"+str(Qt_id[0])+"' AND SERVICE_ID NOT IN (SELECT ADNPRDOFR_ID FROM MAADPR(NOLOCK)) ) A WHERE SNO>= "+str(start)+" AND SNO<="+str(end)+" ")

		if str(ent_query) != "None":
			
			start = start + 1
			end = end + 1
			
			
			if start == 2:
				#Trace.Write("--->"+str(start))
				SAQIEN_SEL = SqlHelper.GetFirst("sp_executesql @T=N'declare @H int; Declare @val Varchar(MAX);DECLARE @XML XML; SELECT @val = FINAL from(select  REPLACE(entitlement_xml,''<QUOTE_ITEM_ENTITLEMENT>'',sml) AS FINAL FROM (select ''<QUOTE_ITEM_ENTITLEMENT><QUOTE_ID>''+quote_id+''</QUOTE_ID><SERVICE_ID>''+service_id+''</SERVICE_ID><EQUIPMENT_ID>''+equipment_id+''</EQUIPMENT_ID>'' AS sml,replace(entitlement_xml,''&'','';#38'')  as entitlement_xml from SAQSCE(nolock) where quote_id=''"+str(Qt_id[0])+"'' AND cpqtableentryid = "+str(ent_query.cpqtableentryid)+" )A )a SELECT @XML = CONVERT(XML,''<ROOT>''+@VAL+''</ROOT>'') exec sys.sp_xml_preparedocument @H output,@XML; select QUOTE_ID,EQUIPMENT_ID,SERVICE_ID,ENTITLEMENT_NAME,ENTITLEMENT_DESCRIPTION,ENTITLEMENT_VALUE_CODE INTO "+str(SAQIEN)+"  from openxml(@H, ''ROOT/QUOTE_ITEM_ENTITLEMENT'', 0) with (QUOTE_ID VARCHAR(100) ''QUOTE_ID'',EQUIPMENT_ID VARCHAR(100) ''EQUIPMENT_ID'',ENTITLEMENT_NAME VARCHAR(100) ''ENTITLEMENT_NAME'',SERVICE_ID VARCHAR(100) ''SERVICE_ID'',ENTITLEMENT_VALUE_CODE VARCHAR(100) ''ENTITLEMENT_VALUE_CODE'',ENTITLEMENT_DESCRIPTION VARCHAR(100) ''ENTITLEMENT_DESCRIPTION'') ; exec sys.sp_xml_removedocument @H; '")
			
			else:
				SAQIEN_SEL = SqlHelper.GetFirst("sp_executesql @T=N'declare @H int; Declare @val Varchar(MAX);DECLARE @XML XML; SELECT @val = FINAL from(select  REPLACE(entitlement_xml,''<QUOTE_ITEM_ENTITLEMENT>'',sml) AS FINAL FROM (select ''<QUOTE_ITEM_ENTITLEMENT><QUOTE_ID>''+quote_id+''</QUOTE_ID><SERVICE_ID>''+service_id+''</SERVICE_ID><EQUIPMENT_ID>''+equipment_id+''</EQUIPMENT_ID>'' AS sml,replace(entitlement_xml,''&'','';#38'')  as entitlement_xml from SAQSCE(nolock) where quote_id=''"+str(Qt_id[0])+"'' AND cpqtableentryid = "+str(ent_query.cpqtableentryid)+" )A )a SELECT @XML = CONVERT(XML,''<ROOT>''+@VAL+''</ROOT>'') exec sys.sp_xml_preparedocument @H output,@XML; insert "+str(SAQIEN)+" (QUOTE_ID,EQUIPMENT_ID,SERVICE_ID,ENTITLEMENT_NAME,ENTITLEMENT_DESCRIPTION,ENTITLEMENT_VALUE_CODE) select QUOTE_ID,EQUIPMENT_ID,SERVICE_ID,ENTITLEMENT_NAME,ENTITLEMENT_DESCRIPTION,ENTITLEMENT_VALUE_CODE  from openxml(@H, ''ROOT/QUOTE_ITEM_ENTITLEMENT'', 0) with (QUOTE_ID VARCHAR(100) ''QUOTE_ID'',EQUIPMENT_ID VARCHAR(100) ''EQUIPMENT_ID'',ENTITLEMENT_NAME VARCHAR(100) ''ENTITLEMENT_NAME'',SERVICE_ID VARCHAR(100) ''SERVICE_ID'',ENTITLEMENT_VALUE_CODE VARCHAR(100) ''ENTITLEMENT_VALUE_CODE'',ENTITLEMENT_DESCRIPTION VARCHAR(100) ''ENTITLEMENT_DESCRIPTION''); exec sys.sp_xml_removedocument @H; '")
		
		else:
			Check_flag=0
			
	SAQSCO_UPD = SqlHelper.GetFirst("sp_executesql @T=N'UPDATE A SET COVERAGE=ENTITLEMENT_VALUE_CODE FROM  "+str(SAQSCO)+" A(NOLOCK) JOIN "+str(SAQIEN)+" B(NOLOCK) ON A.QUOTE_ID = B.QUOTE_ID AND A.SERVICE_ID = B.SERVICE_ID AND A.EQUIPMENT_ID = B.EQUIPMENT_ID WHERE B.ENTITLEMENT_DESCRIPTION=''Contract Coverage''  ' ") 
	
	SAQSCO_UPD = SqlHelper.GetFirst("sp_executesql @T=N'UPDATE A SET TECHFORCE=ENTITLEMENT_VALUE_CODE FROM  "+str(SAQSCO)+" A(NOLOCK) JOIN "+str(SAQIEN)+" B(NOLOCK) ON A.QUOTE_ID = B.QUOTE_ID AND A.SERVICE_ID = B.SERVICE_ID AND A.EQUIPMENT_ID = B.EQUIPMENT_ID WHERE B.ENTITLEMENT_DESCRIPTION=''Tech Force''  ' ")
	
	SAQSCA_SEL = SqlHelper.GetFirst("sp_executesql @T=N'select QUOTE_ID,EQUIPMENT_ID,SERVICE_ID,ASSEMBLY_ID INTO "+str(SAQSCA)+" from SAQSCA(NOLOCK) WHERE QUOTE_ID = ''"+str(Qt_id[0])+"'' AND SERVICE_ID NOT IN (SELECT ADNPRDOFR_ID FROM MAADPR(NOLOCK)) ' ")

	SAQSAP_SEL = SqlHelper.GetFirst("sp_executesql @T=N'select QUOTE_ID,EQUIPMENT_ID,SERVICE_ID,ASSEMBLY_ID,PM_FREQUENCY, PM_NAME INTO "+str(SAQSAP)+" from SAQSAP(NOLOCK) WHERE QUOTE_ID = ''"+str(Qt_id[0])+"'' AND PM_NAME = ''Wet Clean'' AND SERVICE_ID NOT IN (SELECT ADNPRDOFR_ID FROM MAADPR(NOLOCK))' ")
	

	table = SqlHelper.GetFirst(
		"SELECT replace ('{\"QTQICA\": ['+STUFF((SELECT ','+ JSON FROM (SELECT DISTINCT '{\"SESSION_ID\" : \"'+SESSION_ID+'\",\"QUOTE_ID\" : \"'+QUOTE_ID+'\",\"EQUIPMENT_ID\" : \"'+EQUIPMENT_ID+'\",\"SERVICE_ID\" : \"'+SERVICE_ID+'\",\"ASSEMBLY_ID\" : \"'+ASSEMBLY_ID+'\",\"LABOR_COVERAGE\" : \"'+LABOR_COVERAGE+'\",\"TECHFORCE\" : \"'+TECHFORCE+'\",\"PM_NAME\" : \"'+PM_NAME+'\",\"PM_PER_YEAR\" : \"'+PM_PER_YEAR+'\"}' AS JSON from (SELECT DISTINCT  "+str(timestamp_sessionid)+" as SESSION_ID, ISNULL(B.QUOTE_ID,'') AS QUOTE_ID, ISNULL(B.EQUIPMENT_ID,'') AS EQUIPMENT_ID,ISNULL(B.SERVICE_ID,'') AS SERVICE_ID,ISNULL(A.ASSEMBLY_ID,'') AS ASSEMBLY_ID,ISNULL( COVERAGE,'' ) AS LABOR_COVERAGE,ISNULL(TECHFORCE,'') AS TECHFORCE, ISNULL(PM_NAME,'') AS PM_NAME,ISNULL(CONVERT(VARCHAR(50),PM_FREQUENCY),'') AS PM_PER_YEAR FROM "+str(SAQSCO)+" B(NOLOCK) JOIN "+str(SAQSCA)+"(NOLOCK) A ON A.QUOTE_ID = B.QUOTE_ID AND A.SERVICE_ID= B.SERVICE_ID AND A.EQUIPMENT_ID = B.EQUIPMENT_ID LEFT JOIN "+str(SAQSAP)+" C(NOLOCK) ON A.QUOTE_ID = C.QUOTE_ID AND A.SERVICE_ID = C.SERVICE_ID AND A.EQUIPMENT_ID = C.EQUIPMENT_ID AND A.ASSEMBLY_ID=C.ASSEMBLY_ID AND PM_NAME = 'Wet Clean' WHERE B.QUOTE_ID = '"+str(Qt_id[0])+"' ) t 	) A FOR XML PATH ('')  ), 1, 1, '')+']}','amp;#','#') AS RESULT "
	)
	if str(table).upper() != "NONE" and str(type(table.RESULT)) == "<type 'str'>":
		Flag = "True"
		
		#Log.Info("44444555 table.RESULT ---->"+str(table.RESULT))

		Parameter = SqlHelper.GetFirst("SELECT QUERY_CRITERIA_1 FROM SYDBQS (NOLOCK) WHERE QUERY_NAME = 'SELECT' ")

		primaryQueryItems = SqlHelper.GetFirst( ""+ str(Parameter.QUERY_CRITERIA_1)+ " SYINPL (INTEGRATION_PAYLOAD,SESSION_ID,INTEGRATION_NAME)  select ''"+str(table.RESULT)+ "'','"+ str(timestamp_sessionid)+ "',''CPQ_TO_SSCM_LOAD'' ' ")
		
		#F5 AUTHENTICATION
		
		LOGIN_CRE = SqlHelper.GetFirst("SELECT  URL FROM SYCONF where EXTERNAL_TABLE_NAME ='CPQ_TO_SSCM_QUOTE'")
		Oauth_info = SqlHelper.GetFirst("SELECT  DOMAIN,URL FROM SYCONF where EXTERNAL_TABLE_NAME ='OAUTH'")
		
		requestdata =Oauth_info.DOMAIN
		webclient = System.Net.WebClient()
		webclient.Headers[System.Net.HttpRequestHeader.ContentType] = "application/x-www-form-urlencoded"
		response = webclient.UploadString(Oauth_info.URL,str(requestdata))

		response = eval(response)
		access_token = response['access_token']
		
		authorization = "Bearer " + access_token
		webclient = System.Net.WebClient()
		webclient.Headers[System.Net.HttpRequestHeader.ContentType] = "application/json"
		webclient.Headers[System.Net.HttpRequestHeader.Authorization] = authorization;	

		crm_response = webclient.UploadString(str(LOGIN_CRE.URL),str(table.RESULT))	
		Log.Info("789 crm_response --->"+str(crm_response))

		#StatusUpdate = SqlHelper.GetFirst("sp_executesql @T=N'UPDATE B SET PRICING_STATUS='''' FROM SAQICO B(NOLOCK)  WHERE B.QUOTE_ID = ''"+str(Qt_id[0])+"''   '")
		
		SAQSCO_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSCO)+"'' ) BEGIN DROP TABLE "+str(SAQSCO)+" END  ' ")
		
		SAQIEN_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQIEN)+"'' ) BEGIN DROP TABLE "+str(SAQIEN)+" END  ' ")
		
		SAQSCA_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSCA)+"'' ) BEGIN DROP TABLE "+str(SAQSCA)+" END  ' ")

		SAQSAP_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSAP)+"'' ) BEGIN DROP TABLE "+str(SAQSAP)+" END  ' ")

		StatusUpdate = SqlHelper.GetFirst("sp_executesql @T=N'UPDATE SAQICO SET PRICING_STATUS=''ACQUIRING'' FROM SAQICO (NOLOCK) JOIN SAQSCA(NOLOCK) ON SAQSCA.QUOTE_ID = SAQICO.QUOTE_ID AND SAQSCA.EQUIPMENT_ID = SAQICO.EQUIPMENT_ID AND SAQSCA.SERVICE_ID = SAQICO.SERVICE_ID WHERE SAQSCA.QUOTE_ID = ''"+str(Qt_id[0])+"'' AND SAQICO.SERVICE_ID NOT IN (SELECT ADNPRDOFR_ID FROM MAADPR(NOLOCK))  '")
		
		#StatusUpdate = SqlHelper.GetFirst("sp_executesql @T=N'UPDATE SAQICO SET PRICING_STATUS=''ERROR'',COST_CALCULATION_STATUS=''Assembly not mapped in CPQ'' FROM SAQICO (NOLOCK) LEFT JOIN SAQSCA(NOLOCK) ON SAQSCA.QUOTE_ID = SAQICO.QUOTE_ID AND SAQSCA.EQUIPMENT_ID = SAQICO.EQUIPMENT_ID AND SAQSCA.SERVICE_ID = SAQICO.SERVICE_ID WHERE SAQSCA.QUOTE_ID = ''"+str(Qt_id[0])+"'' AND SAQICO.EQUIPMENT_ID IS NULL  '")

		Emailinfo = SqlHelper.GetFirst("SELECT QUOTE_ID,CPQ,SSCM,CPQ-SSCM AS REMANING FROM (SELECT SAQICO.QUOTE_ID,COUNT(DISTINCT SAQICO.EQUIPMENT_ID) AS CPQ,COUNT(DISTINCT SAQSCA.EQUIPMENT_ID) AS SSCM  FROM SAQICO (NOLOCK) LEFT JOIN SAQSCA(NOLOCK) ON SAQSCA.QUOTE_ID = SAQICO.QUOTE_ID AND SAQSCA.EQUIPMENT_ID = SAQICO.EQUIPMENT_ID AND SAQSCA.SERVICE_ID = SAQICO.SERVICE_ID WHERE SAQICO.QUOTE_ID = '"+str(Qt_id[0])+"' group by SAQICO.Quote_ID )SUB_SAQICO ")
		
		ToEml = SqlHelper.GetFirst("SELECT ISNULL(OWNER_ID,'X0116959') AS OWNER_ID FROM SAQTMT (NOLOCK) WHERE SAQTMT.QUOTE_ID = '"+str(Qt_id[0])+"'  ") 

		Header = "<!DOCTYPE html><html><head><style>table {font-family: Calibri, sans-serif; border-collapse: collapse; width: 75%}td, th {  border: 1px solid #dddddd;  text-align: left; padding: 8px;}.im {color: #222;}tr:nth-child(even) {background-color: #dddddd;} #grey{background: rgb(245,245,245);} #bd{color : 'black'} </style></head><body id = 'bd'>"


		Table_start = "<p>Hi Team,<br><br>The Equipment and Assembly information has been successfully sent to retrieve the cost information from SSCM for the below Quote</p><table class='table table-bordered'><tr><th id ='grey'>QUOTE ID</th><th id = 'grey'>TOTAL EQUIPMENT (CPQ)</th><th id = 'grey'>EQUIPMENT SENT (SSCM)</th><th id = 'grey'>EQUIPMENT NOT SENT TO SSCM (NO ASSEMBLY MAPPED)</th><th id = 'grey'>PRICE CALCULATION STATUS</th></tr><tr><td >"+str(Qt_id[0])+"</td><td >"+str(Emailinfo.CPQ)+"</td ><td >"+str(Emailinfo.SSCM)+"</td><td >"+str(Emailinfo.REMANING)+"</td><td>Acquiring</td></tr>"

		Table_info = ""
		Table_End = "</table><p><strong>Note : </strong>Please do not reply to this email.</p></body></html>"

		Error_Info = Header + Table_start + Table_info + Table_End

		LOGIN_CRE = SqlHelper.GetFirst("SELECT USER_NAME as Username,Password FROM SYCONF where Domain ='SUPPORT_MAIL'")

		# Create new SmtpClient object
		mailClient = SmtpClient()

		# Set the host and port (eg. smtp.gmail.com)
		mailClient.Host = "smtp.gmail.com"
		mailClient.Port = 587
		mailClient.EnableSsl = "true"

		# Setup NetworkCredential
		mailCred = NetworkCredential()
		mailCred.UserName = str(LOGIN_CRE.Username)
		mailCred.Password = str(LOGIN_CRE.Password)
		mailClient.Credentials = mailCred

		#Current user email(ToEmail)
		#UserId = User.Id
		#Log.Info("123 UserId.UserId --->"+str(UserId))
		UserEmail = SqlHelper.GetFirst("SELECT isnull(email,'INTEGRATION.SUPPORT@BOSTONHARBORCONSULTING.COM') as email FROM saempl (nolock) where employee_id  = '"+str(ToEml.OWNER_ID)+"'")
		#Log.Info("123 UserEmail.email --->"+str(UserEmail.email))

		# Create two mail adresses, one for send from and the another for recipient
		if UserEmail is None:
			toEmail = MailAddress("suresh.muniyandi@bostonharborconsulting.com")
		else:
			toEmail = MailAddress(UserEmail.email)
		fromEmail = MailAddress("INTEGRATION.SUPPORT@BOSTONHARBORCONSULTING.COM")

		# Create new MailMessage object
		msg = MailMessage(fromEmail, toEmail)

		# Set message subject and body
		msg.Subject = "Quote Successfully Sent to SSCM"
		msg.IsBodyHtml = True
		msg.Body = Error_Info

		# Bcc Emails	
		copyEmail4 = MailAddress("baji.baba@bostonharborconsulting.com")
		msg.Bcc.Add(copyEmail4)

		copyEmail1 = MailAddress("ranjani.parkavi@bostonharborconsulting.com")
		msg.Bcc.Add(copyEmail1) 

		#copyEmail2 = MailAddress("aditya.shivkumar@bostonharborconsulting.com")
		#msg.Bcc.Add(copyEmail2)

		copyEmail3 = MailAddress("sathyabama.akhala@bostonharborconsulting.com")
		msg.Bcc.Add(copyEmail3) 

		copyEmail5 = MailAddress("ashish.gandotra@bostonharborconsulting.com")
		msg.Bcc.Add(copyEmail5)
		
		copyEmail6 = MailAddress("suresh.muniyandi@bostonharborconsulting.com")
		msg.Bcc.Add(copyEmail6)

		# Send the message
		mailClient.Send(msg)		
		

	if Flag == "True":
		ApiResponse = ApiResponseFactory.JsonResponse({"Response": [{"Status": "200", "Message": str(crm_response)}]})
	else:

		SAQSCO_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSCO)+"'' ) BEGIN DROP TABLE "+str(SAQSCO)+" END  ' ")
	
		SAQIEN_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQIEN)+"'' ) BEGIN DROP TABLE "+str(SAQIEN)+" END  ' ")
		
		SAQSCA_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSCA)+"'' ) BEGIN DROP TABLE "+str(SAQSCA)+" END  ' ")

		SAQSAP_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSAP)+"'' ) BEGIN DROP TABLE "+str(SAQSAP)+" END  ' ")

		ApiResponse = ApiResponseFactory.JsonResponse(
			{"Response": [{"Status": "200", "Message": "No Data available to process the request."}]}
		)


except:

	CRMQT = SqlHelper.GetFirst("select convert(varchar(100),c4c_quote_id) as c4c_quote_id from SAQTMT(nolock) WHERE QUOTE_ID = '"+str(Qt_id[0])+"' ")
	
	SAQSCO = "SAQSCO_BKP_1"+str(CRMQT.c4c_quote_id)
	SAQIEN = "SAQIEN_BKP_1"+str(CRMQT.c4c_quote_id)
	SAQSCA = "SAQSCA_BKP_1"+str(CRMQT.c4c_quote_id)
	SAQSAP = "SAQSAP_BKP_1"+str(CRMQT.c4c_quote_id)
	
	SAQSCO_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSCO)+"'' ) BEGIN DROP TABLE "+str(SAQSCO)+" END  ' ")
	
	SAQIEN_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQIEN)+"'' ) BEGIN DROP TABLE "+str(SAQIEN)+" END  ' ")
	
	SAQSCA_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSCA)+"'' ) BEGIN DROP TABLE "+str(SAQSCA)+" END  ' ")

	SAQSAP_DRP = SqlHelper.GetFirst("sp_executesql @T=N'IF EXISTS (SELECT ''X'' FROM SYS.OBJECTS WHERE NAME= ''"+str(SAQSAP)+"'' ) BEGIN DROP TABLE "+str(SAQSAP)+" END  ' ")
	
	Log.Info("QTPOSTPRSM ERROR---->:" + str(sys.exc_info()[1]))
	Log.Info("QTPOSTPRSM ERROR LINE NO---->:" + str(sys.exc_info()[-1].tb_lineno))
	ApiResponse = ApiResponseFactory.JsonResponse({"Response": [{"Status": "400", "Message": str(sys.exc_info()[1])}]})