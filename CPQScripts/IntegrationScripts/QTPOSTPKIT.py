# =========================================================================================================================================
#   __script_name : QTPOSTPKIT.PY
#   __script_description : THIS SCRIPT HIT WEBMETHOD WITH APPROPIATE INPUT AND GET REAL TIME KIT DATA AND STORED IN SYINPL
#   __primary_author__ : BAJI
#   __create_date :
#   Â© BOSTON HARBOR TECHNOLOGY LLC - ALL RIGHTS RESERVED
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
import datetime

try:
	input_data = [str(param_result.Value) for param_result in Param.CPQ_Columns]	
	input_data = [input_data]
	
	Parameter = SqlHelper.GetFirst("SELECT QUERY_CRITERIA_1 FROM SYDBQS (NOLOCK) WHERE QUERY_NAME = 'SELECT' ")
	Parameter1 = SqlHelper.GetFirst("SELECT QUERY_CRITERIA_1 FROM SYDBQS (NOLOCK) WHERE QUERY_NAME = 'UPD' ")
	Parameter2 = SqlHelper.GetFirst("SELECT QUERY_CRITERIA_1 FROM SYDBQS (NOLOCK) WHERE QUERY_NAME = 'DEL' ")

	for crmifno in input_data:	
		
		Quote_Id = crmifno[0]
		Revision_Id = crmifno[-1]

	primaryQuerysession =  SqlHelper.GetFirst("SELECT NEWID() AS A")
	today = datetime.datetime.now()
	Modi_date = today.strftime("%m/%d/%Y %H:%M:%S %p")

	sessionid = SqlHelper.GetFirst("SELECT NEWID() AS A")
	timestamp_sessionid = "'" + str(sessionid.A) + "'"

	RTKM_INPUT_QUERY = SqlHelper.GetFirst(
				"SELECT replace ('{\"QTQICA\": ['+STUFF((SELECT ','+ JSON FROM (SELECT DISTINCT '{\"SESSION_ID\" : \"'+SESSION_ID+'\",\"QUOTE_ID\" : \"'+QUOTE_ID+'\",\"EQUIPMENT_ID\" : \"'+EQUIPMENT_ID+'\",\"SERVICE_ID\" : \"'+SERVICE_ID+'\",\"Assembly_ID\" : \"'+ASSEMBLY_ID+'\",\"PREVENTIVE_MAINTENANCE\" : \"'+PREVENTIVE_MAINTENANCE+'\",\"CORRECTIVE_MAINTENANCE\" : \"'+CORRECTIVE_MAINTENANCE+'\",\"WET_CLEAN\" : \"'+WET_CLEAN+'\"}' AS JSON from (SELECT DISTINCT  "+str(timestamp_sessionid)+"  as SESSION_ID, SAQSCA.QUOTE_ID AS QUOTE_ID,ISNULL(SAQSCA.EQUIPMENT_ID,'') AS EQUIPMENT_ID,ISNULL(SAQSCA.SERVICE_ID,'') AS SERVICE_ID,ISNULL(SAQSCA.ASSEMBLY_ID,'') AS ASSEMBLY_ID,ISNULL(PMLAB_ENT,'') AS PREVENTIVE_MAINTENANCE,ISNULL(CMLAB_ENT,'') AS CORRECTIVE_MAINTENANCE,ISNULL(WETCLN_ENT,'') AS WET_CLEAN FROM SAQSCA (NOLOCK) JOIN SAQSCE (NOLOCK) ON SAQSCA.QUOTE_ID = SAQSCE.QUOTE_ID AND SAQSCA.QTEREV_ID = SAQSCE.QTEREV_ID AND SAQSCA.SERVICE_ID = SAQSCE.SERVICE_ID AND SAQSCA.EQUIPMENT_ID = SAQSCA.EQUIPMENT_ID  WHERE SAQSCA.QUOTE_ID = '"+str(Quote_Id)+"' AND SAQSCA.QTEREV_ID = '"+str(Revision_Id)+"') t 	) A FOR XML PATH ('')  ), 1, 1, '')+']}','amp;#','#') AS RESULT ")

	if  str(RTKM_INPUT_QUERY).upper() != 'NONE' and str(type(RTKM_INPUT_QUERY.RESULT)) == "<type 'str'>":

		LOGIN_CRE = SqlHelper.GetFirst("SELECT URL FROM SYCONF (nolock) where EXTERNAL_TABLE_NAME ='CPQ_TO_SSCM_REAL_TIME_KIT'")
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
		webclient.Headers.Add("Environment-Identifier", "X")
		crm_response1 = webclient.UploadString(str(LOGIN_CRE.URL),RTKM_INPUT_QUERY.RESULT)

		syinpl_data = ''
		if 'Param' in crm_response1 and "'" in crm_response1:
			l =  crm_response1.rindex("'")
			f = crm_response1.index("'")+1
			syinpl_data = crm_response1[f:l]			
		else:
			syinpl_data = crm_response1
			
		
		if len(syinpl_data) > 0:		

			Parameter = SqlHelper.GetFirst("SELECT QUERY_CRITERIA_1 FROM SYDBQS (NOLOCK) WHERE QUERY_NAME = 'SELECT' ")

			primaryQueryItems = SqlHelper.GetFirst( ""+ str(Parameter.QUERY_CRITERIA_1)+ " SYINPL (INTEGRATION_PAYLOAD,INTEGRATION_NAME,CpqTableEntryDateModified,INTEGRATION_KEY)  select ''"+syinpl_data+ "'',''REAL_TIME_KIT'',GETDATE(),''"+str(Quote_Id)+"'' ' ")

			
			rebuilt_data = eval(syinpl_data.replace('false','"false"').replace('true','"true"').replace('null','"NALL"'))      

			if len(rebuilt_data) != 0:      

				rebuilt_data = rebuilt_data["CPQ_Columns"]
				Table_Names = rebuilt_data.keys()
				Check_flag = 0
				
				for tn in Table_Names:
					if tn in rebuilt_data:
						Check_flag = 1
						if str(tn).upper() == "QTQICA":
							if str(type(rebuilt_data[tn])) == "<type 'dict'>":
								Tbl_data = [rebuilt_data[tn]]
							else:
								Tbl_data = rebuilt_data[tn] 						
								
							for record_dict in Tbl_data:
							
								splt_info = """ ''{TOOL_ID}'',''{Assembly_ID}'',''{PM_Event}'',''{PM_Freq}'',''{KIT_ID}'',''{KIT_Number}'',''{Seedstock_Cost}'',''{Logistics_Cost}'',''{TKM_Cost_Per_Event}'',''{Modi_date}'',''{KIT_MASTER_ID}'',''{APPLICATION}'',''{CLEANING_REGION}'',''{CUSTOMER_MARKETING_NAME}'',''{DEVICE}'',''{PROCESS_TYPE}'',''{SERVICE_COMPLEXITY}'',''{TECH_NODE}'',''{HW_TYPE}'',''{ARCM_Module_ID}'',''{RFP_Edit}'',''{Maintenance_Event_Level}'',''{KIT_CleaningCoating_Differentiation}'',''{QUOTE_ID}'',''{SERVICE_ID}'',''{SESSION_ID}'',''{MODULE_VERSION_ID}'' ,''{Event_Period}''  """.format(TOOL_ID = record_dict['TOOL_ID'],Assembly_ID = str(record_dict['Assembly_ID']),PM_Event = str(record_dict['PM_Event']),PM_Freq = record_dict['PM_Freq'],KIT_ID= str(record_dict['KIT_ID']),KIT_Number = str(record_dict['KIT_Number']),Seedstock_Cost = str(record_dict['Seedstock_Cost']),Logistics_Cost = str(record_dict['Logistics_Cost']),TKM_Cost_Per_Event = str(record_dict['TKM_Cost_Per_Event']),Modi_date = str(Modi_date),KIT_MASTER_ID= record_dict['KIT_MASTER_ID'],APPLICATION = record_dict['APPLICATION'],CLEANING_REGION = str(record_dict['CLEANING_REGION']),CUSTOMER_MARKETING_NAME = str(record_dict['CUSTOMER_MARKETING_NAME']),DEVICE = str(record_dict['DEVICE']),PROCESS_TYPE= str(record_dict['PROCESS_TYPE']),SERVICE_COMPLEXITY = str(record_dict['SERVICE_COMPLEXITY']),TECH_NODE = str(record_dict['TECH_NODE']),HW_TYPE = str(record_dict['HW_TYPE']),ARCM_Module_ID = str(record_dict['ARCM_Module_ID']),RFP_Edit = str(record_dict['RFP_Edit']),Maintenance_Event_Level = str(record_dict['Maintenance_Event_Level']),KIT_CleaningCoating_Differentiation = str(record_dict['KIT_CleaningCoating_Differentiation']),QUOTE_ID = str(record_dict['QUOTE_ID']),SERVICE_ID = str(record_dict['SERVICE_ID']),SESSION_ID = str(record_dict['SESSION_ID']) ,MODULE_VERSION_ID = str(record_dict['MODULE_VERSION_ID']),Event_Period = str(record_dict['Event_Period']))
								
								primaryQueryItems = SqlHelper.GetFirst( ""+ str(Parameter.QUERY_CRITERIA_1)+ " MAEAPM_INBOUND (QTEREV_ID,EQUIPMENT_ID,ASSEMBLY_ID,PM_NAME,PM_FREQUENCY,KIT_ID,KIT_NUMBER,SEEDSTOCK_COST,LOGISTICS_COST,TKM_COST_PER_EVENT,cpqtableentrydatemodified,KIT_MASTER_ID,APPLICATION,REGION,CUSTOMER_MARKETING_NAME,DEVICE,PROCESS_TYPE,SERVICE_COMPLEXITY,TECHNOLOGY_NODE,HW_TYPE,ARCM_MODULE_ID,RFP_EDIT,PM_LEVEL,CLEAN_COATING,QUOTE_ID,SERVICE_ID,SESSION_ID,MODULE_VERSION_ID,EVENT_PERIOD)  select ''"+str(Revision_Id)+ "'',"+str(splt_info)+ " ' ")
								
								if 'BOM' in record_dict:
									
									if str(type(record_dict['BOM'])) == "<type 'dict'>":
										Bom_data = [record_dict['BOM']]
									else:
										Bom_data = record_dict['BOM'] 
										
									for Bom_dict in Bom_data:
										primaryQueryItems = SqlHelper.GetFirst( ""+ str(Parameter.QUERY_CRITERIA_1)+ " MAKTPT_INBOUND (QUOTE_ID,QTEREV_ID,SERVICE_ID,SESSION_ID,KIT_ID,PART_NUMBER,QUANTITY,cpqtableentrydatemodified,KIT_MASTER_ID)  select  ''"+str(record_dict['QUOTE_ID'])+ "'', ''"+str(Revision_Id)+ "'',''"+str(record_dict['SERVICE_ID'])+ "'',''"+str(record_dict['SESSION_ID'])+ "'',''"+Bom_dict['KIT_ID']+ "'',''"+Bom_dict['PartNumber']+ "'',''"+str(Bom_dict['Qty'])+ "'',''"+ str(Modi_date)+ "'',''"+str(Bom_dict['KIT_MASTER_ID'])+ "'' ' ")   
			
				#Kit Master
				primaryQueryItems = SqlHelper.GetFirst(
				""
				+ str(Parameter.QUERY_CRITERIA_1)
				+ " MAMKIT(KIT_NAME,CPQTABLEENTRYADDEDBY,ADDUSR_RECORD_ID,CPQTABLEENTRYDATEADDED,KIT_RECORD_ID,KIT_ID)SELECT DISTINCT KIT_NAME,''"+ str(User.UserName)
				+ "'',''"+ str(User.Id)
				+ "'',GETDATE(),CONVERT(VARCHAR(1000),NEWID()),KIT_ID FROM (SELECT DISTINCT MAKTPT_INBOUND.KIT_ID AS KIT_NAME,MAKTPT_INBOUND.KIT_ID FROM MAKTPT_INBOUND (NOLOCK)  LEFT JOIN MAMKIT (NOLOCK) ON MAKTPT_INBOUND.KIT_ID = MAMKIT.KIT_ID WHERE MAMKIT.KIT_ID IS NULL)SUB_MAMKIT '")
				
				primaryQueryItems = SqlHelper.GetFirst(
				""
				+ str(Parameter2.QUERY_CRITERIA_1)
				+ " MAKTPT FROM MAKTPT JOIN MAKTPT_INBOUND  ON MAKTPT.KIT_ID = MAKTPT_INBOUND.KIT_ID WHERE ISNULL(PROCESS_STATUS,'''')= ''READY FOR UPLOAD'' AND TIMESTAMP = '"+str(timestamp_sessionid)+"'  '")
				
				primaryQueryItems = SqlHelper.GetFirst(
				""
				+ str(Parameter.QUERY_CRITERIA_1)
				+ "  MAKTPT(KIT_ID,KIT_NAME,KIT_RECORD_ID,PART_DESCRIPTION,PART_NUMBER,PART_RECORD_ID,QUANTITY,BOM_STATUS,CPQTABLEENTRYADDEDBY,ADDUSR_RECORD_ID,CPQTABLEENTRYDATEADDED,KIT_PART_RECORD_ID) SELECT DISTINCT SUB_MAKTPT.KIT_ID,SUB_MAKTPT.KIT_NAME,SUB_MAKTPT.KIT_RECORD_ID,SUB_MAKTPT.SAP_DESCRIPTION,SUB_MAKTPT.PART_NUMBER,SUB_MAKTPT.MATERIAL_RECORD_ID,SUB_MAKTPT.QUANTITY,SUB_MAKTPT.BOM_STATUS,''"+ str(User.UserName)
				+ "'',''"+ str(User.Id)
				+ "'',GETDATE(),CONVERT(VARCHAR(1000),NEWID()) FROM (SELECT DISTINCT MAMKIT.KIT_ID,MAMKIT.KIT_NAME,MAMKIT.KIT_RECORD_ID,SAP_DESCRIPTION,MAKTPT_INBOUND.PART_NUMBER,MATERIAL_RECORD_ID,MAKTPT_INBOUND.QUANTITY,''ACTIVE'' AS BOM_STATUS FROM MAKTPT_INBOUND (NOLOCK) JOIN MAMKIT (NOLOCK) ON MAKTPT_INBOUND.KIT_ID = MAMKIT.KIT_ID JOIN MAMTRL (NOLOCK) ON MAKTPT_INBOUND.PART_NUMBER = MAMTRL.SAP_PART_NUMBER)SUB_MAKTPT LEFT JOIN MAKTPT (NOLOCK) ON SUB_MAKTPT.KIT_ID = MAKTPT.KIT_ID AND SUB_MAKTPT.PART_NUMBER = MAKTPT.PART_NUMBER WHERE MAKTPT.PART_NUMBER IS NULL  '")
			
			
				ApiResponse = ApiResponseFactory.JsonResponse({"Response": [{"Status": "200", "Message": "REAL TIME KIT DATA SUCCESSFULLY UPLOADED"}]})	
		else:
			ApiResponse = ApiResponseFactory.JsonResponse({"Response": [{"Status": "400", "Message": "REAL TIME KIT DATA GETTING ERROR IN RESPONSE"}]})

except:
	Log.Info("QTPOSTPKIT ERROR---->:" + str(sys.exc_info()[1]))
	Log.Info("QTPOSTPKIT ERROR LINE NO---->:" + str(sys.exc_info()[-1].tb_lineno))
	ApiResponse = ApiResponseFactory.JsonResponse({"Response": [{"Status": "400", "Message": str(sys.exc_info()[1])}]})