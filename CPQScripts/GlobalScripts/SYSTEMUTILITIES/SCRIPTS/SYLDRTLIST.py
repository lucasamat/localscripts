# ==========================================================================================================================================
#   __script_name : SYLDRTLIST.PY
#   __script_description : THIS SCRIPT IS USED TO LOAD RELATED LISTS FOR A GIVEN OBJECT.
#   __primary_author__ : JOE EBENEZER
#   __create_date :
#   © BOSTON HARBOR TECHNOLOGY LLC - ALL RIGHTS RESERVED
# ==========================================================================================================================================
import re
import SYTABACTIN as Table
import SYCNGEGUID as CPQID
from datetime import datetime
from SYDATABASE import SQL
import time

Sql = SQL()

get_user_id = User.Id

productAttributesGetByName = lambda productAttribute: Product.Attributes.GetByName(productAttribute) or ""


class SYLDRTLIST:
    def MDYNMICSQLOBJECT(self, RECORD_ID, PerPage, PageInform, SubTab, PR_CURR, TP): 
        #current_prod = Product.Name or "Sales" 
        TestProduct = Webcom.Configurator.Scripting.Test.TestProduct() or ""
        materialRecID = useridval = getyears = col_year = footer_tot = ""
        column_names = getQuotetype = exclamation=""
        PR_CURRENCY = PR_CURR
        Page_start = (
            CurrentObj_Names
        ) = (
            QueryCount
        ) = (
            Page_End
        ) = (
            Wh_API_NAMEs
        ) = (
            TreeParam
        ) = (
            TreeParentParam
        ) = (
            TreeSuperParentParam
        ) = (
            Erp_attr_obj_chck1
        ) = (
            current_rec_id
        ) = (
            Query_Obj
        ) = (
            rev_status_to_indicate
        ) = (
            TreeParam
        ) = (
            TreeParentParam
        ) = (
            TreeSuperParentParam
        ) = (
            TreeSuperTopParentParam
        ) = (
            TopTreeSuperParentParam
        ) = (
            TreeTopSuperParentParam
        ) = (
            tabName
        ) = (
            Columns
        ) = (
            Obj_Name
        ) = (
            table_id
        ) = (
            COLUMN_REC_ID
        ) = (
            Qstn_REC_ID
        ) = (
            CurrentObj_Recordno
        ) = (
            CurrentObj_Name
        ) = (
            Wh_API_NAME
        ) = (
            Wh_OBJECT_NAME
        ) = (
            Query_Obj
        ) = (
            ObjectName
        ) = dbl_clk_function = col = QuotaSubCat_ID = text = texts = Qury_str = QuryCount_str = table_ids = lookup_str = curr_symbol_obj = curr_symbol = decimal_place = SAQICO_dbl_clk_function =  ""

        Action_permission, treeparam_dict, related_list_permissions, attr_list, attrs_datatype_dict = ({} for i in range(5))

        (
            list_of_tabs,
            cell_api,
            table_list,
            k_list,
            tables_list,
            dict_key,
            ATTRIBUTE_NAME_list,
            lookup_rl_popup,
            primary_link_popup,
            lookup_link_popup,
            dblclick_ele,
            checkbox_list,
            name,
            lookup_disply_list,
            edit_field,
        ) = ([] for i in range(15))
        Qustr = ""
        table_header = ""
        lock_pricbkst = lock_pricbk = "FALSE"
        segment_rec_id = Product.GetGlobal("segment_rec_id")
        segment_revision_id = Product.GetGlobal("segmentRevisionId")
        TreeParam = Product.GetGlobal("TreeParam")
        TreeParentParam = Product.GetGlobal("TreeParentLevel0")
        
        if str(PerPage) == "" and str(PageInform) == "":
            Page_start = 1
            Page_End = PerPage = 10
            PageInform = "1___10___10"
        else:
            Page_start = int(PageInform.split("___")[0])
            
            Page_End = int(PageInform.split("___")[1])
            
            PerPage = PerPage
        try:
            current_prod = Product.Name
        except:
            current_prod = "Sales"
        

        for tab in Product.Tabs:            
            if tab.IsSelected == True:
                tabName = str(tab.Name)
        try:        
            contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
        except:
            contract_quote_record_id = ''    
        Trace.Write('139---'+str(RECORD_ID))
        '''obj_obj = Sql.GetFirst(
            """SELECT SYOBJR.RECORD_ID, SYOBJR.SAPCPQ_ATTRIBUTE_NAME,SYOBJR.PARENT_LOOKUP_REC_ID, SYOBJR.OBJ_REC_ID, SYOBJR.NAME, SYOBJR.COLUMN_REC_ID, SYOBJR.COLUMNS, SYOBJR.RELATED_LIST_SINGULAR_NAME, SYOBJR.DISPLAY_ORDER, SYOBJR.ORDERS_BY FROM SYOBJR (NOLOCK) WHERE SYOBJR.SAPCPQ_ATTRIBUTE_NAME = '{RECORD_ID}'""".format(
                RECORD_ID=str(RECORD_ID), get_user_id=str(get_user_id)
            )
        )'''
        '''obj_obj = Sql.GetFirst(
            """
                                    SELECT
                                        SYOBJR.RECORD_ID, SYOBJR.SAPCPQ_ATTRIBUTE_NAME,SYOBJR.PARENT_LOOKUP_REC_ID, SYOBJR.OBJ_REC_ID,
                                        SYOBJR.NAME, SYOBJR.COLUMN_REC_ID, SYOBJR.COLUMNS,
                                        SYOBJR.RELATED_LIST_SINGULAR_NAME,SYOBJR.CAN_ADD, SYOBJR.CAN_EDIT, SYOBJR.CAN_DELETE,
                                        SYOBJR.DISPLAY_ORDER, SYOBJR.ORDERS_BY
                                    FROM
                                        SYOBJR (NOLOCK) 
                                    WHERE
                                        SYOBJR.SAPCPQ_ATTRIBUTE_NAME = '{RECORD_ID}'
                                    """.format(
                RECORD_ID=str(RECORD_ID)
            )
        )'''
        #object level permissions
        obj_obj = Sql.GetFirst(
            """SELECT   SYOBJR.RECORD_ID, SYOBJR.SAPCPQ_ATTRIBUTE_NAME,SYOBJR.PARENT_LOOKUP_REC_ID, SYOBJR.OBJ_REC_ID,
                                        SYOBJR.NAME, SYOBJR.COLUMN_REC_ID, SYOBJR.COLUMNS,
                                        SYPROH.CAN_ADD, SYPROH.CAN_EDIT, SYPROH.CAN_DELETE, SYOBJR.RELATED_LIST_SINGULAR_NAME,
                                        SYOBJR.DISPLAY_ORDER, SYOBJR.ORDERS_BY
                                    FROM
                                        SYOBJR (NOLOCK) inner join SYPROH (NOLOCK) on SYPROH.OBJECT_RECORD_ID = SYOBJR.OBJ_REC_ID INNER JOIN USERS_PERMISSIONS (NOLOCK) UP ON UP.PERMISSION_ID = SYPROH.PROFILE_RECORD_ID

                                    WHERE
                                        SYOBJR.SAPCPQ_ATTRIBUTE_NAME = '{RECORD_ID}'  AND SYPROH.VISIBLE= 1 AND UP.USER_ID = '{get_user_id}'
                                    """.format(
                RECORD_ID=str(RECORD_ID), get_user_id=str(get_user_id)
            )
        )
        CurrentModuleObj = Sql.GetFirst("select * from SYAPPS (NOLOCK) where APP_LABEL = '" + str(current_prod) + "'")
        #TestProduct = Webcom.Configurator.Scripting.Test.TestProduct()
        
        crnt_prd_val = str(CurrentModuleObj.APP_ID) or ""
        Product_Name = ""
        tabs = Product.Tabs or "Quotes"       
        for tab in tabs:
            list_of_tabs.append(tab.Name)
        try:
            TestProduct = Webcom.Configurator.Scripting.Test.TestProduct()
            Product_Name = TestProduct.Name
            #Trace.Write('TestProduct--'+str(TestProduct))
        except:
            Product_Name = "Sales"
        try:

            current_tab = str(TestProduct.CurrentTab)            
        except:            
            current_tab = "Quote"              
        Tree_Enable = ""
        Tree_Enable = Sql.GetFirst(
            "select ENABLE_TREE FROM SYTABS (NOLOCK) where UPPER(SAPCPQ_ALTTAB_NAME) ='"
            + str(current_tab).upper()
            + "' AND APP_RECORD_ID = '"
            + str(str(CurrentModuleObj.APP_RECORD_ID))
            + "'"
        )
        
        if Tree_Enable is not None or len(Tree_Enable) > 0:
            Trace.Write('mmmm')                        
            if str(Tree_Enable.ENABLE_TREE).upper() == "TRUE":
                Trace.Write('LLLL'+str(Product_Name))
                if Product_Name.upper() == "SYSTEM ADMIN" or Product_Name.upper() == "SALES":   
                    #Trace.Write('llll'+str(TestProduct.Name))                 
                    (
                        TreeParam,
                        TreeParentParam,
                        TreeSuperParentParam,
                        TopTreeSuperParentParam,
                        TreeFirstSuperTopParentParam,
                        TreeSecondSuperTopParentParam,
                    ) = (
                        Product.GetGlobal("TreeParam"),
                        Product.GetGlobal("TreeParentLevel0"),
                        Product.GetGlobal("TreeParentLevel1"),
                        Product.GetGlobal("TreeParentLevel2"),
                        Product.GetGlobal("TreeParentLevel3"),
                        Product.GetGlobal("TreeParentLevel4"),
                    )
                 

                else:
                    Trace.Write('kkkkkkk')
                    (
                        TreeParam,
                        TreeParentParam,
                        TreeSuperParentParam,
                        TopTreeSuperParentParam,
                        TreeTopSuperParentParam,
                        TreeFirstSuperTopParentParam,
                    ) = (
                        Product.GetGlobal("CommonTreeParam"),
                        Product.GetGlobal("CommonTreeParentParam"),
                        Product.GetGlobal("CommonTreeSuperParentParam"),
                        Product.GetGlobal("CommonTreeTopSuperParentParam"),
                        Product.GetGlobal("CommonTopTreeSuperParentParam"),
                        Product.GetGlobal("CommonTreeFirstSuperTopParentParam"),
                    )
                """if (
                    TestProduct.Name.upper() == "SYSTEM ADMIN"
                ):
                    if (TestProduct.Name.upper() == "SALES" or TestProduct.Name.upper() == "SYSTEM ADMIN"):
                        if (current_tab == "Object" or current_tab == "Tab"):
                            
                            (
                                TreeParam,
                                TreeParentParam,
                                TreeSuperParentParam,
                                TopTreeSuperParentParam,
                                TreeFirstSuperTopParentParam,
                            ) = (
                                Product.GetGlobal("TreeParam"),
                                Product.GetGlobal("TreeParentLevel0"),
                                Product.GetGlobal("TreeParentLevel1"),
                                Product.GetGlobal("TreeParentLevel2"),
                                Product.GetGlobal("TreeParentLevel3"),
                            )
                        else:
                            (
                                TreeParam,
                                TreeParentParam,
                                TreeSuperParentParam,
                                TopTreeSuperParentParam,
                                TreeTopSuperParentParam,
                                TreeFirstSuperTopParentParam,
                            ) = (
                                Product.GetGlobal("CommonTreeParam"),
                                Product.GetGlobal("CommonTreeParentParam"),
                                Product.GetGlobal("CommonTreeSuperParentParam"),
                                Product.GetGlobal("CommonTreeTopSuperParentParam"),
                                Product.GetGlobal("CommonTopTreeSuperParentParam"),
                                Product.GetGlobal("CommonTreeFirstSuperTopParentParam"),
                            )
                else:
                    (
                        TreeParam,
                        TreeParentParam,
                        TreeSuperParentParam,
                        TopTreeSuperParentParam,
                        TreeTopSuperParentParam,
                        TreeFirstSuperTopParentParam,
                    ) = (
                        Product.GetGlobal("CommonTreeParam"),
                        Product.GetGlobal("CommonTreeParentParam"),
                        Product.GetGlobal("CommonTreeSuperParentParam"),
                        Product.GetGlobal("CommonTreeTopSuperParentParam"),
                        Product.GetGlobal("CommonTopTreeSuperParentParam"),
                        Product.GetGlobal("CommonTreeFirstSuperTopParentParam"),
                    )"""
    
        if obj_obj is None:
            return "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
        # Billing Matrix - Pivot - Start
        billing_date_column = ''        
        # Billing Matrix - Pivot - End
        if obj_obj is not None:
            Columns = obj_obj.COLUMNS
            Trace.Write('302-------')
            #Hide columns in Related list based on Quote type start
            if Currenttab == 'Quotes':
                quote_rec_id = Product.GetGlobal("contract_quote_record_id")
                Trace.Write('306-------')           
                if  quote_rec_id:                
                    getQuote = Sql.GetFirst("SELECT QUOTE_TYPE FROM SAQTMT (NOLOCK) WHERE MASTER_TABLE_QUOTE_RECORD_ID = '"+str(quote_rec_id)+"'")
                    getQuotetype = getQuote.QUOTE_TYPE
                    Trace.Write("QUOTE_TYP "+str(getQuotetype)+" TP_J "+str(TreeParam))
                    if str(getQuotetype).upper() == "ZWK1 - SPARES" and  str(TreeParam) in ['Quote Items','Quote Preview','Contract Items','Contract Preview']:
                        if RECORD_ID == "SYOBJR-00006" and str(TreeParam) == "Quote Preview":
                            rem_list_sp = ["QUOTE_ITEM_FORECAST_PART_RECORD_ID","ITEM_LINE_SEQUENCE","SCHEDULE_MODE","DELIVERY_MODE"]
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                            
                        elif RECORD_ID == "SYOBJR-98837" and str(TreeParam) == "Contract Preview":
                            rem_list_sp = ["CONTRACT_ITEM_FORECAST_PART_RECORD_ID","MATPRIGRP_ID","SCHEDULE_MODE","DELIVERY_MODE"]
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                            
                        elif RECORD_ID == "SYOBJR-00008" and str(TreeParam) == "Quote Items":
                            rem_list_sp = ['TARGET_PRICE','CEILING_PRICE','SALES_DISCOUNT_PRICE','BD_PRICE','BD_PRICE_MARGIN','DISCOUNT','SALES_PRICE','YEAR_OVER_YEAR','YEAR_1','YEAR_2','YEAR_3','YEAR_4','YEAR_5','SERVICE_DESCRIPTION','QUANTITY']
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])  
                        if RECORD_ID == "SYOBJR-98792" and str(TreeParam) == "Quote Preview":                    
                            rem_list_sp = ["QUOTE_ITEM_RECORD_ID","PO_NOTES","QUANTITY","EQUIPMENT_QUANTITY","TARGET_PRICE","CEILING_PRICE","SALES_DISCOUNT_PRICE","BD_PRICE","BD_PRICE_MARGIN","DISCOUNT","SALES_PRICE","YEAR_OVER_YEAR","YEAR_1","YEAR_2",]
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                            
                        elif RECORD_ID == "SYOBJR-98819" and str(TreeParam) == "Contract Preview":                    
                            rem_list_sp = ["CONTRACT_ITEM_RECORD_ID","PO_NOTES","QUANTITY","DISCOUNT"]
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                            
                        else:
                            rem_list_sp = ['ITEM_TYPE','ITEM_STATUS','EQUIPMENT_QUANTITY','SALES_DISCOUNT_PRICE','DISCOUNT','UOM_ID']
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])
                    elif str(getQuotetype).upper() == "ZTBC - TOOL BASED" and  str(TreeParam) in ['Quote Items','Quote Preview','Contract Items','Contract Preview']:
                        if RECORD_ID == "SYOBJR-98795" and str(TreeParam) == "Quote Preview":
                            rem_list_sp = ["QUOTE_ITEM_COVERED_OBJECT_RECORD_ID","EQUIPMENT_STATUS","BD_DISCOUNT","DISCOUNT","BASE_PRICE","LIST_PRICE","BD_PRICE_MARGIN"]
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                                                 
                        elif RECORD_ID == "SYOBJR-98822" and str(TreeParam) == "Contract Preview":
                            rem_list_sp = ["CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID","EQUIPMENT_STATUS"]
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                            
                        if RECORD_ID == "SYOBJR-98792" and str(TreeParam) == "Quote Preview":                    
                            rem_list_sp = ["QUOTE_ITEM_RECORD_ID","PO_NOTES","ONSITE_PURCHASE_COMMIT","DISCOUNT"]
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                            
                        elif RECORD_ID == "SYOBJR-98819" and str(TreeParam) == "Contract Preview":                    
                            rem_list_sp = ["CONTRACT_ITEM_RECORD_ID","PO_NOTES","ONSITE_PURCHASE_COMMIT"]
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                            
                        else:     
                            rem_list_sp = ['ITEM_TYPE','ITEM_STATUS','ONSITE_PURCHASE_COMMIT','UOM_ID']
                            #rem_list_sp = ['ONSITE_PURCHASE_COMMIT']
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])
                    elif str(getQuotetype).upper() == "ZTBC - TOOL BASED" and  (str(TreeParentParam) =='Quote Items' or str(TreeSuperParentParam) == "Quote Items" or str(TopTreeSuperParentParam) == "Quote Items" or str(TreeParam) == "Quote Items"):
                        if RECORD_ID == "SYOBJR-00009" and (str(TreeParentParam) == "Quote Items" or str(TreeSuperParentParam) == "Quote Items" or str(TopTreeSuperParentParam) == "Quote Items" or str(TreeParam) == "Quote Items") :
                            if TreeParam == 'Quote Items':                                  
                                rem_list_sp = ["BASE_PRICE"]
                            else:
                                rem_list_sp = ["SERVICE_ID","BASE_PRICE"]    
                            Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                                                         
                    else:                    
                        Columns = obj_obj.COLUMNS
            # elif  Product.Attributes.GetByName("QSTN_SYSEFL_CT_00004"):
                
            #     getContracttype = Product.Attributes.GetByName("QSTN_SYSEFL_CT_00004").GetValue()
            #     if str(getContracttype).upper() == "ZWK1 - SPARES" and  str(TreeParam) in ['Contract Items','Contract Preview']:
            #         if RECORD_ID == "SYOBJR-98837" and str(TreeParam) == "Contract Preview":
            #             rem_list_sp = ["CONTRACT_ITEM_FORECAST_PART_RECORD_ID","MATPRIGRP_ID","SCHEDULE_MODE","DELIVERY_MODE"]
            #             Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])    
                        
            #         if RECORD_ID == "SYOBJR-98819" and str(TreeParam) == "Contract Preview":                    
            #             rem_list_sp = ["CONTRACT_ITEM_RECORD_ID","PO_NOTES","QUANTITY","DISCOUNT"]
            #             Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])    
                        
            #         else:
            #             rem_list_sp = ['ITEM_TYPE','ITEM_STATUS','DISCOUNT','UOM_ID']
            #             Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                        
            #     elif str(getContracttype).upper() == "ZTBC - TOOL BASED" and  str(TreeParam) in ['Contract Items','Contract Preview']:
                    
            #         if RECORD_ID == "SYOBJR-98822" and str(TreeParam) == "Contract Preview":
            #             rem_list_sp = ["CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID","EQUIPMENT_STATUS"]
            #             Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])    
                        
            #         if RECORD_ID == "SYOBJR-98819" and str(TreeParam) == "Contract Preview":                    
            #             rem_list_sp = ["CONTRACT_ITEM_RECORD_ID","PO_NOTES","ONSITE_PURCHASE_COMMIT"]
            #             Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])    
                        
            #         else:     
            #             rem_list_sp = ['ITEM_TYPE','ITEM_STATUS','ONSITE_PURCHASE_COMMIT','UOM_ID','QUANTITY']
            #             #rem_list_sp = ['ONSITE_PURCHASE_COMMIT']
            #             Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])                            
            #     else:
                    
            #         Columns = obj_obj.COLUMNS 
            # Trace.Write("CHKNG_J "+str(Columns))
            #Hide columns in Related list based on Quote type End
            Obj_Name = obj_obj.OBJ_REC_ID
            
            COLUMN_REC_ID = obj_obj.COLUMN_REC_ID
            
            REC_NAME = obj_obj.NAME
            objsk_permiss = Sql.GetFirst(
                "SELECT CAN_ADD, CAN_EDIT, CAN_DELETE FROM SYOBJR  WHERE SAPCPQ_ATTRIBUTE_NAME = '" + str(RECORD_ID) + "'"
            )
            PARENT_LOOKUP_REC_ID = obj_obj.PARENT_LOOKUP_REC_ID
            
            if objsk_permiss:
                if str(objsk_permiss.CAN_EDIT).upper() == "TRUE":
                    Action_permission["Edit"] = obj_obj.CAN_EDIT                    
                else:
                    Action_permission["Edit"] = objsk_permiss.CAN_EDIT                    
                if str(objsk_permiss.CAN_DELETE).upper() == "TRUE":
                    Action_permission["Delete"] = obj_obj.CAN_DELETE                    
                else:
                    Action_permission["Delete"] = objsk_permiss.CAN_DELETE
            
            objd_where_obj = Sql.GetFirst("select * from  SYOBJD (NOLOCK) where RECORD_ID = '" + str(COLUMN_REC_ID) + "'")
            
            if objd_where_obj is not None:
                Wh_API_NAME = objd_where_obj.API_NAME
                Wh_OBJECT_NAME = objd_where_obj.OBJECT_NAME
            #Contract valid start date & End date Calculation--START
            
            Getyear = Sql.GetFirst("select CONTRACT_VALID_FROM,CONTRACT_VALID_TO from SAQTMT where MASTER_TABLE_QUOTE_RECORD_ID = '"+str(contract_quote_record_id)+"'")
            if Getyear:
                start_date = datetime(Getyear.CONTRACT_VALID_FROM)
                end_date = datetime(Getyear.CONTRACT_VALID_TO)
                mm = (end_date. year - start_date. year) * 12 + (end_date. month - start_date. month)
                quotient, remainder = divmod(mm, 12)
                getyears = quotient + (1 if remainder > 0 else 0)
                
                if not getyears:
                    getyears = 1
                if Quote is not None:
                    Quote.GetCustomField('GetBillingMatrix_Year').Content = str(getyears)
                if getyears == 1:
                    rem_list_sp = ["YEAR_2","YEAR_3","YEAR_4","YEAR_5"]
                    Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp]) 
                elif getyears == 2:
                    rem_list_sp = ["YEAR_3","YEAR_4","YEAR_5"]
                    Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])
                elif getyears == 3:
                    rem_list_sp = ["YEAR_4","YEAR_5"]
                    Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])
                elif getyears == 4:
                    rem_list_sp = ["YEAR_5"]
                    Columns = str([ele for ele in  eval(Columns) if ele not in rem_list_sp])
                else:
                    Columns
            #Contract valid start date & End date Calculation--END
            # Billing Matrix - Pivot - Start
            if Wh_OBJECT_NAME == 'SAQIBP':
                if SubTab:
                    Trace.Write('SubTab----'+str(SubTab))
                    end = int(SubTab.split(' ')[-1]) * 12
                    start = end - 12 + 1
                    
                item_billing_plans_obj = Sql.GetList("""SELECT FORMAT(BILLING_DATE, 'MM-dd-yyyy') as BILLING_DATE FROM (SELECT ROW_NUMBER() OVER(ORDER BY BILLING_DATE)
                                    AS ROW, * FROM (SELECT DISTINCT BILLING_DATE
                                                        FROM SAQIBP (NOLOCK) WHERE QUOTE_RECORD_ID = '{}' 
                                                        GROUP BY EQUIPMENT_ID, BILLING_DATE) IQ) OQ WHERE OQ.ROW BETWEEN {} AND {}""".format(
                                                            contract_quote_record_id, start, end))
                if item_billing_plans_obj:
                    billing_date_column = [item_billing_plan_obj.BILLING_DATE for item_billing_plan_obj in item_billing_plans_obj]
                    billing_date_column_joined = ",".join(["'{}'".format(billing_data) for billing_data in billing_date_column])
                    Columns = Columns.replace(']', ','+billing_date_column_joined+']')   
            # Billing Matrix - Pivot - End
            CurrentObj = Sql.GetFirst(
                "select API_NAME, OBJECT_NAME from  SYOBJD (NOLOCK) where PARENT_OBJECT_RECORD_ID = '"
                + str(PARENT_LOOKUP_REC_ID)
                + "' and DATA_TYPE ='AUTO NUMBER'"
            )
            
            if CurrentObj is not None:
                CurrentObj_Recordno = CurrentObj.API_NAME
                CurrentObj_Name = CurrentObj.OBJECT_NAME
            CurrentObj2 = Sql.GetFirst(
                "select OBJECT_NAME from  SYOBJD (NOLOCK) where PARENT_OBJECT_RECORD_ID = '" + str(Obj_Name) + "' "
            )
            
            if CurrentObj2 != "" and CurrentObj2 is not None:
                CurrentObj_Names = CurrentObj2.OBJECT_NAME
            Qstn_where_obj = Sql.GetFirst(
                "select QN.* from SYSEFL (NOLOCK) QN INNER JOIN SYSECT (nolock) SE on SE.RECORD_ID = QN.SECTION_RECORD_ID INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID where QN.API_NAME = '"
                + str(CurrentObj_Name)
                + "' and QN.API_FIELD_NAME = '"
                + str(CurrentObj_Recordno).strip()
                + "' and QN.SAPCPQ_ATTRIBUTE_NAME like '%"
                + str(crnt_prd_val)
                + "%' and PG.TAB_RECORD_ID != '' "
            )
            RecAttValue = ""
            
            if Qstn_where_obj is not None:
                Qstn_REC_ID = Qstn_where_obj.SAPCPQ_ATTRIBUTE_NAME                
                if Qstn_REC_ID != "":
                    wh_Qstn_REC_ID = "QSTN_" + Qstn_REC_ID.replace("-", "_")                    
                    RecAttValue = ""
                    try:                        
                        RecAtt = productAttributesGetByName(str(wh_Qstn_REC_ID))                        
                        if RecAtt is not None:                            
                            RecAttValue = RecAtt.GetValue()
                    except:
                        RecAttValue = ""
            table_id = obj_obj.SAPCPQ_ATTRIBUTE_NAME.replace("-", "_") + "_" + str(Obj_Name).replace("-", "_")
            table_ids = "#" + str(table_id)
        if 'SYOBJR_98797' in table_id:
            table_header = (
                '<table id="'
                + table_id
                + '" data-pagination="false" data-filter-control="true" data-detail-view="true" data-maintain-selected="true" data-locale = "en-US"><thead>'
            )
        else:
            table_header = (
                '<table id="'
                + table_id
                + '" data-pagination="false" data-filter-control="true"  data-maintain-selected="true" data-locale = "en-US"><thead>'
            )
        related_list_edit_permission = False
        related_list_delete_permission = False
        #Realted list permissions start
        related_list_permission_obj = Sql.GetFirst(
            """
                                    SELECT
                            SYOBJR.RELATED_LIST_SINGULAR_NAME,SYPROH.CAN_ADD,SYPROH.CAN_DELETE,SYPROH.CAN_EDIT,SYOBJR.COLUMN_REC_ID ,SYOBJR.COLUMNS,SYOBJR.DISPLAY_ORDER, SYOBJR.NAME,SYOBJR.OBJ_REC_ID,SYOBJR.PARENT_LOOKUP_REC_ID,SYOBJR.RECORD_ID,SYOBJR.SAPCPQ_ATTRIBUTE_NAME,SYOBJR.VISIBLE
                        FROM
                            SYOBJR (NOLOCK)
                        JOIN SYPROH (NOLOCK) ON SYPROH.OBJECT_RECORD_ID = SYOBJR.OBJ_REC_ID
                        JOIN USERS_PERMISSIONS (NOLOCK) UP ON UP.PERMISSION_ID = SYPROH.PROFILE_RECORD_ID
                        WHERE
                            SYOBJR.SAPCPQ_ATTRIBUTE_NAME = '{RECORD_ID}' AND
                            SYPROH.VISIBLE = 1 AND
                            UP.USER_ID = '{get_user_id}'
                            """.format(
                RECORD_ID=str(RECORD_ID), get_user_id=str(get_user_id)
            )
        )
        #Realted list permissions end
        '''related_list_permission_obj = Sql.GetFirst(
            """
                                    SELECT
                                        SYOBJR.RECORD_ID,SYOBJR.SAPCPQ_ATTRIBUTE_NAME, SYOBJR.PARENT_LOOKUP_REC_ID, SYOBJR.OBJ_REC_ID,
                                        SYOBJR.NAME, SYOBJR.COLUMN_REC_ID, SYOBJR.COLUMNS,
                                        SYOBJR.CAN_ADD, SYOBJR.CAN_EDIT, SYOBJR.CAN_DELETE, SYOBJR.RELATED_LIST_SINGULAR_NAME,
                                        SYOBJR.DISPLAY_ORDER, SYOBJR.ORDERS_BY, SYOBJR.VISIBLE
                                    FROM
                                        SYOBJR (NOLOCK)

                                    WHERE

                                        SYOBJR.SAPCPQ_ATTRIBUTE_NAME = '{RECORD_ID}'
                                    """.format(
                RECORD_ID=str(RECORD_ID)
            )
        )'''       

        if related_list_permission_obj is not None:
            related_list_edit_permission = related_list_permission_obj.CAN_EDIT
            related_list_delete_permission = related_list_permission_obj.CAN_DELETE
            related_list_permissions.update(
                {"canAdd": related_list_permission_obj.CAN_ADD, "canDelete": related_list_delete_permission}
            )

        objRecName = ""
        # Billing Matrix - Pivot - Start
        column_before_pivot_change = ""
        # Billing Matrix - Pivot - End
        if Columns != "" and Obj_Name != "":
            
            objh_obj = Sql.GetFirst("select * from SYOBJH (NOLOCK) where RECORD_ID = '" + str(Obj_Name) + "' ")
            if objh_obj is not None:
                ObjectName = objh_obj.OBJECT_NAME.strip()
                objRecName = objh_obj.RECORD_NAME.strip()
            Objd_Obj = Sql.GetList(
                "select FIELD_LABEL,API_NAME,LOOKUP_OBJECT,LOOKUP_API_NAME,DATA_TYPE,FORMULA_DATA_TYPE,FIELD_SHORT_LABEL from  SYOBJD (NOLOCK) where OBJECT_NAME = '"
                + str(ObjectName)
                + "' "
            )

            if Objd_Obj is not None:
                for attr in Objd_Obj:

                    attrs_datatype_dict[str(attr.API_NAME)] = str(attr.DATA_TYPE)
                    if attr.FIELD_SHORT_LABEL is not None and str(attr.FIELD_SHORT_LABEL) != "":
                        attr_list[str(attr.API_NAME)] = str(attr.FIELD_SHORT_LABEL)
                    else:
                        attr_list[str(attr.API_NAME)] = str(attr.FIELD_LABEL)
                    if (
                        str(attr.LOOKUP_API_NAME) != ""
                        and str(attr.LOOKUP_API_NAME) is not None
                        and str(attr.LOOKUP_API_NAME) not in ["CONTROLLING_FIELD", "DEPENDENT_FIELD"]
                    ):
                        lookup_disply_list.append(str(attr.API_NAME))
                        
                checkbox_list = [
                    inn.API_NAME for inn in Objd_Obj if (inn.DATA_TYPE == "CHECKBOX" or inn.FORMULA_DATA_TYPE == "CHECKBOX")
                ]
                
                right_align_list = [
                    inn.API_NAME
                    for inn in Objd_Obj
                    if (
                        inn.DATA_TYPE == "CURRENCY"
                        or inn.API_NAME == "SALE_DISCOUNT" or inn.API_NAME == "ANNUAL_QUANTITY" or inn.API_NAME == "ONSITE_PURCHASE_COMMIT"   or (inn.DATA_TYPE == "FORMULA" and inn.FORMULA_DATA_TYPE == "NUMBER")
                        or inn.FORMULA_DATA_TYPE == "CURRENCY"
                        or inn.DATA_TYPE == "PERCENT"
                        or inn.FORMULA_DATA_TYPE == "PERCENT"
                        or inn.DATA_TYPE == "NUMBER"
                    )
                ]
                
                center_align_list = [
                    inn.API_NAME
                    for inn in Objd_Obj
                    if (
                        inn.DATA_TYPE == "DATE" or inn.API_NAME == "EFFECTIVEDATE_BEG" or inn.API_NAME == "EFFECTIVEDATE_END" or inn.API_NAME == "ITEM_LINE_SEQUENCE" or inn.API_NAME == "WARRANTY_END_DATE" and  inn.FORMULA_DATA_TYPE == "DATE"
                    )
                ]
                
                lookup_list = {
                    ins.LOOKUP_API_NAME: ins.API_NAME
                    for ins in Objd_Obj
                    if str(ins.LOOKUP_API_NAME) != "" and str(ins.LOOKUP_API_NAME) is not None
                }
            
            lookup_disply_list123 = ""
            lookup_str = ",".join(list(lookup_disply_list))
            if len(list(lookup_disply_list)) > 1:
                lookup_disply_list123 = list(lookup_disply_list)[0]
            else:
                if len(list(eval(Columns))) > 1:
                    lookup_disply_list123 = list(eval(Columns))[0]
            obj_str = ",".join(list(eval(Columns)))
            if lookup_str != "":
                select_obj_str = str(obj_str) + "," + str(lookup_str)
            else:
                select_obj_str = str(obj_str)
            
            name = select_obj_str.split(",")
            for text in name:                
                s = Sql.GetList(
                    "select DATA_TYPE,LENGTH,API_NAME,DECIMALS,FORMULA_DATA_TYPE from  SYOBJD (NOLOCK) WHERE LTRIM(RTRIM(API_NAME))='"
                    + str(text).strip()
                    + "' and OBJECT_NAME='"
                    + str(ObjectName).strip()
                    + "'"
                )                
                for ins in s:                    
                    if (ins.DATA_TYPE == "DATE" or ins.FORMULA_DATA_TYPE == "DATE") or (
                        ins.API_NAME
                        in [
                            "EFFECTIVEDATE_BEG",
                            "EFFECTIVEDATE_END",
                            "PROMOTION_START_DATE",
                            "PROMOTION_END_DATE",
                            "EXCHANGE_RATE_DATE",
                        ]
                    ):  
                        if str(RECORD_ID) == "SYOBJR-00007" and ins.API_NAME == 'BILLING_DATE':
                            text = "CONVERT(VARCHAR(10),FORMAT(" + str(text) + ",'MM-dd-yyyy'),101) AS [" + str(text) + "]"
                            texts = texts + "," + str(text)                  
                        elif texts != "":
                            text = "CONVERT(VARCHAR(10)," + str(text) + ",101) AS [" + str(text) + "]"
                            texts = texts + "," + str(text)
                        else:
                            text = "CONVERT(VARCHAR(10)," + str(text) + ",101) AS [" + str(text) + "]"
                            texts = str(text)
                            
                    else:
                        if col != "":
                            col = col + "," + text                            
                        else:
                            col = str(text)                            
            if texts != "":
                col = col + "," + texts
            # Billing Matrix - Pivot - Start            
            if billing_date_column:
                column_before_pivot_change = col
                col += ","+ ",".join(billing_date_column)
            # Billing Matrix - Pivot - End
            select_obj_str = col
            
            orderStr = """
                                    SELECT
                                        SYOBJR.RECORD_ID,SYOBJR.SAPCPQ_ATTRIBUTE_NAME, SYOBJR.PARENT_LOOKUP_REC_ID, SYOBJR.OBJ_REC_ID,
                                        SYOBJR.NAME, SYOBJR.COLUMN_REC_ID, SYOBJR.COLUMNS,
                                        SYOBJR.CAN_ADD, SYOBJR.CAN_EDIT, SYOBJR.CAN_DELETE, SYOBJR.RELATED_LIST_SINGULAR_NAME,
                                        SYOBJR.DISPLAY_ORDER, SYOBJR.ORDERS_BY
                                    FROM
                                        SYOBJR (NOLOCK)

                                    WHERE

                                        SYOBJR.SAPCPQ_ATTRIBUTE_NAME = '{RECORD_ID}'
                                    """.format(
                RECORD_ID=str(RECORD_ID)
            )
            OrderBy_obj = Sql.GetFirst(orderStr)
            
            if Qstn_REC_ID != "" and Wh_API_NAME != "":                
                if OrderBy_obj is not None:
                    if OrderBy_obj.ORDERS_BY:
                        Wh_API_NAMEs = OrderBy_obj.ORDERS_BY
                    else:
                        Wh_API_NAMEs = Wh_API_NAME
                else:
                    Wh_API_NAMEs = Wh_API_NAME
                
                TreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")                

                if RECORD_ID == "SYOBJR-95868":
                    
                    Qury_str = (
                        "select top "
                        + str(PerPage)
                        + " "
                        + "SYSEFL."
                        + str(select_obj_str)
                        + ",SYSEFL.CpqTableEntryId from "
                        + str(ObjectName)
                        + " (nolock) INNER JOIN SYSECT (nolock) ON SYSEFL.SECTION_RECORD_ID = SYSECT.RECORD_ID  AND "
                        + str(Wh_API_NAME)
                        + " = '"
                        + str(RecAttValue)
                        + "' "
                        + "where SYSEFL.SECTION_NAME = '"
                        + str(TreeParentParam)
                        + "' ORDER BY abs(SYSEFL.DISPLAY_ORDER)"
                    )
                    QuryCount_str = (
                        "select count(*) as cnt from "
                        + str(ObjectName)
                        + " (nolock) INNER JOIN SYSECT (nolock) ON SYSEFL.SECTION_RECORD_ID = SYSECT.RECORD_ID and "
                        + str(Wh_API_NAME)
                        + " = '"
                        + str(RecAttValue)
                        + "' where SYSEFL.SECTION_NAME = '"
                        + str(TreeParentParam)
                        + "'"
                    )                    
                elif RECORD_ID == "SYOBJR-95843" and TreeParentParam != "" :
                    RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_03295").GetValue()
                    
                    Qury_str = (
                        "select top "
                        + str(PerPage)
                        + " * "
                        + " from "
                        + str(ObjectName)
                        + " (nolock) WHERE "
                        + str(Wh_API_NAME)
                        + " = '"
                        + str(RecAttValue)
                        + "' AND PAGE_NAME = '"
                        + str(TreeParentParam)
                        + "'"
                    )
                    QuryCount_str = (
                        "select count(*) as cnt from "
                        + str(ObjectName)
                        + " (nolock) WHERE "
                        + str(Wh_API_NAME)
                        + " = '"
                        + str(RecAttValue)
                        + "' AND PAGE_NAME = '"
                        + str(TreeParentParam)
                        + "'"
                    )
                    
                   
                elif RECORD_ID == "SYOBJR-94441":
                    Trace.Write('94441###------')                    
                    RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00152").GetValue()
                    Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                
                elif RECORD_ID == "SYOBJR-94587" and TreeParam =="Section Actions" :
                    Trace.Write("sectio111----------")
                    RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                    
                    tabRecord = ""
                    gettabres = Sql.GetFirst(
                        "Select TB.RECORD_ID,TB.PAGE_NAME,SE.SECTION_NAME from SYTABS (NOLOCK)TB INNER JOIN SYPAGE (NOLOCK) PG ON PG.TAB_RECORD_ID = TB.RECORD_ID INNER JOIN SYSECT (NOLOCK) SE ON SE.PAGE_RECORD_ID = PG.RECORD_ID where TB.TAB_LABEL = '" + str(TreeSecondSuperTopParentParam) + "'AND SE.SECTION_NAME = '"+str(TreeParentParam)+"'"
                    )
                    if gettabres:                        
                        tabRecord = str(gettabres.SECTION_NAME)
                    Qustr = " where SECTION_NAME = '" + str(tabRecord) + "'"
                    # Qustr = " where " + str(Wh_API_NAME) + " = '" + str(gettabidval) + "'"
                
                elif RECORD_ID == "SYOBJR-94489":                    
                    GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()                   

                    Qury_str = (
                        "select DISTINCT top 10 RECORD_ID,SECTION_NAME,DISPLAY_ORDER,PARENT_SECTION_RECORD_ID,OWNER_RECORD_ID,PRIMARY_OBJECT_RECORD_ID,PAGE_LABEL,PAGE_RECORD_ID,CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by DISPLAY_ORDER) AS ROW,* from SYSECT where PAGE_LABEL = '"
                        + str(TreeParentParam)
                        + "') m where m.ROW BETWEEN 1 and 10"
                    )
                    
                    QuryCount_str = (
                        "select count(*) as cnt from SYSECT (nolock) where PAGE_LABEL = '" + str(TreeParentParam) + "'"
                    )
                elif RECORD_ID == "SYOBJR-97459":
                    getrecordpage = ""
                    
                    gettabval = Sql.GetFirst(
                        "Select RECORD_ID,PAGE_NAME from SYPAGE where PAGE_LABEL = '" + str(TreeParentParam) + "'"
                    )
                    if gettabval:
                        getrecordpage = gettabval.PAGE_NAME
                  
                    Qustr = " where PAGE_NAME = '" + str(getrecordpage) + "'"
                elif RECORD_ID == "SYOBJR-94490":
                    tabRecord = ""
                   
                    GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()                   
                    gettabres = Sql.GetFirst(
                        "Select RECORD_ID from SYSECT where PAGE_LABEL = '"
                        + str(TopTreeSuperParentParam)
                        + "' and SECTION_NAME = '"
                        + str(TreeParentParam)
                        + "'"
                    )
                    if gettabres:                        
                        tabRecord = str(gettabres.RECORD_ID)
                    
                    Qustr = " where SECTION_RECORD_ID = '" + str(tabRecord) + "'"                    
                elif RECORD_ID == "SYOBJR-98782":
                    getsectvalue = ""

                    GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                    
                    gettabval = Sql.GetFirst(
                        "Select RECORD_ID,PAGE_NAME,TAB_LABEL from SYTABS where TAB_LABEL = '" + str(TreeParentParam) + "'"
                    )
                    if gettabval:
                        getpagename = gettabval.TAB_LABEL
                    Qustr = " where TAB_LABEL = '" + str(getpagename) + "'"
                    
                elif RECORD_ID == "SYOBJR-98784" and TreeParam !="Section Actions":
                    gettabval = getptabname = ""
                    CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                    GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                    gettabval = Sql.GetFirst(
                        "Select RECORD_ID,PAGE_NAME,TAB_LABEL from SYTABS where PAGE_NAME = '"
                        + str(TreeParentParam)
                        + "' and TAB_LABEL = '"
                        + str(TopTreeSuperParentParam)
                        + "'"
                    )                    
                    if gettabval:
                        getptabname = gettabval.RECORD_ID
                    Qustr = " where TAB_RECORD_ID = '" + str(getptabname) + "'"                    
                elif RECORD_ID == "SYOBJR-98784" and TreeParam =="Section Actions":
                    gettabval= Sql.GetFirst(
                        "Select RECORD_ID,ACTION_NAME from SYPSAC where SECTION_NAME = '" + str(TreeParentParam) + "'"
                    )
                    
                
                elif RECORD_ID == "SYOBJR-94587" and TreeParam =="Section Actions":
                    Trace.Write("sectio----------")
                    gettabval = ""

                    GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                    gettabval = Sql.GetFirst(
                        "Select RECORD_ID,PAGE_NAME from SYTABS where TAB_LABEL = '" + str(TreeFirstSuperTopParentParam) + "'"
                    )
                    if gettabval:
                        getpagename = gettabval.PAGE_NAME
                    Qustr = " where PAGE_NAME = '" + str(getpagename) + "'"                    
                # elif RECORD_ID == "SYOBJR-98788":
                  
                #     if ObjectName == 'SAQTSV'and TreeParentParam == 'Offerings':
                #         Qustr = " WHERE SERVICE_TYPE = '{}'".format(TreeParam)
                else:                    
                    Curr_OM_Node = Product.GetGlobal("Curr_OM_Node")                    
                    PLN_ID = Product.GetGlobal("PLN_ID")
                    if PLN_ID != "":
                        PLN_ID = PLN_ID.split("-")[1]
                    SORG_ID = Product.GetGlobal("SORG_ID")
                    if SORG_ID != "":
                        SORG_ID = SORG_ID.split("-")[1]

                    elif RECORD_ID == "SYOBJR-93121":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " PROFILE_APP_RECORD_ID,APP_ID,VISIBLE,[DEFAULT],PROFILE_RECORD_ID,CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by APP_ID) AS ROW, * from SYPRAP (nolock)  where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " order by APP_ID"
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from SYPRAP (nolock)  where PROFILE_ID = '" + str(RecAttValue) + "'"
                        )

                    elif RECORD_ID == "SYOBJR-93122":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        Qury_str = (
                            "select  top "
                            + str(PerPage)
                            + " PROFILE_OBJECT_RECORD_ID,OBJECT_RECORD_ID,OBJECT_NAME, VISIBLE,CpqTableEntryId from ( select ROW_NUMBER() OVER( order by PROFILE_OBJECT_RECORD_ID) AS ROW, PROFILE_OBJECT_RECORD_ID,OBJECT_RECORD_ID,OBJECT_NAME, VISIBLE,CpqTableEntryId from SYPROH (nolock) where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + "  order by OBJECT_NAME"
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from SYPROH (nolock) where  PROFILE_ID = '" + str(RecAttValue) + "'"
                        )
                    
                    elif RECORD_ID == "SYOBJR-93169":
                        CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        objrecid = ""
                        QueryTest = Sql.GetFirst(
                            "select TAB_RECORD_ID from SYPRTB (NOLOCK) where TAB_ID='"
                            + str(CommonTreeParentParam)
                            + "' and APP_ID = '"
                            + str(CommonTreeTopSuperParentParam)
                            + "' and PROFILE_ID = '"
                            + str(RecAttValue)
                            + "'"
                        )
                        if QueryTest is not None:
                            objrecid = str(QueryTest.TAB_RECORD_ID)
                        

                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " PROFILE_ACTION_RECORD_ID,ACTION_ID,VISIBLE,CpqTableEntryId from ( select ROW_NUMBER() OVER( order by ACTION_ID) AS ROW,PROFILE_ACTION_RECORD_ID,ACTION_ID,VISIBLE,CpqTableEntryId from SYPRAC (nolock) where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "'  and TAB_RECORD_ID='"
                            + str(objrecid)
                            + "') m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " order by ACTION_ID"
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from SYPRAC (nolock)  where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and TAB_RECORD_ID='"
                            + str(objrecid)
                            + "'"
                        )

                    elif RECORD_ID == "SYOBJR-93160":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        GetAppname_query = ""
                        if TreeTopSuperParentParam == "App Level Permissions":
                            CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")
                            
                            GetAppname_query = Sql.GetFirst(
                                "SELECT TAB_RECORD_ID FROM SYPRTB where APP_ID = '"
                                + str(CommonTreeSuperParentParam)
                                + "' and TAB_ID = '"
                                + str(TreeParam)
                                + "'"
                            )
                        else:
                            TreeParam = Product.GetGlobal("CommonTreeParentParam")
                            GetAppname_query = Sql.GetFirst(
                                "SELECT TAB_RECORD_ID FROM SYPRTB where APP_ID = '"
                                + str(TreeTopSuperParentParam)
                                + "' and TAB_ID = '"
                                + str(TreeParam)
                                + "'"
                            )

                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " *  from ( select ROW_NUMBER() OVER(order by P.PROFILE_RECORD_ID) AS ROW, P.PROFILE_SECTION_RECORD_ID,P.SECTION_RECORD_ID,P.SECTION_ID,P.TAB_ID,P.VISIBLE,P.PROFILE_RECORD_ID,P.CpqTableEntryId,s.DISPLAY_ORDER from SYPRSN P (nolock) inner join SYSECT s on s.RECORD_ID = P.SECTION_RECORD_ID where P.PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and P.TAB_ID = '"
                            + str(TreeParam)
                            + "' and P.TAB_RECORD_ID ='"
                            + str(GetAppname_query.TAB_RECORD_ID)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + "  order by m.DISPLAY_ORDER"
                        )
                        
                        QuryCount_str = (
                            "select count(*) as cnt from SYPRSN (nolock)  where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and TAB_ID = '"
                            + str(TreeParam)
                            + "' and TAB_RECORD_ID ='"
                            + str(GetAppname_query.TAB_RECORD_ID)
                            + "'"
                        )

                    elif RECORD_ID == "SYOBJR-93188":
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        TreeFirstSuperTopParentParam = Product.GetGlobal("CommonTreeFirstSuperTopParentParam")
                        CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        GetAppname_query = ""
                        
                        QueryTest = SqlHelper.GetFirst(
                            "select TAB_RECORD_ID from SYPRTB (NOLOCK) where TAB_ID='"
                            + str(CommonTreeTopSuperParentParam)
                            + "' and APP_ID = '"
                            + str(TreeFirstSuperTopParentParam)
                            + "' and PROFILE_ID = '"
                            + str(RecAttValue)
                            + "'"
                        )
                        if QueryTest is not None:
                            objrecid = str(QueryTest.TAB_RECORD_ID)
                            
                            GetAppname_query = SqlHelper.GetFirst(
                                "SELECT SECTION_RECORD_ID FROM SYPRSN where TAB_RECORD_ID = '"
                                + str(objrecid)
                                + "' and TAB_ID = '"
                                + str(CommonTreeTopSuperParentParam)
                                + "' and SECTION_ID = '"
                                + str(CommonTreeParentParam)
                                + "' and PROFILE_ID = '"
                                + str(RecAttValue)
                                + "'"
                            )
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " PROFILE_ACTION_RECORD_ID,ACTION_ID,VISIBLE,PROFILE_RECORD_ID,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by PROFILE_RECORD_ID) AS ROW, * from SYPRAC (nolock)  where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "'  and SECTION_RECORD_ID ='"
                                + str(GetAppname_query.SECTION_RECORD_ID)
                                + "' and  SECTION_ID = '"
                                + str(CommonTreeParentParam)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " "
                            )
                            
                            QuryCount_str = (
                                "select count(*) as cnt from SYPRAC (nolock)  where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "'   and SECTION_RECORD_ID ='"
                                + str(GetAppname_query.SECTION_RECORD_ID)
                                + "' and  SECTION_ID = '"
                                + str(CommonTreeParentParam)
                                + "'"
                            )

                    elif RECORD_ID == "SYOBJR-93162":

                        CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")
                        CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                        CommonTopTreeSuperParentParam = Product.GetGlobal("CommonTopTreeSuperParentParam")
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        TreeFirstSuperTopParentParam = Product.GetGlobal("CommonTreeFirstSuperTopParentParam")
                        if TreeFirstSuperTopParentParam == "App Level Permissions":
                            getTabrec = Sql.GetFirst(
                                "SELECT TAB_RECORD_ID from SYPRTB where APP_ID = '"
                                + str(CommonTopTreeSuperParentParam)
                                + "' and PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and TAB_ID = '"
                                + str(CommonTreeSuperParentParam)
                                + "'"
                            )
                            sectrecid = Tabrecordid = ""
                            if getTabrec is not None:
                                Tabrecordid = str(getTabrec.TAB_RECORD_ID)
                                
                                getsectrec = Sql.GetFirst(
                                    "SELECT SECTION_RECORD_ID from SYPRSN where TAB_RECORD_ID = '"
                                    + str(Tabrecordid)
                                    + "' and SECTION_ID ='"
                                    + str(TreeParam)
                                    + "'"
                                )
                                if getsectrec is not None:
                                    sectrecid = str(getsectrec.SECTION_RECORD_ID)

                        else:
                            getTabrec = Sql.GetFirst(
                                "SELECT TAB_RECORD_ID from SYPRTB where APP_ID = '"
                                + str(TreeFirstSuperTopParentParam)
                                + "' and PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and TAB_ID = '"
                                + str(CommonTreeTopSuperParentParam)
                                + "'"
                            )
                            sectrecid = Tabrecordid = ""
                            if getTabrec is not None:
                                Tabrecordid = str(getTabrec.TAB_RECORD_ID)
                                
                                getsectrec = Sql.GetFirst(
                                    "SELECT SECTION_RECORD_ID from SYPRSN where TAB_RECORD_ID = '"
                                    + str(Tabrecordid)
                                    + "' and SECTION_ID ='"
                                    + str(CommonTreeParentParam)
                                    + "'"
                                )
                                if getsectrec is not None:
                                    sectrecid = str(getsectrec.SECTION_RECORD_ID)
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " * from ( select ROW_NUMBER() OVER(order by P.SECTION_FIELD_ID ) AS ROW,P.PROFILE_SECTIONFIELD_RECORD_ID,P.SECTIONFIELD_RECORD_ID,P.SECTION_FIELD_ID ,P.VISIBLE,P.EDITABLE,P.PROFILE_RECORD_ID,P.CpqTableEntryId,s.DISPLAY_ORDER from SYPRSF P (nolock)  inner join SYSEFL s on s.RECORD_ID = P.SECTIONFIELD_RECORD_ID where P.PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and P.SECTION_RECORD_ID = '"
                            + str(sectrecid)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + "  order by m.DISPLAY_ORDER"
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from SYPRSF (nolock)  where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and SECTION_RECORD_ID = '"
                            + str(sectrecid)
                            + "'"
                        )
                    elif RECORD_ID == "SYOBJR-94441":
                        Trace.Write('94441------')
                        RECORD_ID = Product.GetGlobal("RecordNo")                        
                        if RECORD_ID != "":
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " RECORD_ID,TAB_LABEL,TAB_TYPE,APP_RECORD_ID,APP_LABEL,ATTRIBUTE_NAME,CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by RECORD_ID) AS ROW, * from SYTABS (nolock)  where "
                                + str(ATTRIBUTE_VALUE_STR)
                                + " APP_RECORD_ID = '"
                                + str(RECORD_ID)
                                + "' ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + ""
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from "
                                + str(ObjectName)
                                + " (nolock) where APP_RECORD_ID = '"
                                + str(RECORD_ID)
                                + "' "
                            )
                    #elif RECORD_ID == "SYOBJR-95843":     
                        
                        #RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00200").GetValue()
   
                    elif RECORD_ID == "SYOBJR-93123":
                        Wh_API_NAME = "PROFILE_ID"
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()

                        Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'" 
                    elif RECORD_ID == "SYOBJR-94452":
                        Wh_API_NAME = "ROLE_RECORD_ID"
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00001").GetValue()

                        Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"                        
                    elif RECORD_ID == "SYOBJR-95800":                        
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        permiss_id = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00125").GetValue()
                        
                        Qury_str = (
                            "select DISTINCT TOP "
                            + str(PerPage)
                            + " ID,USERNAME,NAME,ACTIVE from ( select ROW_NUMBER() OVER(order by ID) AS ROW, ID,USERNAME,NAME,ACTIVE from USERS U (nolock) inner join users_permissions up on U.id = up.user_id   where up.permission_id = '"
                            + str(permiss_id)
                            + "'  ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = (
                            "select count(U.ID) as cnt from USERS U (nolock)  inner join users_permissions up on U.id = up.user_id  where  up.permission_id = '"
                            + str(permiss_id)
                            + "'  "
                        )
                    elif RECORD_ID == "SYOBJR-98784" and TreeParam =="Section Actions":
                        gettabval= Sql.GetFirst(
                            "Select RECORD_ID,ACTION_NAME from SYPSAC where SECTION_NAME = '" + str(TreeParentParam) + "'"
                        )                        
                    elif RECORD_ID == "SYOBJR-93130":
                        CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")
                        CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                        CommonTopTreeSuperParentParam = Product.GetGlobal("CommonTopTreeSuperParentParam")
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        if CommonTreeParentParam == "Object Level Permissions":
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " * from ( select ROW_NUMBER() OVER(order by PROFILE_RECORD_ID ASC) AS ROW,p.PROFILE_OBJECTFIELD_RECORD_ID,p.OBJECTFIELD_RECORD_ID,s.DISPLAY_ORDER,p.OBJECT_FIELD_ID,p.OBJECT_RECORD_ID,p.OBJECT_NAME,p.VISIBLE,p.EDITABLE,p.CpqTableEntryId from SYPROD p (nolock)  inner join  SYOBJD s on s.RECORD_ID = p.OBJECTFIELD_RECORD_ID where  p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.OBJECT_NAME='"
                                + str(TreeParam)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )

                            QuryCount_str = (
                                "select count(*) as cnt from SYPROD (nolock) where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and OBJECT_NAME='"
                                + str(TreeParam)
                                + "'"
                            )
                        else:

                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " * from ( select ROW_NUMBER() OVER(order by PROFILE_RECORD_ID ASC) AS ROW,p.PROFILE_OBJECTFIELD_RECORD_ID,p.OBJECTFIELD_RECORD_ID,s.DISPLAY_ORDER,p.OBJECT_FIELD_ID,p.OBJECT_RECORD_ID,p.OBJECT_NAME,p.VISIBLE,p.EDITABLE,p.CpqTableEntryId from SYPROD p (nolock)  inner join  SYOBJD s on s.RECORD_ID = p.OBJECTFIELD_RECORD_ID where  p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.OBJECT_NAME='"
                                + str(CommonTreeParentParam)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )

                            QuryCount_str = (
                                "select count(*) as cnt from SYPROD (nolock) where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and OBJECT_NAME='"
                                + str(CommonTreeParentParam)
                                + "'"
                            )
                    
                    else:
                        
                        if Wh_API_NAME == "FACTOR_ID":
                            dataobjPRICEFACTOR = Sql.GetFirst(
                                "SELECT FACTOR_ID FROM PRCAFC WHERE CALCULATION_FACTORS_RECORD_ID='" + str(RecAttValue) + "'"
                            )
                            if dataobjPRICEFACTOR:
                                Qustr = " where " + str(Wh_API_NAME) + " = '" + str(dataobjPRICEFACTOR.FACTOR_ID) + "'"
                        elif Wh_API_NAME == "APPROVAL_RECORD_ID":
                            dataobjAPHISTORY = Sql.GetFirst(
                                "SELECT APPROVAL_RECORD_ID FROM ACAPTX WHERE APPROVAL_TRANSACTION_RECORD_ID='" + str(RecAttValue) + "'"
                            )
                            if dataobjAPHISTORY:
                                Qustr = " where " + str(Wh_API_NAME) + " = '" + str(dataobjAPHISTORY.APPROVAL_RECORD_ID) + "'"
                        else:
                            CommonTreeParam = Product.GetGlobal("CommonTreeParam")
                            CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")
                            CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                            CommonTopTreeSuperParentParam = Product.GetGlobal("CommonTopTreeSuperParentParam")
                            CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                            if current_prod.upper() == "SALES" or  current_prod.upper() == "APPROVAL CENTER":
                                if Currenttab == "Contracts":
                                    RecAttValue = Quote.GetGlobal("contract_record_id")		
                                else:
                                    RecAttValue = Quote.GetGlobal("contract_quote_record_id")
                                Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                            elif current_prod.upper() == "PRICE MODELS" and TP == "Sales":                                
                                Qustr = " where QUOTE_CURRENCY = '"+str(PR_CURR)+"'"
                            elif current_prod.upper() == "PRICE MODELS" and TP == "Sales Orgs":
                                Qustr = " where DEF_CURRENCY = '"+str(PR_CURR)+"'"
                            elif current_prod.upper() == "PRICE MODELS" and TP == "Exchange Rates":
                                Qustr = " where FROM_CURRENCY = '"+str(PR_CURR)+"'"
                            elif str(RECORD_ID) == "SYOBJR-98815":
                                splitTP = TP.split('-')
                                TP = splitTP[1]
                                Qustr = "where SALESORG_ID = '"+str(TP)+"' and SORG_CURRENCY='"+str(PR_CURR)+"'"
                            elif str(RECORD_ID) == "SYOBJR-95824":
                                Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"                                   
                            # elif str(RECORD_ID) == "SYOBJR-93123":
                            #     Qustr = " where PROFILE_RECORD_ID = '" + str(RecAttValue) + "'"
                            # 
                            elif str(RECORD_ID) == "SYOBJR-95840": 
                                Wh_API_NAMEs = "PAGEACTION_RECORD_ID"                       
                                RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00723").GetValue()
                                Qustr =  " where SCRIPT_RECORD_ID = '" + str(RecAttValue) + "'"     
                            else:    
                                Trace.Write("check1234")                         
                                Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                                Trace.Write("Qustr"+str(Qustr))
                

                if str(Qury_str) == "" and str(QuryCount_str) == "":                    
                    QStrWhere = QStrWhere_Count = ""                   
                    TreeParam = Product.GetGlobal("TreeParam")
                    TreeParentParam = Product.GetGlobal("TreeParentLevel0")
                    try:
		                CurrentTabName = TestProduct.CurrentTab
                    except:
		                CurrentTabName = "Quotes"
                    if str(RECORD_ID) == "SYOBJR-98795":                                           
                        qt_rec_id = Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")
                        Serv_id = SqlHelper.GetFirst("SELECT SERVICE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")    
                        LineAndEquipIDList = TreeParam.split(' - ')
                        
                        if getyears == 1:
                            col_year =  'YEAR_1'
                        elif getyears == 2:
                            col_year =  'YEAR_1,YEAR_2'
                        elif getyears == 3:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3'
                        elif getyears == 4:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                        else:
                            col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'
                        if TreeParam == "Quote Preview":                            
                            Qury_str = (
                            "select top "
                                + str(PerPage)
                                + " QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, EQUIPMENT_ID,SERVICE_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",BASE_PRICE,SERIAL_NO, GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE_MARGIN, TARGET_PRICE, SALES_DISCOUNT_PRICE, CEILING_PRICE, SALES_DISCOUNT, TAX_PERCENTAGE,TAX,LINE,SRVTAXCLA_DESCRIPTION, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from SAQICO (NOLOCK) where QUOTE_ID = '"
                                + str(qt_rec_id.QUOTE_ID)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                            )
                            QuryCount_str = (
                                    "select count(*) as cnt FROM SAQICO where QUOTE_ID = '{}'".format(str(qt_rec_id.QUOTE_ID))
                            )
                    elif str(RECORD_ID) == "SYOBJR-00009":
                        if getyears == 1:
                            col_year =  'YEAR_1'
                        elif getyears == 2:
                            col_year =  'YEAR_1,YEAR_2'
                        elif getyears == 3:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3'
                        elif getyears == 4:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                        else:
                            col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'    
                        Trace.Write("TP "+str(TreeParam)+"TPP "+str(TreeParentParam)+"TSP "+str(Product.GetGlobal("TreeParentLevel1")))
                        if Product.GetGlobal("TreeParentLevel2") == "Quote Items":                            
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            error = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                            partially_priced = '<img title="Partially Priced" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Red1_Circle.svg>'
                            assembly_missing = '<img title="Assembly Missing" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Orange1_Circle.svg>'
                            TreeParentParam = Product.GetGlobal("TreeParentLevel1")
                            
                            try:
                                if str(TreeParentParam.split("-")[3]):
                                    ServiceId = TreeParentParam.split("-")[-2].strip()
                                else:
                                    ServiceId = TreeParentParam.split("-")[1].strip() 
                            except:
                                ServiceId = TreeParentParam.split("-")[1].strip()
                            fab_location_id = Product.GetGlobal("TreeParentLevel0")                    
                            Qury_str = (
                                    "SELECT DISTINCT TOP "
                                    + str(PerPage)
                                    + " CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '"+ exclamation +"' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,EQUIPMENT_ID,SERVICE_ID,SERIAL_NO,GREENBOOK,FABLOCATION_ID,TOTAL_COST,TARGET_PRICE_MARGIN,TARGET_PRICE,CEILING_PRICE,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",SALES_DISCOUNT,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,BASE_PRICE,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,BD_DISCOUNT_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,QUOTE_RECORD_ID,MNT_PLANT_RECORD_ID,SALE_DISCOUNT_RECORD_ID,SALES_DISCOUNT_PRICE,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,QUOTE_CURRENCY_RECORD_ID,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQICO (nolock)  where QUOTE_RECORD_ID ='"+str(RecAttValue)
                                    +"' and GREENBOOK = '"+str(TreeParam)+"' and FABLOCATION_ID = '"+str(fab_location_id)+"' and SERVICE_ID = '"+str(ServiceId)+"') m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " AND "
                                    + str(Page_End)
                                )

                            QuryCount_str = (
                                "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQICO (nolock) WHERE QUOTE_RECORD_ID = '"
                                    + str(RecAttValue)
                                    + "'and GREENBOOK = '"+str(TreeParam)+"' and FABLOCATION_ID = '"+str(fab_location_id)+"' and SERVICE_ID = '"+str(ServiceId)+"'"
                            )                                
                        else:    
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            error = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                            partially_priced = '<img title="Partially Priced" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Red1_Circle.svg>'
                            assembly_missing = '<img title="Assembly Missing" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Orange1_Circle.svg>'
                            qt_rec_id = SqlHelper.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")
                            if TreeParentParam == "Quote Items": 
                                try:
                                    if str(TreeParam.split("-")[3]):
                                        LineAndEquipIDList = TreeParam.split(' - ')[-2].strip()
                                    else:
                                        LineAndEquipIDList = TreeParam.split(' - ')[1].strip() 
                                except:
                                    LineAndEquipIDList = TreeParam.split('-')[1].strip()
                            # elif TreeSuperParentParam == "Quote Items":
                            #     try:
                            #         if str(TreeParentParam.split("-")[3]):
                            #             LineAndEquipIDList = TreeParentParam.split(' - ')[-2].strip()
                            #         else:
                            #             LineAndEquipIDList = TreeParentParam.split(' - ')[1].strip() 
                            #     except:
                            #         LineAndEquipIDList = TreeParentParam.split(' - ')[1].strip()
                            
                            if TreeParentParam == "Quote Items":
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE  WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, EQUIPMENT_ID,SERVICE_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",BASE_PRICE,SERIAL_NO, GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE_MARGIN, TARGET_PRICE, SALES_DISCOUNT_PRICE, CEILING_PRICE, SALES_DISCOUNT,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from SAQICO (NOLOCK) where QUOTE_ID = '"
                                        + str(qt_rec_id.QUOTE_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList)
                                        + "' and LINE_ITEM_ID = '"+str(TreeParam.split(' -')[0])+"') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM SAQICO where SERVICE_ID = '"+str(LineAndEquipIDList)+"' and QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"' and LINE_ITEM_ID = '"+str(TreeParam.split(' -')[0])+"'"
                                )
                            elif TreeParam == "Quote Items":
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"'  ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, EQUIPMENT_ID,SERVICE_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",BASE_PRICE,SERIAL_NO, GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE_MARGIN, TARGET_PRICE, SALES_DISCOUNT_PRICE, CEILING_PRICE, SALES_DISCOUNT, SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from SAQICO (NOLOCK) where QUOTE_ID = '"
                                        + str(qt_rec_id.QUOTE_ID)
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM SAQICO where QUOTE_ID = '{}'".format(
                                            str(qt_rec_id.QUOTE_ID))
                                )
                            elif Product.GetGlobal("TreeParentLevel1") == 'Quote Items': 
                                try:                               
                                    if str(TreeParentParam.split("-")[3]):
                                        ServiceId = TreeParentParam.split("-")[-2].strip()
                                    else:
                                        ServiceId = TreeParentParam.split("-")[1].strip()
                                except:
                                    ServiceId = TreeParentParam.split("-")[1].strip()
                                Qury_str = (
                                    "SELECT DISTINCT TOP "
                                    + str(PerPage)
                                    + " CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '"+ exclamation +"' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,EQUIPMENT_ID,SERVICE_ID,SERIAL_NO,GREENBOOK,FABLOCATION_ID, TOTAL_COST,TARGET_PRICE_MARGIN,TARGET_PRICE,CEILING_PRICE,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",SALES_DISCOUNT,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,BASE_PRICE,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,BD_DISCOUNT_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,QUOTE_RECORD_ID,MNT_PLANT_RECORD_ID,SALE_DISCOUNT_RECORD_ID,SALES_DISCOUNT_PRICE,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,QUOTE_CURRENCY_RECORD_ID,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQICO (nolock)  where QUOTE_RECORD_ID ='"+str(RecAttValue)
                                    +"' and FABLOCATION_ID = '"+str(TreeParam)+"' and SERVICE_ID = '"+str(ServiceId)+"' and LINE_ITEM_ID = '"+str(TreeParentParam.split(' -')[0])+"') m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " AND "
                                    + str(Page_End)
                                )

                                QuryCount_str = (
                                    "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQICO (nolock) WHERE QUOTE_RECORD_ID = '"
                                        + str(RecAttValue)
                                        + "'and FABLOCATION_ID = '"+str(TreeParam)+"'and SERVICE_ID = '"+str(ServiceId)+"' and LINE_ITEM_ID = '"+str(TreeParentParam.split(' -')[0])+"'"
                                )          
                            else:
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " * from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from SAQICO (NOLOCK) where QUOTE_ID = '"
                                        + str(qt_rec_id.QUOTE_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList[1])
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM SAQICO where SERVICE_ID = '{}' and QUOTE_ID = '{}'".format(
                                            LineAndEquipIDList[1], str(qt_rec_id.QUOTE_ID))
                                )
                    elif str(RECORD_ID) == "SYOBJR-91822":
                        contractrecid = Product.GetGlobal("contract_record_id")
                            
                        if Product.GetGlobal("TreeParentLevel1") == "Contract Items":                                                     
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            TreeParentParam = Product.GetGlobal("TreeParentLevel0")
                            ServiceId = TreeParentParam.split("-")[1].strip()                           
                            Qury_str = (
                                    "SELECT DISTINCT TOP "
                                    + str(PerPage)
                                    + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CONTRACT_CURRENCY,CONTRACT_CURRENCY_RECORD_ID,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from CTCICO (nolock)  where CONTRACT_RECORD_ID ='"+str(RecAttValue)
                                    +"' and GREENBOOK = '"+str(TreeParam)+"' and SERVICE_ID = '"+str(ServiceId)+"') m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " AND "
                                    + str(Page_End)
                                )

                            QuryCount_str = (
                                "SELECT COUNT(CpqTableEntryId) AS cnt FROM CTCICO (nolock) WHERE CONTRACT_RECORD_ID = '"
                                    + str(RecAttValue)
                                    + "'and GREENBOOK = '"+str(TreeParam)+"'and SERVICE_ID = '"+str(ServiceId)+"'"
                            )                                
                        else:                            
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            qt_rec_id = SqlHelper.GetFirst("SELECT CONTRACT_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID='" + str(
                            contractrecid) + "'")
                            LineAndEquipIDList = TreeParam.split(' - ')
                            if TreeParentParam == "Contract Items":
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where CONTRACT_ID = '"
                                        + str(qt_rec_id.CONTRACT_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList[1])
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM CTCICO where SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                            LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                )
                            else:                                   
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " * from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where CONTRACT_ID = '"
                                        + str(qt_rec_id.CONTRACT_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList[1])
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM CTCICO where SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                            LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                )
                    elif str(RECORD_ID) == 'SYOBJR-98799':
                        contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                        qt_rec_id = Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                        contract_quote_record_id) + "'")
                        try:
                            quote_id = qt_rec_id.QUOTE_ID
                        except:
                            quote_id = ""
                        imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                        acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                        Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE WHEN STATUS = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ acquiring_img_str +"' END AS STATUS, QUOTE_DOCUMENT_RECORD_ID, DOCUMENT_ID,DOCUMENT_NAME,LANGUAGE_ID,LANGUAGE_NAME,CPQTABLEENTRYDATEADDED,QUOTE_RECORD_ID,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY STATUS) AS ROW, * from SAQDOC (NOLOCK) where QUOTE_ID = '"
                                        + str(quote_id)
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                        QuryCount_str = (
                                "select count(*) as cnt FROM SAQDOC where QUOTE_ID = '{}'".format(
                                    str(quote_id))
                        )
                    elif str(RECORD_ID) == "SYOBJR-00015" and str(TreeParentParam) == "Approval Chain Steps":
                        Qury_str = (
                            " SELECT TOP "
                            + str(PerPage)
                            + " * FROM (SELECT ROW_NUMBER() OVER(ORDER BY APPROVAL_TRACKED_FIELD_RECORD_ID) AS ROW,APPROVAL_TRACKED_FIELD_RECORD_ID,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRACKING_TYPE,ACAPTF.CpqTableEntryId FROM ACAPTF (NOLOCK) INNER JOIN ACACST (NOLOCK) ON ACAPTF.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID WHERE ACACST.APRCHN_RECORD_ID = '"
                            + str(RecAttValue)
                            + "' AND ACACST.APRCHNSTP_NAME = '"
                            + str(TreeParam).split(': ')[1]
                            + "' )m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " "
                        )

                        QuryCount_str = (
                            "SELECT COUNT(APPROVAL_TRACKED_FIELD_RECORD_ID) AS cnt FROM ACAPTF (NOLOCK) INNER JOIN ACACST (NOLOCK) ON ACAPTF.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID WHERE ACACST.APRCHN_RECORD_ID = '"
                            + str(RecAttValue)
                            + "' AND ACACST.APRCHNSTP_NAME = '"
                            + str(TreeParam).split(': ')[1]
                            + "' "
                        )    
                    elif str(RECORD_ID) == "SYOBJR-00014":                        
                        step_name = TreeParam.split(':')[1].strip()
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " * from ( select ROW_NUMBER() OVER( order by APPROVAL_CHAIN_STEP_APPROVER_RECORD_ID) AS ROW,ACACSA.APPROVAL_CHAIN_STEP_APPROVER_RECORD_ID,ACACSA.APRCHN_ID,ACACSA.APRCHNSTP_APPROVER_ID,ACACSA.APPROVER_SELECTION_METHOD,ACACSA.USERNAME,ACACSA.PROFILE_ID,ACACSA.ROLE_ID,ACACSA.NOTIFICATION_ONLY,ACACSA.CpqTableEntryId from ACACSA (nolock) INNER JOIN ACACST (NOLOCK) ON ACACST.APPROVAL_CHAIN_STEP_RECORD_ID = ACACSA.APRCHNSTP_RECORD_ID WHERE  ACACSA."
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND ACACST.APRCHNSTP_NAME = '"
                            + str(step_name)
                            + "') m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " AND "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = (
                            "select count(ACACSA.CpqTableEntryId) as cnt from ACACSA (nolock) INNER JOIN ACACST (NOLOCK) ON ACACST.APPROVAL_CHAIN_STEP_RECORD_ID = ACACSA.APRCHNSTP_RECORD_ID WHERE ACACSA."
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND ACACST.APRCHNSTP_NAME = '"
                            + str(step_name)
                            + "'"
                        )
                    elif str(RECORD_ID) == "SYOBJR-98822":     
                        if Product.GetGlobal("TreeParentLevel1") == "Contract Items":                            
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            
                            Qury_str = (
                                    "SELECT DISTINCT TOP "
                                    + str(PerPage)
                                    + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from CTCICO (nolock)  where CONTRACT_RECORD_ID ='"+str(RecAttValue)
                                    +"' and GREENBOOK = '"+str(TreeParam)+"') m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " AND "
                                    + str(Page_End)
                                )

                            QuryCount_str = (
                                "SELECT COUNT(CpqTableEntryId) AS cnt FROM CTCICO (nolock) WHERE CONTRACT_RECORD_ID = '"
                                    + str(RecAttValue)
                                    + "'and GREENBOOK = '"+str(TreeParam)+"'"
                            )  
                        else:    
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            contract_record_id = Product.GetGlobal("contract_record_id")
                            qt_rec_id = SqlHelper.GetFirst("SELECT CONTRACT_ID, SERVICE_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID ='" + str(
                            contract_record_id) + "'")
                            LineAndEquipIDList = TreeParam.split(' - ')
                            if qt_rec_id.CONTRACT_ID == '70011556':
                                SERV_DESC = "Z0091"
                            else:
                                SERV_DESC = qt_rec_id.SERVICE_ID
                            if TreeParentParam == "Contract Items":
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, SERVICE_ID, EQUIPMENT_ID,LINE_ITEM_ID,DISCOUNT,SERIAL_NO, GREENBOOK, TOTAL_COST, TAX, EXTENDED_PRICE, CONTRACT_CURRENCY, CONTRACT_CURRENCY_RECORD_ID,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where CONTRACT_ID = '"
                                        + str(qt_rec_id.CONTRACT_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList[1])
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM CTCICO where SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                            LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                )
                            else:
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " * from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where CONTRACT_ID = '"
                                        + str(qt_rec_id.CONTRACT_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(SERV_DESC)
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM CTCICO where SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                            SERV_DESC, str(qt_rec_id.CONTRACT_ID))
                                )
                    elif str(RECORD_ID) == "SYOBJR-98788":
                        #contract_quote_record_id = Quote.CompositeNumber
                        Trace.Write("contract_quote_record_id1234"+str(contract_quote_record_id))
                        contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")                        
                        qt_rec_id= Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='"+str(contract_quote_record_id)+"'")
                        if qt_rec_id is not None:
                            if TreeParentParam:
                                Qustr = "where QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"' and SERVICE_TYPE = '{}'".format(TreeParam)
                            else:
                                Qustr = "where QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"'"
                            
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + " "
                                + str(select_obj_str)
                                + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                                + str(Wh_API_NAMEs)
                                + ") AS ROW, * from "
                                + str(ObjectName)
                                + " (nolock) "
                                + str(Qustr)
                                + " ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + ""
                            )
                            QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                        else: 
                            Trace.Write('checking----') 
                            #Qustr = "where QUOTE_ID = '"+str(contract_quote_record_id)+"'"                          
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + " "
                                + str(select_obj_str)
                                + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                                + str(Wh_API_NAMEs)
                                + ") AS ROW, * from "
                                + str(ObjectName)
                                + " (nolock) "
                                + str(Qustr)
                                + " ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + ""
                            )
                            
                            QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-98853" and str(TreeParam) == "Tracked Objects":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_AC_00063").GetValue()
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " APPROVAL_TRACKED_FIELD_RECORD_ID,APRCHN_ID,APRCHNSTP,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRACKING_TYPE,CpqTableEntryId from (SELECT ROW_NUMBER() OVER(order by APPROVAL_TRACKED_FIELD_RECORD_ID) AS ROW,ACAPTF.APPROVAL_TRACKED_FIELD_RECORD_ID,ACAPTF.APRCHN_ID,ACAPTF.APRCHNSTP,ACAPTF.TRKOBJ_TRACKEDFIELD_LABEL,ACAPTF.TRKOBJ_NAME,ACAPTF.TRACKING_TYPE,ACAPTF.CpqTableEntryId FROM ACAPTF (NOLOCK) INNER JOIN ACAPTX ON ACAPTF.APRCHN_ID = ACAPTX.APRCHN_ID WHERE ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                            + str(RecAttValue)
                            + "') S where S.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " "
                        )
                        QuryCount_str = (
                            "SELECT count(DISTINCT ACAPTF.APPROVAL_TRACKED_FIELD_RECORD_ID) as cnt FROM ACAPTF (NOLOCK) INNER JOIN ACAPTX ON ACAPTF.APRCHN_ID = ACAPTX.APRCHN_ID WHERE ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                            + str(RecAttValue)                            
                            + "' "
                        )
                    elif str(RECORD_ID) == "SYOBJR-00026" and str(TreeParentParam) == "Tracked Objects":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_AC_00063").GetValue()
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " APPROVAL_TRACKED_VALUE_RECORD_ID,APRCHN_ID,APRCHNSTP,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRKOBJ_TRACKEDFIELD_OLDVALUE,TRKOBJ_TRACKEDFIELD_NEWVALUE,TRKOBJ_CPQTABLEENTRYID,CpqTableEntryId from (SELECT ROW_NUMBER() OVER(order by APPROVAL_TRACKED_VALUE_RECORD_ID) AS ROW,ACAPFV.TRKOBJ_TRACKEDFIELD_OLDVALUE,ACAPFV.APPROVAL_TRACKED_VALUE_RECORD_ID,ACAPFV.APRCHN_ID,ACAPFV.APRCHNSTP,ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL,ACAPFV.TRKOBJ_NAME,ACAPFV.TRKOBJ_TRACKEDFIELD_NEWVALUE, ACAPFV.CpqTableEntryId,ACAPFV.TRKOBJ_CPQTABLEENTRYID FROM ACAPFV (NOLOCK) INNER JOIN ACAPTX ON ACAPFV.APRCHN_ID = ACAPTX.APRCHN_ID AND ACAPFV.APPROVAL_ID = ACAPTX.APPROVAL_ID WHERE ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                            + str(RecAttValue)
                            + "' AND ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL= '"
                            + str(TreeParam)                            
                            + "') S where S.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " "
                        )
                        QuryCount_str = (
                            "SELECT count(DISTINCT ACAPFV.APPROVAL_TRACKED_VALUE_RECORD_ID) as cnt FROM ACAPFV (NOLOCK) INNER JOIN ACAPTX ON ACAPFV.APRCHN_ID = ACAPTX.APRCHN_ID WHERE ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                            + str(RecAttValue) 
                            + "' AND ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL= '"
                            + str(TreeParam)                           
                            + "' "
                        )
                    elif str(RECORD_ID) == "SYOBJR-98816":
                                               
                        #contract_quote_record_id = Product.GetGlobal("contract_quote_record_id")
                        contract_quote_record_id = Quote.GetGlobal("contract_record_id")
                        Trace.Write("Contract "+str(contract_quote_record_id))
                        ct_rec_id= SqlHelper.GetFirst("SELECT CONTRACT_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID ='"+str(contract_quote_record_id)+"'")
                        try:
                            if TreeParentParam:
                                Qustr = "where  CONTRACT_ID = '"+str(ct_rec_id.CONTRACT_ID)+"' and PRODUCT_TYPE = '{}'".format(TreeParam)
                            else:
                                Qustr = "where  CONTRACT_ID = '"+str(ct_rec_id.CONTRACT_ID)+"'"
                        except:
                            Qustr=" where  CONTRACT_ID = '' "
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                                      
                     ## involved parties equipmemt starts
                    elif str(RECORD_ID) == "SYOBJR-00007": # Billing Matrix - Pivot - Start                        
                        pivot_columns = ",".join(['[{}]'.format(billing_date) for billing_date in billing_date_column])
                        if Qustr:
                            Qustr += " AND BILLING_DATE BETWEEN '{}' AND '{}'".format(billing_date_column[0], billing_date_column[-1])
                        pivot_query_str = """
                                    SELECT ROW_NUMBER() OVER(ORDER BY EQUIPMENT_ID)
                                    AS ROW, *
                                        FROM (
                                            SELECT 
                                                {Columns}                                           
                                            FROM {ObjectName}
                                            {WhereString}
                                        ) AS IQ
                                        PIVOT
                                        (
                                            SUM(BILLING_AMOUNT)
                                            FOR BILLING_DATE IN ({PivotColumns})
                                        )AS PVT
                                    """.format(OrderByColumn=Wh_API_NAMEs, Columns=column_before_pivot_change, ObjectName=ObjectName,
                                                WhereString=Qustr, PivotColumns=pivot_columns)                        
                        Qury_str = """
                                    SELECT DISTINCT TOP {PerPage} * FROM ( SELECT * FROM ({InnerQuery}) OQ WHERE ROW BETWEEN {Start} AND {End} ) AS FQ ORDER BY EQUIPMENT_ID
                                    """.format(PerPage=PerPage, OrderByColumn=Wh_API_NAMEs, InnerQuery=pivot_query_str, Start=Page_start, End=Page_End)
                        QuryCount_str = "SELECT COUNT(*) AS cnt FROM ({InnerQuery}) OQ ".format(InnerQuery=pivot_query_str)
                        
                        # Billing Matrix - Pivot - End 
                    ##involved parties equipmemt starts
                    elif (str(RECORD_ID) == "SYOBJR-98858" or str(RECORD_ID) == "SYOBJR-00028") and str(TreeParam) == "Quote Information":
                        account_id = Product.GetGlobal("stp_account_id")
                        
                        Qury_str = ("""select DISTINCT top {PerPage} * from (select ROW_NUMBER() OVER( ORDER BY SAQSTE.FABLOCATION_ID DESC) AS ROW,SAQSTE.* from SAQSTE  inner join SAQSCF(nolock)  on SAQSTE.QUOTE_RECORD_ID = SAQSCF.QUOTE_RECORD_ID and SAQSTE.SRCFBL_ID = SAQSCF.SRCFBL_ID where SAQSTE.QUOTE_RECORD_ID = '{contract_quote_record_id}' and SAQSTE.SRCACC_ID = '{account_id}')m where m.ROW BETWEEN """.format(PerPage = PerPage,account_id = account_id,
                        contract_quote_record_id = str(RecAttValue))+ str(Page_start) + " and " + str(Page_End))
                        
                        
                        
                        QuryCount_str = "select count(SAQSTE.CpqTableEntryId) as cnt from SAQSTE  inner join SAQSCF(nolock) on SAQSTE.QUOTE_RECORD_ID = SAQSCF.QUOTE_RECORD_ID and SAQSTE.SRCFBL_ID= SAQSCF.SRCFBL_ID where SAQSTE.QUOTE_RECORD_ID = '{contract_quote_record_id}' and SAQSTE.SRCACC_ID = '{account_id}'".format(account_id = account_id,contract_quote_record_id=str(RecAttValue))
                    ##involved parties equipmemt ends
                    
                    ##involved parties source fab starts
                    elif (str(RECORD_ID) == "SYOBJR-98857") and str(TreeParam) == "Quote Information":
                        account_id = Product.GetGlobal("stp_account_id")                        
                        Qustr += " AND SRCACC_ID = '{}'".format(account_id)
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    ##involved parties source fab ends
                    elif str(RECORD_ID) == "SYOBJR-98859":
                        
                        Qustr += " AND SERVICE_ID = '"+str(TreeParentParam)+"' "
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-98862":
                        Qustr = " WHERE APP_ID = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-98863":
                        Qustr = " WHERE TAB_ID = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-98864":
                        Qustr = " WHERE TAB_NAME = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-93123":
                        app_ObjectName = Sql.GetFirst("select PRIMARY_OBJECT_NAME FROM SYTABS INNER JOIN SYAPPS ON SYTABS.APP_LABEL = SYAPPS.APP_LABEL WHERE SYTABS.TAB_LABEL = '"+str(TopTreeSuperParentParam)+"' AND SYAPPS.APP_LABEL = '"+str(TreeSecondSuperTopParentParam)+"'")
                        Qustr = " WHERE SECTION_NAME = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"' "
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)    
                    elif str(RECORD_ID) == "SYOBJR-98784" and TreeFirstSuperTopParentParam == "Pages":
                        Qustr = " WHERE SECTION_NAME = '"+str(TreeParentParam)+"' AND TAB_NAME = '"+str(TreeSecondSuperTopParentParam)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-93188":
                        Trace.Write('SYOBJR-93188@222')
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        GetAppname_query = ""
                        Qustr = " WHERE TAB_NAME = '"+str(TreeParentParam)+"' AND PROFILE_ID ='"+str(RecAttValue)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-95825" and str(TreeParentParam) == 'Constraints':
                        Qustr = "WHERE CONSTRAINT_TYPE = '"+str(TreeParam)+"' AND OBJECT_RECORD_ID='"+str(RecAttValue)+"'" 
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-98834":
                        #contract_quote_record_id = Product.GetGlobal("contract_quote_record_id")
                        contract_quote_record_id = Quote.GetGlobal("contract_record_id")
                        Trace.Write("Contract Rec Id"+str(contract_quote_record_id))
                        Qustr = "where  CONTRACT_RECORD_ID = '"+str(contract_quote_record_id)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-98817":
                                               
                        #contract_quote_record_id = Product.GetGlobal("contract_quote_record_id")
                        contract_quote_record_id = Quote.GetGlobal("contract_record_id")
                        Trace.Write("Contract"+str(contract_quote_record_id))
                        ct_rec_id= Sql.GetList("SELECT CONTRACT_ID FROM CTCFBL WHERE CONTRACT_RECORD_ID ='"+str(contract_quote_record_id)+"'")
                        Trace.Write("Record Id "+str(ct_rec_id))
                        Qustr = "where  CONTRACT_RECORD_ID = '"+str(contract_quote_record_id)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)   
                   

                    else:
                        if  str(RECORD_ID) == "SYOBJR-98789" and "Sending Account -" in TreeParam :
                            Qustr += " AND RELOCATION_FAB_TYPE = 'SENDING FAB'"
                        elif  str(RECORD_ID) == "SYOBJR-98789" and "Receiving Account -" in TreeParam :
                            Qustr += " AND RELOCATION_FAB_TYPE = 'RECEIVING FAB'"
                        Trace.Write('In 1958---'+str(Qustr))
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)

                if RECORD_ID == "SYOBJR-94442" and str(current_tab) == "Tab":                    
                    Qury_str = (
                        "SELECT TOP "
                        + str(PerPage)
                        + " * FROM (SELECT ROW_NUMBER() OVER (ORDER BY RECORD_ID DESC) AS ROW,RECORD_ID,ACTION_NAME,TAB_NAME,ATTRIBUTE_NAME,ACTVIS_VARIABLE_RECORD_ID,SCRIPT_RECORD_ID,TAB_RECORD_ID,CpqTableEntryId FROM SYPSAC WHERE TAB_RECORD_ID = '"
                        + str(RecAttValue)
                        + "' GROUP BY RECORD_ID,ACTION_NAME,TAB_NAME,ATTRIBUTE_NAME,ACTVIS_VARIABLE_RECORD_ID,SCRIPT_RECORD_ID,TAB_RECORD_ID,CpqTableEntryId) m WHERE m.ROW BETWEEN "
                        + str(Page_start)
                        + " AND "
                        + str(Page_End)
                    )
                    QuryCount_str = "SELECT COUNT(*) AS cnt FROM SYPSAC WHERE TAB_RECORD_ID = '" + str(RecAttValue) + "'"
                if RECORD_ID == "SYOBJR-94443" and str(current_tab) == "Tab":                    
                    Qury_str = (
                        "SELECT TOP "
                        + str(PerPage)
                        + " * FROM (SELECT ROW_NUMBER() OVER (ORDER BY SE.RECORD_ID DESC) AS ROW,SE.RECORD_ID,SE.SECTION_NAME,PG.TAB_NAME,SE.ATTRIBUTE_NAME,PG.TAB_RECORD_ID,SE.CpqTableEntryId FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE PG.TAB_RECORD_ID = '"
                        + str(RecAttValue)
                        + "' GROUP BY SE.RECORD_ID,SE.SECTION_NAME,PG.TAB_NAME,SE.ATTRIBUTE_NAME,PG.TAB_RECORD_ID,SE.CpqTableEntryId) m WHERE m.ROW BETWEEN "
                        + str(Page_start)
                        + " AND "
                        + str(Page_End)
                    )
                    QuryCount_str = (
                        "SELECT COUNT(SE.CpqTableEntryId) AS cnt FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE PG.TAB_RECORD_ID = '"
                        + str(RecAttValue)
                        + "'"
                    )
                elif RECORD_ID == 'SYOBJR-00006' and TreeParam == "Quote Preview":
                    
                    Qury_str = (
                    "SELECT DISTINCT TOP "
                    + str(PerPage)
                    + " QUOTE_ITEM_FORECAST_PART_RECORD_ID,PART_LINE_ID,PART_NUMBER,MATPRIGRP_ID,PART_DESCRIPTION,BASEUOM_ID,SCHEDULE_MODE,DELIVERY_MODE,UNIT_PRICE,EXTENDED_PRICE,ANNUAL_QUANTITY,PRICING_STATUS,CUSTOMER_PART_NUMBER_RECORD_ID,BASEUOM_RECORD_ID,MATPRIGRP_RECORD_ID,QTEITM_RECORD_ID,QUOTE_RECORD_ID,SALESORG_RECORD_ID,SERVICE_RECORD_ID,PART_RECORD_ID,SALESUOM_RECORD_ID,CpqTableEntryId,TAX,TAX_PERCENTAGE,SERVICE_ID,SRVTAXCLA_DESCRIPTION from ( select TOP "+ str(PerPage)+" ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQIFP (nolock)  where QUOTE_RECORD_ID ='"+str(RecAttValue)
                    +"') m where m.ROW BETWEEN "
                    + str(Page_start)
                    + " AND "
                    + str(Page_End)+" "
                    )
                    QuryCount_str = (
                        "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQIFP (nolock) WHERE QUOTE_RECORD_ID = '"
                        + str(RecAttValue)
                        + "'"
                    )
                elif RECORD_ID == 'SYOBJR-00010':
                    imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                    acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'  
                    Qury_str = (
                        "SELECT DISTINCT TOP "
                        + str(PerPage)
                        + " QUOTE_ITEM_FORECAST_PART_RECORD_ID, CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS,SERVICE_ID, PART_LINE_ID,PART_NUMBER,MATPRIGRP_ID,PART_DESCRIPTION,BASEUOM_ID,SCHEDULE_MODE,DELIVERY_MODE,UNIT_PRICE,EXTENDED_PRICE,ANNUAL_QUANTITY,CUSTOMER_PART_NUMBER_RECORD_ID,BASEUOM_RECORD_ID,MATPRIGRP_RECORD_ID,QTEITM_RECORD_ID,QUOTE_RECORD_ID,SALESORG_RECORD_ID,SERVICE_RECORD_ID,PART_RECORD_ID,SALESUOM_RECORD_ID,CpqTableEntryId,TAX,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE from ( select TOP "+ str(PerPage)+" ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQIFP (nolock)  where QUOTE_RECORD_ID ='"+str(RecAttValue)
                        +"') m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " AND "
                        + str(Page_End)+" ORDER BY PART_LINE_ID,PRICING_STATUS ASC"
                    )
                    QuryCount_str = (
                        "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQIFP (nolock) WHERE QUOTE_RECORD_ID = '"
                        + str(RecAttValue)
                        + "'"
                    )

                elif RECORD_ID == 'SYOBJR-00008':
                    imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                    acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                    exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'

                    if getyears == 1:
                        col_year =  'YEAR_1'
                    elif getyears == 2:
                        col_year =  'YEAR_1,YEAR_2'
                    elif getyears == 3:
                        col_year =  'YEAR_1,YEAR_2,YEAR_3'
                    elif getyears == 4:
                        col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                    else:
                        col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'
                    price_status = []
                    # quote_itm_rec = Sql.GetFirst("SELECT QUOTE_ITEM_RECORD_ID FROM SAQITM (NOLOCK) "+str(Qustr)+"")
                    if str(getQuotetype).upper() == "ZWK1 - SPARES":
                        quote_item_obj = Sql.GetFirst("SELECT PRICING_STATUS FROM SAQITM (NOLOCK) "+str(Qustr)+"")
                        if quote_item_obj:
                            if quote_item_obj.PRICING_STATUS == 'ACQUIRED':
                                icon = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            else:
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                    else:
                        SAQICO_status = Sql.GetList("SELECT DISTINCT PRICING_STATUS FROM SAQICO (NOLOCK) "+str(Qustr)+"")
                        for pricing_status in SAQICO_status:
                            price_status.append(pricing_status.PRICING_STATUS)


                        
                        all_acquired = ["ACQUIRING","APPROVAL REQUIRED","ERROR"]
                        all_error = ["APPROVAL REQUIRED","ACQUIRING","ACQUIERD"]
                        all_required = ["ACQUIERD","ACQUIRING","ERROR"]
                        all_acquiring = ["ACQUIERD","ERROR","APPROVAL REQUIRED"]
                        acq_error = ["ACQUIERD","ERROR"]
                        acq_req = ["ACQUIERD","APPROVAL REQUIRED"]
                        not_acq_req = ["ACQUIRING","ERROR"]
                        acq_error_approval = ["ACQUIERD","ERROR","APPROVAL"]
                        not_acq_error = ["ACQUIRING","APPROVAL REQUIRED"]

                        if "ACQUIRED" in price_status and ('ACQUIRING' not in price_status and 'APPROVAL REQUIRED' not in price_status and 'ERROR' not in price_status):
                            icon = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                        elif "ERROR" in price_status and ('ACQUIRED' not in price_status and 'APPROVAL REQUIRED' not in price_status and 'ACQUIRING' not in price_status):
                            icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                        elif "APPROVAL REQUIRED" in price_status and ('ACQUIRED' not in price_status and 'ERROR' not in price_status and 'ACQUIRING' not in price_status):
                            icon = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                        elif "ACQUIRING" in price_status and 'ACQUIRED' not in price_status and 'ERROR' not in price_status and 'APPROVAL REQUIRED' not in price_status:
                            icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                        elif ("ACQUIRED" in price_status and "ERROR" in price_status) and ('ACQUIRING' not in price_status and 'APPROVAL REQUIRED' not in price_status):
                            icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                        elif ("ACQUIRED" in price_status and "ACQUIRING" in price_status) and ('ERROR' not in price_status and 'APPROVAL REQUIRED' not in price_status):
                            icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                        elif ("ACQUIRED" in price_status and "APPROVAL REQUIRED" in price_status) and ('ERROR' not in price_status and 'ACQUIRING' not in price_status):
                            icon = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                        elif ("ACQUIRED" in price_status and 'ERROR' in price_status and 'APPROVAL REQUIRED' in price_status) and "ACQUIRING" not in price_status :
                            icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                        elif ("ACQUIRING" in price_status and 'APPROVAL REQUIRED' in price_status) and ('ACQUIRED' not in price_status and "ERROR" not in price_status) :
                            icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                        else:
                            icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                    

                    if TreeParam == "Quote Items":                        
                        
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " '"+ icon +"' AS PO_NOTES, QUOTE_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, OBJECT_QUANTITY, QUANTITY,TOTAL_COST, ONSITE_PURCHASE_COMMIT, SALES_DISCOUNT_PRICE,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE, TARGET_PRICE, CEILING_PRICE, BD_PRICE, BD_PRICE_MARGIN, DISCOUNT, SALES_PRICE, YEAR_OVER_YEAR, "+col_year+" "
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    
                elif RECORD_ID == 'SYOBJR-00024':                    
                    quote_obj = Sql.GetFirst("select QUOTE_ID,MASTER_TABLE_QUOTE_RECORD_ID from SAQTMT where MASTER_TABLE_QUOTE_RECORD_ID = '{contract_quote_record_id}'".format(contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")))
                    quote_id = quote_obj.QUOTE_ID
                    TreeParam = Product.GetGlobal("TreeParam")
                    TreeParentParam = Product.GetGlobal("TreeParentLevel0")
                    try:
                        chain_step_name = subTab.split(':')[1].strip()
                        
                        step_id = chain_step_name.split(' ')[1]
                        
                    except:
                        step_id=""
                        
                    dynamic_condtn=""
                    round_value=""
                    if TreeSuperParentParam == 'Approvals':
                        round_value = TreeParam.split()[1]
                        dynamic_condtn=" and ACAPTX.APRCHNSTP_ID = '{chain_step_name}' and ACAPTX.APPROVAL_ROUND = '{step_value}'".format(chain_step_name = step_id,step_value = round_value)
                    Qury_str = ("""select DISTINCT top {PerPage} * from (select ROW_NUMBER() OVER( ORDER BY ACAPTX.APRCHNSTP_ID) AS ROW,ACAPTX.APPROVAL_TRANSACTION_RECORD_ID, ACAPTX.APPROVAL_ID,ACAPTX.APRCHNSTP_ID,ACAPTX.APRCHNSTP_APPROVER_ID,ACAPTX.APPROVAL_ROUND,ACAPTX.APPROVALSTATUS,ACAPTX.RECIPIENT_COMMENTS,ACAPTX.APRCHNSTP_RECORD_ID,ACAPTX.APPROVAL_RECIPIENT,ACAPTX.CpqTableEntryId FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID  and ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHN_ID = '{chain_id}' {dynamic_condtn})m where m.ROW BETWEEN """.format(PerPage = PerPage,contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id,dynamic_condtn=dynamic_condtn,chain_id=TreeParentParam if TreeSuperParentParam == 'Approvals' else TreeParam) + str(Page_start) + " and " + str(Page_End))
                    QuryCount_str = """select count(ACAPTX.CpqTableEntryId) as cnt FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID and  ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHN_ID = '{chain_id}' """.format(contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id,dynamic_condtn=dynamic_condtn,chain_id=TreeParentParam if TreeSuperParentParam == 'Approvals' else TreeParam)
            
                ##involved parties source fab starts
                elif (str(RECORD_ID) == "SYOBJR-98857") and str(TreeParam) == "Quote Information":
                    account_id = Product.GetGlobal("stp_account_id")                    
                    Qustr += " AND SRCACC_ID = '{}'".format(account_id)
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                ##involved parties source fab ends
                elif str(RECORD_ID) == "SYOBJR-98859":
                    Qustr += " AND SERVICE_ID = '"+str(TreeParentParam)+"' "
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                elif str(RECORD_ID) == "SYOBJR-98862":
                    Qustr = " WHERE APP_ID = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                elif str(RECORD_ID) == "SYOBJR-98863":
                    Qustr = " WHERE TAB_ID = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                
                elif str(RECORD_ID) == "SYOBJR-98864":
                    Qustr = " WHERE TAB_NAME = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                elif str(RECORD_ID) == "SYOBJR-93123":
                    TreeParentParam = Product.GetGlobal("TreeParentLevel0") 
                    
                    app_ObjectName = Sql.GetFirst("select PRIMARY_OBJECT_NAME FROM SYTABS INNER JOIN SYAPPS ON SYTABS.APP_LABEL = SYAPPS.APP_LABEL WHERE SYTABS.TAB_LABEL = '"+str(TopTreeSuperParentParam)+"' AND SYAPPS.APP_LABEL = '"+str(TreeSecondSuperTopParentParam)+"'")
                    Qustr = " WHERE SECTION_NAME = '"+str(TreeParentParam)+"' AND PROFILE_ID ='"+str(RecAttValue)+"' AND OBJECT_NAME = '"+str(ObjectName)+"' "
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                        )
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)    
                elif str(RECORD_ID) == "SYOBJR-98784" and TreeFirstSuperTopParentParam == "Pages":
                    Qustr = " WHERE SECTION_NAME = '"+str(TreeParentParam)+"' AND TAB_NAME = '"+str(TreeSecondSuperTopParentParam)+"'"
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                elif str(RECORD_ID) == "SYOBJR-95985" and str(current_tab) == "Page":
                    #tree_var = Sql.GetFirst("SELECT * FROM SYTREE WHERE PAGE_RECORD_ID = '"+str(RecAttValue)+"'") 
                      
                    Qustr = "WHERE TREE_NAME = '"+str(TreeParentParam)+"' "
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                elif str(RECORD_ID) == "SYOBJR-93188":
                    Trace.Write('SYOBJR-93188@3333')
                    RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                    GetAppname_query = ""
                    Qustr = " WHERE TAB_NAME = '"+str(TreeParentParam)+"' AND PROFILE_ID ='"+str(RecAttValue)+"'"
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                elif str(RECORD_ID) == "SYOBJR-95825" and str(TreeParentParam) == 'Constraints':
                        Qustr = "WHERE CONSTRAINT_TYPE = '"+str(TreeParam)+"' AND OBJECT_RECORD_ID ='"+str(RecAttValue)+"'" 
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                elif RECORD_ID == 'SYOBJR-98841':
                    imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                    acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'

                    
                    if TreeParam == "Contract Items":                       
                        
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + "  CASE WHEN ITEM_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS PO_NOTES, CONTRACT_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, QUANTITY, TAX, DISCOUNT, EXTENDED_PRICE"
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)

                elif RECORD_ID == 'SYOBJR-98792' and str(TreeParam) == "Quote Preview":
                    
                    if getyears == 1:
                        col_year =  'YEAR_1'
                    elif getyears == 2:
                        col_year =  'YEAR_1,YEAR_2'
                    elif getyears == 3:
                        col_year =  'YEAR_1,YEAR_2,YEAR_3'
                    elif getyears == 4:
                        col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                    else:
                        col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'
                    Qury_str = (
                        "select DISTINCT top "
                        + str(PerPage)
                        + " QUOTE_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, ONSITE_PURCHASE_COMMIT, OBJECT_QUANTITY, TOTAL_COST, SALES_DISCOUNT_PRICE, TAX, EXTENDED_PRICE, QUANTITY, TARGET_PRICE, CEILING_PRICE, BD_PRICE, BD_PRICE_MARGIN, DISCOUNT, SALES_PRICE, YEAR_OVER_YEAR, "+col_year+" , SRVTAXCLA_DESCRIPTION, TAX_PERCENTAGE, CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "          
                        
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + "  AND SERVICE_ID NOT LIKE '%BUNDLE%') m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr) + " AND SERVICE_ID NOT LIKE '%BUNDLE%' "
                
                try:
                    Query_Obj = Sql.GetList(str(Qury_str))
                    
                    
                    QueryCount_Obj = Sql.GetFirst(str(QuryCount_str))
                    
                    if QueryCount_Obj is not None:
                        QueryCount = QueryCount_Obj.cnt
                        
                except:
                    
                    if OrderBy_obj is not None:
                        if OrderBy_obj.ORDERS_BY:
                            Wh_API_NAMEs = OrderBy_obj.ORDERS_BY
                        else:
                            Wh_API_NAMEs = lookup_disply_list123
                    else:
                        Wh_API_NAMEs = lookup_disply_list123
                    Qury_str = (
                        "select * from ( select ROW_NUMBER() OVER( order by "
                        + str(lookup_disply_list123)
                        + " ) AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) where 1=1 ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    # Trace.Write(
                    #     "LLLLL"
                    #     + str(
                    #         "select * from ( select ROW_NUMBER() OVER( order by "
                    #         + str(lookup_disply_list123)
                    #         + " ) AS ROW, * from "
                    #         + str(ObjectName)
                    #         + " (nolock) where 1=1 ) m where m.ROW BETWEEN "
                    #         + str(Page_start)
                    #         + " and "
                    #         + str(Page_End)
                    #         + ""
                    #     )
                    # )
                    QuryCount_str = "select count(*) as cnt  from " + str(ObjectName) + " (nolock) where 1=1 "
                    Query_Obj = Sql.GetList(Qury_str)
                    
                    QueryCount_Obj = Sql.GetFirst(str(QuryCount_str))
                    if QueryCount_Obj is not None:
                        QueryCount = QueryCount_Obj.cnt
            
          
            tab_obj1 = Sql.GetFirst(
                "SELECT PG.TAB_NAME,PG.TAB_RECORD_ID FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE SE.PRIMARY_OBJECT_NAME='"
                + str(ObjectName)
                + "' and SE.SECTION_NAME ='BASIC INFORMATION'"
            )
            
            if Query_Obj is not None:
                for ik in Query_Obj:
                    if str(ObjectName) == "USERS":
                        useridval = ik.ID                    
                    new_dict = {}
                    ids = {}
                    seg_pric = {}
                    primary = ""
                    primary_view = ""
                    product_id = ""
                    product_name = ""
                    other_tab = ""
                    key_value = ""
                    decimal_place = 3                    
                    product_id_val = ""
                    editvalue = {}
                    red_color = ""
                    pop_val = {}
                    list_lineup = []
                    list_lineup1 = []
                    if ObjectName != 'SAQIBP':
                        Action_str = '<div class="btn-group dropdown"><div class="dropdown" id="ctr_drop"><i data-toggle="dropdown" id="dropdownMenuButton" class="fa fa-sort-desc dropdown-toggle" aria-expanded="false"></i><ul class="dropdown-menu left" aria-labelledby="dropdownMenuButton">'
                    else:
                        Action_str = '<div class="btn-group dropdown"><div class="dropdown" id="ctr_drop"><i data-toggle="dropdown" id="dropdownMenuButton" class="fa fa-sort-desc dropdown-toggle" aria-expanded="false"></i><ul class="dropdown-menu left" style="display: none;" aria-labelledby="dropdownMenuButton">'
                    #Action_str = '<div class="btn-group dropdown"><div class="dropdown" id="ctr_drop"><i data-toggle="dropdown" id="dropdownMenuButton" class="fa fa-sort-desc dropdown-toggle" aria-expanded="false"></i><ul class="dropdown-menu left" aria-labelledby="dropdownMenuButton">'
                    
                    for inm in ik:
                        value123 = str(inm).split(",")[0].replace("[", "").lstrip()
                        value1234 = str(inm).split(",")[1].replace("]", "").lstrip()
                        
                        if (
                            str(obj_obj.SAPCPQ_ATTRIBUTE_NAME) == "SYOBJR-30114"
                            or str(obj_obj.SAPCPQ_ATTRIBUTE_NAME) == "SYOBJR-60052"
                            or str(obj_obj.SAPCPQ_ATTRIBUTE_NAME) == "SYOBJR-70085"
                        ):
                            if value123 == objRecName:
                                other_tab = "0"
                                primary_view = value1234

                        else:
                            if value123 == objRecName:
                                tab_obj1 = Sql.GetFirst(
                                    "SELECT PG.TAB_NAME,PG.TAB_RECORD_ID FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE SE.PRIMARY_OBJECT_NAME='"
                                    + str(ObjectName)
                                    + "' and SE.SECTION_NAME ='BASIC INFORMATION'"
                                )
                        
                    if primary_view != "":
                        if str(current_tab).upper() == "PROFILE" and (ObjectName != "SYPROD"):
                            Action_str += (
                                '<li><a class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)">VIEW</a></li>'
                            )
                        elif str(current_tab).upper() == "PROFILE" and (ObjectName == "SYPROF"):
                            Action_str += '<li><a class="dropdown-item" href="#" onclick="profileObjSet(this)" data-target="#viewProfileRelatedList" data-toggle="modal">VIEW<a><li>'

                    else:
                        if str(current_tab).upper() == "PROFILE" and (ObjectName == "SYPROF"):
                            Action_str += '<li><a class="dropdown-item" href="#" onclick="profileObjSet(this)" data-target="#viewProfileRelatedList" data-toggle="modal">VIEW<a><li>'
                        elif str(current_tab).upper() == "PROFILE" and (ObjectName != "SYPROF"):
                            
                            Action_str += (
                                '<li><a class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)"  >VIEW<a><li>'
                            )
                        
                        # elif str(current_tab).upper() == "APP" and str(ObjectName)=="SYTABS":                    
                        #     Action_str += '<li><a class="dropdown-item" href="#" onclick="Move_to_parent_obj(this)">VIEW<a><li>'  
                        # elif str(current_tab).upper() == "ROLE":
                            # Action_str += '<li><a class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)"  >VIEW<a><li>'
                            
                        else:
                            #if ObjectName == "SAQSAO":
                            #Action_str += '<li><a class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)">VIEW</a></li>'
                            if ObjectName != "SAQIBP" :
                                Action_str += '<li><a class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)">VIEW</a></li>'
                            elif ObjectName == "SAQSAO":
                                Action_str += '<li><a id = '' class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)">VIEW</a></li>'


                    Trace.Write("12111111===3=====>"+str(Action_permission.get("Edit")).upper())
                    if str(Action_permission.get("Edit")).upper() == "TRUE":
                        if related_list_edit_permission:
                            if primary_view != "":
                                if other_tab == "1":
                                    Action_str += (
                                        '<li><a class="dropdown-item curptr"  href="../Configurator.aspx?pid='
                                        + str(product_id_val)
                                        + '" id = "'
                                        + primary_view
                                        + '"   onclick="Move_to_parent_obj_edit(this)">EDIT</a></li>'
                                    )
                                elif other_tab != "0":
                                    Action_str += (
                                        '<li><a class="dropdown-item curptr" href="#" id = "'
                                        + primary_view
                                        + '"  onclick="Move_to_parent_obj_edit(this)">EDIT</a></li>'
                                    )

                                elif str(current_tab).upper() == "PROFILE":
                                    Action_str += (
                                        '<li><a class="dropdown-item" href="#" onclick="Commontree_edit_RL(this)">EDIT</a></li>'
                                    )
                                else:
                                    if str(current_tab).upper() == "PROFILE":
                                        Action_str += '<li><a class="dropdown-item" href="#" onclick="Commontree_edit_RL(this)">EDIT</a></li>'
                                    elif str(current_tab).upper() == "SYPROF":
                                        Action_str += '<li><a class="dropdown-item" href="#" data-toggle="modal" data-target="#viewProfileRelatedList" onclick="profileObjSetEdit(this)">EDIT</a></li>'
                                    else:
                                        Action_str += '<li><a class="dropdown-item" href="#" onclick="cont_openedit(this)" data-target="#cont_viewModalSection" data-toggle="modal">EDIT</a></li>'

                            elif (
                                ObjectName == "SYPRAP"
                                or ObjectName == "SYPRTB"
                                or ObjectName == "SYPRSN"
                                or ObjectName == "SYPRAC"
                            ):
                                Action_str += (
                                    '<li><a class="dropdown-item" href="#" onclick="Commontree_edit_RL(this)">EDIT</a></li>'
                                )
                            elif ObjectName == "SYPROF":
                                Action_str += '<li><a class="dropdown-item" href="#" data-toggle="modal" data-target="#viewProfileRelatedList" onclick="profileObjSetEdit(this)">EDIT</a></li>'
                            else:
                                if str(current_tab).upper() == "PROFILE":
                                    Action_str += (
                                        '<li><a class="dropdown-item" href="#" onclick="Commontree_edit_RL(this)">EDIT</a></li>'
                                    )

                                elif Tree_Enable is not None and str(Tree_Enable.ENABLE_TREE).upper() == "TRUE":
                                    Action_str += (
                                        '<li><a class="dropdown-item" href="#" onclick="Commontree_edit_RL(this)">EDIT</a></li>'
                                    )
                                elif str(current_tab).upper() == "PROFILE":
                                    Action_str += (
                                        '<li><a class="dropdown-item" href="#" onclick="Commontree_edit_RL(this)">EDIT</a></li>'
                                    )
                                elif str(current_tab).upper() == "SYPROF":
                                    Action_str += '<li><a class="dropdown-item" href="#" data-toggle="modal" data-target="#viewProfileRelatedList" onclick="profileObjSetEdit(this)">EDIT</a></li>'
                                else:
                                    Action_str += '<li><a class="dropdown-item" href="#" onclick="cont_openedit(this)" data-target="#cont_viewModalSection" data-toggle="modal">EDIT</a></li>'
                    if str(Action_permission.get("Delete")).upper() == "TRUE":
                        if related_list_delete_permission:
                            onclick = "CommonDelete(this, '" + str(ObjectName) + "', 'WARNING')"
                            if str(ObjectName) == "SYOBJC":
                                Action_str += (
                                    '<li><a class="dropdown-item" href="#" id="deletebtn" onclick="'
                                    + str(onclick)
                                    + '" data-target="#cont_CommonModalDelete" data-toggle="modal">DROP</a></li>'
                                )
                            else:
                                Action_str += (
                                    '<li><a class="dropdown-item" href="#" id="deletebtn" onclick="'
                                    + str(onclick)
                                    + '" data-target="#cont_CommonModalDelete" data-toggle="modal">DELETE</a></li>'
                                )
                    Action_str += "</ul></div></div>"
                    
                    list_lineup1.append(("ACTIONS", Action_str))
                    OBJ_CpqTableEntryId = ""
                    try:
                        if str(ik.CpqTableEntryId) is not None and str(ik.CpqTableEntryId) != "":
                            OBJ_CpqTableEntryId = str(ik.CpqTableEntryId)
                            
                    except:
                        pass
                    for inm in ik:
                        a = str(inm).split(",")
                        value123 = a[0].replace("[", "").lstrip()
                        valu = ",".join(a[1:])
                        value1234 = valu.replace("]", "").lstrip()
                        
                        if value123 == objRecName:
                            current_rec_id = value1234
                        curr_symbol = ""
                        cur_api_name = Sql.GetFirst(
                            "select API_NAME,DATA_TYPE,FORMULA_DATA_TYPE from  SYOBJD (nolock) where API_NAME = '"
                            + str(value123)
                            + "' and OBJECT_NAME = '"
                            + str(ObjectName)
                            + "' "
                        )
                        
                        data_type_val = ""
                        formu_data_type_val = ""
                        if cur_api_name is not None:
                            data_type_val = cur_api_name.DATA_TYPE
                            formu_data_type_val = cur_api_name.FORMULA_DATA_TYPE
                        
                        if str(cur_api_name) is not None and (
                            str(data_type_val) == "CURRENCY" or str(formu_data_type_val) == "CURRENCY"
                        ):
                            
                            cur_api_name_obj = Sql.GetFirst(
                                "select CURRENCY_INDEX from  SYOBJD (nolock) where API_NAME = '"
                                + str(value123)
                                + "' and OBJECT_NAME = '"
                                + str(ObjectName)
                                + "' "
                            )
                            curr_symbol_obj = ""
                            try:
                                if cur_api_name_obj.CURRENCY_INDEX != "":
                                    if str(ObjectName) == "SAQIBP":
                                        contract_quote_record_id = Product.GetGlobal("contract_quote_record_id")
                                        curr_symbol_obj = Sql.GetFirst(
                                            "select SYMBOL,CURRENCY,DISPLAY_DECIMAL_PLACES from PRCURR (nolock) where CURRENCY_RECORD_ID = (select "
                                            + str(cur_api_name_obj.CURRENCY_INDEX)
                                            + " from SAQTMT"
                                            + " where MASTER_TABLE_QUOTE_RECORD_ID  "
                                            + " = '"
                                            + str(contract_quote_record_id)
                                            + "' ) "
                                        )
                                    else:
                                        if str(cur_api_name_obj.CURRENCY_INDEX) =="GLOBAL_CURRENCY":
                                            Globalcurrency=Sql.GetFirst("SELECT CURRENCY_RECORD_ID FROM PRCURR(NOLOCK) WHERE CURRENCY = 'USD' ")
                                            curr_symbol_obj = Sql.GetFirst(
                                                "select SYMBOL,CURRENCY,DISPLAY_DECIMAL_PLACES from PRCURR (nolock) where CURRENCY_RECORD_ID = '"+str(Globalcurrency.CURRENCY_RECORD_ID)+"'"
                                            )
                                        
                                        else:
                                            curr_symbol_obj = Sql.GetFirst(
                                                "select SYMBOL,CURRENCY,DISPLAY_DECIMAL_PLACES from PRCURR (nolock) where CURRENCY_RECORD_ID = (select "
                                                + str(cur_api_name_obj.CURRENCY_INDEX)
                                                + " from "
                                                + str(ObjectName)
                                                + " where  "
                                                + str(objRecName)
                                                + " = '"
                                                + str(current_rec_id)
                                                + "' ) "
                                            )
                                            
                                cur_api_name_obj = ""
                            except:
                                curr_symbol_obj = ""
                            curr_symbol = ""
                            decimal_place = 3
                            if curr_symbol_obj is not None and len(curr_symbol_obj) > 0 and curr_symbol_obj != "":
                                
                                curr_symbol = curr_symbol_obj.CURRENCY
                                decimal_place = curr_symbol_obj.DISPLAY_DECIMAL_PLACES
                                
                            if value1234 is not None:
                                if value1234 != "":
                                    if "-" in value1234:
                                        ccc = value1234.split("-")
                                        value1234 = value1234[0] + "" + ccc[1] + curr_symbol
                                    else:
                                        my_format = "{:,." + str(decimal_place) + "f}"
                                        value1234 = str(my_format.format(round(float(value1234), int(decimal_place))))
                                        if str(value123) == "ANNUAL_BILLING_AMOUNT" and str(ObjectName) == "SAQIBP":
                                            value1234 = value1234
                                        else:
                                            #Trace.Write("value123value123value123"+str(value123))
                                            value1234 = value1234 + " " + curr_symbol
                        if str(cur_api_name) is not None and (
                            str(data_type_val) == "PERCENT" or str(formu_data_type_val) == "PERCENT"
                        ):
                            decimal_place = 2
                            percentSymbol = "%"
                            
                            if value1234 is not None and value1234 != '':
                                my_format = "{:." + str(decimal_place) + "f}"
                                value1234 = str(my_format.format(round(float(value1234), int(decimal_place)))) + " %"

                        if value123 in lookup_disply_list:
                            for key, value in lookup_list.items():
                                if value == value123:
                                    if value123 == "ATTRIBUTE_UOM":
                                        key = ""
                                    lookup_obj = Sql.GetFirst(
                                        "SELECT LOOKUP_OBJECT FROM  SYOBJD (nolock) WHERE OBJECT_NAME = '"
                                        + str(ObjectName)
                                        + "' AND LOOKUP_API_NAME ='"
                                        + str(key)
                                        + "' AND DATA_TYPE = 'LOOKUP'"
                                    )                                    
                                    lookup_val = str(lookup_obj.LOOKUP_OBJECT)
                                    tab_obj = Sql.GetFirst(
                                        "SELECT TOP 10 PG.TAB_NAME,PG.TAB_RECORD_ID FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE SE.PRIMARY_OBJECT_NAME='"
                                        + str(lookup_val)
                                        + "' and SE.SECTION_NAME ='BASIC INFORMATION' ORDER BY SE.CpqTableEntryId asc"
                                    )
                                    if tab_obj is not None:
                                        tab_val = str(tab_obj.TAB_NAME).strip()
                                        if tab_val in list_of_tabs:
                                            ids[key] = value1234 + "|" + tab_val
                                            lookup_link_popup.append(key)
                                        else:
                                            product_name = Sql.GetFirst(
                                                "select APP_LABEL from SYTABS (nolock) where RECORD_ID='"
                                                + str(tab_obj.TAB_RECORD_ID)
                                                + "'"
                                            )
                                            if product_name is not None:
                                                module_txt = str(product_name.APP_LABEL).strip()
                                                product_id = Sql.GetFirst(
                                                    "select PRODUCT_ID from products (nolock) where PRODUCT_NAME='"
                                                    + str(module_txt)
                                                    + "'"
                                                )
                                            if product_id != "" and product_id is not None:
                                                pop_val[key] = value1234 + "|" + tab_val + "," + str(product_id.PRODUCT_ID)
                                            else:
                                                lookup_obj = Sql.GetFirst(
                                                    "SELECT LOOKUP_OBJECT FROM  SYOBJD (nolock) WHERE OBJECT_NAME = '"
                                                    + str(ObjectName)
                                                    + "' AND LOOKUP_API_NAME ='"
                                                    + str(key)
                                                    + "' AND DATA_TYPE = 'LOOKUP'"
                                                )
                                                lookup_val = str(lookup_obj.LOOKUP_OBJECT)
                                                pop_val[key] = value1234 + "|" + lookup_val
                                            lookup_rl_popup.append(key)
                                    else:
                                        lookup_obj = Sql.GetFirst(
                                            "SELECT LOOKUP_OBJECT FROM  SYOBJD (nolock) WHERE OBJECT_NAME = '"
                                            + str(ObjectName)
                                            + "' AND LOOKUP_API_NAME ='"
                                            + str(key)
                                            + "' AND DATA_TYPE = 'LOOKUP'"
                                        )
                                        lookup_val = str(lookup_obj.LOOKUP_OBJECT)
                                        pop_val[key] = value1234 + "|" + lookup_val
                                        lookup_rl_popup.append(key)
                        elif value123 == objRecName:
                            key_value = str(value1234)
                            if str(ObjectName) == "USERS":
                                value1234 = str(ObjectName) + "-" + str(key_value).rjust(6, "0")
                            elif str(ObjectName) == 'SAQDOC' and key_value == 'Pending':
                                value1234 = 'Pending'
                            else:
                                value1234 = str(ObjectName) + "-" + str(OBJ_CpqTableEntryId).rjust(6, "0")
                            tab_obj1 = Sql.GetFirst(
                                "SELECT PG.TAB_NAME,PG.TAB_RECORD_ID FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE SE.PRIMARY_OBJECT_NAME='"
                                + str(ObjectName)
                                + "' and SE.SECTION_NAME ='BASIC INFORMATION'"
                            )
                        else:
                            Trace.Write('At line 2805 -- Else')
                            imgValue = ''
                            if value1234.startswith("<img"):
                                # value1234 = value1234.replace('"', "&quot;")
                                value1234 = value1234.replace("<p>", " ")
                                value1234 = value1234.replace("</p>", " ")
                                imgValue = value1234
                                value1234 = value1234.split('"')
                                
                                value1234 = value1234[1]
                                
                            else:
                                value1234 = value1234.replace('"', "&quot;")
                                value1234 = value1234.replace("<p>", " ")
                                value1234 = value1234.replace("</p>", " ")
                            
                            #value1234 = value1234.split("&quot;")
                            #value1234 = value1234[1]
                            
                            img_list = ['PO_NOTES','PRICING_STATUS','EQUIPMENT_STATUS']
                            if str(ObjectName) == "SAQIFP":
                                img_list.append('PRICING_STATUS')
                            if str(ObjectName) == "SAQDOC":
                                img_list.append('STATUS')
                            if value123 in img_list:
                                new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + imgValue + "</abbr>")
                            else:
                                Trace.Write('At line 2832-- second else')
                                new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>")                            
                        ## addon product hyperlink starts
                        if str(RECORD_ID) == "SYOBJR-98859" and value123 == 'ADNPRD_ID':
                            contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                            get_key_value = Sql.GetFirst("SELECT {} AS VAL from {} (nolock) where QUOTE_RECORD_ID = '{}' and ADNPRD_ID = '{}' and SERVICE_ID = '{}'".format(str(objRecName),str(ObjectName),contract_quote_record_id,str(value1234),str(TreeParentParam)))
                            key_value = get_key_value.VAL
                        ## addon product hyperlink ends
                        if value123 in edit_field:
                            value1234 = value1234.replace('"', "&quot;")
                            value1234 = value1234.replace("<p>", " ")
                            value1234 = value1234.replace("</p>", " ")
                            
                            new_dict[value123] = (
                                '<abbr id ="' + value1234 + '" title="' + value1234 + '">' + value1234 + "</abbr>"
                            )                       
                            Trace.Write('At line 2848 edit field')     
                        else:
                            if value123 in checkbox_list:
                                new_dict[value123] = value1234
                            else:
                                if (value123 == "SET_NAME" or value123 == "SETMAT_NAME") and (
                                    RECORD_ID == "SYOBJR-90016" or RECORD_ID == "SYOBJR-30101"
                                ):
                                    new_dict[value123] = (
                                        "<a id='"
                                        + str(primary_view)
                                        + "' onclick='Move_to_parent_obj(this)'>"
                                        + value1234
                                        + "</a>"
                                    )
                                else:
                                    value1234 = value1234.replace('"', "&quot;")
                                    value1234 = value1234.replace("<p>", " ")
                                    value1234 = value1234.replace("</p>", " ")

                                    if value123 in [
                                        "ERROR",
                                        "MINIMUM_PRICE",
                                        "CATCLC_PRICE_INSORG_CURR",
                                        "INVCLC_UNITPRICE_INSORG_CURR",
                                    ]:
                                        new_dict[value123] = value1234
                                        seg_pric[value123] = value1234.replace(curr_symbol, "").replace(" ", "")
                                        seg_pric["PRICE_FACTOR"] = PriceFactor
                                    else:
                                        if str(TreeParentParam).upper() == "BRIDGE PRODUCTS" and  str(RECORD_ID) == "SYOBJR-00005" and str(value123) in ['SCHEDULE_MODE','CUSTOMER_ANNUAL_QUANTITY']:
                                            
                                            new_dict[value123] = (
                                                '<input id ="' + key_value + '" value="' + value1234 + '" style="border: 0px solid;" disabled> </input>'
                                            )
                                        elif str(value123) in billing_date_column:
                                            contract_quote_record_id = Product.GetGlobal("contract_quote_record_id")
                                            curr_symbol_obj = Sql.GetFirst(
                                                "select SYMBOL,CURRENCY,DISPLAY_DECIMAL_PLACES from PRCURR (nolock) where CURRENCY_RECORD_ID = (select QUOTE_CURRENCY_RECORD_ID"
                                                + " from SAQTMT"
                                                + " where MASTER_TABLE_QUOTE_RECORD_ID  "
                                                + " = '"
                                                + str(contract_quote_record_id)
                                                + "' ) "
                                            )
                                            concatedata = ""
                                            if curr_symbol_obj:
                                                curr_symbol = curr_symbol_obj.CURRENCY
                                                
                                                try:
                                                    decimal_place = curr_symbol_obj.DISPLAY_DECIMAL_PLACES
                                                    Trace.Write('curr_symbol--2289--'+str(curr_symbol))
                                                    my_format = "{:,." + str(decimal_place) + "f}"
                                                    value1234 = str(my_format.format(round(float(value1234), int(decimal_place))))
                                                except:
                                                    value1234
                                            new_dict[value123] = (
                                                '<abbr id ="' + key_value + '" class= "billclassedit"  value="' + value1234 + '" style="border: 0px solid;"  title="' + value1234 + '" disabled>' + value1234 + '</abbr>'
                                            )
                                        else:                                            
                                            if str(value123) != "CUSTOMER_ANNUAL_QUANTITY":
                                                precentage_columns = ['SALES_DISCOUNT','BD_DISCOUNT','TARGET_PRICE_MARGIN','BD_PRICE_MARGIN','YEAR_OVER_YEAR']
                                                if value123 in precentage_columns:
                                                    # perc = Sql.GetList("SELECT DISCOUNT FROM SAQICO WHERE "+str(value123)+" = '"+str(value1234)+"'")
                                                    string_val = str(value1234)
                                                    #string_val = string_val.replace('0','')
                                                    string_val1 = string_val.split('.')
                                                    str_val = string_val1[0]
                                                    value1234 = str_val
                                                    
                                                    if value1234 is not None and value1234 != '':
                                                        new_dict[value123] = (
                                                            '<abbr id ="' + key_value + '" title="' + value1234 +'">' + value1234 +  ' %' +  "</abbr>"
                                                        )
                                                        Trace.Write('At line 2899')
                                                    else:
                                                        new_dict[value123] = (
                                                        '<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>"
                                                    )    
                                                        Trace.Write('At line 2904')
                                                else:
                                                    
                                                    img_list = ['PO_NOTES','PRICING_STATUS','EQUIPMENT_STATUS']
                                                    if str(ObjectName) == "SAQIFP":
                                                        img_list.append('PRICING_STATUS')
                                                    if str(ObjectName) == "SAQDOC":
                                                        img_list.append('STATUS')
                                                    if value123 in img_list:
                                                        
                                                        new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + imgValue + "</abbr>")
                                                    # for redirecting the left tree node while viewing record from listgrid - start    
                                                    elif ObjectName in value1234: 
                                                        new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>") 
                                                        Trace.Write('At line 2918')
                                                    # for redirecting the left tree node while viewing record from listgrid - end       
                                                    elif ObjectName == "SAQSAO":
                                                        
                                                        new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>") 
                                                    else:
                                                        Trace.Write('At line 2924')
                                                        new_dict[value123] = ('<abbr title="' + value1234 + '">' + value1234 + "</abbr>")
                                                
                        
                        new_dict["ACTIONS"] = Action_str   
                        new_dict["ids"] = ids
                        new_dict["seg_pric"] = seg_pric
                        new_dict["pop_val"] = pop_val
                        new_dict["primary"] = primary
                        list_lineup.append(value123)
                    dict_key = list_lineup                   
                    table_list.append(new_dict)
                table_header += "<tr id='getbannername'>"
            #A055S000P01-682 start to hide the Actions column for related list
            rowspan = ''
            if RECORD_ID == 'SYOBJR-00009':
                rowspan = 'rowspan="2"'  
                
                #table_header += '<th colspan="23" data-align="right"><div><label class="onlytext"><div>QUOTE ITEMS</div></label></div></th>'
            if TreeParam == "Quote Preview" or TreeParam == "Contract Preview":
                table_header += ''            
            else:
                # A055S000P01-682 end to hide the Actions column for related list                 
                table_header += (
                    '<th data-field="ACTIONS" '
                    + rowspan
                    +'><div class="action_col">ACTIONS</div><button class="searched_button" id="Act_'
                    + str(table_id)
                    + '">Search</button></th>'
                )
                #A055S000P01-682 start to hide the Select column for related list    
            if TreeParam == "Quote Preview" or TreeParam == "Contract Preview":
                table_header += ''
            else:
                #A055S000P01-682 end to hide the Select column for related list                
                table_header += '<th data-field="SELECT"  class="wth45" data-checkbox="true" '+rowspan+'></th>'
            # if RECORD_ID == 'SYOBJR-00006':
            #     table_header += (
            #         '<th data-field="emp"  data-filter-control="input" data-title-tooltip="emp" data-formatter="" data-sortable="true"></th>'
            #     )
            # if TreeParam == "Items":
            #     table_header += (
            #         '<th data-field="ACTIONS"><div class="action_col">STATUS</div><button class="searched_button" id="STAT_'
            #         + str(table_id)
            #         + '"></button></th>'
            #     )
                # table_header += '<th data-field="STATUS"  class="wth45" ></th>'
                # table_header += (
                #     '<th data-field="emp"  data-filter-control="input" data-title-tooltip="emp" data-formatter="" data-sortable="true"></th>'
                # )

            filter_control_function = ""
            values_list = ""
            dict_form = {}
            ATTRIBUTE_NAME_List = []
            cv_list = []
            ignorecol = ['BILLING_DATE', 'BILLING_AMOUNT']
            for invs in list(eval(Columns)):
                table_ids = "#" + str(table_id)
                if invs in billing_date_column: # Billing Matrix - Pivot - Start
                    filter_clas = ("#" + str(table_id) + " .bootstrap-table-filter-control-" + str(invs).replace('-','_'))
                    values_list += "var x_" + str(invs).replace('-','_') + ' = $("' + str(filter_clas) + '").val(); '
                    values_list += "ATTRIBUTE_VALUEList.push(x_" + str(invs).replace('/','_').replace('-','_') + "); "              
                else:# Billing Matrix - Pivot - End
                    if invs not in ignorecol:
                        filter_clas = ("#" + str(table_id) + " .bootstrap-table-filter-control-" + str(invs))
                        values_list += "var " + str(invs) + ' = $("' + str(filter_clas) + '").val(); '
                        values_list += "ATTRIBUTE_VALUEList.push(" + str(invs) + "); "
                        

            Currentcol = Sql.GetFirst(
                "select COLUMNS from  SYOBJR (NOLOCK) where SAPCPQ_ATTRIBUTE_NAME ='" + str(RECORD_ID) + "'"
            )
            CountCol = eval(Currentcol.COLUMNS)
            
            # Billing Matrix - Pivot - Start
            Trace.Write('Colcount--ObjectName-----'+str(ObjectName))
            Colcount = 0
            #Trace.Write('Colcount--ObjectName-----'+str(ObjectName))
            Trace.Write('Colcount--billing_date_column-----'+str(len(billing_date_column)))
            if ObjectName == 'SAQIBP':
                Colcount += len(billing_date_column)
            # Billing Matrix - Pivot - End
            Colcount = len(CountCol) + 2
            

            filter_class = "#Act_" + str(table_id)
            filter_control_function += (
                '$("'
                + filter_class
                + '").click( function(){ var table_id = $(this).closest("table").attr("id"); ATTRIBUTE_VALUEList = []; '
                + str(values_list)
                + " var attribute_value = $(this).val(); SortColumn = localStorage.getItem('"
                + str(table_id)
                + "_SortColumn'); if (SortColumn === null){ SortColumn = \"\"; } SortColumnOrder = localStorage.getItem('"
                + str(table_id)
                + '_SortColumnOrder\'); if (SortColumnOrder === null){ SortColumnOrder = ""; } PerPage = $("#'
                + str(table_id)
                + '_PageCountValue").val(); PageInform = "1___" + PerPage + "___" + PerPage; cpq.server.executeScript("SYLDRTLIST", {"REC_ID":table_id, "ATTRIBUTE_NAME": '
                + str(list(eval(Columns)))
                + ', "ATTRIBUTE_VALUE": ATTRIBUTE_VALUEList, "ACTION" : "PRODUCT_ONLOAD_FILTER",  "SortColumn":SortColumn, "SortColumnOrder": SortColumnOrder, "PerPage": PerPage, "PageInform": PageInform, "PR_CURR": PR_CURR, "TP": TP ,"SUBTAB":"'
                + str(SubTab)
                +'"}, function(data) { console.log(data);$("'
                + str(table_ids)
                + '").bootstrapTable("load", data[0] );if (document.getElementById(\''
                + str(table_id)
                + "_totalItemCount')) { document.getElementById('"
                + str(table_id)
                + "_totalItemCount').innerHTML = data[1]; if ($('#"
                + str(table_id)
                + "_totalItemCount').text() == '0') { $('#"
                + str(table_id)
                + " > tbody').html('<tr class=\"noRecDisp\"><td colspan="
                + str(Colcount)
                + " class=\"txtltimp\">No Records to Display</td></tr>'); document.getElementById('"
                + str(table_id)+"').deleteTFoot();} }if (document.getElementById('"
                + str(table_id)
                + "_NumberofItem')) { document.getElementById('"
                + str(table_id)
                + "_NumberofItem').innerHTML = data[2];; } if(document.getElementById('"
                + str(table_id)
                + "_page_count')) { document.getElementById('"
                + str(table_id)
                + "_page_count').innerHTML = '1'; } $(\"#"
                + str(table_id)
                + '_PageCountValue").val(10); }); });'
            )
            filter_control_function +=("$('#SYOBJR_00009_E5504B40_36E7_4EA6_9774_EA686705A63F_RelatedMutipleCheckBoxDrop_0').on('checkChange', function (event){ setTimeout(function () { try{ var GetValInput = $('#dropdownlistContentSYOBJR_00009_E5504B40_36E7_4EA6_9774_EA686705A63F_RelatedMutipleCheckBoxDrop_0 span').text(); gevalSplit = GetValInput.split(','); if(gevalSplit[0].indexOf('>') != -1){ var RemoveImg = (GetValInput).split('>'); if(gevalSplit[1] != undefined) imgtext = RemoveImg[1]+','+gevalSplit[1]; else imgtext = RemoveImg[1]; } else if(gevalSplit[1].indexOf('>') != -1){ var RemoveImg = (GetValInput).split('>'); if(gevalSplit[0] != undefined) imgtext = gevalSplit[0]+','+RemoveImg[1]; else imgtext = RemoveImg[1]; } else{ imgtext = GetValInput; } $('#dropdownlistContentSYOBJR_00009_E5504B40_36E7_4EA6_9774_EA686705A63F_RelatedMutipleCheckBoxDrop_0 span').text(imgtext); } catch(err){ console.log('wrong---'); } }, 600); });")                                      
                    
           
            # Item Covered Object Column Grouping - Start
            table_group_columns = ''
            
            for key, invs in enumerate(list(eval(Columns))):
                table_ids = "#" + str(table_id)
                invs = str(invs).strip()
                
                qstring = attr_list.get(str(invs)) or ""
                if qstring == "":
                    qstring = invs.replace("_", " ")
               
                rowspan = ''
                if RECORD_ID == 'SYOBJR-00009':
                    rowspan = 'rowspan="2"'
                    #table_header += '<th colspan="5" data-align="right"><div><label class="onlytext"><label class="onlytext"><div>QUOTE ITEMS</div></label></div></th>'
                if key == 0:
                    if invs in primary_link_popup:
                        
                        if str(current_tab).upper() == "APP" and current_prod.upper() == "SYSTEM ADMIN":
                            
                            table_header += (
                                '<th  data-field="'
                                + str(invs)
                                + '" data-filter-control="input" data-title-tooltip="'
                                + str(qstring)
                                + '" data-formatter="primaryListHyperLink" data-sortable="true" '
                                + rowspan
                                +'>'
                                + str(qstring)
                                + "</th>"
                            )         
                        else:  
                            if str(TreeParam) != 'Quote Preview' and  str(TreeParam) != 'Billing Matrix':                                                      
                                
                                
                                table_header += (
                                    '<th  data-field="'
                                    + str(invs)
                                    + '" data-filter-control="input" data-title-tooltip="'
                                    + str(qstring)
                                    + '" data-formatter="commonrealtedhyperlink" data-sortable="true" '
                                    + rowspan
                                    +'>'
                                    + str(qstring)
                                    + "</th>"
                                )                                
                            else:
                                
                                table_header += (
                                    '<th  data-field="'
                                    + str(invs)
                                    + '" data-filter-control="input" data-title-tooltip="'
                                    + str(qstring)
                                    + '" data-sortable="true" '
                                    + rowspan
                                    +'>'
                                    + str(qstring)
                                    + "</th>"
                                )    
                                
                    # elif TreeParam == "Quote Preview" and RECORD_ID == 'SYOBJR-98792':                        
                    #     table_header += ''
                    # elif TreeParam == "Quote Preview" and RECORD_ID == 'SYOBJR-98795':                        
                    #     table_header += ''
                    # elif TreeParam == "Quote Preview" and RECORD_ID == 'SYOBJR-00006':                        
                    #     table_header += ''                                           
                    else:        
                        
                        if str(qstring) == "Purchase Order Notes" or str(qstring) == "Equipment Status":
                            table_header += (
                                '<th class="wth60" data-field="'
                                + str(invs)
                                + '" data-filter-control="input" data-align="center" data-title-tooltip="'
                                + str("STATUS")
                                + '" data-sortable="false" '
                                + rowspan
                                +'>'
                                + str("STATUS")
                                + "</th>"
                            )
                        elif RECORD_ID == 'SYOBJR-00010' and str(invs) == 'SERVICE_ID' and TreeParam != "Quote Preview":
                            table_header += (
                                '<th class="wth60" data-field="'
                                + str(invs)
                                + '" data-filter-control="input" data-align="center" data-title-tooltip="'
                                + str("STATUS")
                                + '" data-sortable="false" '
                                + rowspan
                                +'>'
                                + str("STATUS")
                                + "</th>"
                            )
                        else:
                            if (str(TreeParam) != 'Quote Preview' and str(TreeParam) != 'Contract Preview' and  str(TreeParam) != 'Billing Matrix' and str(current_tab).upper() != "APP"):
                               
                                table_header += (
                                    '<th  data-field="'
                                    + str(invs)
                                    + '" data-filter-control="input" data-title-tooltip="'
                                    + str(qstring)
                                    + '" data-formatter="commonrealtedhyperlink" data-sortable="true" '
                                    + rowspan
                                    +'>'
                                    + str(qstring)
                                    + "</th>"
                                )     
                            elif str(current_tab).upper() == "APP":
                                if (str(TreeParam) == "Tabs" or str(TreeParam) == "Pages"):
                                    table_header += (
                                        '<th  data-field="'
                                        + str(invs)
                                        + '" data-filter-control="input" data-title-tooltip="'
                                        + str(qstring)
                                        + '" data-formatter="ParentListHyperLink" data-sortable="true" '
                                        + rowspan
                                        +'>'
                                        + str(qstring)
                                        + "</th>"
                                    )    
                                else:
                                    table_header += (
                                        '<th  data-field="'
                                        + str(invs)
                                        + '" data-filter-control="input" data-title-tooltip="'
                                        + str(qstring)
                                        + '" data-formatter="commonrealtedhyperlink" data-sortable="true" '
                                        + rowspan
                                        +'>'
                                        + str(qstring)
                                        + "</th>"
                                    )  
                            else:
                                table_header += (
                                    '<th  data-field="'
                                    + str(invs)
                                    + '" data-filter-control="input" data-title-tooltip="'
                                    + str(qstring)
                                    + '" data-sortable="true" '
                                    + rowspan
                                    +'>'
                                    + str(qstring)
                                    + "</th>"
                                )    
                                

                
                elif RECORD_ID == 'SYOBJR-00009' and invs in ('PRICE_BENCHMARK_TYPE','TOOL_CONFIGURATION','ANNUAL_BENCHMARK_BOOKING_PRICE','CONTRACT_ID','CONTRACT_VALID_FROM','CONTRACT_VALID_TO','BENCHMARKING_THRESHOLD'):
                    
                    align = ''
                   
                    if not table_group_columns:
                        table_header += '<th colspan="7" data-align="center"><div><button style="border:none;" class="glyphicon glyphicon-minus-sign" id="price-benchmark-column-toggle" onclick="price_benchmark_column_toggle(this)"></button>PRICE BENCHMARKING</div></th>'
                    if str(invs) in right_align_list:
                        align = 'right'
                    elif str(invs) in center_align_list:
                        align = 'center'
                    table_group_columns += (
                                '<th data-toggle="bootstrap-table" data-field="'
                                + str(invs)
                                + '" data-filter-control="input" data-align="'
                                + str(align)
                                +'" data-title-tooltsip="'
                                + str(qstring)
                                + '" data-sortable="true">'
                                + str(qstring)
                                + "</th>"
                            )           
                    continue
                elif len(cell_api) > 0 and invs in cell_api:                    
                    table_header += (
                        '<th  data-field="'
                        + str(invs)
                        + '" data-filter-control="input" data-cell-style="SgpbenrowStyle" data-title-tooltip="'
                        + str(qstring)
                        + '" data-sortable="true" '
                        + rowspan
                        +'>'
                        + str(qstring)
                        + "</th>"
                    )
                    
                elif lookup_link_popup is not None and invs in lookup_link_popup and (str(invs) != "TAB_NAME" and str(ObjectName) != "SYPSAC"):                    
                    table_header += (
                        '<th  data-field="'
                        + str(invs)
                        + '" data-filter-control="input" data-title-tooltip="'
                        + str(qstring)
                        + '" data-formatter="ParentListHyperLink" data-sortable="true" '
                        + rowspan
                        +'>'
                        + str(qstring)
                        + "</th>"
                    )
                    
                elif lookup_rl_popup is not None and invs in lookup_rl_popup:            
                    footer_text_formatter = ''

                    if RECORD_ID == 'SYOBJR-00024' and invs == 'APRCHNSTP_ID':                        
                        table_header += (
                            '<th  data-field="'
                            + str(invs)
                            + '" data-filter-control="input" data-align="right" data-title-tooltip="'
                            + str(qstring)
                            + '" data-sortable="true" '                            
                            + rowspan
                            +'>'
                            + str(qstring)
                            + "</th>"
                        )
                    else:        
                        table_header += (
                            '<th  data-field="'
                            + str(invs)
                            + '" data-filter-control="input" data-title-tooltip="'
                            + str(qstring)
                            + '" data-sortable="true" '
                            + str(footer_text_formatter)
                            + ' '
                            + rowspan
                            +'>'
                            + str(qstring)
                            + "</th>"
                        )                    
                    
                # + '" data-formatter="ParentRelatedListHyperLink" data-sortable="true">'
                elif checkbox_list is not None and invs in checkbox_list:
                                        
                    table_header += (
                        '<th  data-field="'
                        + str(invs)
                        + '" data-filter-control="input" data-align="center" data-title-tooltip="'
                        + str(qstring)
                        + '" data-formatter="CheckboxFieldRelatedList" data-sortable="true" '
                        + rowspan
                        +'>'
                        + str(qstring)
                        + "</th>"
                    )
                    
                elif edit_field is not None and invs in edit_field:                    
                    table_header += (
                        '<th  data-field="'
                        + str(invs)
                        + '" data-filter-control="input" data-title-tooltip="'
                        + str(qstring)
                        + '" data-formatter="editIconIfValueChanged" data-sortable="true" '
                        + rowspan
                        +'>'
                        + str(qstring)
                        + "</th>"
                    )
                                        
                else:
                                       
                    dblclick_ele.append(invs)
                    if str(invs) in right_align_list:                        
                        visible = ""
                        if RECORD_ID == 'SYOBJR-00007' and str(invs) == 'BILLING_AMOUNT':                            
                            visible = 'data-visible="false"'               
                        table_header += (
                            '<th  data-field="'
                            + str(invs)
                            + '" data-filter-control="input" data-align="right" data-title-tooltip="'
                            + str(qstring)
                            + '" data-sortable="true" '
                            + str(visible)
                            + ' '
                            + rowspan
                            + '>'
                            + str(qstring)
                            + "</th>"
                        )                        
                    elif str(invs) in center_align_list:                        
                        if RECORD_ID == 'SYOBJR-00010' and str(invs) == 'SERVICE_ID' and TreeParam != "Quote Preview":
                            table_header += (
                                '<th class="wth60" data-field="'
                                + str(invs)
                                + '" data-filter-control="input" data-align="center" data-title-tooltip="'
                                + str("STATUS")
                                + '" data-sortable="false" '
                                + rowspan
                                +'>'
                                + str("STATUS")
                                + "</th>"
                            )
                        else:                            
                            visible = ""
                            if RECORD_ID == 'SYOBJR-00007' and str(invs) == 'BILLING_DATE':
                                visible = 'data-visible="false"'                   
                            table_header += (
                                '<th  data-field="'
                                + str(invs)
                                + '" data-filter-control="input" data-align="center" data-title-tooltip="'
                                + str(qstring)
                                + '" data-sortable="true" '
                                + str(visible)
                                + ' '
                                + rowspan
                                +'>'
                                + str(qstring)
                                + "</th>"
                            )
                    else:                        
                        if str(qstring) == "Key": 
                            
                            if ObjectName == "CTCICO":
                                table_header += (
                                    '<th  data-field="'
                                    + str(invs)
                                    + '" data-filter-control="input" data-title-tooltip="'
                                    + str(qstring)
                                    + '" data-formatter="" data-sortable="true" '
                                    + rowspan
                                    +'>'
                                    + str(qstring)
                                    + "</th>"
                                )
                            else:
                                table_header += (
                                    '<th  data-field="'
                                    + str(invs)
                                    + '" data-filter-control="input" data-title-tooltip="'
                                    + str(qstring)
                                    + '" data-formatter="commonrealtedhyperlink" data-sortable="true" '
                                    + rowspan
                                    +'>'
                                    + str(qstring)
                                    + "</th>"
                                )
                        elif RECORD_ID == 'SYOBJR-00007' and str(invs) in billing_date_column: # Billing Matrix Date Change Model and Footer - Start
                            
                            footer_formatter = ''
                            #'data-footer-formatter="priceSumFormatter"'
                            tooltip = qstring
                            qstring = '<a onclick="openBillingMatrixDateChangeModal(\'{Value}\')" href="#">{Value}</a>'.format(Value=qstring.replace('-','/'))
                            #data_field = invs.replace('/','-')
                            #Trace.Write('2780-------month-------'+ str(invs))
                            table_header += (
                                '<th  data-field="'
                                + str(invs)
                                + '" data-filter-control="input" class="text-right cust_billing_date" data-title-tooltip="'
                                + str(tooltip)
                                + '" data-sortable="true" '
                                + str(footer_formatter)
                                + ' '
                                + rowspan
                                +'>'
                                + str(qstring)
                                + "</th>"
                            ) # Billing Matrix Date Change Model and Footer - Start
                        else:                    
                            table_header += (
                                '<th  data-field="'
                                + str(invs)
                                + '" data-filter-control="input" class="cust_billing_name" data-title-tooltip="'
                                + str(qstring)
                                + '" data-sortable="true" '
                                + rowspan
                                +'>'
                                + str(qstring)
                                + "</th>"
                            )
            table_header += "</tr>"
        if RECORD_ID == 'SYOBJR-00009' and table_group_columns:
            table_header += '<tr>{}</tr>'.format(table_group_columns)
        if RECORD_ID == 'SYOBJR-00009':
            cls = "eq(3)"
            table_header += '</thead><tbody onclick="Table_Onclick_Scroll(this)"></tbody></table>'
        else:
            table_header += '</thead><tbody onclick="Table_Onclick_Scroll(this)"></tbody></table>'
        cls = "eq(2)"
        CHL_STS_OBJ = None

        if CHL_STS_OBJ is not None:
            
            dbl_clk_function += (
                '$("'
                + str(table_ids)
                + '").on("all.bs.table", function (e, name, args) { $(".bs-checkbox input").addClass("custom"); $(".bs-checkbox input").after("<span class=\'lbl\'></span>"); }); $("'
                + str(table_ids)
                + '\ th.bs-checkbox div.th-inner").before("<div class=\'pad0brdbt\'>SELECT</div>"); $(".bs-checkbox input").addClass("custom"); $(".bs-checkbox input").after("<span class=\'lbl\'></span>"); function onClickCell(event, field, value, row, $element) { var reco_id=""; var reco = []; reco = localStorage.getItem("multiedit_checkbox_clicked"); if (reco === null || reco === undefined ){ reco = []; } if (reco.length > 0){reco = reco.split(",");} if (reco.length > 0){ reco.push($element.closest("tr").find("td:'
                + str(cls)
                + '").text());  data1 = $element.closest("tr").find("td:'
                + str(cls)
                + '").text(); localStorage.setItem("multiedit_save_date", data1); reco_id = removeDuplicates(reco); }else{reco_id=$element.closest("tr").find("td:'
                + str(cls)
                + '").text(); reco_id=reco_id.split(","); localStorage.setItem("multiedit_save_date", reco_id); } localStorage.setItem("multiedit_data_clicked", reco_id); localStorage.setItem("table_id_RL_edit", "'
                + str(table_id)
                + '"); cpq.server.executeScript("SYBLKETRLG", {"TITLE":field, "VALUE":value, "CLICKEDID":"'
                + str(table_id)
                + '", "RECORDID":reco_id, "ELEMENT":"RELATEDEDIT"}, function(data) { data1=data[0]; data2=data[1]; if(data1 != "NO"){ if(document.getElementById("RL_EDIT_DIV_ID") ) { document.getElementById("RL_EDIT_DIV_ID").innerHTML = data1; document.getElementById("cont_multiEditModalSection").style.display = "block"; $("#cont_multiEditModalSection").prepend("<div class=\'modal-backdrop fade in\'></div>"); var divHeight = $("#cont_multiEditModalSection").height(); $("#cont_multiEditModalSection .modal-backdrop").css("min-height", divHeight+"px"); $("#cont_multiEditModalSection .modal-dialog").css("width","550px"); $(".modal-dialog").css("margin-top","100px"); } if (data2.length !== 0){ $.each( data2, function( key, values ) { onclick_datepicker(values) }); } } }); }                   $("'
                + str(table_ids)
                + "\").on('sort.bs.table', function (e, name, order) {  currenttab = $(\"ul#carttabs_head .active\").text().trim(); localStorage.setItem('"
                + str(table_id)
                + "_SortColumn', name); localStorage.setItem('"
                + str(table_id)
                + "_SortColumnOrder', order); RelatedContainerSorting(name, order, '"
                + str(table_id)
                + "'); }); "
            )

        else:
            
            dbl_clk_function += (
                'var checkedRows=[]; localStorage.setItem("multiedit_checkbox_clicked", []); $("'
                + str(table_ids)
                + '").on("check.bs.table", function (e, row, $element) { console.log("checked00009==");checkedRows.push($element.closest("tr").find("td:'
                + str(cls)
                + '").text()); localStorage.setItem("multiedit_checkbox_clicked", checkedRows); }); $("'
                + str(table_ids)
                + '").on("check-all.bs.table", function (e) { var table = $("'
                + str(table_ids)
                + '").closest("table"); table.find("tbody tr").each(function() { checkedRows.push($(this).find("td:nth-child(3)").text()); }); localStorage.setItem("multiedit_checkbox_clicked", checkedRows); }); $("'
                + str(table_ids)
                + '").on("uncheck-all.bs.table", function (e) { localStorage.setItem("multiedit_checkbox_clicked", []); checkedRows=[]; }); $("'
                + str(table_ids)
                + '").on("uncheck.bs.table", function (e, row, $element) { var rec_ids=$element.closest("tr").find("td:'
                + str(cls)
                + '").text(); $.each(checkedRows, function(index, value) { if (value === rec_ids) { checkedRows.splice(index,1); }}); localStorage.setItem("multiedit_checkbox_clicked", checkedRows); });'
            )
            dbl_clk_function += (
                '$("'
                + str(table_ids)
                + '").on("dbl-click-cell.bs.table", onClickCell); $("'
                + str(table_ids)
                + '").on("all.bs.table", function (e, name, args) { $(".bs-checkbox input").addClass("custom"); $(".bs-checkbox input").after("<span class=\'lbl\'></span>"); }); $("'
                + str(table_ids)
                + '\ th.bs-checkbox div.th-inner").before("<div class=\'pad0brdbt\' >SELECT</div>"); $(".bs-checkbox input").addClass("custom"); $(".bs-checkbox input").after("<span class=\'lbl\'></span>"); function onClickCell(event, field, value, row, $element) { var reco_id=""; var reco = []; reco = localStorage.getItem("multiedit_checkbox_clicked"); if (reco === null || reco === undefined ){ reco = []; } if (reco.length > 0){reco = reco.split(",");} if (reco.length > 0){ reco.push($element.closest("tr").find("td:'
                + str(cls)
                + '").text());  data1 = $element.closest("tr").find("td:'
                + str(cls)
                + '").text(); localStorage.setItem("multiedit_save_date", data1); reco_id = removeDuplicates(reco); }else{reco_id=$element.closest("tr").find("td:'
                + str(cls)
                + '").text(); reco_id=reco_id.split(","); localStorage.setItem("multiedit_save_date", reco_id); } localStorage.setItem("multiedit_data_clicked", reco_id); localStorage.setItem("table_id_RL_edit", "'
                + str(table_id)
                + '"); cpq.server.executeScript("SYBLKETRLG", {"TITLE":field, "VALUE":value, "CLICKEDID":"'
                + str(table_id)
                + '", "RECORDID":reco_id, "ELEMENT":"RELATEDEDIT"}, function(data) { data1=data[0]; data2=data[1]; if(data1 != "NO"){ if(document.getElementById("RL_EDIT_DIV_ID") ) { document.getElementById("RL_EDIT_DIV_ID").innerHTML = data1; document.getElementById("cont_multiEditModalSection").style.display = "block"; $("#cont_multiEditModalSection").prepend("<div class=\'modal-backdrop fade in\'></div>"); var divHeight = $("#cont_multiEditModalSection").height(); $("#cont_multiEditModalSection .modal-backdrop").css("min-height", divHeight+"px"); $("#cont_multiEditModalSection .modal-dialog").css("width","550px"); $(".modal-dialog").css("margin-top","100px"); }TreeParentParam = localStorage.getItem("CommonTreeParentParam");var sparePartsBulkSAVEBtn = $(".secondary_highlight_panel").find("button#spare-parts-bulk-save-btn");var sparePartsBulkEDITBtn = $(".secondary_highlight_panel").find("button#spare-parts-bulk-edit-btn");var sparePartsBulkAddBtn = $(".secondary_highlight_panel").find("button#spare-parts-bulk-add-modal-btn");if (sparePartsBulkAddBtn.length == 0 && TreeParentParam =="Bridge Products"){$("#cont_multiEditModalSection").css("display","none");} else if(sparePartsBulkAddBtn.length == 1 && TreeParentParam =="Bridge Products"){$("#cont_multiEditModalSection").css("display","block");$("#spare-parts-bulk-edit-btn").css("display","none");$("#spare-parts-bulk-add-modal-btn").css("display","none");}; if (data2.length !== 0){ $.each( data2, function( key, values ) { onclick_datepicker(values) }); } } }); }                   $("'
                + str(table_ids)
                + "\").on('sort.bs.table', function (e, name, order) {  currenttab = $(\"ul#carttabs_head .active\").text().trim(); localStorage.setItem('"
                + str(table_id)
                + "_SortColumn', name); localStorage.setItem('"
                + str(table_id)
                + "_SortColumnOrder', order); RelatedContainerSorting(name, order, '"
                + str(table_id)
                + "'); }); "
            )            
        
        

        NORECORDS = ""
        if len(table_list) == 0:
            NORECORDS = "NORECORDS"
        DropDownList = []
        filter_level_list = []
        filter_clas_name = ""
        cv_list = []
        TableclassName = "form-control" + table_id
        footer_str, footer = "", ""
        gettotalamt = getgrandtotalamt = ""
        if ObjectName == "SAQIBP":
            ContractRecordId = Product.GetGlobal("contract_quote_record_id")
            gettotaldateamt = Sql.GetList("SELECT BILLING_AMOUNT=SUM(BILLING_AMOUNT),ANNUAL_BILLING_AMOUNT = SUM(ANNUAL_BILLING_AMOUNT),BILLING_DATE FROM SAQIBP WHERE BILLING_DATE in {billing_date_column} and QUOTE_RECORD_ID ='{cq}' group by BILLING_DATE ".format(cq=str(ContractRecordId),billing_date_column=str(tuple(billing_date_column))))
            if gettotaldateamt:
                my_format = "{:,." + str(decimal_place) + "f}"
                for val in gettotaldateamt: 
                    gettotalamt = str(my_format.format(round(float(val.ANNUAL_BILLING_AMOUNT), int(decimal_place))))  
                    
            if gettotaldateamt:
                my_format = "{:,." + str(decimal_place) + "f}"
            
                
                footer_tot += '<th colspan="1" class="text-left">{}</th>'.format(curr_symbol)
                footer_tot += '<th colspan="1" class="text-right">{}</th>'.format(gettotalamt)
                for val in gettotaldateamt:
                    getamt = str(my_format.format(round(float(val.BILLING_AMOUNT), int(decimal_place))))
                    footer_tot += '<th class="text-right">{}</th>'.format(getamt)
            
        for key, col_name in enumerate(list(eval(Columns))):            
            StringValue_list = []
            filter_level_data = ""
            objss_obj = Sql.GetFirst(
                "SELECT API_NAME, DATA_TYPE, FORMULA_LOGIC, PICKLIST FROM  SYOBJD (nolock) WHERE OBJECT_NAME='"
                + str(ObjectName)
                + "' and API_NAME = '"
                + str(col_name)
                + "'"
            )           
            if objss_obj:
                try:
                     
                    FORMULA_LOGIC = objss_obj.FORMULA_LOGIC.strip()
                    FORMULA_col = FORMULA_LOGIC.split(" ")[1].strip()
                    FORMULA_table = FORMULA_LOGIC.split(" ")[3].strip()
                    if str(objss_obj.PICKLIST).upper() == "TRUE":                                                
                        filter_level_data = "select"                        
                        filter_clas_name = (
                            '<div dropDownWidth="true" id = "'
                            + str(table_id)
                            + "_RelatedMutipleCheckBoxDrop_"
                            + str(key)
                            + '" class="form-control bootstrap-table-filter-control-'
                            + str(col_name)
                            + " RelatedMutipleCheckBoxDrop_"
                            + str(key)
                            + ' "></div>'
                        )
                        filter_level_list.append(filter_level_data)
                    else:                        
                        filter_level_data = "input"
                        filter_clas_name = (
                            '<input type="text"   class="width100_vis form-control bootstrap-table-filter-control-'
                            + str(col_name)
                            + '">'
                        )
                        filter_level_list.append(filter_level_data)
                except:
                    if str(objss_obj.PICKLIST).upper() == "TRUE": 
                                         
                        filter_level_data = "select"
                        filter_clas_name = (
                            '<div  id = "'
                            + str(table_id)
                            + "_RelatedMutipleCheckBoxDrop_"
                            + str(key)
                            + '" class="form-control bootstrap-table-filter-control-'
                            + str(col_name)
                            + " RelatedMutipleCheckBoxDrop_"
                            + str(key)
                            + ' "></div>'
                        )
                        filter_level_list.append(filter_level_data)
                    else:                        
                        filter_level_data = "input"
                        filter_clas_name = (
                            '<input type="text"  class="width100_vis form-control bootstrap-table-filter-control-'
                            + str(col_name)
                            + '">'
                        )
                        filter_level_list.append(filter_level_data)
                cv_list.append(filter_clas_name)
            if filter_level_data == "select" and col_name not in checkbox_list:                
                try:
                    if str(col_name) == "EXCHANGE_RATE_DATE":
                        zzz = (
                            "SELECT Top 1000 CONVERT(VARCHAR(10),"
                            + str(col_name)
                            + ",101) as EXCHANGE_RATE_DATE  from "
                            + str(ObjectName)
                            + " (nolock) where "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' ORDER BY CONVERT(DateTime,"
                            + str(col_name)
                            + ",101) DESC "
                        )
                        xcdStr = (
                            "SELECT  Top 1000 CONVERT(VARCHAR(10),"
                            + str(col_name)
                            + ",101) as EXCHANGE_RATE_DATE  from "
                            + str(ObjectName)
                            + " (nolock) where "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' ORDER BY CONVERT(DateTime,"
                            + str(col_name)
                            + ",101) DESC"
                        )
                        
                    else:
                        if str(col_name) == 'TRACKING_TYPE':
                            RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_AC_00159").GetValue()
                            Wh_API_NAME = "APPROVAL_TRACKED_FIELD_RECORD_ID"
                        xcdStr = (
                            "SELECT DISTINCT TOP 10000000 "
                            + col_name
                            + " FROM "
                            + str(ObjectName)
                            + " (nolock) where "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "'"
                            + " ORDER BY "
                            + str(col_name)
                        )
                    xcd = Sql.GetList(xcdStr)
                except:
                    
                    if str(col_name) != "EXCHANGE_RATE_DATE":
                        
                        xcdStr = (
                            "SELECT "
                            + str(col_name)
                            + "  from "
                            + str(ObjectName)
                            + " (nolock) where "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "'"
                        )
                        xcd = Sql.GetList(xcdStr)
                

                try:
                    if xcd is not None:
                        StringValue_list = [
                            str(eval("ins." + str(col_name))) for ins in xcd if eval("ins." + str(col_name)) != ""
                        ]
                        
                        StringValue_list = filter(None, list(set(StringValue_list)))
                        if len(StringValue_list) == 0:
                            StringValue_list = [""]
                    else:
                        StringValue_list = [""]
                    if str(col_name) == "EXCHANGE_RATE_DATE":
                        StringValue_list.sort(key=lambda x: time.mktime(time.strptime(x, "%d/%m/%Y")), reverse=True)
                    elif str(col_name) == 'TRACKING_TYPE':
                        StringValue_list = ["ALL VALUES","ANY CHANGE"]
                    else:
                        StringValue_list.sort()
                except:
                    StringValue_list = [""]
                StringValue_lists=[]
                
                for string in StringValue_list:
                    if string == "ACQUIRED":
                        string_value = string.replace("ACQUIRED","<img title='Acquired' src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg> ACQUIRED")
                    if string == "APPROVAL REQUIRED":
                        string_value = string.replace("APPROVAL REQUIRED","<img title='Approval Required' src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg> APPROVAL REQUIRED")
                    if string == "ACQUIRING":                        
                        string_value = string.replace("ACQUIRING","<img title='Acquiring' src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg> ACQUIRING")
                    if string == "ERROR":
                        string_value = string.replace("ERROR","<img title='Error' src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg> ERROR")
                    if string == "ASSEMBLY MISSING":
                        string_value = string.replace("ASSEMBLY MISSING","<img title='Assembly Missing' src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Orange1_Circle.svg> ASSEMBLY MISSING")
                    if string == "PARTIALLY PRICED":
                        string_value = string.replace("PARTIALLY PRICED","<img title='Partially Priced' src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Red1_Circle.svg> PARTIALLY PRICED")
                    if string != "ACQUIRED" and string != "APPROVAL REQUIRED" and string != "ERROR" and string != "ASSEMBLY MISSING" and string != "PARTIALLY PRICED" and string != "ACQUIRING":                        
                        string_value = string
                    StringValue_lists.append(string_value)
                DropDownList.append(StringValue_lists)
                
            elif col_name in checkbox_list:
                DropDownList.append(["True", "False"])
            elif ObjectName == 'SAQIBP' and (col_name in billing_date_column or col_name == 'BILLING_CURRENCY'):# Billing Matrix - Pivot - Start
                try:
                    gettotaldateamt =""
                    #Trace.Write('col_name-----3087-----'+str(col_name))
                    if col_name in billing_date_column:                    
                        my_format = "{:,." + str(decimal_place) + "f}"
                        tovalue = 0.00
                        getamt = BILLING_AMOUNTTOL = ""                        
                        #footer += '<th>{}{}</th>'.format(my_format.(sum([float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0].split(" ")[0].replace(",","")) for data in table_list])) ,curr_symbol)
                        for data in table_list:
                            #Trace.Write('getval ---------'+str(float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0].replace(",",""))))
                            tovalue += float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0].replace(",",""))
                            getamt = str(my_format.format(round(float(tovalue), int(decimal_place))))
                        #Trace.Write('getamt----'+str(getamt)+'-----tovalue----'+str(tovalue))
                        footer += '<th class="text-right">{}</th>'.format(getamt)
                    else:
                        if table_list:
                            currency_obj = re.search(r'>(.+?)<', table_list[0].get(col_name))
                            if currency_obj:
                                footer += '<th colspan="2" class="text-left">{}</th>'.format(currency_obj.group(1))
                            else:
                                footer += '<th colspan="2" class="text-left"></th>'
                    
                    
                    #footer += '<th>{}{}</th>'.format(sum([float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0].split(" ")[0].replace(",","")) for data in table_list]),curr_symbol)
                    #footer += '<th>{}</th>'.format(sum([float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0]) for data in table_list]))
                except Exception:                    
                    footer += '<th>0.00</th>'
                    footer_tot += '<th>0.00</th>'
                filter_level_data = "input"
                col_name = col_name.replace('/','-')
                col_name = col_name.replace('-','_')                
                filter_clas_name = (
                    '<input type="text" class="width100_vis form-control bootstrap-table-filter-control-'
                    + str(col_name)
                    + '">'
                )
                filter_level_list.append(filter_level_data)
                cv_list.append(filter_clas_name)
            else:
                DropDownList.append("")
        if ObjectName == 'SAQIBP':
            #footer_str = '<tfoot><tr><th colspan="7" id= "getbill1year" class="text-left">{}</th>{}</tr><tr><th colspan="7" id= "getbillyear" class="text-left">{}</th>{}</tr></tfoot>'.format("SUBTOTAL", footer,str(SubTab)+" Total",footer_tot)
            footer_str = '<tfoot><tr><th colspan="7" id= "getbill1year" class="text-left">{}</th>{}</tr><tr></tr></tfoot>'.format("GRAND TOTAL", footer_tot)
        RelatedDrop_str = (
            "try { if( document.getElementById('"
            + str(table_id)
            + "') ) { var listws = document.getElementById('"
            + str(table_id)
            + "').getElementsByClassName('filter-control');  for (i = 0; i < listws.length; i++) { document.getElementById('"
            + str(table_id)
            + "').getElementsByClassName('filter-control')[i].innerHTML = data6[i];  } for (j = 0; j < listws.length; j++) { if (data7[j] == 'select') { var dataAdapter = new $.jqx.dataAdapter(data8[j]); if(data8[j].length>5){ $('#"
            + str(table_id)
            + "_RelatedMutipleCheckBoxDrop_' + j.toString() ).jqxDropDownList( { checkboxes: true, source: dataAdapter, dropDownWidth:200}); }else{$('#"
            + str(table_id)
            + "_RelatedMutipleCheckBoxDrop_' + j.toString() ).jqxDropDownList( { checkboxes: true, source: dataAdapter ,width: 200, autoDropDownHeight: true, dropDownWidth:200});} } } } }  catch(err) { setTimeout(function() { var listws = document.getElementById('"
            + str(table_id)
            + "').getElementsByClassName('filter-control');  for (i = 0; i < listws.length; i++) { document.getElementById('"
            + str(table_id)
            + "').getElementsByClassName('filter-control')[i].innerHTML = data6[i];  } for (j = 0; j < listws.length; j++) { if (data7[j] == 'select') { var dataAdapter = new $.jqx.dataAdapter(data8[j]); $('#"
            + str(table_id)
            + "_RelatedMutipleCheckBoxDrop_' + j.toString() ).jqxDropDownList( { checkboxes: true, source: dataAdapter, width: 200, dropDownWidth:200, scrollBarSize :10 }); } } }, 10); }"
        )
        
        try:
            get_Param_Val = Product.GetGlobal("CurrTreeParamVal")
            Selected_Node = Product.GetGlobal("SEL_NODE_LIST")
            EXECUTION_TIME = Product.GetGlobal("EXECUTION")
            if get_Param_Val != "" and Selected_Node != "":
                Selected_Node = eval(Selected_Node)
                if get_Param_Val in Selected_Node:
                    if Selected_Node.get(str(get_Param_Val)) == "1":
                        
                        filter_control_function += (
                            'try { $("#'
                            + str(table_id)
                            + '").colResizable({ resizeMode:"overflow", onResize: function(){ $("div[id^=\''
                            + str(table_id)
                            + '_RelatedMutipleCheckBoxDrop\']").jqxDropDownList("close"); } }); } catch (err) { setTimeout(function(){ $("#'
                            + str(table_id)
                            + '").colResizable({ resizeMode:"overflow", onResize: function(){ $("div[id^=\''
                            + str(table_id)
                            + '_RelatedMutipleCheckBoxDrop\']").jqxDropDownList("close"); }}); }, 3000); } finally { setTimeout(function(){ $("#'
                            + str(table_id)
                            + '").colResizable({ resizeMode:"overflow" }); }, 5000); }'
                        )
                        
            else:
                
                filter_control_function += (
                    'try { $("#'
                    + str(table_id)
                    + '").colResizable({ resizeMode:"overflow", onResize: function(){ $("div[id^=\''
                    + str(table_id)
                    + '_RelatedMutipleCheckBoxDrop\']").jqxDropDownList("close"); } }); } catch (err) { setTimeout(function(){ $("#'
                    + str(table_id)
                    + '").colResizable({ resizeMode:"overflow", onResize: function(){ $("div[id^=\''
                    + str(table_id)
                    + '_RelatedMutipleCheckBoxDrop\']").jqxDropDownList("close"); } }); }, 3000); }  finally { setTimeout(function(){ $("#'
                    + str(table_id)
                    + '").colResizable({ resizeMode:"overflow" }); }, 5000); }'
                )
                
        except:
            
            filter_control_function += (
                'try { $("#'
                + str(table_id)
                + '").colResizable({ resizeMode:"overflow", onResize: function(){ $("div[id^=\''
                + str(table_id)
                + '_RelatedMutipleCheckBoxDrop\']").jqxDropDownList("close"); } }); } catch (err) { setTimeout(function(){ $("#'
                + str(table_id)
                + '").colResizable({ resizeMode:"overflow", onResize: function(){ $("div[id^=\''
                + str(table_id)
                + '_RelatedMutipleCheckBoxDrop\']").jqxDropDownList("close"); } }); }, 3000); } finally { setTimeout(function(){ $("#'
                + str(table_id)
                + '").colResizable({ resizeMode:"overflow"}); }, 5000); }'
            )
              
        filter_control_function += (
            "try {$('#SYOBJR_00005_7EAA11B4_82C9_400B_8E48_65497373A578').on('check-all.bs.table', function (e, row) {console.log('spare test edit----');$('#spare-parts-bulk-edit-btn').css('display','block') ;var selectedspares = []; var selectAll = false; $('#SYOBJR_00005_7EAA11B4_82C9_400B_8E48_65497373A578').find('[type =\"checkbox\"]:checked').map(function () { console.log('checked checkbox select------');if ($(this).attr('name') == 'btSelectAll'){ selectAll = true; } var sel_val = $(this).closest('tr').find('td:nth-child(3)').text(); if (sel_val != '') { selectedspares.push(sel_val);$('#spare-parts-bulk-edit-btn').css('display','block'); }else{$('#spare-parts-bulk-edit-btn').css('display','none');} }); console.log('selectedspares---',selectedspares); localStorage.setItem('selectedspares', selectedspares);if(selectedspares){console.log('indide spares--selectAll---',selectAll);}$('#SYOBJR_00005_7EAA11B4_82C9_400B_8E48_65497373A578').find('[type =\"checkbox\"]:not(:checked)').map(function () {console.log('indide spares--selectAll---',selectAll); if ($(this).attr('name') == 'btSelectAll'){$('#spare-parts-bulk-edit-btn').css('display','none');} })}) }catch (err){console.log('catch-----')}"
        )
        filter_control_function += ("try {$('#SYOBJR_95825_CD53CDDF_4575_493A_AFEF_BE4811E922FA').on('check-all.bs.table', function (e, row) {console.log('spare test edit----');var selectedconstriants= []; var selectAll = false; $('#SYOBJR_95825_CD53CDDF_4575_493A_AFEF_BE4811E922FA').find('[type =\"checkbox\"]:checked').map(function () { console.log('checked checkbox select------');if ($(this).attr('name') == 'btSelectAll'){ selectAll = true; } var sel_val = $(this).closest('tr').find('td:nth-child(3)').text(); if (sel_val != '') { $('#DROP_CONSTRAINT_BTN').css('display','block');$('#RECREATE_CONSTRAINT_BTN').css('display','none');$('#ADDNEW__SYOBJR_95825_SYOBJ_00426').css('display','none'); }else{$('#spare-parts-bulk-edit-btn').css('display','none');} }); console.log('selectedspares---',selectedspares); $('#SYOBJR_95825_CD53CDDF_4575_493A_AFEF_BE4811E922FA').find('[type =\"checkbox\"]:not(:checked)').map(function () {console.log('indide spares--selectAll---',selectAll); if ($(this).attr('name') == 'btSelectAll'){$('#DROP_CONSTRAINT_BTN').css('display','none');$('#RECREATE_CONSTRAINT_BTN').css('display','none');$('#ADDNEW__SYOBJR_95825_SYOBJ_00426').css('display','block');} })}) }catch (err){console.log('catch-----')}")
        
  
        dbl_clk_function += (
            "try {var bildict = [];$('#SYOBJR_00007_26B8147E_C59C_4010_AA3A_38176869E305').on('click-row.bs.table', function (e, row, $element) { $('#SYOBJR_00007_26B8147E_C59C_4010_AA3A_38176869E305').find(':input(:disabled)').prop('disabled', false);$('#billingmatrix_save').css('display','block');$('#billingmatrix_cancel').css('display','block'); $('.billclassedit').parent().css('background-color','lightyellow');$('#SYOBJR_00007_26B8147E_C59C_4010_AA3A_38176869E305  tbody  tr td input').css('background-color','lightyellow');$('#billingmatrix_save').css('display','block');$('#billingmatrix_cancel').css('display','block'); var BillingmatrixBtn = $('.secondary_highlight_panel').find('button#REFRESH_MATRIX'); var billsave = $('.secondary_highlight_panel').find('button#billingmatrix_save'); var billcan = $('.secondary_highlight_panel').find('button#billingmatrix_cancel'); if (BillingmatrixBtn.length == 1){ BillingmatrixBtn.remove() } $('#billingmatrix_save').css('display','block'); $('#billingmatrix_cancel').css('display','block');$('#SYOBJR_00007_26B8147E_C59C_4010_AA3A_38176869E305 tbody tr td input').change(function () {console.log('on change function--');var getbillamt = $(this).val();console.log('getbillamt-------',getbillamt);var equipid = $(this).closest('tr').find('td:nth-child(4)').text();console.log('eduip-----',equipid);var test = $(this).closest('td').index();var getindex = test+1;var getheaderdate = $('#SYOBJR_00007_26B8147E_C59C_4010_AA3A_38176869E305 thead th:nth-child('+getindex+')').text();var getannualtotal = $('#SYOBJR_00007_26B8147E_C59C_4010_AA3A_38176869E305 thead th:nth-child('+getindex+')').text();console.log('getannualtotal----',getannualtotal);var concate_data = equipid+ ' - '+getheaderdate+ '- '+getbillamt;if(!bildict.includes(concate_data)){bildict.push(concate_data)};getbilldictdata = JSON.stringify(bildict);localStorage.setItem('getbilldictdata', getbilldictdata);}); })}catch (err){console.log('catch-----')}"
        )
                         
        if ObjectName == 'SAQICO':
            cls = "eq(3)"
            SAQICO_dbl_clk_function += (
                'var checkedRows=[]; localStorage.setItem("multiedit_checkbox_clicked", []); $("'
                + str(table_ids)
                + '").on("check.bs.table", function (e, row, $element) { console.log("checked00009==");checkedRows.push($element.closest("tr").find("td:'
                + str(cls)
                + '").text()); localStorage.setItem("multiedit_checkbox_clicked", checkedRows); }); $("'
                + str(table_ids)
                + '").on("check-all.bs.table", function (e) { var table = $("'
                + str(table_ids)
                + '").closest("table"); table.find("tbody tr").each(function() { checkedRows.push($(this).find("td:nth-child(4)").text()); }); localStorage.setItem("multiedit_checkbox_clicked", checkedRows); }); $("'
                + str(table_ids)
                + '").on("uncheck-all.bs.table", function (e) { localStorage.setItem("multiedit_checkbox_clicked", []); checkedRows=[]; }); $("'
                + str(table_ids)
                + '").on("uncheck.bs.table", function (e, row, $element) { var rec_ids=$element.closest("tr").find("td:'
                + str(cls)
                + '").text(); $.each(checkedRows, function(index, value) { if (value === rec_ids) { checkedRows.splice(index,1); }}); localStorage.setItem("multiedit_checkbox_clicked", checkedRows); });'
            )
            SAQICO_dbl_clk_function += (	
                '$("'	
                + str(table_ids)	
                + '").on("dbl-click-cell.bs.table", onClickCell); $("'	
                + str(table_ids)	
                + '").on("all.bs.table", function (e, name, args) { $(".bs-checkbox input").addClass("custom"); $(".bs-checkbox input").after("<span class=\'lbl\'></span>"); }); $("'	
                + str(table_ids)	
                + '\ th.bs-checkbox div.th-inner").before(""); $(".bs-checkbox input").addClass("custom"); $(".bs-checkbox input").after("<span class=\'lbl\'></span>"); function onClickCell(event, field, value, row, $element) { var reco_id=""; var reco = []; reco = localStorage.getItem("multiedit_checkbox_clicked"); if (reco === null || reco === undefined ){ reco = []; } if (reco.length > 0){reco = reco.split(",");} if (reco.length > 0){ reco.push($element.closest("tr").find("td:'	
                + str(cls)	
                + '").text());  data1 = $element.closest("tr").find("td:'	
                + str(cls)	
                + '").text(); localStorage.setItem("multiedit_save_date", data1); reco_id = removeDuplicates(reco); }else{reco_id=$element.closest("tr").find("td:'	
                + str(cls)	
                + '").text(); reco_id=reco_id.split(","); localStorage.setItem("multiedit_save_date", reco_id); } localStorage.setItem("multiedit_data_clicked", reco_id); localStorage.setItem("table_id_RL_edit", "'	
                + str(table_id)	
                + '"); cpq.server.executeScript("SYBLKETRLG", {"TITLE":field, "VALUE":value, "CLICKEDID":"'	
                + str(table_id)	
                + '", "RECORDID":reco_id, "ELEMENT":"RELATEDEDIT"}, function(data) { data1=data[0]; data2=data[1]; if(data1 != "NO"){ if(document.getElementById("RL_EDIT_DIV_ID") ) { document.getElementById("RL_EDIT_DIV_ID").innerHTML = data1; document.getElementById("cont_multiEditModalSection").style.display = "block"; $("#cont_multiEditModalSection").prepend("<div class=\'modal-backdrop fade in\'></div>"); var divHeight = $("#cont_multiEditModalSection").height(); $("#cont_multiEditModalSection .modal-backdrop").css("min-height", divHeight+"px"); $("#cont_multiEditModalSection .modal-dialog").css("width","550px"); $(".modal-dialog").css("margin-top","100px"); } if (data2.length !== 0){ $.each( data2, function( key, values ) { onclick_datepicker(values) }); } } }); }                   $("'	
                + str(table_ids)	
                + "\").on('sort.bs.table', function (e, name, order) {  currenttab = $(\"ul#carttabs_head .active\").text().trim(); localStorage.setItem('"	
                + str(table_id)	
                + "_SortColumn', name); localStorage.setItem('"	
                + str(table_id)	
                + "_SortColumnOrder', order); }); "	
            )	

            SAQICO_dbl_clk_function += (
                    '$("'
                    + str(table_ids)
                    + '").on("all.bs.table", function (e, name, args) { console.log("sort.bs.table ============>11");$(".bs-checkbox input").addClass("custom"); $(".bs-checkbox input").after("<span class=\'lbl\'></span>"); }); $("'
                    + str(table_ids)
                    + '\ th.bs-checkbox div.th-inner").before("<div class=\'pad0brdbt\'>SELECT</div>"); $(".bs-checkbox input").addClass("custom"); $(".bs-checkbox input").after("<span class=\'lbl\'></span>"); $("'
                    + str(table_ids)
                    + "\").on('sort.bs.table', function (e, name, order) { console.log('sort.bs.table ============>', e); e.stopPropagation(); currenttab = $(\"ul#carttabs_head .active\").text().trim(); localStorage.setItem('"
                    + str(table_id)
                    + "_SortColumn', name); localStorage.setItem('"
                    + str(table_id)
                    + "_SortColumnOrder', order); ATTRIBUTE_VALUEList = []; "+str(values_list)+"  QuoteitemContainerSorting(name, order, '"
                    + str(table_id)
                    + "',"+ str(list(eval(Columns)))+", ATTRIBUTE_VALUEList,'"+str(PR_CURR)+"','"+str(TP)+"','"+str(SubTab)+"'); }); "
                    )          

            
            dbl_clk_function = SAQICO_dbl_clk_function
        # Added to append SUBTOTAL, TAX, TOTAL rows to Subtotal by offerings & line item details grids in quote preview node - start
        
        # if str(TreeParam) == "Quote Preview":
        
        #     subt = ''
        #     Quote_Type = ''            
        #     contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
        #     var_subtotal = Sql.GetFirst("SELECT SUM(EXTENDED_PRICE) AS Total,SUM(TAX) AS Tax,CURRENCY FROM SAQITM WHERE QUOTE_RECORD_ID = '"+str(contract_quote_record_id)+"' GROUP BY CURRENCY ")
        #     total = Sql.GetFirst("SELECT SUM(EXTENDED_PRICE) AS Total,SUM(TAX) AS Tax,SUM(UNIT_PRICE) AS UnitPrice FROM SAQIFP WHERE QUOTE_RECORD_ID = '"+str(contract_quote_record_id)+"' ")
        #     Qt_total = Sql.GetFirst("SELECT SUM(EXTENDED_PRICE) AS Total,SUM(TAX) AS Tax FROM SAQICO WHERE QUOTE_RECORD_ID = '"+str(contract_quote_record_id)+"' ")
            
        #     Quote_Type = Product.Attr('QSTN_SYSEFL_QT_00723').GetValue()
        #     if var_subtotal:
        #         if ObjectName == 'SAQITM'and TreeParam == "Quote Preview" and Quote_Type != 'ZTBC - TOOL BASED':
        #             
        #             dbl_clk_function += (
        #                 '$("#SYOBJR_98792_3F435A71_A620_4F6A_AA5F_932100742526 tbody").after(\'<tr ><td style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="SUBTOTAL">SUBTOTAL</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(subt)+'">'+str(subt)+'</abbr></td></tr><tr ><td style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="TAX/VAT/GST">TAX/VAT/GST</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(var_subtotal.Tax)+'">'+str(var_subtotal.Tax)+'</abbr></td></tr><tr ><td style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="TOTAL">TOTAL</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(var_subtotal.Total)+'">'+str(var_subtotal.Total)+'</abbr></td></tr>\');')
                        
        #         if ObjectName == 'SAQITM'and TreeParam == "Quote Preview" and Quote_Type == 'ZTBC - TOOL BASED':
        #             
        #             dbl_clk_function += (
        #                 '$("#SYOBJR_98792_3F435A71_A620_4F6A_AA5F_932100742526 tbody").after(\'<tr ><td style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="SUBTOTAL">SUBTOTAL</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(subt)+'">'+str(subt)+'</abbr></td></tr><tr ><td style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="TAX/VAT/GST">TAX/VAT/GST</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(var_subtotal.Tax)+'">'+str(var_subtotal.Tax)+'</abbr></td></tr><tr ><td style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="TOTAL">TOTAL</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(var_subtotal.Total)+'">'+str(var_subtotal.Total)+'</abbr></td></tr>\');')
                            
        #     if ObjectName == 'SAQIFP'and TreeParam == "Quote Preview":
        #         
        #         dbl_clk_function += (
        #             '$("#SYOBJR_00006_C32BD9D5_A954_49A9_861A_544F30C66C26 tbody").after(\'<tr ><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="SUBTOTAL">SUBTOTAL</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(total.Total)+'">'+str(total.Total)+'</abbr></td></tr><tr ><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="TAX/VAT/GST">TAX/VAT/GST</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(total.Tax)+'">'+str(total.Tax)+'</abbr></td></tr><tr ><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="TOTAL">TOTAL</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(total.UnitPrice)+'">'+str(total.UnitPrice)+'</abbr></td></tr>\');')
                        
        #     if ObjectName == 'SAQICO'and TreeParam == "Quote Preview":
        #        
        #         dbl_clk_function += (
        #             '$("#SYOBJR_98795_E5504B40_36E7_4EA6_9774_EA686705A63F tbody").after(\'<tr ><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="SUBTOTAL">SUBTOTAL</abbr></td><td style="text-align: right; "><abbr id="" title=""></abbr></td></tr><tr ><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="TAX/VAT/GST">TAX/VAT/GST</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(Qt_total.Tax)+'">'+str(Qt_total.Tax)+'</abbr></td></tr><tr ><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td class="cust_billing_name" style=""></td><td style=""></td><td style=""></td><td style="text-align: right; "></td><td style="text-align: right; "></td><td class="cust_billing_name" style=""></td><td style="text-align: right; "></td><td style="text-align: right; "><abbr id="" title="TOTAL">TOTAL</abbr></td><td style="text-align: right; "><abbr id="" title="'+str(Qt_total.Total)+'">'+str(Qt_total.Total)+'</abbr></td></tr>\');')          
        # Added to append SUBTOTAL, TAX, TOTAL rows to Subtotal by offerings & line item details grids in quote preview node - end             
        if QueryCount < int(Page_End):
            PageInformS = str(Page_start) + " - " + str(QueryCount) + " of"
        else:
            PageInformS = str(Page_start) + " - " + str(Page_End) + " of"
        Test = (
            '<div class="col-md-12 brdr listContStyle padbthgt30"  ><div class="col-md-4 pager-numberofitem  clear-padding"><span class="pager-number-of-items-item noofitem" id="'
            + str(table_id)
            + '_NumberofItem"  >'
            + str(PageInformS)
            + ' </span><span class="pager-number-of-items-item fltltpad2mrg0" id="'
            + str(table_id)
            + '_totalItemCount"  >'
            + str(QueryCount)
            + '</span><div class="clear-padding fltltmrgtp3" ><div  class="pull-right veralmert"><select onchange="PageFunctestChild(this, \'RelatedList\',\''
            + str(RECORD_ID)
            + "','"
            + str(table_id)
            + '\')" id="'
            + str(table_id)
            + '_PageCountValue"  class="form-control pagecunt"><option value="10" selected>10</option><option value="20">20</option><option value="50">50</option><option value="100">100</option><option value="200">200</option></select> </div></div></div><div class="col-xs-8 col-md-4  clear-padding totcnt"   data-bind="visible: totalItemCount"><div class="clear-padding col-xs-12 col-sm-6 col-md-12 brdr0"  ><ul class="pagination pagination"><li class="disabled"  ><a href="javascript:void(0)"  onclick="FirstPageLoad_paginationChild(\'RelatedList\', \''
            + str(RECORD_ID)
            + "','"
            + str(table_id)
            + '\')"><i class="fa fa-caret-left fnt14bold"  ></i><i class="fa fa-caret-left fnt14"  ></i></a></li><li class="disabled"><a href="javascript:void(0)" onclick="Previous12334Child(\'RelatedList\', \''
            + str(RECORD_ID)
            + "','"
            + str(table_id)
            + '\')" ><i class="fa fa-caret-left fnt14"  "></i>PREVIOUS</a></li><li class="disabled"><a href="javascript:void(0)" class="disabledPage"  onclick="Next12334Child(\'RelatedList\', \''
            + str(RECORD_ID)
            + "','"
            + str(table_id)
            + '\')">NEXT<i class="fa fa-caret-right fnt14"  ></i></a></li><li class="disabled"><a href="javascript:void(0)" onclick="LastPageLoad_paginationChild(\'RelatedList\', \''
            + str(RECORD_ID)
            + "','"
            + str(table_id)
            + '\')" class="disabledPage" ><i class="fa fa-caret-right fnt14"  ></i><i class="fa fa-caret-right fnt14bold"  ></i></a></li></ul></div> </div> <div class="col-md-4 pr_page_pad"  > <span id="'
            + str(table_id)
            + '_page_count" class="currentPage page_right_content">1</span><span class="page_right_content pad_rt_2"  >Page </span></div></div>'
        )
        
        return (
            table_header,
            table_list,
            table_id,
            filter_control_function,
            NORECORDS,
            dbl_clk_function,
            cv_list,
            filter_level_list,
            DropDownList,
            RelatedDrop_str,
            ObjectName,
            RECORD_ID,
            Test,
            PageInformS,
            PageInform,
            QueryCount,
            related_list_permissions,
            footer_str
        )

    def MDYNMICSQLOBJECTFILTER(
        self, RECORD_ID, ATTRIBUTE_NAME, ATTRIBUTE_VALUE, PerPage, PageInform, SortColumn, SortColumnOrder,  PR_CURR, TP ,SubTab
    ):
        obj_obj1 = ""
        price_status = []
        obj_obj12 = getyears = col_year =exclamation= ""
        lock_pricbkst = "FALSE"
        lock_pricbk = "FALSE"
        PageInformS = ""
        Page_start = ""
        QueryCount = key_value = ""
        Page_End = ""
        try:
            current_prod = Product.Name
        except:
            current_prod = "Sales"
        TreeParam = ""
        TreeParentParam = ""
        TreeSuperParentParam = ""
        TreeTopSuperParentParam = ""
        tabName = ""
        Qustr = ""
        imgValue = ""
        #if SubTab != "":
            #SubTab = re.findall(r"\d",str(SubTab))
            #SubTab = 'Year '+str(SubTab)[2]
        TreeParam = Product.GetGlobal("TreeParam")
        TreeParentParam = Product.GetGlobal("TreeParentLevel0") 
        
        if str(PerPage) == "" and str(PageInform) == "":
            Page_start = 1
            Page_End = 10
            PerPage = 10
            PageInform = "1___10___10"
        else:
            Page_start = int(PageInform.split("___")[0])
            Page_End = int(PageInform.split("___")[1])
            PerPage = PerPage
        for tab in Product.Tabs:
            if tab.IsSelected == True:
                tabName = str(tab.Name)
        obj_obj = Sql.GetFirst(
            """SELECT
                                        SYOBJR.RECORD_ID,SYOBJR.SAPCPQ_ATTRIBUTE_NAME, SYOBJR.PARENT_LOOKUP_REC_ID, SYOBJR.OBJ_REC_ID,
                                        SYOBJR.NAME, SYOBJR.COLUMN_REC_ID, SYOBJR.COLUMNS, SYOBJR.VISIBLE,
                                        SYOBJR.CAN_ADD, SYOBJR.CAN_EDIT, SYOBJR.CAN_DELETE, SYOBJR.RELATED_LIST_SINGULAR_NAME,
                                        SYOBJR.DISPLAY_ORDER, SYOBJR.ORDERS_BY
                                    FROM
                                        SYOBJR (NOLOCK)

                                    WHERE
                                        SYOBJR.SAPCPQ_ATTRIBUTE_NAME = '{RECORD_ID}'
                                    """.format(
                RECORD_ID=str(RECORD_ID)
            )
        )
        Columns = ""
        Obj_Name = ""
        table_id = ""
        COLUMN_REC_ID = ""
        col = ""
        text = ""
        texts = ""
        name = []
        related_list_edit_permission = False
        if current_prod == "SYSTEM ADMIN":
            current_prod = "SYSTEM ADMIN"

        CurrentModuleObj = Sql.GetFirst("select * from SYAPPS (NOLOCK) where APP_LABEL = '" + str(current_prod) + "'")
        crnt_prd_val = str(CurrentModuleObj.APP_ID)
        
        Qstn_REC_ID = ""
        CurrentObj_Recordno = ""
        CurrentObj_Name = ""
        Product_Name = ""
        tabs = Product.Tabs or "Quotes"
        list_of_tabs = []
        for tab in tabs:
            list_of_tabs.append(tab.Name)
        try:    
            TestProduct = Webcom.Configurator.Scripting.Test.TestProduct()
            Product_Name = TestProduct.Name
        except:
            Product_Name = "Sales"
        try:        
            current_tab = str(TestProduct.CurrentTab)
        except:
            current_tab = "Quotes"    
        Tree_Enable = ""
        Tree_Enable = Sql.GetFirst(
            "select ENABLE_TREE FROM SYTABS (NOLOCK) where UPPER(SAPCPQ_ALTTAB_NAME) ='"
            + str(current_tab).upper()
            + "' AND APP_RECORD_ID = '"
            + str(str(CurrentModuleObj.APP_RECORD_ID))
            + "'"
        )
        
        if Tree_Enable is not None:
            if str(Tree_Enable.ENABLE_TREE).upper() == "TRUE":
                (
                    TreeParam,
                    TreeParentParam,
                    TreeSuperParentParam,
                    TopTreeSuperParentParam,
                    TreeTopSuperParentParam,
                    TreeFirstSuperTopParentParam,
                ) = (
                    Product.GetGlobal("TreeParam"),
                    Product.GetGlobal("TreeParentLevel0"),
                    Product.GetGlobal("TreeParentLevel1"),
                    Product.GetGlobal("TreeParentLevel2"),
                    Product.GetGlobal("TreeParentLevel3"),
                    Product.GetGlobal("TreeParentLevel4"),
                )                

        if obj_obj is None:
            return "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
        Action_permission = {}
        Wh_API_NAME = ""
        Wh_OBJECT_NAME = ""
        Query_Obj = ""
        billing_date_column = ''
        if obj_obj is not None:
            Columns = obj_obj.COLUMNS
            Obj_Name = obj_obj.OBJ_REC_ID
            Obj_Name = obj_obj.OBJ_REC_ID
            COLUMN_REC_ID = obj_obj.COLUMN_REC_ID
            REC_NAME = obj_obj.NAME
            PARENT_LOOKUP_REC_ID = obj_obj.PARENT_LOOKUP_REC_ID
            Action_permission["Edit"] = obj_obj.CAN_EDIT
            Action_permission["Delete"] = obj_obj.CAN_DELETE
            related_list_edit_permission = str(obj_obj.CAN_EDIT)            
            objd_where_obj = Sql.GetFirst("select * from  SYOBJD where RECORD_ID = '" + str(COLUMN_REC_ID) + "'")
            if objd_where_obj is not None:
                Wh_API_NAME = objd_where_obj.API_NAME
                Wh_OBJECT_NAME = objd_where_obj.OBJECT_NAME   
            try:                 
                contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
            except:
                contract_quote_record_id = ''    
            
            if Wh_OBJECT_NAME == 'SAQIBP':
                if SubTab:
                    end = int(SubTab.split(' ')[-1]) * 12
                    start = end - 12 + 1
                    
                item_billing_plans_obj = Sql.GetList("""SELECT FORMAT(BILLING_DATE, 'MM-dd-yyyy') as BILLING_DATE FROM (SELECT ROW_NUMBER() OVER(ORDER BY BILLING_DATE)
                                    AS ROW, * FROM (SELECT DISTINCT BILLING_DATE
                                                        FROM SAQIBP (NOLOCK) WHERE QUOTE_RECORD_ID = '{}' 
                                                        GROUP BY EQUIPMENT_ID, BILLING_DATE) IQ) OQ WHERE OQ.ROW BETWEEN {} AND {}""".format(
                                                            contract_quote_record_id, start, end))
                if item_billing_plans_obj:
                    billing_date_column = [item_billing_plan_obj.BILLING_DATE for item_billing_plan_obj in item_billing_plans_obj]                    
                    billing_date_column_joined = ",".join(["'{}'".format(billing_data) for billing_data in billing_date_column])                    
                    Columns = Columns.replace(']', ','+billing_date_column_joined+']')                     
            CurrentObj = Sql.GetFirst(
                "select API_NAME, OBJECT_NAME from  SYOBJD (nolock) where PARENT_OBJECT_RECORD_ID = '"
                + str(PARENT_LOOKUP_REC_ID)
                + "' and DATA_TYPE ='AUTO NUMBER'"
            )
            if CurrentObj is not None:
                CurrentObj_Recordno = CurrentObj.API_NAME                
                CurrentObj_Name = CurrentObj.OBJECT_NAME
            try:
                CurrentTabName = TestProduct.CurrentTab
            except:
                CurrentTabName = "Quotes"
            crnt_prd_val = str(CurrentModuleObj.APP_ID)
            Qstn_where_obj = Sql.GetFirst(
                "select * from SYSEFL (nolock) where API_NAME = '"
                + str(CurrentObj_Name)
                + "' and API_FIELD_NAME = '"
                + str(CurrentObj_Recordno).strip()
                + "' and SAPCPQ_ATTRIBUTE_NAME like '%"
                + str(crnt_prd_val)
                + "%' "
            )

            if Qstn_where_obj is not None:
                Qstn_REC_ID = Qstn_where_obj.SAPCPQ_ATTRIBUTE_NAME
                if Qstn_REC_ID != "":
                    wh_Qstn_REC_ID = "QSTN_" + Qstn_REC_ID.replace("-", "_")  
                                     
                    RecAttValue = ""
                    try:
                        RecAtt = productAttributesGetByName(str(wh_Qstn_REC_ID))
                        

                        if RecAtt is not None:
                            RecAttValue = RecAtt.GetValue()
                        #A055S000P01-3414 - start related list sort issue    
                        if str(current_tab) == "Tab" and str(current_prod) == "SYSTEM ADMIN":
                            
                            RecAttValue = productAttributesGetByName("QSTN_SYSEFL_SY_03295").GetValue()
                        #A055S000P01-3414 - end related list sort issue     
                        if str(current_tab) == "Account" and str(current_prod) == "QUOTAS":
                            RecAttValue = productAttributesGetByName("QSTN_SYSEFL_TQ_00084").GetValue()
                            
                    except:
                        RecAttValue = ""
            table_id = obj_obj.SAPCPQ_ATTRIBUTE_NAME.replace("-", "_") + "_" + str(Obj_Name).replace("-", "_")
        k_list = []
        table_list = []
        dict_key = []
        QuotaSubCat_ID = ""
        Qury_str = ""

        QuryCount_str = ""
        footer_str = ""
        footer_tot = ""
        if Columns != "" and Obj_Name != "":
            objh_obj = Sql.GetFirst("select * from SYOBJH (nolock) where RECORD_ID = '" + str(Obj_Name) + "'")
            
            ObjectName = objh_obj.OBJECT_NAME
            objRecName = objh_obj.RECORD_NAME.strip()
            Objd_Obj = Sql.GetList(
                "select FIELD_LABEL,FORMULA_DATA_TYPE,DATA_TYPE,API_NAME,LOOKUP_API_NAME,FIELD_SHORT_LABEL from  SYOBJD (nolock) where OBJECT_NAME = '"
                + str(ObjectName)
                + "'"
            )
            
            attr_list = []
            lookup_disply_list = []
            if Objd_Obj is not None:
                attr_list = {}
                for attr in Objd_Obj:
                    if attr.FIELD_SHORT_LABEL is not None or attr.FIELD_SHORT_LABEL != "":
                        attr_list[str(attr.API_NAME)] = str(attr.FIELD_SHORT_LABEL)
                    else:
                        attr_list[str(attr.API_NAME)] = str(attr.FIELD_LABEL)

                    attr_list[str(attr.API_NAME)] = str(attr.FIELD_LABEL)
                    if attr is not None:
                        if (
                            attr.LOOKUP_API_NAME is not None
                            and attr.LOOKUP_API_NAME != ""
                            and str(attr.LOOKUP_API_NAME) not in ["CONTROLLING_FIELD", "DEPENDENT_FIELD"]
                        ):
                            lookup_disply_list.append(str(attr.API_NAME))
                        checkbox_list = [
                            inn.API_NAME
                            for inn in Objd_Obj
                            if (inn.DATA_TYPE == "CHECKBOX" or inn.FORMULA_DATA_TYPE == "CHECKBOX")
                        ]
                lookup_list = {ins.LOOKUP_API_NAME: ins.API_NAME for ins in Objd_Obj}
            lookup_str = ",".join(list(lookup_disply_list))
            obj_str = ",".join(list(eval(Columns)))
            if lookup_str != "":
                select_obj_str = str(obj_str) + "," + str(lookup_str)
            else:
                select_obj_str = str(obj_str)
            lookup_disply_list123 = ""
            lookup_str = ",".join(list(lookup_disply_list))
            if len(list(lookup_disply_list)) > 1:
                lookup_disply_list123 = list(lookup_disply_list)[0]
            else:
                if len(list(eval(Columns))) > 1:
                    lookup_disply_list123 = list(eval(Columns))[0]
            name = select_obj_str.split(",")
            
            for text in name:
                s = Sql.GetList(
                    "select DATA_TYPE,API_NAME,LENGTH,DECIMALS,FORMULA_DATA_TYPE from  SYOBJD (nolock) WHERE API_NAME='"
                    + str(text)
                    + "' and OBJECT_NAME='"
                    + str(ObjectName).strip()
                    + "'"
                )
                for ins in s:
                    if (ins.DATA_TYPE == "DATE" or ins.FORMULA_DATA_TYPE == "DATE") or (
                        ins.API_NAME
                        in [
                            "EFFECTIVEDATE_BEG",
                            "EFFECTIVEDATE_END",
                            "PROMOTION_START_DATE",
                            "PROMOTION_END_DATE",
                            "EXCHANGE_RATE_DATE",
                        ]
                    ):
                        if str(RECORD_ID) == "SYOBJR-00007" and ins.API_NAME == 'BILLING_DATE':
                            text = "CONVERT(VARCHAR(10),FORMAT(" + str(text) + ",'MM-dd-yyyy'),101) AS [" + str(text) + "]"
                            texts = texts + "," + str(text)
                        elif texts != "":
                            text = "CONVERT(VARCHAR(10)," + str(text) + ",101) AS [" + str(text) + "]"
                            texts = texts + "," + str(text)
                        else:
                            text = "CONVERT(VARCHAR(10)," + str(text) + ",101) AS [" + str(text) + "]"
                            texts = str(text)
                    else:
                        if col != "":
                            col = col + "," + text
                        else:
                            col = str(text)
            if texts != "":
                col = col + "," + texts
            if billing_date_column:
                column_before_pivot_change = col
                col += ","+ ",".join(billing_date_column)

            edit_field = []
            OrderBy_obj = Sql.GetFirst("select ORDERS_BY from SYOBJR (NOLOCK) where RECORD_ID = '" + str(RECORD_ID) + "'")
            
            if Qstn_REC_ID != "" and Wh_API_NAME != "":
                if OrderBy_obj is not None:
                    if OrderBy_obj.ORDERS_BY:
                        Wh_API_NAMEs = OrderBy_obj.ORDERS_BY
                    else:
                        Wh_API_NAMEs = Wh_API_NAME
                else:
                    Wh_API_NAMEs = Wh_API_NAME

                Trace.Write("Wh_API_NAMEs---->" + str(Wh_API_NAMEs))

                if (
                    RECORD_ID != "SYOBJR-92121"
                    and RECORD_ID != "SYOBJR-92122"
                    and RECORD_ID != "SYOBJR-93171"
                    and RECORD_ID != "SYOBJR-93164"
                    and RECORD_ID != "SYOBJR-93155"
                    and RECORD_ID != "SYOBJR-93163"
                ):                    
                    if SortColumn == "" and SortColumnOrder == "":                        
                        Wh_API_NAMEs = Wh_API_NAMEs
                    elif SortColumn in billing_date_column:
                        Wh_API_NAMEs = " CONVERT(VARCHAR(10),FORMAT("+str(SortColumn)+",'MM-dd-yyyy'),101) " + str(SortColumnOrder).upper()
                    else:                        
                        Wh_API_NAMEs = str(SortColumn) + " " + str(SortColumnOrder).upper()                                              
                else:                    
                    if SortColumn == "" and SortColumnOrder == "":
                        if not "DESC" in Wh_API_NAMEs and "ASC" in Wh_API_NAMEs:
                            Wh_API_NAMEs = Wh_API_NAMEs + " ASC"
                    else:                        
                        Wh_API_NAMEs = str(SortColumn) + " " + str(SortColumnOrder).upper() 
                                              
                Trace.Write('Sort param '+str(Wh_API_NAMEs))
                ATTRIBUTE_VALUE_STR = ""
                Dict_formation = dict(zip(ATTRIBUTE_NAME, ATTRIBUTE_VALUE))
                              

                if ATTRIBUTE_NAME:
                    if ObjectName == 'SAQICO' and RECORD_ID == 'SYOBJR-00009': #added the code for pricing status image filters
                        xa = list(ATTRIBUTE_NAME)[1]
                    else:
                        xa = list(ATTRIBUTE_NAME)[0] 
                                
                    if Dict_formation.get(str(xa)) != "":

                        if str(Dict_formation.get(str(xa))).find(",") == -1:
                            if str(Dict_formation.get(str(xa))).find("-") == -1:
                                try:
                                    J_str = (
                                        "select "
                                        + str(xa)
                                        + " from "
                                        + str(ObjectName)
                                        + " (nolock) where CpqTableEntryId = '"
                                        + str(Dict_formation.get(str(xa)))
                                        + "' "
                                    )

                                except:
                                    J_str = (
                                        "select "
                                        + str(xa)
                                        + " from "
                                        + str(ObjectName)
                                        + " (nolock) where CpqTableEntryId = '"
                                        + str(Dict_formation.get(str(xa)))
                                        + "' "
                                    )
                            else:
                                xa_str = Dict_formation.get(str(xa)).split("-")[1]
                                
                                J_str = (
                                    "select "
                                    + str(xa)
                                    + " from "
                                    + str(ObjectName)
                                    + " (nolock) where CpqTableEntryId = '"
                                    + str(int(xa_str))
                                    + "' "
                                )
                        else:
                            xa_str = []                        
                            for data in Dict_formation.get(str(xa)).split(","):
                                xa_str.append(
                                    int(data.split("-")[1]) if str(Dict_formation.get(str(xa))).find("-") != -1 else int(data)
                                )
                            xa_str = tuple(xa_str)                        
                            J_str = (
                                "select "
                                + str(xa)
                                + " from "
                                + str(ObjectName)
                                + " (nolock) where CpqTableEntryId in "
                                + str(xa_str)
                                + ""
                            )
                        J_obj = Sql.GetList(J_str)

                        if J_obj is not None and str(J_obj) != "" and len(J_obj) > 0:
                            xa_list = [eval("kn." + str(xa)) for kn in J_obj]
                            Dict_formation[str(xa)] = ",".join(xa_list)
                        else:
                            xa_list = [""]
                            Dict_formation[str(xa)]

                for quer_key, quer_value in enumerate(Dict_formation):                    
                    if Dict_formation.get(quer_value) != "" and Dict_formation.get(quer_value) is not None:
                        quer_values = str(Dict_formation.get(quer_value)).strip()
                        
                        SYOBJD_obj = Sql.GetFirst(
                            "select DATA_TYPE, PICKLIST, FORMULA_DATA_TYPE from SYOBJD (nolock) where API_NAME = '"
                            + str(quer_value)
                            + "' and OBJECT_NAME ='"
                            + str(ObjectName)
                            + "' "
                        )

                        picklist_data = ""
                        api_data_type = ""

                        if SYOBJD_obj is not None:
                            api_data_type = (
                                str(SYOBJD_obj.DATA_TYPE)
                                if str(SYOBJD_obj.DATA_TYPE) != "FORMULA"
                                else str(SYOBJD_obj.FORMULA_DATA_TYPE)
                            )
                            picklist_data = str(SYOBJD_obj.PICKLIST)
                                                      
                        if str(quer_values).find(",") == -1:
                            
                            if str(picklist_data).upper() == "TRUE":
                                if str(quer_values).upper() == "TRUE":
                                    quer_values = ["1", "true"]
                                    ##removed additional braces for checkbox column at first and last in ATTRIBUTE_VALUE_STR 
                                    ATTRIBUTE_VALUE_STR += (
                                        str(quer_value) + " in " + str(tuple(quer_values)) + " and "
                                    )                                    
                                elif str(quer_values).upper() == "FALSE":
                                    if RECORD_ID == "SYOBJR-30330":
                                        quer_values = ["0", "false"]
                                        ATTRIBUTE_VALUE_STR += (
                                            "(" + str(quer_value) + " in " + str(tuple(quer_values)) + ") and "
                                        )
                                    else:
                                        quer_values = ["0", "false", " ", ""]

                                        quer_values = str(tuple(quer_values)) + " OR " + str(quer_value) + " IS NULL "
                                        ATTRIBUTE_VALUE_STR += "(" + str(quer_value) + " in " + str(quer_values) + ") AND "  
                                elif str(quer_values).upper() == "TRUE" and str(quer_values).upper() == "FALSE":                                    
                                    quer_values = ["0", "false", " ", "", "1", "true"]
                                    quer_values = str(tuple(quer_values)) + " OR " + str(quer_value) + " IS NULL "
                                    trueFalseCondition = True
                                    Falsecondition = True
                                    if str(quer_value) == "EXCLUSIVE_MATERIAL":
                                        ATTRIBUTE_VALUE_STR += (
                                            "(EXCLUSIVE_MATERIAL is NULL or "
                                            + str(quer_value)
                                            + " in "
                                            + str(tuple(quer_values))
                                            + ") and "
                                        )
                                    elif str(quer_value) == "ACTIVE":
                                        ATTRIBUTE_VALUE_STR += (
                                            "(ACTIVE is NULL or "
                                            + str(quer_value)
                                            + " in "
                                            + str(tuple(quer_values))
                                            + ") and "
                                        )
                                    elif str(quer_value) == "FULFILLMENT_EXCLUDED":
                                        ATTRIBUTE_VALUE_STR += (
                                            "(FULFILLMENT_EXCLUDED is NULL or "
                                            + str(quer_value)
                                            + " in "
                                            + str(tuple(quer_values))
                                            + ") and "
                                        )
                                    else:
                                        if Falsecondition:
                                            ATTRIBUTE_VALUE_STR += (
                                                "(" + str(quer_value) + " in " + str(quer_values) + ") and "
                                            )
                                        else:
                                            ATTRIBUTE_VALUE_STR += (
                                                str(quer_value) + " in " + str(tuple(quer_values)) + " and "
                                            ) 
                                elif str(quer_value) == 'PRICING_STATUS' and str(RECORD_ID) == 'SYOBJR-00009':
                                    if 'ACQUIRING' in quer_values:
                                        quer_values = "ACQUIRING"
                                    elif 'MISSING' in quer_values:
                                        quer_values = "ASSEMBLY MISSING"
                                    elif 'ACQUIRED' in quer_values:
                                        quer_values = "ACQUIRED"
                                    elif 'PARTIALLY PRICED' in quer_values:
                                        quer_values = "PARTIALLY PRICED"
                                    elif 'APPROVAL REQUIRED' in quer_values:
                                        quer_values = "APPROVAL REQUIRED"
                                    elif 'ERROR' in quer_values:
                                        quer_values = "ERROR"
                                    ATTRIBUTE_VALUE_STR += str(quer_value) + " = '" + str(quer_values) + "' and "                                          
                                else:
                                    ATTRIBUTE_VALUE_STR += str(quer_value) + " = '" + str(quer_values) + "' and "
                            else:
                                                             
                                if re.search(r"(\d+/\d+/\d+)", quer_values) and api_data_type in ("DATE"):
                                    if api_data_type == "DATE":
                                        re_format = r"^(((0)[0-9])|((1)[0-2]))(\/)([0-2][0-9]|(3)[0-1])(\/)\d{4}$"
                                        result = re.match(re_format, quer_values)
                                        if result is None:
                                            quer_values = ""
                                    ATTRIBUTE_VALUE_STR += " " + str(quer_value) + " = '" + str(quer_values) + "' and "                                    

                                elif api_data_type == "AUTO NUMBER":
                                    if len(quer_values) >= 1:
                                        if "," not in str(quer_values):
                                            quer_values = quer_values
                                        else:
                                            quer_values = tuple(quer_values)
                                        quer_values = quer_values
                                        if str(quer_values) != "":
                                            ATTRIBUTE_VALUE_STR += (
                                                str(quer_value) + " = '" + str(quer_values) + "' and "
                                                if str(quer_values) != ""
                                                else " 1=1 and "
                                            )
                                elif ObjectName == 'SAQIBP' and (str(quer_value) in 'BILLING_AMOUNT' or 'BILLING_DATE' in str(quer_value) or '20' in str(quer_value)):                                    
                                    ATTRIBUTE_VALUE_STR += "BILLING_DATE = '" + str(SortColumn) + "' and BILLING_AMOUNT like '%" + str(quer_values) + "%' and "                                  
                                else:
                                                                        
                                    ATTRIBUTE_VALUE_STR += str(quer_value) + " like '%" + str(quer_values) + "%' and "
                        else:                            
                            quer_values = quer_values.split(",")
                            quer_values = tuple(list(quer_values)) if len(quer_values) > 1 else "('" + quer_values[0] + "')"
                            
                            if "TRUE" in str(quer_values).upper() and "FALSE" in str(quer_values).upper():
                                quer_values_list = ["0", "false", " ", "", "1", "true"]
                                quer_values = str(tuple(quer_values_list)) + " OR " + str(quer_value) + " IS NULL "
                                trueFalseCondition = True                                

                            if str(quer_value) == "EXCLUSIVE_MATERIAL":
                                ATTRIBUTE_VALUE_STR += str(quer_value) + " in " + str(tuple(quer_values)) + " and "
                            elif str(quer_value) == "FULFILLMENT_EXCLUDED":
                                quer_values = ["0", "false", " ", "", "1", "true"]
                                ATTRIBUTE_VALUE_STR += (
                                    "(FULFILLMENT_EXCLUDED is NULL or "
                                    + str(quer_value)
                                    + " in "
                                    + str(tuple(quer_values))
                                    + ") and "
                                )
                            elif str(quer_value) == "STD_FULFILL_TO_CTY":
                                quer_values = ["0", "false", " ", "", "1", "true"]
                                ATTRIBUTE_VALUE_STR += (
                                    "(STD_FULFILL_TO_CTY is NULL or "
                                    + str(quer_value)
                                    + " in "
                                    + str(tuple(quer_values))
                                    + ") and "
                                )

                            elif str(quer_value) == "XFR_FULFILL_TO_CTY":
                                quer_values = ["0", "false", " ", "", "1", "true"]
                                ATTRIBUTE_VALUE_STR += (
                                    "(XFR_FULFILL_TO_CTY is NULL or "
                                    + str(quer_value)
                                    + " in "
                                    + str(tuple(quer_values))
                                    + ") and "
                                )
                            elif str(quer_value) == "EXP_FULFILL_TO_CTY":
                                quer_values = ["0", "false", " ", "", "1", "true"]
                                ATTRIBUTE_VALUE_STR += (
                                    "(EXP_FULFILL_TO_CTY is NULL or "
                                    + str(quer_value)
                                    + " in "
                                    + str(tuple(quer_values))
                                    + ") and "
                                )

                            elif str(quer_value) == "VISIBLEINCATALOG":                                
                                quer_values = ["0", "false", " ", "", "1", "true"]
                                ATTRIBUTE_VALUE_STR += (
                                    "(VISIBLEINCATALOG is NULL or "
                                    + str(quer_value)
                                    + " in "
                                    + str(tuple(quer_values))
                                    + ") and "
                                )
                            elif str(quer_value) == 'PRICING_STATUS' and str(RECORD_ID) == 'SYOBJR-00009':
                                quer_values = list(quer_values)
                                
                                for i in range(0,len(quer_values)):

                                    if 'ACQUIRING' in quer_values[i]:
                                        quer_values[i] = "ACQUIRING"
                                    elif 'MISSING' in quer_values[i]:
                                        quer_values[i] = "ASSEMBLY MISSING"
                                    elif 'ACQUIRED' in quer_values[i]:
                                        quer_values[i] = "ACQUIRED"
                                    elif 'PARTIALLY PRICED' in quer_values[i]:
                                        quer_values[i] = "PARTIALLY PRICED"
                                    elif 'APPROVAL REQUIRED' in quer_values[i]:
                                        quer_values[i] = "APPROVAL REQUIRED"
                                    elif 'ERROR' in quer_values[i]:
                                        quer_values[i] = "ERROR"
                                quer_values = tuple(quer_values)
                                
                                ATTRIBUTE_VALUE_STR += "(" + str(quer_value) + " in " + str(quer_values) + ") and "                                          
                            else:
                                if api_data_type == "AUTO NUMBER":
                                    ATTRIBUTE_VALUE_STR += (
                                        str(quer_value) + " in " + str(quer_values) + " and "
                                        if str(quer_values) != ""
                                        else " 1=1 and "
                                    )
                                elif (
                                    re.search(r"(\d+/\d+/\d+)", quer) for quer in str(quer_values).split(",")
                                ) and api_data_type in ("DATE"):
                                    ATTRIBUTE_VALUE_STR += " " + str(quer_value) + " in " + str(quer_values) + " and "
                                else:
                                    trueFalseCondition = True
                                    if trueFalseCondition:
                                        ATTRIBUTE_VALUE_STR += "(" + str(quer_value) + " in " + str(quer_values) + ") and "
                                    else:
                                        ATTRIBUTE_VALUE_STR += str(quer_value) + " in " + str(quer_values) + " and "
                
                #Contract valid start date & End date Calculation--START
                try:
                    contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                except:
                    contract_quote_record_id = ''    
                Getyear = Sql.GetFirst("select CONTRACT_VALID_FROM,CONTRACT_VALID_TO from SAQTMT where MASTER_TABLE_QUOTE_RECORD_ID = '"+str(contract_quote_record_id)+"'")
                
                if Getyear:
                    start_date = datetime(Getyear.CONTRACT_VALID_FROM)
                    end_date = datetime(Getyear.CONTRACT_VALID_TO)
                    mm = (end_date. year - start_date. year) * 12 + (end_date. month - start_date. month)
                    quotient, remainder = divmod(mm, 12)
                    getyears = quotient + (1 if remainder > 0 else 0)                   
                    if not getyears:
                        getyears = 1
                    
                #Contract valid start date & End date Calculation--END
                Trace.Write('Attr str--->'+str(ATTRIBUTE_VALUE_STR))
                if ATTRIBUTE_VALUE_STR != "":
                    
                    TreeParam = Product.GetGlobal("TreeParam")
                    TreeParentParam = Product.GetGlobal("TreeParentLevel0")  
                    TreeSuperParentParam =  Product.GetGlobal("TreeParentLevel1")               
                    TreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                    try:
                        RecAttValue = Quote.GetGlobal("contract_quote_record_id")
                    except:
                        RecAttValue = ''    
                    if RECORD_ID == "SYOBJR-95868":                        
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " "
                            + "SYSEFL."
                            + str(select_obj_str)
                            + ",SYSEFL.CpqTableEntryId from "
                            + str(ObjectName)
                            + " (nolock) INNER JOIN SYSECT (nolock) ON SYSEFL.SECTION_RECORD_ID = SYSECT.RECORD_ID  AND "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' "
                            + "where SYSEFL.SECTION_NAME = '"
                            + str(TreeParentParam)
                            + "'"
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from "
                            + str(ObjectName)
                            + " (nolock) INNER JOIN SYSECT (nolock) ON SYSEFL.SECTION_RECORD_ID = SYSECT.RECORD_ID and "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' where SYSEFL.SECTION_NAME = '"
                            + str(TreeParentParam)
                            + "'"
                        )                        
                    elif RECORD_ID == "SYOBJR-95843" and TreeParentParam != "" :  
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_03295").GetValue()
                        Qury_str = (
                        "select top "
                        + str(PerPage)
                        + " * "
                        + " from "
                        + str(ObjectName)
                        + " (nolock) WHERE "
                        + str(Wh_API_NAME)
                        + " = '"
                        + str(RecAttValue)
                        + "' AND PAGE_NAME = '"
                        + str(TreeParentParam)
                        + "'"
                        
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from "
                            + str(ObjectName)
                            + " (nolock) WHERE "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND PAGE_NAME = '"
                            + str(TreeParentParam)
                            + "'"
                        )

                    elif RECORD_ID == "SYOBJR-94489":                        
                        GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                        GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                        Qury_str = (
                            "select DISTINCT top 10 RECORD_ID,SECTION_NAME,DISPLAY_ORDER,PARENT_SECTION_RECORD_ID,OWNER_RECORD_ID,PRIMARY_OBJECT_RECORD_ID,PAGE_LABEL,PAGE_RECORD_ID,CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by DISPLAY_ORDER) AS ROW,* from SYSECT where "+str(ATTRIBUTE_VALUE_STR)+" PAGE_LABEL = '"
                            + str(TreeParentParam)
                            + "') m where m.ROW BETWEEN 1 and 10"
                        )
                        
                        QuryCount_str = (
                            "select count(*) as cnt from SYSECT (nolock) where "+str(ATTRIBUTE_VALUE_STR)+"  PAGE_LABEL = '" + str(TreeParentParam) + "'"
                        )

                    elif RECORD_ID == "SYOBJR-94490":
                        GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()                        
                        gettabres = Sql.GetFirst(
                            "Select RECORD_ID from SYSECT where PAGE_NAME = '"
                            + str(TopTreeSuperParentParam)
                            + "' and SECTION_NAME = '"
                            + str(TreeParentParam)
                            + "'"
                        )
                        if gettabres:                            
                            tabRecord = str(gettabres.RECORD_ID)

                        Qustr = " where "+str(ATTRIBUTE_VALUE_STR)+" SECTION_RECORD_ID = '" + str(tabRecord) + "'"

                    elif RECORD_ID == "SYOBJR-95800":                        
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        permiss_id = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00125").GetValue()
                        
                        Qury_str = (
                            "select DISTINCT TOP "
                            + str(PerPage)
                            + " ID,USERNAME,NAME,ACTIVE from ( select ROW_NUMBER() OVER(order by ID) AS ROW, ID,USERNAME,NAME,ACTIVE from USERS U (nolock) inner join users_permissions up on U.id = up.user_id   where "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " up.permission_id = '"
                            + str(permiss_id)
                            + "'  ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = (
                            "select count(U.ID) as cnt from USERS U (nolock)  inner join users_permissions up on U.id = up.user_id  where "
                             + str(ATTRIBUTE_VALUE_STR)
                            + " up.permission_id = '"
                            + str(permiss_id)
                            + "'  "
                        )
                    elif RECORD_ID == "SYOBJR-93159":
                        Wh_API_NAME = "PROFILE_ID"
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")
                        appId = Product.GetGlobal("CommonTreeParentParam")
                        if appId == "App Level Permissions":
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " *  from ( select ROW_NUMBER() OVER(order by S.DISPLAY_ORDER) AS ROW, p.PROFILE_TAB_RECORD_ID,p.TAB_ID,p.VISIBLE,p.PROFILE_RECORD_ID,p.CpqTableEntryId,S.DISPLAY_ORDER from SYPRTB p (nolock) inner join SYTABS S on S.RECORD_ID = p.TAB_RECORD_ID where "
                                + str(ATTRIBUTE_VALUE_STR)
                                + " p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.APP_ID = '"
                                + str(TreeParam)
                                + "' ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )                            
                            QuryCount_str = (
                                "select count(*) as cnt from SYPRTB (nolock)  where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and APP_ID = '"
                                + str(TreeParam)
                                + "'"
                            )
                        else:
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " *  from ( select ROW_NUMBER() OVER(order by S.DISPLAY_ORDER) AS ROW, p.PROFILE_TAB_RECORD_ID,p.TAB_ID,p.VISIBLE,p.PROFILE_RECORD_ID,p.CpqTableEntryId,S.DISPLAY_ORDER from SYPRTB p (nolock) inner join SYTABS S on S.RECORD_ID = p.TAB_RECORD_ID where "
                                + str(ATTRIBUTE_VALUE_STR)
                                + " p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.APP_ID = '"
                                + str(appId)
                                + "' ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from SYPRTB (nolock)  where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and APP_ID = '"
                                + str(appId)
                                + "'"
                            )
                    elif RECORD_ID == "SYOBJR-93160":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        GetAppname_query = ""
                        if TreeTopSuperParentParam == "App Level Permissions":
                            CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")                            
                            GetAppname_query = Sql.GetFirst(
                                "SELECT TAB_RECORD_ID FROM SYPRTB where APP_ID = '"
                                + str(CommonTreeSuperParentParam)
                                + "' and TAB_ID = '"
                                + str(TreeParam)
                                + "'"
                            )
                        else:
                            TreeParam = Product.GetGlobal("CommonTreeParentParam")
                            GetAppname_query = Sql.GetFirst(
                                "SELECT TAB_RECORD_ID FROM SYPRTB where APP_ID = '"
                                + str(TreeTopSuperParentParam)
                                + "' and TAB_ID = '"
                                + str(TreeParam)
                                + "'"
                            )
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " *  from ( select ROW_NUMBER() OVER(order by P.PROFILE_RECORD_ID) AS ROW, P.PROFILE_SECTION_RECORD_ID,P.SECTION_RECORD_ID,P.SECTION_ID,P.TAB_ID,P.VISIBLE,P.PROFILE_RECORD_ID,P.CpqTableEntryId,s.DISPLAY_ORDER from SYPRSN P (nolock) inner join SYSECT s on s.RECORD_ID = P.SECTION_RECORD_ID where "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " P.PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and P.TAB_ID = '"
                            + str(TreeParam)
                            + "' and P.TAB_RECORD_ID ='"
                            + str(GetAppname_query.TAB_RECORD_ID)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + "  order by m.DISPLAY_ORDER"
                        )

                        QuryCount_str = (
                            "select count(*) as cnt from SYPRSN (nolock)  where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and TAB_ID = '"
                            + str(TreeParam)
                            + "' and TAB_RECORD_ID ='"
                            + str(GetAppname_query.TAB_RECORD_ID)
                            + "'"
                        )
                    elif RECORD_ID == "SYOBJR-93162":
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        TreeFirstSuperTopParentParam = Product.GetGlobal("CommonTreeFirstSuperTopParentParam")
                        CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        getTabrec = Sql.GetFirst(
                            "SELECT TAB_RECORD_ID from SYPRTB where APP_ID = '"
                            + str(TreeFirstSuperTopParentParam)
                            + "' and PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and TAB_ID = '"
                            + str(CommonTreeTopSuperParentParam)
                            + "'"
                        )
                        sectrecid = Tabrecordid = ""
                        if getTabrec is not None:
                            Tabrecordid = str(getTabrec.TAB_RECORD_ID)                            
                            getsectrec = Sql.GetFirst(
                                "SELECT SECTION_RECORD_ID from SYPRSN where TAB_RECORD_ID = '"
                                + str(Tabrecordid)
                                + "' and SECTION_ID ='"
                                + str(CommonTreeParentParam)
                                + "'"
                            )
                            if getsectrec is not None:
                                sectrecid = str(getsectrec.SECTION_RECORD_ID)
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " * from ( select ROW_NUMBER() OVER(order by P.SECTION_FIELD_ID ) AS ROW,P.PROFILE_SECTIONFIELD_RECORD_ID,P.SECTIONFIELD_RECORD_ID,P.SECTION_FIELD_ID ,P.VISIBLE,P.EDITABLE,P.PROFILE_RECORD_ID,P.CpqTableEntryId,s.DISPLAY_ORDER from SYPRSF P (nolock)  inner join SYSEFL s on s.RECORD_ID = P.SECTIONFIELD_RECORD_ID where "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " P.PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and P.SECTION_RECORD_ID = '"
                            + str(sectrecid)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + "  order by m.DISPLAY_ORDER"
                        )

                        QuryCount_str = (
                            "select count(*) as cnt from SYPRSF (nolock)  where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and SECTION_RECORD_ID = '"
                            + str(sectrecid)
                            + "'"
                        )
                    elif RECORD_ID == "SYOBJR-93122":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()

                        Qury_str = (
                            "select  top "
                            + str(PerPage)
                            + " PROFILE_OBJECT_RECORD_ID,OBJECT_RECORD_ID, OBJECT_NAME, VISIBLE,CpqTableEntryId from ( select ROW_NUMBER() OVER( order by PROFILE_RECORD_ID) AS ROW, PROFILE_OBJECT_RECORD_ID,OBJECT_RECORD_ID, OBJECT_NAME, VISIBLE,CpqTableEntryId from SYPROH (nolock) where  "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " PROFILE_ID = '"
                            + str(RecAttValue)
                            + "') m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " order by OBJECT_NAME"
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from SYPROH (nolock) where  PROFILE_ID = '" + str(RecAttValue) + "'"
                        )

                    elif RECORD_ID == "SYOBJR-93130":
                        CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")
                        CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                        CommonTopTreeSuperParentParam = Product.GetGlobal("CommonTopTreeSuperParentParam")
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        if CommonTreeParentParam == "Object Level Permissions":
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " * from ( select ROW_NUMBER() OVER(order by PROFILE_RECORD_ID ASC) AS ROW,p.PROFILE_OBJECTFIELD_RECORD_ID,p.OBJECTFIELD_RECORD_ID,s.DISPLAY_ORDER,p.OBJECT_FIELD_ID,p.OBJECT_RECORD_ID,p.OBJECT_NAME,p.VISIBLE,p.EDITABLE,p.CpqTableEntryId from SYPROD p (nolock)  inner join  SYOBJD s on s.RECORD_ID = p.OBJECTFIELD_RECORD_ID where  p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.OBJECT_NAME='"
                                + str(TreeParam)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from SYPROD (nolock) where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and OBJECT_NAME='"
                                + str(TreeParam)
                                + "'"
                            )
                        else:
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " * from ( select ROW_NUMBER() OVER(order by PROFILE_RECORD_ID ASC) AS ROW,p.PROFILE_OBJECTFIELD_RECORD_ID,p.OBJECTFIELD_RECORD_ID,s.DISPLAY_ORDER,p.OBJECT_FIELD_ID,p.OBJECT_RECORD_ID,p.OBJECT_NAME,p.VISIBLE,p.EDITABLE,p.CpqTableEntryId from SYPROD p (nolock)  inner join  SYOBJD s on s.RECORD_ID = p.OBJECTFIELD_RECORD_ID where  p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.OBJECT_NAME='"
                                + str(CommonTreeParentParam)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from SYPROD (nolock) where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and OBJECT_NAME='"
                                + str(CommonTreeParentParam)
                                + "'"
                            )
                    elif RECORD_ID == "SYOBJR-93130":
                        CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")
                        CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                        CommonTopTreeSuperParentParam = Product.GetGlobal("CommonTopTreeSuperParentParam")
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        if CommonTreeParentParam == "Object Level Permissions":
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " * from ( select ROW_NUMBER() OVER(order by PROFILE_RECORD_ID ASC) AS ROW,p.PROFILE_OBJECTFIELD_RECORD_ID,p.OBJECTFIELD_RECORD_ID,s.DISPLAY_ORDER,p.OBJECT_FIELD_ID,p.OBJECT_RECORD_ID,p.OBJECT_NAME,p.VISIBLE,p.EDITABLE,p.CpqTableEntryId from SYPROD p (nolock)  inner join  SYOBJD s on s.RECORD_ID = p.OBJECTFIELD_RECORD_ID where  p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.OBJECT_NAME='"
                                + str(TreeParam)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from SYPROD (nolock) where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and OBJECT_NAME='"
                                + str(TreeParam)
                                + "'"
                            )
                        else:
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " * from ( select ROW_NUMBER() OVER(order by PROFILE_RECORD_ID ASC) AS ROW,p.PROFILE_OBJECTFIELD_RECORD_ID,p.OBJECTFIELD_RECORD_ID,s.DISPLAY_ORDER,p.OBJECT_FIELD_ID,p.OBJECT_RECORD_ID,p.OBJECT_NAME,p.VISIBLE,p.EDITABLE,p.CpqTableEntryId from SYPROD p (nolock)  inner join  SYOBJD s on s.RECORD_ID = p.OBJECTFIELD_RECORD_ID where  p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.OBJECT_NAME='"
                                + str(CommonTreeParentParam)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from SYPROD (nolock) where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and OBJECT_NAME='"
                                + str(CommonTreeParentParam)
                                + "'"
                            )
                    elif str(RECORD_ID) == "SYOBJR-94454" or str(RECORD_ID) == "SYOBJR-94455":
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + " from ( select ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock)  where  "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from "
                            + str(ObjectName)
                            + " (nolock) where  "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' "
                        ) 
                    elif str(RECORD_ID) == "SYOBJR-91822":
                        contractrecid = Product.GetGlobal("contract_record_id")
                        
                        if Product.GetGlobal("TreeParentLevel1") == "Contract Items": 
                                                
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            TreeParentParam = Product.GetGlobal("TreeParentLevel0")
                            ServiceId = TreeParentParam.split("-")[1].strip()                           
                            Qury_str = (
                                    "SELECT DISTINCT TOP "
                                    + str(PerPage)
                                    + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from CTCICO (nolock)  where "+ str(ATTRIBUTE_VALUE_STR)+" CONTRACT_RECORD_ID ='"+str(RecAttValue)
                                    +"' and GREENBOOK = '"+str(TreeParam)+"' and SERVICE_ID = '"+str(ServiceId)+"') m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " AND "
                                    + str(Page_End)
                                )

                            QuryCount_str = (
                                "SELECT COUNT(CpqTableEntryId) AS cnt FROM CTCICO (nolock) WHERE "+ str(ATTRIBUTE_VALUE_STR)+" CONTRACT_RECORD_ID = '"
                                    + str(RecAttValue)
                                    + "'and GREENBOOK = '"+str(TreeParam)+"'and SERVICE_ID = '"+str(ServiceId)+"'"
                            )                                
                        else:
                            
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            qt_rec_id = SqlHelper.GetFirst("SELECT CONTRACT_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID='" + str(
                            contractrecid) + "'")
                            LineAndEquipIDList = TreeParam.split(' - ')
                            if TreeParentParam == "Contract Items":
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where "+ str(ATTRIBUTE_VALUE_STR)+" CONTRACT_ID = '"
                                        + str(qt_rec_id.CONTRACT_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList[1])
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM CTCICO where "+ str(ATTRIBUTE_VALUE_STR)+" SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                            LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                )
                            else:
                            
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " * from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where "+ str(ATTRIBUTE_VALUE_STR)+" CONTRACT_ID = '"
                                        + str(qt_rec_id.CONTRACT_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList[1])
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM CTCICO where "+ str(ATTRIBUTE_VALUE_STR)+" SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                            LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                )                              
                    elif str(RECORD_ID) == "SYOBJR-98795":                        
                        TreeParam = Product.GetGlobal("TreeParam")
                        TreeParentParam = Product.GetGlobal("TreeParentLevel0")
                        contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                        qt_rec_id = Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")
                        Serv_id = SqlHelper.GetFirst("SELECT SERVICE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")    
                        LineAndEquipIDList = TreeParam.split(' - ')                        
                        if getyears == 1:
                            col_year =  'YEAR_1'
                        elif getyears == 2:
                            col_year =  'YEAR_1,YEAR_2'
                        elif getyears == 3:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3'
                        elif getyears == 4:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                        else:
                            col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'
                        if TreeParam == "Quote Preview":                            
                            Qury_str = (
                            "select top "
                                + str(PerPage)
                                + " QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, EQUIPMENT_ID,SERVICE_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",BASE_PRICE,SERIAL_NO, GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE_MARGIN, TARGET_PRICE, SALES_DISCOUNT_PRICE, CEILING_PRICE, SALES_DISCOUNT, TAX_PERCENTAGE,TAX,LINE,SRVTAXCLA_DESCRIPTION, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from SAQICO (NOLOCK) where QUOTE_ID = '"
                                + str(qt_rec_id.QUOTE_ID)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                            )
                            QuryCount_str = (
                                    "select count(*) as cnt FROM SAQICO where " + str(ATTRIBUTE_VALUE_STR) +" QUOTE_ID = '{}'".format(
                                        str(qt_rec_id.QUOTE_ID))
                            )
                    elif str(RECORD_ID) == "SYOBJR-00009":
                        Trace.Write("123")
                        if Product.GetGlobal("TreeParentLevel2") == "Quote Items":  
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            error = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                            partially_priced = '<img title="Partially Priced" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Red1_Circle.svg>'
                            assembly_missing = '<img title="Assembly Missing" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Orange1_Circle.svg>'
                            if getyears == 1:
                                col_year =  'YEAR_1'
                            elif getyears == 2:
                                col_year =  'YEAR_1,YEAR_2'
                            elif getyears == 3:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3'
                            elif getyears == 4:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                            else:
                                col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5' 
                            TreeParentParam = Product.GetGlobal("TreeParentLevel1")
                            
                            try:
                                if str(TreeParentParam.split("-")[3]):
                                    ServiceId = TreeParentParam.split("-")[-2].strip()
                                else:
                                    ServiceId = TreeParentParam.split("-")[1].strip() 
                            except:
                                ServiceId = TreeParentParam.split("-")[1].strip()
                            fab_location_id = Product.GetGlobal("TreeParentLevel0")
                            Qury_str = (
                                    "SELECT DISTINCT TOP "
                                    + str(PerPage)
                                    + " CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '"+ exclamation +"' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,TARGET_PRICE_MARGIN,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,FABLOCATION_ID,TOTAL_COST,TARGET_PRICE,CEILING_PRICE,SALES_DISCOUNT,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",BASE_PRICE,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,BD_DISCOUNT_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,QUOTE_RECORD_ID,MNT_PLANT_RECORD_ID,SALES_DISCOUNT_PRICE,SALE_DISCOUNT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,QUOTE_CURRENCY_RECORD_ID,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQICO (nolock)  where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_RECORD_ID ='"+str(RecAttValue)
                                    +"' and GREENBOOK = '"+str(TreeParam)+"' and FABLOCATION_ID = '"+str(fab_location_id)+"' and SERVICE_ID = '"+str(ServiceId)+"') m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " AND "
                                    + str(Page_End)
                                )

                            QuryCount_str = (
                                "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQICO (nolock) WHERE " + str(ATTRIBUTE_VALUE_STR) +" QUOTE_RECORD_ID = '"
                                    + str(RecAttValue)
                                    + "'and GREENBOOK = '"+str(TreeParam)+"' and FABLOCATION_ID = '"+str(fab_location_id)+"' and SERVICE_ID = '"+str(ServiceId)+"'"
                            )    
                        else:
                            if getyears == 1:
                                col_year =  'YEAR_1'
                            elif getyears == 2:
                                col_year =  'YEAR_1,YEAR_2'
                            elif getyears == 3:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3'
                            elif getyears == 4:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                            else:
                                col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'   
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            error = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                            partially_priced = '<img title="Partially Priced" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Red1_Circle.svg>'
                            assembly_missing = '<img title="Assembly Missing" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Orange1_Circle.svg>'
                            qt_rec_id = SqlHelper.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")                            
                            

                            if TreeParam == "Quote Items":
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"'  ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, EQUIPMENT_ID,SERVICE_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",BASE_PRICE,SERIAL_NO, GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE_MARGIN, TARGET_PRICE, SALES_DISCOUNT_PRICE, CEILING_PRICE, SALES_DISCOUNT,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY "+ str(Wh_API_NAMEs)
                                        +") AS ROW, * from SAQICO (NOLOCK) where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_ID = '"
                                        + str(qt_rec_id.QUOTE_ID)
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)+" ORDER BY "+ str(Wh_API_NAMEs)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM SAQICO where "+ str(ATTRIBUTE_VALUE_STR)+"  QUOTE_ID = '{}'".format(
                                            str(qt_rec_id.QUOTE_ID))
                                )


                            elif TreeParentParam == "Quote Items": 
                                try:
                                    if str(TreeParam.split("-")[3]):
                                        LineAndEquipIDList = TreeParam.split(' - ')[-2].strip()
                                    else:
                                        LineAndEquipIDList = TreeParam.split(' - ')[1].strip() 
                                except:
                                    LineAndEquipIDList = TreeParam.split('-')[1].strip()
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE  WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, SERVICE_ID, EQUIPMENT_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,YEAR_1,BASE_PRICE, SERIAL_NO,GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE, SALES_DISCOUNT_PRICE, TARGET_PRICE_MARGIN, CEILING_PRICE, SALES_DISCOUNT,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY "+ str(Wh_API_NAMEs)
                                        +") AS ROW, * from SAQICO (NOLOCK) where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_ID = '"
                                        + str(qt_rec_id.QUOTE_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList)
                                        + "' and LINE_ITEM_ID = '"+str(TreeParam.split(' -')[0])+"') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM SAQICO where "+ str(ATTRIBUTE_VALUE_STR)+" SERVICE_ID = '"+ str(LineAndEquipIDList) + "' and QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"' and LINE_ITEM_ID = '"+str(TreeParam.split(' -')[0])+"'"
                                )
                            
                                
                            ## code is not using anywhere    TreeSuperParentParam
                            elif TreeSuperParentParam == "Quote Items":
                                
                                LineAndEquipIDList = TreeParentParam.split('-')[1].strip()
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE  WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, SERVICE_ID, EQUIPMENT_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,YEAR_1,BASE_PRICE, SERIAL_NO,GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE, SALES_DISCOUNT_PRICE, TARGET_PRICE_MARGIN, CEILING_PRICE, SALES_DISCOUNT, TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY "+ str(Wh_API_NAMEs)
                                        +") AS ROW, * from SAQICO (NOLOCK) where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_ID = '"
                                        + str(qt_rec_id.QUOTE_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList)
                                        + "' AND FABLOCATION_ID = '"+str(TreeParam)+"' and LINE_ITEM_ID = '"+str(TreeParentParam.split(' -')[0])+"') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM SAQICO where "+ str(ATTRIBUTE_VALUE_STR)+" SERVICE_ID = '"+ str(LineAndEquipIDList)+"' and FABLOCATION_ID = '"+str(TreeParam)+"'  and QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"' and LINE_ITEM_ID = '"+str(TreeParentParam.split(' -')[0])+"'"
                                )
                            

                    elif str(RECORD_ID) == 'SYOBJR-98799':     
                        contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")                
                        qt_rec_id = Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                        contract_quote_record_id) + "'")
                        try:
                            quote_id = qt_rec_id.QUOTE_ID
                        except:
                            quote_id = ""
                        imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                        acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                        Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE WHEN STATUS = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ acquiring_img_str +"' END AS STATUS, QUOTE_DOCUMENT_RECORD_ID, DOCUMENT_ID,DOCUMENT_NAME,LANGUAGE_ID,LANGUAGE_NAME,CPQTABLEENTRYDATEADDED,QUOTE_RECORD_ID,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY STATUS) AS ROW, * from SAQDOC (NOLOCK) where " + str(ATTRIBUTE_VALUE_STR)+" QUOTE_ID = '"
                                        + str(qt_rec_id.QUOTE_ID)
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                        QuryCount_str = (
                                "select count(*) as cnt FROM SAQDOC where " + str(ATTRIBUTE_VALUE_STR)+" QUOTE_ID = '{}'".format(
                                    str(qt_rec_id.QUOTE_ID))
                        )
                    elif str(RECORD_ID) == "SYOBJR-00007": # Billing Matrix - Pivot - Start                        
                        pivot_columns = ",".join(['[{}]'.format(billing_date) for billing_date in billing_date_column])
                        Qustr = " where " + str(ATTRIBUTE_VALUE_STR)+" "+ str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                        if Qustr:
                            Qustr += " AND BILLING_DATE BETWEEN '{}' AND '{}'".format(billing_date_column[0], billing_date_column[-1])
                        pivot_query_str = """
                                    SELECT ROW_NUMBER() OVER(ORDER BY EQUIPMENT_ID)
                                    AS ROW, *
                                        FROM (
                                            SELECT 
                                                {Columns}                                           
                                            FROM {ObjectName}
                                            {WhereString}
                                        ) AS IQ
                                        PIVOT
                                        (
                                            SUM(BILLING_AMOUNT)
                                            FOR BILLING_DATE IN ({PivotColumns})
                                        )AS PVT
                                    """.format(OrderByColumn=Wh_API_NAMEs, Columns=column_before_pivot_change, ObjectName=ObjectName,
                                                WhereString=Qustr, PivotColumns=pivot_columns)
                        Qury_str = """
                                    SELECT DISTINCT TOP {PerPage} * FROM ( SELECT * FROM ({InnerQuery}) OQ WHERE ROW BETWEEN {Start} AND {End} ) AS FQ ORDER BY EQUIPMENT_ID
                                    """.format(PerPage=PerPage, OrderByColumn=Wh_API_NAMEs, InnerQuery=pivot_query_str, Start=Page_start, End=Page_End)
                        QuryCount_str = "SELECT COUNT(*) AS cnt FROM ({InnerQuery}) OQ".format(InnerQuery=pivot_query_str)
                        Trace.Write("====>>>>>>>>>>>> Qury_str "+str(Qury_str))
                        Trace.Write("====>>>>>>>>>>>> QuryCount_str "+str(QuryCount_str))
                        # Billing Matrix - Pivot - End
                    elif str(RECORD_ID) == "SYOBJR-00015" and str(TreeParentParam) == "Approval Chain Steps":
                        Qury_str = (
                            " SELECT TOP "
                            + str(PerPage)
                            + " * FROM (SELECT ROW_NUMBER() OVER(ORDER BY APPROVAL_TRACKED_FIELD_RECORD_ID) AS ROW,APPROVAL_TRACKED_FIELD_RECORD_ID,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRACKING_TYPE,ACAPTF.CpqTableEntryId FROM ACAPTF (NOLOCK) INNER JOIN ACACST (NOLOCK) ON ACAPTF.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID WHERE "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " ACACST.APRCHNSTP_NAME = '"
                            + str(TreeParam).split(': ')[1]
                            + "' AND ACACST.APRCHN_RECORD_ID = '"
                            + str(RecAttValue)
                            + "')m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " "
                        )

                        QuryCount_str = (
                            "SELECT COUNT(APPROVAL_TRACKED_FIELD_RECORD_ID) AS cnt FROM ACAPTF (NOLOCK) INNER JOIN ACACST (NOLOCK) ON ACAPTF.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID WHERE "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " ACACST.APRCHNSTP_NAME = '"
                            + str(TreeParam).split(': ')[1]
                            + "' AND ACACST.APRCHN_RECORD_ID = '"
                            + str(RecAttValue)
                            + "' "
                        )
                    elif str(RECORD_ID) == "SYOBJR-00014":
                        step_name = TreeParam.split(':')[1].strip()
                        
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " * from ( select ROW_NUMBER() OVER( order by APPROVAL_CHAIN_STEP_APPROVER_RECORD_ID) AS ROW,ACACSA.APPROVAL_CHAIN_STEP_APPROVER_RECORD_ID,ACACSA.APRCHN_ID,ACACSA.APRCHNSTP_APPROVER_ID,ACACSA.APPROVER_SELECTION_METHOD,ACACSA.USERNAME,ACACSA.PROFILE_ID,ACACSA.ROLE_ID,ACACSA.NOTIFICATION_ONLY,ACACSA.CpqTableEntryId from ACACSA (nolock) INNER JOIN ACACST (NOLOCK) ON ACACST.APPROVAL_CHAIN_STEP_RECORD_ID = ACACSA.APRCHNSTP_RECORD_ID WHERE  "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " ACACSA."
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND ACACST.APRCHNSTP_NAME = '"
                            + str(step_name)
                            + "') m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " AND "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = (
                            "select count(ACACSA.CpqTableEntryId) as cnt from ACACSA (nolock) INNER JOIN ACACST (NOLOCK) ON ACACST.APPROVAL_CHAIN_STEP_RECORD_ID = ACACSA.APRCHNSTP_RECORD_ID WHERE ACACSA."
                            + str(ATTRIBUTE_VALUE_STR)
                            + " ACACSA."
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND ACACST.APRCHNSTP_NAME = '"
                            + str(step_name)
                            + "'"
                        )  
                    elif str(RECORD_ID) == "SYOBJR-98822":     
                        if Product.GetGlobal("TreeParentLevel1") == "Contract Items":                            
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            
                            Qury_str = (
                                    "SELECT DISTINCT TOP "
                                    + str(PerPage)
                                    + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CONTRACT_CURRENCY,CONTRACT_CURRENCY_RECORD_ID,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from CTCICO (nolock)  where CONTRACT_RECORD_ID ='"+str(RecAttValue)
                                    +"' and GREENBOOK = '"+str(TreeParam)+"') m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " AND "
                                    + str(Page_End)
                                )

                            QuryCount_str = (
                                "SELECT COUNT(CpqTableEntryId) AS cnt FROM CTCICO (nolock) WHERE CONTRACT_RECORD_ID = '"
                                    + str(RecAttValue)
                                    + "'and GREENBOOK = '"+str(TreeParam)+"'"
                            )  
                        else:    
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            qt_rec_id = SqlHelper.GetFirst("SELECT CONTRACT_ID, SERVICE_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")
                            LineAndEquipIDList = TreeParam.split(' - ')
                            if qt_rec_id.CONTRACT_ID == '70011556':
                                SERV_DESC = "Z0091"
                            else:
                                SERV_DESC = qt_rec_id.SERVICE_ID                            
                            if TreeParentParam == "Contract Items":                                
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, SERVICE_ID, EQUIPMENT_ID,LINE_ITEM_ID,DISCOUNT,SERIAL_NO, GREENBOOK, TOTAL_COST, TAX, EXTENDED_PRICE,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where CONTRACT_ID = '"
                                        + str(qt_rec_id.CONTRACT_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(LineAndEquipIDList[1])
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM CTCICO where SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                            LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                )
                            else:
                                Qury_str = (
                                    "select top "
                                        + str(PerPage)
                                        + " * from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where CONTRACT_ID = '"
                                        + str(qt_rec_id.CONTRACT_ID)
                                        + "' AND SERVICE_ID = '"
                                        + str(SERV_DESC)
                                        + "') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " and "
                                        + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM CTCICO where SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                            SERV_DESC, str(qt_rec_id.CONTRACT_ID))
                                )
                    elif str(RECORD_ID) == "SYOBJR-98788":   
                        Trace.Write("test2")       
                        contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                        qt_rec_id= Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='"+str(contract_quote_record_id)+"'")
                        
                        if TreeParentParam:
                            Qustr = "where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"' and SERVICE_TYPE = '{}'".format(TreeParam)
                        else:
                            Qustr = "where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"'"
                        
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-98853" and str(TreeParam) == "Tracked Objects":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_AC_00063").GetValue()
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " APPROVAL_TRACKED_FIELD_RECORD_ID,APRCHN_ID,APRCHNSTP,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRACKING_TYPE,CpqTableEntryId from (SELECT ROW_NUMBER() OVER(order by APPROVAL_TRACKED_FIELD_RECORD_ID) AS ROW,ACAPTF.APPROVAL_TRACKED_FIELD_RECORD_ID,ACAPTF.APRCHN_ID,ACAPTF.APRCHNSTP,ACAPTF.TRKOBJ_TRACKEDFIELD_LABEL,ACAPTF.TRKOBJ_NAME,ACAPTF.TRACKING_TYPE,ACAPTF.CpqTableEntryId FROM ACAPTF (NOLOCK) INNER JOIN ACAPTX ON ACAPTF.APRCHN_ID = ACAPTX.APRCHN_ID WHERE "+str(ATTRIBUTE_VALUE_STR)+" ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                            + str(RecAttValue)
                            + "') S where S.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " "
                        )
                        QuryCount_str = (
                            "SELECT count(DISTINCT ACAPTF.APPROVAL_TRACKED_FIELD_RECORD_ID) as cnt FROM ACAPTF (NOLOCK) INNER JOIN ACAPTX ON ACAPTF.APRCHN_ID = ACAPTX.APRCHN_ID WHERE "+str(ATTRIBUTE_VALUE_STR)+" ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                            + str(RecAttValue)                            
                            + "' "
                        )
                    elif str(RECORD_ID) == "SYOBJR-00026" and str(TreeParentParam) == "Tracked Objects":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_AC_00063").GetValue()
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " APPROVAL_TRACKED_VALUE_RECORD_ID,APRCHN_ID,APRCHNSTP,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRKOBJ_TRACKEDFIELD_OLDVALUE,TRKOBJ_TRACKEDFIELD_NEWVALUE,TRKOBJ_CPQTABLEENTRYID,CpqTableEntryId from (SELECT ROW_NUMBER() OVER(order by APPROVAL_TRACKED_VALUE_RECORD_ID) AS ROW,ACAPFV.TRKOBJ_TRACKEDFIELD_OLDVALUE,ACAPFV.APPROVAL_TRACKED_VALUE_RECORD_ID,ACAPFV.APRCHN_ID,ACAPFV.APRCHNSTP,ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL,ACAPFV.TRKOBJ_NAME,ACAPFV.TRKOBJ_TRACKEDFIELD_NEWVALUE, ACAPFV.CpqTableEntryId,ACAPFV.TRKOBJ_CPQTABLEENTRYID FROM ACAPFV (NOLOCK) INNER JOIN ACAPTX ON ACAPFV.APRCHN_ID = ACAPTX.APRCHN_ID AND ACAPFV.APPROVAL_ID = ACAPTX.APPROVAL_ID WHERE "+str(ATTRIBUTE_VALUE_STR)+" ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                            + str(RecAttValue)
                            + "' AND ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL= '"
                            + str(TreeParam)                            
                            + "') S where S.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + " "
                        )
                        QuryCount_str = (
                            "SELECT count(DISTINCT ACAPFV.APPROVAL_TRACKED_VALUE_RECORD_ID) as cnt FROM ACAPFV (NOLOCK) INNER JOIN ACAPTX ON ACAPFV.APRCHN_ID = ACAPTX.APRCHN_ID WHERE "+str(ATTRIBUTE_VALUE_STR)+" ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                            + str(RecAttValue)
                            + "' AND ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL= '"
                            + str(TreeParam)                            
                            + "' "
                        )
                    elif str(RECORD_ID) == "SYOBJR-98816":                        
                        contract_quote_record_id = Quote.GetGlobal("contract_record_id")
                        ct_rec_id= SqlHelper.GetFirst("SELECT CONTRACT_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID ='"+str(contract_quote_record_id)+"'")
                        if TreeParentParam:
                            Qustr = "where "+str(ATTRIBUTE_VALUE_STR)+" CONTRACT_ID = '"+str(ct_rec_id.CONTRACT_ID)+"' and PRODUCT_TYPE = '{}'".format(TreeParam)
                        else:
                            Qustr = "where "+str(ATTRIBUTE_VALUE_STR)+ " CONTRACT_ID = '"+str(ct_rec_id.CONTRACT_ID)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif RECORD_ID == 'SYOBJR-00006' and TreeParam == "Quote Preview":                        
                        Qury_str = (
                        "SELECT DISTINCT TOP "
                        + str(PerPage)
                        + " QUOTE_ITEM_FORECAST_PART_RECORD_ID,PART_LINE_ID,PART_NUMBER,MATPRIGRP_ID,PART_DESCRIPTION,BASEUOM_ID,SCHEDULE_MODE,DELIVERY_MODE,UNIT_PRICE,EXTENDED_PRICE,ANNUAL_QUANTITY,PRICING_STATUS,CUSTOMER_PART_NUMBER_RECORD_ID,BASEUOM_RECORD_ID,MATPRIGRP_RECORD_ID,QTEITM_RECORD_ID,QUOTE_RECORD_ID,SALESORG_RECORD_ID,SERVICE_RECORD_ID,PART_RECORD_ID,SALESUOM_RECORD_ID,CpqTableEntryId,TAX,TAX_PERCENTAGE,SERVICE_ID,SRVTAXCLA_DESCRIPTION from ( select TOP "+ str(PerPage)+" ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQIFP (nolock)  where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_RECORD_ID ='"+str(RecAttValue)
                        +"') m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " AND "
                        + str(Page_End)+" "
                        )
                        QuryCount_str = (
                            "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQIFP (nolock) WHERE "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_RECORD_ID = '"
                            + str(RecAttValue)
                            + "'"
                        )
                    elif RECORD_ID == 'SYOBJR-00010':
                        imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                        acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'                     
                        Qury_str = (
                            "SELECT DISTINCT TOP "
                            + str(PerPage)
                            + "QUOTE_ITEM_FORECAST_PART_RECORD_ID, CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS,SERVICE_ID,PART_LINE_ID,PART_NUMBER,PART_DESCRIPTION,MATPRIGRP_ID,BASEUOM_ID,SCHEDULE_MODE,DELIVERY_MODE,UNIT_PRICE,EXTENDED_PRICE,ANNUAL_QUANTITY,CUSTOMER_PART_NUMBER_RECORD_ID,BASEUOM_RECORD_ID,MATPRIGRP_RECORD_ID,QTEITM_RECORD_ID,QUOTE_RECORD_ID,SALESORG_RECORD_ID,SERVICE_RECORD_ID,PART_RECORD_ID,SALESUOM_RECORD_ID,CpqTableEntryId,TAX,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE from ( select TOP 10 ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQIFP (nolock)  where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_RECORD_ID ='"+str(RecAttValue)
                            +"') m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " AND "
                            + str(Page_End)+" ORDER BY PRICING_STATUS ASC"
                        )
                        QuryCount_str = (
                            "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQIFP (nolock) WHERE "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_RECORD_ID = '"
                            + str(RecAttValue)
                            + "'"
                        )
                    elif RECORD_ID == 'SYOBJR-00008':
                        imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                        acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                        exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'

                        if getyears == 1:
                            col_year =  'YEAR_1'
                        elif getyears == 2:
                            col_year =  'YEAR_1,YEAR_2'
                        elif getyears == 3:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3'
                        elif getyears == 4:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                        else:
                            col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'

                        price_status = []
                        # quote_itm_rec = Sql.GetFirst("SELECT QUOTE_ITEM_RECORD_ID FROM SAQITM (NOLOCK) "+str(Qustr)+"")
                        SAQICO_status = Sql.GetList("SELECT DISTINCT PRICING_STATUS FROM SAQICO (NOLOCK) "+str(Qustr)+"")
                        for pricing_status in SAQICO_status:
                            price_status.append(pricing_status.PRICING_STATUS)
                        
                        all_acquired = ["ACQUIRING","APPROVAL REQUIRED","ERROR"]
                        all_error = ["APPROVAL REQUIRED","ACQUIRING","ACQUIERD"]
                        all_required = ["ACQUIERD","ACQUIRING","ERROR"]
                        all_acquiring = ["ACQUIERD","ERROR","APPROVAL REQUIRED"]
                        acq_error = ["ACQUIERD","ERROR"]
                        acq_req = ["ACQUIERD","APPROVAL REQUIRED"]
                        not_acq_req = ["ACQUIRING","ERROR"]
                        acq_error_approval = ["ACQUIERD","ERROR","APPROVAL"]
                        not_acq_error = ["ACQUIRING","APPROVAL REQUIRED"]

                        if "ACQUIRED" in price_status and ('ACQUIRING' not in price_status and 'APPROVAL REQUIRED' not in price_status and 'ERROR' not in price_status):
                            icon = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                        elif "ERROR" in price_status and ('ACQUIRED' not in price_status and 'APPROVAL REQUIRED' not in price_status and 'ACQUIRING' not in price_status):
                            icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                        elif "APPROVAL REQUIRED" in price_status and ('ACQUIRED' not in price_status and 'ERROR' not in price_status and 'ACQUIRING' not in price_status):
                            icon = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                        elif "ACQUIRING" in price_status and 'ACQUIRED' not in price_status and 'ERROR' not in price_status and 'APPROVAL REQUIRED' not in price_status:
                            icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                        elif ("ACQUIRED" in price_status and "ERROR" in price_status) and ('ACQUIRING' not in price_status and 'APPROVAL REQUIRED' not in price_status):
                            icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                        elif ("ACQUIRED" in price_status and "ACQUIRING" in price_status) and ('ERROR' not in price_status and 'APPROVAL REQUIRED' not in price_status):
                            icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                        elif ("ACQUIRED" in price_status and "APPROVAL REQUIRED" in price_status) and ('ERROR' not in price_status and 'ACQUIRING' not in price_status):
                            icon = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                        elif ("ACQUIRED" in price_status and 'ERROR' in price_status and 'APPROVAL REQUIRED' in price_status) and "ACQUIRING" not in price_status :
                            icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                        elif ("ACQUIRING" in price_status and 'APPROVAL REQUIRED' in price_status) and ('ACQUIRED' not in price_status and "ERROR" not in price_status) :
                            icon = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                        else:
                            icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                        


                        if TreeParam == "Quote Items":                            
                            Qustr = "where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_RECORD_ID ='"+str(RecAttValue)+"'"
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + " '"+ icon +"' AS PO_NOTES, QUOTE_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, OBJECT_QUANTITY,QUANTITY, TOTAL_COST, SALES_DISCOUNT_PRICE,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE, TARGET_PRICE, CEILING_PRICE, BD_PRICE, BD_PRICE_MARGIN, DISCOUNT, SALES_PRICE, YEAR_OVER_YEAR, "+col_year+" "
                                + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                                + str(Wh_API_NAMEs)
                                + ") AS ROW, * from "
                                + str(ObjectName)
                                + " (nolock) "
                                + str(Qustr)
                                + " ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + ""
                            )
                            QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif RECORD_ID == 'SYOBJR-00024':
                        
                        quote_obj = Sql.GetFirst("select QUOTE_ID,MASTER_TABLE_QUOTE_RECORD_ID from SAQTMT where MASTER_TABLE_QUOTE_RECORD_ID = '{contract_quote_record_id}'".format(contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")))
                        quote_id = quote_obj.QUOTE_ID
                        TreeParam = Product.GetGlobal("TreeParam")
                        if TreeSuperParentParam == 'Approvals':
                            chain_step_name = subTab.split(':')[1].strip()
                            step_id = chain_step_name.split(' ')[1]
                            round_value = TreeParam.split()[1]
                            TreeParam = Product.GetGlobal("TreeParam")
                            Qury_str = ("""select DISTINCT top {PerPage} * from (select ROW_NUMBER() OVER( ORDER BY ACAPTX.APRCHNSTP_ID) AS ROW,ACAPTX.APPROVAL_TRANSACTION_RECORD_ID, ACAPTX.APPROVAL_ID,ACAPTX.APRCHNSTP_ID,ACAPTX.APRCHNSTP_APPROVER_ID,ACAPTX.APPROVAL_ROUND,ACAPTX.APPROVALSTATUS,ACAPTX.RECIPIENT_COMMENTS,ACAPTX.APRCHNSTP_RECORD_ID,ACAPTX.APPROVAL_RECIPIENT,ACAPTX.CpqTableEntryId FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID and ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHNSTP_ID = '{chain_step_name}' and ACAPTX.APRCHN_ID = '{chain_id}' and ACAPTX.APPROVAL_ROUND = '{step_value}')m where m.ROW BETWEEN """.format(PerPage = PerPage,contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id, chain_step_name = step_id,chain_id = TreeParentParam,step_value = round_value ) + str(Page_start) + " and " + str(Page_End))
                            QuryCount_str = """select count(ACAPTX.CpqTableEntryId) as cnt FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID and  ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHNSTP_ID = '{chain_step_name}' and ACAPTX.APRCHN_ID = '{chain_id}' and ACAPTX.APPROVAL_ROUND = '{step_value}' """.format(contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id,chain_step_name = step_id,chain_id = TreeParentParam,step_value = round_value)
                        else:
                            
                            Qury_str = ("""select DISTINCT top {PerPage} * from (select ROW_NUMBER() OVER( ORDER BY ACAPTX.APPROVAL_TRANSACTION_RECORD_ID) AS ROW,ACAPTX.APPROVAL_TRANSACTION_RECORD_ID, ACAPTX.APPROVAL_ID,ACAPTX.APRCHNSTP_ID,ACAPTX.APRCHNSTP_APPROVER_ID,ACAPTX.APPROVAL_ROUND,ACAPTX.APPROVALSTATUS,ACAPTX.RECIPIENT_COMMENTS,ACAPTX.APRCHNSTP_RECORD_ID,ACAPTX.APPROVAL_RECIPIENT,ACAPTX.CpqTableEntryId FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID  and ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and  {ATTRIBUTE_VALUE_STR} ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHN_ID = '{Chain}')m where m.ROW BETWEEN """.format(PerPage = PerPage,contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id,Chain = TreeParam,ATTRIBUTE_VALUE_STR = ATTRIBUTE_VALUE_STR) + str(Page_start) + " and " + str(Page_End))
                            QuryCount_str = """select count(ACAPTX.CpqTableEntryId) as cnt FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID and  ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and {ATTRIBUTE_VALUE_STR}  ACAPTX.APRCHN_ID = '{Chain}' """.format(contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id,Chain = TreeParam, ATTRIBUTE_VALUE_STR = ATTRIBUTE_VALUE_STR)
                    
                    ##involved parties equipmemt and tool relocation matrix starts
                    elif (str(RECORD_ID) == "SYOBJR-98858" or str(RECORD_ID) == "SYOBJR-00028") and str(TreeParam) == "Quote Information":
                        account_id = Product.GetGlobal("stp_account_id")
                        
                        Qury_str = ("""select DISTINCT top {PerPage} * from (select ROW_NUMBER() OVER( ORDER BY SAQSTE.FABLOCATION_ID DESC) AS ROW,SAQSTE.* from SAQSTE  inner join SAQSCF(nolock)  on SAQSTE.QUOTE_RECORD_ID = SAQSCF.QUOTE_RECORD_ID and SAQSTE.SRCFBL_ID = SAQSCF.SRCFBL_ID where SAQSTE.QUOTE_RECORD_ID = '{contract_quote_record_id}' and SAQSTE.{ATTRIBUTE_VALUE_STR} SAQSTE.SRCACC_ID = '{account_id}')m where m.ROW BETWEEN """.format(PerPage = PerPage,account_id = account_id,
                        contract_quote_record_id = str(RecAttValue),ATTRIBUTE_VALUE_STR = ATTRIBUTE_VALUE_STR)+ str(Page_start) + " and " + str(Page_End))
                        
                        
                        
                        QuryCount_str = "select count(SAQSTE.CpqTableEntryId) as cnt from SAQSTE  inner join SAQSCF(nolock) on SAQSTE.QUOTE_RECORD_ID = SAQSCF.QUOTE_RECORD_ID and SAQSTE.SRCFBL_ID= SAQSCF.SRCFBL_ID where SAQSTE.QUOTE_RECORD_ID = '{contract_quote_record_id}' and SAQSTE.{ATTRIBUTE_VALUE_STR} SAQSTE.SRCACC_ID = '{account_id}'".format(account_id = account_id,contract_quote_record_id=str(RecAttValue),ATTRIBUTE_VALUE_STR = ATTRIBUTE_VALUE_STR)
                    ##involved parties equipmemt ends
                    elif str(RECORD_ID) == "SYOBJR-98859":
                        Trace.Write("5512")
                        #"where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_RECORD_ID ='"+str(RecAttValue)+"'"
                        Qustr += " where "+ str(ATTRIBUTE_VALUE_STR)+" QUOTE_RECORD_ID ='"+str(RecAttValue)+"' AND  SERVICE_ID = '"+str(TreeParentParam)+"' "
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)

                    ##involved parties source fab starts
                    elif str(RECORD_ID) == "SYOBJR-98862":
                        RecAttValue=Product.Attributes.GetByName("QSTN_SYSEFL_SY_00125").GetValue()
                        Qustr = " WHERE "+str(ATTRIBUTE_VALUE_STR) +" APP_ID = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            +" ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-98863":
                        RecAttValue=Product.Attributes.GetByName("QSTN_SYSEFL_SY_00125").GetValue()
                        Qustr = " WHERE "+str(ATTRIBUTE_VALUE_STR) +" TAB_ID = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                     
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    
                    elif str(RECORD_ID) == "SYOBJR-98864":
                        Qustr = " WHERE "+str(ATTRIBUTE_VALUE_STR) +" TAB_NAME = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-93123":
                        app_ObjectName = Sql.GetFirst("select PRIMARY_OBJECT_NAME FROM SYTABS INNER JOIN SYAPPS ON SYTABS.APP_LABEL = SYAPPS.APP_LABEL WHERE SYTABS.TAB_LABEL = '"+str(TopTreeSuperParentParam)+"' AND SYAPPS.APP_LABEL = '"+str(TreeFirstSuperTopParentParam)+"'")
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        Qustr = " WHERE "+str(ATTRIBUTE_VALUE_STR) +" SECTION_NAME = '"+str(TreeParentParam)+"' AND PROFILE_ID ='"+str(RecAttValue)+"' AND OBJECT_NAME = '"+str(ObjectName)+"' "
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)    
                    elif str(RECORD_ID) == "SYOBJR-98784" and TreeFirstSuperTopParentParam == "Pages":
                        Qustr = " WHERE SECTION_NAME = '"+str(TreeParentParam)+"' AND TAB_NAME = '"+str(TreeSecondSuperTopParentParam)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-93188":
                        Trace.Write('SYOBJR-93188@1111')
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        GetAppname_query = ""
                        Qustr = " WHERE TAB_NAME = '"+str(TreeParentParam)+"'and "+str(ATTRIBUTE_VALUE_STR)+" PROFILE_ID ='"+str(RecAttValue)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif str(RECORD_ID) == "SYOBJR-95825" and str(TreeParentParam) == 'Constraints':
                        Qustr = "WHERE CONSTRAINT_TYPE = '"+str(TreeParam)+"' AND OBJECT_RECORD_ID ='"+str(RecAttValue)+"'" 
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif (str(RECORD_ID) == "SYOBJR-98857") and str(TreeParam) == "Quote Information":
                        account_id = Product.GetGlobal("stp_account_id")
                        quote_rec_id = Product.GetGlobal("contract_quote_record_id")
                        Qustr = " WHERE QUOTE_RECORD_ID = '"+str(quote_rec_id)+"' and "+str(ATTRIBUTE_VALUE_STR) +" SRCACC_ID = '{}'".format(account_id)
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        
                        
                        
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    ##involved parties source fab ends
                    elif RECORD_ID == 'SYOBJR-98841':
                        imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                        acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                        
                        if TreeParam == "Contract Items":
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + "  CASE WHEN ITEM_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS PO_NOTES, CONTRACT_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, QUANTITY, TAX, DISCOUNT, EXTENDED_PRICE"
                                + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                                + str(Wh_API_NAMEs)
                                + ") AS ROW, * from "
                                + str(ObjectName)
                                + " (nolock) "
                                + str(Qustr)
                                + " ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + ""
                            )
                            QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    elif RECORD_ID == 'SYOBJR-98792' and str(TreeParam) == "Quote Preview":                        
                        contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                        Qustr_id = Sql.GetFirst("SELECT QUOTE_ID FROM SAQITM WHERE QUOTE_RECORD_ID ='" + str(
                        contract_quote_record_id) + "'")
                        if getyears == 1:
                            col_year =  'YEAR_1'
                        elif getyears == 2:
                            col_year =  'YEAR_1,YEAR_2'
                        elif getyears == 3:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3'
                        elif getyears == 4:
                            col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                        else:
                            col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'
                        if TreeParam:
                            Qustr = "where QUOTE_ID = '"+str(Qustr_id.QUOTE_ID)+"'"
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " QUOTE_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, ONSITE_PURCHASE_COMMIT,OBJECT_QUANTITY, TOTAL_COST, SALES_DISCOUNT_PRICE, TAX, EXTENDED_PRICE, QUANTITY, TARGET_PRICE, CEILING_PRICE, BD_PRICE, BD_PRICE_MARGIN, DISCOUNT, SALES_PRICE, YEAR_OVER_YEAR, "+col_year+" , SRVTAXCLA_DESCRIPTION, TAX_PERCENTAGE, CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) "
                            + str(Qustr)
                            + " AND SERVICE_ID NOT LIKE '%BUNDLE%') m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)+ " AND SERVICE_ID NOT LIKE '%BUNDLE%' "

                    elif str(RECORD_ID) == "SYOBJR-98815":                        
                        #Qustr = "where SALESORG_ID = '"+str(TP)+"' and SORG_CURRENCY='"+str(PR_CURR)+"'"
                        splitTP = TP.split('-')
                        TP = splitTP[1]
                        Qury_str = (
                            "SELECT DISTINCT TOP "
                            + str(PerPage)
                            + "QUOTE_SALESORG_RECORD_ID,QUOTE_ID,QUOTE_NAME,SALESORG_ID,SALESORG_NAME,DISTRIBUTIONCHANNEL_ID,DIVISION_ID,SALESOFFICE_ID,SALESOFFICE_NAME,CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQTSO (nolock)  where "+ str(ATTRIBUTE_VALUE_STR)+" SALESORG_ID = '"+str(TP)+"' and SORG_CURRENCY='"+str(PR_CURR)+"') m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " AND "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = (
                            "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQTSO (nolock) WHERE "+ str(ATTRIBUTE_VALUE_STR)+" SALESORG_ID = '"+str(TP)+"' and SORG_CURRENCY='"+str(PR_CURR)+"'"
                        )

                    elif RECORD_ID == "SYOBJR-95866":                        
                        Qustr = (
                            " where "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " CFGMATCLS_PAGE_TYPE in ('PRODUCT LANDING PAGE') "
                        )
                    elif RECORD_ID == "SYOBJR-95867":                        
                        Qustr = (
                            " where "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " CFGMATCLS_PAGE_TYPE in ('PRODUCT CONFIGURATION LANDING PAGE') "
                        )
                    elif RECORD_ID == "SYOBJR-95987":                        
                        Qustr = (
                            " where "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND PRODUCT_SPECIFICATION = 0 AND "
                            + str(ATTRIBUTE_VALUE_STR)
                        )
                    elif RECORD_ID == "SYOBJR-98784":
                        gettabval = getptabname = ""
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                        gettabval = Sql.GetFirst(
                            "Select RECORD_ID,PAGE_NAME,TAB_LABEL from SYTABS where PAGE_NAME = '"
                            + str(TreeParentParam)
                            + "' and TAB_LABEL = '"
                            + str(TopTreeSuperParentParam)
                            + "'"
                        )
                        
                        if gettabval:
                            getptabname = gettabval.RECORD_ID
                        Qustr = " where "+ str(ATTRIBUTE_VALUE_STR)+" TAB_RECORD_ID = '" + str(getptabname) + "'"
                    elif RECORD_ID == "SYOBJR-94452":                        
                        Wh_API_NAME = "ROLE_RECORD_ID"
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00001").GetValue()
                          
                        Qustr = " where "+str(ATTRIBUTE_VALUE_STR)+" "+ str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"                             
                    elif RECORD_ID == "SYOBJR-98782":
                        Qustr = " where "+str(ATTRIBUTE_VALUE_STR)+" TAB_LABEL = '" + str(TreeParentParam) + "'"
                    elif RECORD_ID == "SYOBJR-94441":
                        Trace.Write('94441@@@@------')                        
                        RecAttValue = productAttributesGetByName("QSTN_SYSEFL_SY_00152").GetValue()
                        Qustr = " where "+str(ATTRIBUTE_VALUE_STR)+" "+ str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                    elif str(RECORD_ID) == "SYOBJR-95824":
                        #Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'" 
                        RecAttValue = productAttributesGetByName("QSTN_SYSEFL_SY_00701").GetValue()
                        Qustr = " where "+str(ATTRIBUTE_VALUE_STR)+" "+ str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'" 
                    elif str(RECORD_ID) == "SYOBJR-95840": 
                        Wh_API_NAMEs = "PAGEACTION_RECORD_ID"                       
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00723").GetValue()
                        Qustr =  " where "+str(ATTRIBUTE_VALUE_STR)+" SCRIPT_RECORD_ID = '" + str(RecAttValue) + "'"         
                    elif str(RECORD_ID) == "SYOBJR-95890": 
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_03295").GetValue()
                        Qustr = " where "+str(ATTRIBUTE_VALUE_STR)+" "+ str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                    else:    
                        Trace.Write("attri"+str(ATTRIBUTE_VALUE_STR))    
                        Trace.Write("sort param 2 "+str(Wh_API_NAMEs))                                        
                        Qustr = " where "+str(ATTRIBUTE_VALUE_STR)+" "+ str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"

                else:  
                    try:     
                        RecAttValue = Quote.GetGlobal("contract_quote_record_id")
                    except:
                        RecAttValue = ''                 
                    TreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                    if RECORD_ID == "SYOBJR-95868":                        
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " "
                            + "SYSEFL."
                            + str(select_obj_str)
                            + ",SYSEFL.CpqTableEntryId from "
                            + str(ObjectName)
                            + " (nolock) INNER JOIN SYSECT (nolock) ON SYSEFL.SECTION_RECORD_ID = SYSECT.RECORD_ID  AND "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' "
                            + "where SYSEFL.SECTION_NAME = '"
                            + str(TreeParentParam)
                            + "' "
                            + "where SYSEFL.SECTION_NAME = '"
                            + str(TreeParentParam)
                            + "' ORDER BY abs(SYSEFL.DISPLAY_ORDER)"
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from "
                            + str(ObjectName)
                            + " (nolock) INNER JOIN SYSECT (nolock) ON SYSEFL.SECTION_RECORD_ID = SYSECT.RECORD_ID and "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' where SYSEFL.SECTION_NAME = '"
                            + str(TreeParentParam)
                            + "'"
                        )                        
                    elif RECORD_ID == "SYOBJR-95843" and TreeParentParam != "" :  
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_03295").GetValue()      
                        Qury_str = (
                        "select top "
                        + str(PerPage)
                        + " * "
                        + " from "
                        + str(ObjectName)
                        + " (nolock) WHERE "
                        + str(Wh_API_NAME)
                        + " = '"
                        + str(RecAttValue)
                        + "' AND PAGE_NAME = '"
                        + str(TreeParentParam)
                        + "'"
                        
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from "
                            + str(ObjectName)
                            + " (nolock) WHERE "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND PAGE_NAME = '"
                            + str(TreeParentParam)
                            + "'"
                        )
                    elif RECORD_ID == "SYOBJR-94452":                        
                        Wh_API_NAME = "ROLE_RECORD_ID"
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00001").GetValue()

                        Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"   
                    elif RECORD_ID == "SYOBJR-94489":                        
                        GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                        Qury_str = (
                        "select DISTINCT top 10 RECORD_ID,SECTION_NAME,DISPLAY_ORDER,PARENT_SECTION_RECORD_ID,OWNER_RECORD_ID,PRIMARY_OBJECT_RECORD_ID,PAGE_LABEL,PAGE_RECORD_ID,CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by DISPLAY_ORDER) AS ROW,* from SYSECT where PAGE_LABEL = '"
                        + str(TreeParentParam)
                        + "') m where m.ROW BETWEEN 1 and 10"
                        )
                       
                        QuryCount_str = (
                            "select count(*) as cnt from SYSECT (nolock) where PAGE_LABEL = '" + str(TreeParentParam) + "'"
                        )

                    elif RECORD_ID == "SYOBJR-93162":
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        TreeFirstSuperTopParentParam = Product.GetGlobal("CommonTreeFirstSuperTopParentParam")
                        CommonTreeParentParam = Product.GetGlobal("CommonTreeParentParam")
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        getTabrec = Sql.GetFirst(
                            "SELECT TAB_RECORD_ID from SYPRTB where APP_ID = '"
                            + str(TreeFirstSuperTopParentParam)
                            + "' and PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and TAB_ID = '"
                            + str(CommonTreeTopSuperParentParam)
                            + "'"
                        )
                        sectrecid = Tabrecordid = ""
                        if getTabrec is not None:
                            Tabrecordid = str(getTabrec.TAB_RECORD_ID)                            
                            getsectrec = Sql.GetFirst(
                                "SELECT SECTION_RECORD_ID from SYPRSN where TAB_RECORD_ID = '"
                                + str(Tabrecordid)
                                + "' and SECTION_ID ='"
                                + str(CommonTreeParentParam)
                                + "'"
                            )
                            if getsectrec is not None:
                                sectrecid = str(getsectrec.SECTION_RECORD_ID)
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " * from ( select ROW_NUMBER() OVER(order by P.SECTION_FIELD_ID ) AS ROW,P.PROFILE_SECTIONFIELD_RECORD_ID,P.SECTIONFIELD_RECORD_ID,P.SECTION_FIELD_ID ,P.VISIBLE,P.EDITABLE,P.PROFILE_RECORD_ID,P.CpqTableEntryId,s.DISPLAY_ORDER from SYPRSF P (nolock)  inner join SYSEFL s on s.RECORD_ID = P.SECTIONFIELD_RECORD_ID where "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " P.PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and P.SECTION_RECORD_ID = '"
                            + str(sectrecid)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + "  order by m.DISPLAY_ORDER"
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from SYPRSF (nolock)  where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and SECTION_RECORD_ID = '"
                            + str(sectrecid)
                            + "'"
                        )
                    elif RECORD_ID == "SYOBJR-95864":
                        Qustr1 = (
                            " where "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(RecAttValue)
                            + "' AND ACTIVE = '"
                            + str(TreeParam)
                            + "' "
                        )
                        Qustr = Qustr1.replace("Active", "True").replace("Inactive", "False")

                    elif RECORD_ID == "SYOBJR-94441":
                        Trace.Write('94441@@@@------')                        
                        RecAttValue = productAttributesGetByName("QSTN_SYSEFL_SY_00152").GetValue()
                        Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"

                    elif RECORD_ID == "SYOBJR-98782":                        
                        #RecAttValue = productAttributesGetByName("QSTN_SYSEFL_SY_01110").GetValue()
                        #Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'" 
                        Qury_str = (
                            "select DISTINCT top "
                            + str(PerPage)
                            + " "
                            + str(select_obj_str)
                            + " from ( select ROW_NUMBER() OVER(order by "
                            + str(Wh_API_NAMEs)
                            + ") AS ROW, * from "
                            + str(ObjectName)
                            + " (nolock) where TAB_LABEL = '" + str(TreeParentParam) + "'"
                            " ) m where m.ROW BETWEEN " + str(Page_start) + " and " + str(Page_End) + ""
                        )
                        QuryCount_str = (
                            "select count(*) as cnt from "
                            + str(ObjectName)
                            + " (nolock) where TAB_LABEL = '" + str(TreeParentParam) + "'"
                        )               
                    
                    elif RECORD_ID == "SYOBJR-94489":

                        GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()

                        gettabres = Sql.GetFirst(
                            "Select RECORD_ID from SYTABS where APP_LABEL = '"
                            + str(GetappValue)
                            + "' and TAB_LABEL = '"
                            + str(TreeParentParam)
                            + "'"
                        )
                        if gettabres:

                            tabRecord = str(gettabres.RECORD_ID)
                        Qustr = " where TAB_RECORD_ID = '" + str(tabRecord) + "'"

                    elif RECORD_ID == "SYOBJR-95800":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        permiss_id = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00125").GetValue()
                        

                        Qury_str = (
                            "select DISTINCT TOP "
                            + str(PerPage)
                            + " ID,USERNAME,NAME,ACTIVE from ( select ROW_NUMBER() OVER(order by ID) AS ROW, ID,USERNAME,NAME,ACTIVE from USERS U (nolock) inner join users_permissions up on U.id = up.user_id   where "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " up.permission_id = '"
                            + str(permiss_id)
                            + "'  ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + ""
                        )
                        QuryCount_str = (
                            "select count(U.ID) as cnt from USERS U (nolock)  inner join users_permissions up on U.id = up.user_id  where  up.permission_id = '"
                            + str(permiss_id)
                            + "'  "
                        )
                    elif RECORD_ID == "SYOBJR-93121":
                        proff_per_id = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00125").GetValue()
                        Profile_ID_PERMISSION = Product.GetGlobal("Profile_ID_PERMISSION")                        
                        if proff_per_id != "":
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " PROFILE_APP_RECORD_ID,APP_ID,VISIBLE,[DEFAULT],PROFILE_RECORD_ID, CpqTableEntryId from ( select ROW_NUMBER() OVER( order by APP_ID) AS ROW, PROFILE_APP_RECORD_ID,APP_ID,VISIBLE,[DEFAULT],PROFILE_RECORD_ID, CpqTableEntryId  from SYPRAP (nolock) where PROFILE_RECORD_ID = '"
                                + str(proff_per_id)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from "
                                + str(ObjectName)
                                + " (nolock) where  PROFILE_RECORD_ID = '"
                                + str(proff_per_id)
                                + "' "
                            )
                        else:
                            proff_id = Product.GetGlobal("Profile_ID")
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " PROFILE_APP_RECORD_ID,APP_ID,VISIBLE,[DEFAULT],PROFILE_RECORD_ID, CpqTableEntryId from ( select ROW_NUMBER() OVER( order by APP_ID) AS ROW, PROFILE_APP_RECORD_ID,APP_ID,VISIBLE,[DEFAULT],PROFILE_RECORD_ID, CpqTableEntryId  from SYPRAP (nolock) where PROFILE_RECORD_ID = '"
                                + str(Profile_ID_PERMISSION)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from "
                                + str(ObjectName)
                                + " (nolock) where  PROFILE_RECORD_ID = '"
                                + str(Profile_ID_PERMISSION)
                                + "' "
                            )
                    elif RECORD_ID == "SYOBJR-93159":
                        Wh_API_NAME = "PROFILE_ID"
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")
                        appId = Product.GetGlobal("CommonTreeParentParam")                        
                        if appId == "App Level Permissions":
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " *  from ( select ROW_NUMBER() OVER(order by S.DISPLAY_ORDER) AS ROW, p.PROFILE_TAB_RECORD_ID,p.TAB_ID,p.VISIBLE,p.PROFILE_RECORD_ID,p.CpqTableEntryId,S.DISPLAY_ORDER from SYPRTB p (nolock) inner join SYTABS S on S.RECORD_ID = p.TAB_RECORD_ID where "
                                + str(ATTRIBUTE_VALUE_STR)
                                + " p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.APP_ID = '"
                                + str(TreeParam)
                                + "' ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )                            
                            QuryCount_str = (
                                "select count(*) as cnt from SYPRTB (nolock)  where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and APP_ID = '"
                                + str(TreeParam)
                                + "'"
                            )
                        else:
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " *  from ( select ROW_NUMBER() OVER(order by S.DISPLAY_ORDER) AS ROW, p.PROFILE_TAB_RECORD_ID,p.TAB_ID,p.VISIBLE,p.PROFILE_RECORD_ID,p.CpqTableEntryId,S.DISPLAY_ORDER from SYPRTB p (nolock) inner join SYTABS S on S.RECORD_ID = p.TAB_RECORD_ID where "
                                + str(ATTRIBUTE_VALUE_STR)
                                + " p.PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and p.APP_ID = '"
                                + str(appId)
                                + "' ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by m.DISPLAY_ORDER"
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from SYPRTB (nolock)  where PROFILE_ID = '"
                                + str(RecAttValue)
                                + "' and APP_ID = '"
                                + str(appId)
                                + "'"
                            )

                    elif RECORD_ID == "SYOBJR-93160":
                        RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                        GetAppname_query = ""
                        if TreeTopSuperParentParam == "App Level Permissions":
                            CommonTreeSuperParentParam = Product.GetGlobal("CommonTreeSuperParentParam")                            
                            GetAppname_query = Sql.GetFirst(
                                "SELECT TAB_RECORD_ID FROM SYPRTB where APP_ID = '"
                                + str(CommonTreeSuperParentParam)
                                + "' and TAB_ID = '"
                                + str(TreeParam)
                                + "'"
                            )
                        else:
                            TreeParam = Product.GetGlobal("CommonTreeParentParam")
                            GetAppname_query = Sql.GetFirst(
                                "SELECT TAB_RECORD_ID FROM SYPRTB where APP_ID = '"
                                + str(TreeTopSuperParentParam)
                                + "' and TAB_ID = '"
                                + str(TreeParam)
                                + "'"
                            )
                        Qury_str = (
                            "select top "
                            + str(PerPage)
                            + " *  from ( select ROW_NUMBER() OVER(order by P.PROFILE_RECORD_ID) AS ROW, P.PROFILE_SECTION_RECORD_ID,P.SECTION_RECORD_ID,P.SECTION_ID,P.TAB_ID,P.VISIBLE,P.PROFILE_RECORD_ID,P.CpqTableEntryId,s.DISPLAY_ORDER from SYPRSN P (nolock) inner join SYSECT s on s.RECORD_ID = P.SECTION_RECORD_ID where "
                            + str(ATTRIBUTE_VALUE_STR)
                            + " P.PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and P.TAB_ID = '"
                            + str(TreeParam)
                            + "' and P.TAB_RECORD_ID ='"
                            + str(GetAppname_query.TAB_RECORD_ID)
                            + "' ) m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " and "
                            + str(Page_End)
                            + "  order by m.DISPLAY_ORDER"
                        )

                        QuryCount_str = (
                            "select count(*) as cnt from SYPRSN (nolock)  where PROFILE_ID = '"
                            + str(RecAttValue)
                            + "' and TAB_ID = '"
                            + str(TreeParam)
                            + "' and TAB_RECORD_ID ='"
                            + str(GetAppname_query.TAB_RECORD_ID)
                            + "'"
                        )
                    # elif RECORD_ID == "SYOBJR-93123":                        
                    #     prof_id = Product.GetGlobal("Profile_ID_val")
                    #     proff_id = Product.GetGlobal("Profile_ID")
                    #     if prof_id != "":
                    #         Wh_API_NAME = "PROFILE_ID"
                    #         Qustr = " where " + str(Wh_API_NAME) + " = '" + str(prof_id) + "'"
                    #     else:
                    #         Qustr = " where " + str(Wh_API_NAME) + " = '" + str(proff_id) + "'"

                    elif RECORD_ID == "SYOBJR-90020":
                        revision_id = Product.GetGlobal("segmentRevisionId")
                        country_value = ""
                        if (
                            str(TreeParam) != ""
                            and (str(TreeParam) != "Fulfillment Model" and str(TreeParam) != "User Countries")
                        ) and (
                            str(TreeParentParam) == "Fulfillment Model" or str(TreeSuperParentParam) == "Fulfillment Model"
                        ):
                            ctry_obj = Sql.GetFirst(
                                "select * from SACTRY (nolock) where COUNTRY_NAME = '" + str(TreeParam) + "'"
                            )
                        else:
                            ctry_obj = SqlHelper.GetFirst(
                                "select * from PASACS (NOLOCK) where PRICEAGREEMENT_RECORD_ID = '"
                                + str(RecAttValue)
                                + "' AND AGMREV_ID = '"
                                + str(revision_id)
                                + "' AND COUNTRY_NAME = '"
                                + str(TreeParam)
                                + "'"
                            )
                        if ctry_obj is not None:
                            country_value = str(ctry_obj.COUNTRY_RECORD_ID)

                        Qustr = (
                            " where PRICEAGREEMENT_RECORD_ID = '"
                            + str(RecAttValue)
                            + "' AND AGMREV_ID = '"
                            + str(revision_id)
                            + "' AND "
                            + str(Wh_API_NAME)
                            + " = '"
                            + str(country_value)
                            + "'"
                        )
                    elif RECORD_ID == "SYOBJR-98784":
                        gettabval = getptabname = ""
                        CommonTreeTopSuperParentParam = Product.GetGlobal("CommonTreeTopSuperParentParam")
                        GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()
                        gettabval = Sql.GetFirst(
                            "Select RECORD_ID,PAGE_NAME,TAB_LABEL from SYTABS where PAGE_NAME = '"
                            + str(TreeParentParam)
                            + "' and TAB_LABEL = '"
                            + str(TopTreeSuperParentParam)
                            + "'"
                        )                        
                        if gettabval:
                            getptabname = gettabval.RECORD_ID
                        Qustr = " where TAB_RECORD_ID = '" + str(getptabname) + "'"
                    elif RECORD_ID == "SYOBJR-94490":
                        GetappValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00154").GetValue()                        
                        gettabres = Sql.GetFirst(
                            "Select RECORD_ID from SYSECT where PAGE_NAME = '"
                            + str(TopTreeSuperParentParam)
                            + "' and SECTION_NAME = '"
                            + str(TreeParentParam)
                            + "'"
                        )
                        if gettabres:                            
                            tabRecord = str(gettabres.RECORD_ID)

                        Qustr = " where SECTION_RECORD_ID = '" + str(tabRecord) + "'"

                    else:
                        TreeParam = Product.GetGlobal("TreeParam")
                        TreeParentParam = Product.GetGlobal("TreeParentLevel0") 
                        TreeSuperParentParam = Product.GetGlobal("TreeParentLevel1") 
                        Curr_OM_Node = Product.GetGlobal("Curr_OM_Node")                        
                        PLN_ID = Product.GetGlobal("PLN_ID")
                        if PLN_ID != "":
                            PLN_ID = PLN_ID.split("-")[1]
                        SORG_ID = Product.GetGlobal("SORG_ID")
                        if SORG_ID != "":
                            SORG_ID = SORG_ID.split("-")[1]                        
                        if RECORD_ID == "SYOBJR-93122":
                            RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()

                            Qury_str = (
                                "select  top "
                                + str(PerPage)
                                + "  PROFILE_OBJECT_RECORD_ID,OBJECT_RECORD_ID, OBJECT_NAME, VISIBLE,CpqTableEntryId from ( select ROW_NUMBER() OVER( order by OBJECT_NAME) AS ROW,  PROFILE_OBJECT_RECORD_ID,OBJECT_RECORD_ID, OBJECT_NAME, VISIBLE,CpqTableEntryId from SYPROH (nolock) where "
                                + str(ATTRIBUTE_VALUE_STR)
                                + " PROFILE_ID = '"
                                + str(RecAttValue)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " order by OBJECT_NAME"
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from SYPROH (nolock) where  PROFILE_ID = '" + str(RecAttValue) + "' "
                            )

                        elif str(RECORD_ID) == "SYOBJR-94454" or str(RECORD_ID) == "SYOBJR-94455":
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + " "
                                + str(select_obj_str)
                                + " from ( select ROW_NUMBER() OVER(order by "
                                + str(Wh_API_NAMEs)
                                + ") AS ROW, * from "
                                + str(ObjectName)
                                + " (nolock) where "
                                + str(Wh_API_NAME)
                                + " = '"
                                + str(RecAttValue)
                                + "' "
                                " ) m where m.ROW BETWEEN " + str(Page_start) + " and " + str(Page_End) + ""
                            )
                            QuryCount_str = (
                                "select count(*) as cnt from "
                                + str(ObjectName)
                                + " (nolock) where "
                                + str(Wh_API_NAME)
                                + " = '"
                                + str(RecAttValue)
                                + "' "
                            )                        
                        elif str(RECORD_ID) == "SYOBJR-98795":                            
                            TreeParam = Product.GetGlobal("TreeParam")
                            TreeParentParam = Product.GetGlobal("TreeParentLevel0")
                            contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                            qt_rec_id = Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                                contract_quote_record_id) + "'")
                            Serv_id = SqlHelper.GetFirst("SELECT SERVICE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")    
                            LineAndEquipIDList = TreeParam.split(' - ')
                            
                            if getyears == 1:
                                col_year =  'YEAR_1'
                            elif getyears == 2:
                                col_year =  'YEAR_1,YEAR_2'
                            elif getyears == 3:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3'
                            elif getyears == 4:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                            else:
                                col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'
                            if TreeParam == "Quote Preview":                                
                                Qury_str = (
                                "select top "
                                    + str(PerPage)
                                    + " QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, EQUIPMENT_ID,SERVICE_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",BASE_PRICE,SERIAL_NO, GREENBOOK,FABLOCATION_ID, TOTAL_COST, LINE,TARGET_PRICE_MARGIN, TARGET_PRICE, SALES_DISCOUNT_PRICE, SRVTAXCLA_DESCRIPTION, CEILING_PRICE, SALES_DISCOUNT, TAX_PERCENTAGE,TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from SAQICO (NOLOCK) where QUOTE_ID = '"
                                    + str(qt_rec_id.QUOTE_ID)
                                    + "') m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " and "
                                    + str(Page_End)
                                )
                                QuryCount_str = (
                                        "select count(*) as cnt FROM SAQICO where QUOTE_ID = '{}'".format(
                                            str(qt_rec_id.QUOTE_ID))
                                )
                        elif str(RECORD_ID) == "SYOBJR-91822":
                            contractrecid = Product.GetGlobal("contract_record_id")
                            
                            if Product.GetGlobal("TreeParentLevel1") == "Contract Items": 
                                                    
                                imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                                acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                                TreeParentParam = Product.GetGlobal("TreeParentLevel0")
                                ServiceId = TreeParentParam.split("-")[1].strip()                           
                                Qury_str = (
                                        "SELECT DISTINCT TOP "
                                        + str(PerPage)
                                        + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from CTCICO (nolock)  where "+ str(ATTRIBUTE_VALUE_STR)+" CONTRACT_RECORD_ID ='"+str(RecAttValue)
                                        +"' and GREENBOOK = '"+str(TreeParam)+"' and SERVICE_ID = '"+str(ServiceId)+"') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " AND "
                                        + str(Page_End)
                                    )

                                QuryCount_str = (
                                    "SELECT COUNT(CpqTableEntryId) AS cnt FROM CTCICO (nolock) WHERE "+ str(ATTRIBUTE_VALUE_STR)+" CONTRACT_RECORD_ID = '"
                                        + str(RecAttValue)
                                        + "'and GREENBOOK = '"+str(TreeParam)+"'and SERVICE_ID = '"+str(ServiceId)+"'"
                                )                                
                            else:
                                
                                imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                                acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                                qt_rec_id = SqlHelper.GetFirst("SELECT CONTRACT_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID='" + str(
                                contractrecid) + "'")
                                LineAndEquipIDList = TreeParam.split(' - ')
                                if TreeParentParam == "Contract Items":
                                    Qury_str = (
                                        "select top "
                                            + str(PerPage)
                                            + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where "+ str(ATTRIBUTE_VALUE_STR)+" CONTRACT_ID = '"
                                            + str(qt_rec_id.CONTRACT_ID)
                                            + "' AND SERVICE_ID = '"
                                            + str(LineAndEquipIDList[1])
                                            + "') m where m.ROW BETWEEN "
                                            + str(Page_start)
                                            + " and "
                                            + str(Page_End)
                                    )
                                    QuryCount_str = (
                                            "select count(*) as cnt FROM CTCICO where "+ str(ATTRIBUTE_VALUE_STR)+" SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                                LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                    )
                                else:
                                
                                    Qury_str = (
                                        "select top "
                                            + str(PerPage)
                                            + " * from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where "+ str(ATTRIBUTE_VALUE_STR)+" CONTRACT_ID = '"
                                            + str(qt_rec_id.CONTRACT_ID)
                                            + "' AND SERVICE_ID = '"
                                            + str(LineAndEquipIDList[1])
                                            + "') m where m.ROW BETWEEN "
                                            + str(Page_start)
                                            + " and "
                                            + str(Page_End)
                                    )
                                    QuryCount_str = (
                                            "select count(*) as cnt FROM CTCICO where "+ str(ATTRIBUTE_VALUE_STR)+" SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                                LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                    )  
                        elif str(RECORD_ID) == "SYOBJR-00009":
                            
                            if getyears == 1:
                                col_year =  'YEAR_1'
                            elif getyears == 2:
                                col_year =  'YEAR_1,YEAR_2'
                            elif getyears == 3:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3'
                            elif getyears == 4:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                            else:
                                col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'        
                            if Product.GetGlobal("TreeParentLevel2") == "Quote Items":
                                                              
                                imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                                acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                                exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                                error = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                                partially_priced = '<img title="Partially Priced" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Red1_Circle.svg>'
                                assembly_missing = '<img title="Assembly Missing" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Orange1_Circle.svg>'
                                TreeParentParam = Product.GetGlobal("TreeParentLevel1")
                                
                                try:
                                    if str(TreeParentParam.split("-")[3]):
                                        ServiceId = TreeParentParam.split("-")[-2].strip()
                                except:
                                    ServiceId = TreeParentParam.split("-")[1].strip()                            
                                Qury_str = ("SELECT DISTINCT TOP " + str(PerPage) + " CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '"+ exclamation +"' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,TARGET_PRICE_MARGIN,GREENBOOK,FABLOCATION_ID,TOTAL_COST,TARGET_PRICE,CEILING_PRICE,SALES_DISCOUNT,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,BASE_PRICE,FABLOCATION_RECORD_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,YEAR_1,YEAR_2,BD_DISCOUNT_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,QUOTE_RECORD_ID,MNT_PLANT_RECORD_ID,SALE_DISCOUNT_RECORD_ID,SALESORG_RECORD_ID,SALES_DISCOUNT_PRICE,GREENBOOK_RECORD_ID,QUOTE_CURRENCY_RECORD_ID,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by EQUIPMENT_LINE_ID) AS ROW, * from SAQICO (nolock)  where QUOTE_RECORD_ID ='"+str(RecAttValue) +"' and GREENBOOK = '"+str(TreeParam)+"' and SERVICE_ID = '"+str(ServiceId)+"' and FABLOCATION_ID = '"+str(Product.GetGlobal("TreeParentLevel0"))+"') m where m.ROW BETWEEN " + str(Page_start) + " AND " + str(Page_End) )
                                
                                QuryCount_str = (
                                    "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQICO (nolock) WHERE QUOTE_RECORD_ID = '"
                                        + str(RecAttValue)
                                        + "'and GREENBOOK = '"+str(TreeParam)+"' and SERVICE_ID = '"+str(ServiceId)+"' and FABLOCATION_ID = '"+str(Product.GetGlobal("TreeParentLevel0"))+"' "
                                )    
                            else:
                                imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                                acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                                exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                                error = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg>'
                                partially_priced = '<img title="Partially Priced" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Red1_Circle.svg>'
                                assembly_missing = '<img title="Assembly Missing" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Orange1_Circle.svg>'
                                qt_rec_id = SqlHelper.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                                contract_quote_record_id) + "'")
                                if TreeParam == "Quote Items":
                                    
                                    Qury_str = (
                                        "select top "
                                            + str(PerPage)
                                            + " CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"'  ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, EQUIPMENT_ID,SERVICE_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,"+col_year+",BASE_PRICE,SERIAL_NO, GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE_MARGIN, TARGET_PRICE, SALES_DISCOUNT_PRICE, CEILING_PRICE, SALES_DISCOUNT,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY "+ str(Wh_API_NAMEs)
                                            +") AS ROW, * from SAQICO (NOLOCK) where  QUOTE_ID = '"
                                            + str(qt_rec_id.QUOTE_ID)
                                            + "') m where m.ROW BETWEEN "
                                            + str(Page_start)
                                            + " and "
                                            + str(Page_End)+" ORDER BY "+ str(Wh_API_NAMEs)
                                    )
                                    QuryCount_str = (
                                            "select count(*) as cnt FROM SAQICO where  QUOTE_ID = '{}'".format(
                                                str(qt_rec_id.QUOTE_ID))
                                    )


                                elif TreeParentParam == "Quote Items": 
                                    try:
                                        if str(TreeParam.split("-")[3]):
                                            LineAndEquipIDList = TreeParam.split(' - ')[-2].strip()
                                        else:
                                            LineAndEquipIDList = TreeParam.split(' - ')[1].strip() 
                                    except:
                                        LineAndEquipIDList = TreeParam.split('-')[1].strip()
                                    Qury_str = (
                                        "select top "
                                            + str(PerPage)
                                            + " CASE  WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, SERVICE_ID, EQUIPMENT_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,YEAR_1,BASE_PRICE, SERIAL_NO,GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE, SALES_DISCOUNT_PRICE, TARGET_PRICE_MARGIN, CEILING_PRICE, SALES_DISCOUNT, SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY "+ str(Wh_API_NAMEs)
                                            +") AS ROW, * from SAQICO (NOLOCK) where  QUOTE_ID = '"
                                            + str(qt_rec_id.QUOTE_ID)
                                            + "' AND SERVICE_ID = '"
                                            + str(LineAndEquipIDList)
                                            + "' and LINE_ITEM_ID = '"+str(TreeParam.split(' -')[0])+"') m where m.ROW BETWEEN "
                                            + str(Page_start)
                                            + " and "
                                            + str(Page_End)
                                    )
                                    QuryCount_str = (
                                            "select count(*) as cnt FROM SAQICO where  SERVICE_ID = '"+ str(LineAndEquipIDList) + "' and QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"' and LINE_ITEM_ID = '"+str(TreeParam.split(' -')[0])+"'"
                                    )
                                
                                    
                                elif TreeSuperParentParam == "Quote Items":
                                    
                                    LineAndEquipIDList = TreeParentParam.split('-')[1].strip()
                                    Qury_str = (
                                        "select top "
                                            + str(PerPage)
                                            + " CASE  WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' WHEN PRICING_STATUS = 'ERROR' THEN '"+ error +"' WHEN PRICING_STATUS = 'PARTIALLY PRICED' THEN '"+ partially_priced +"' WHEN PRICING_STATUS = 'ASSEMBLY MISSING' THEN '"+ assembly_missing +"' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS, QUOTE_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, SERVICE_ID, EQUIPMENT_ID,LINE_ITEM_ID,LIST_PRICE,BD_DISCOUNT,BD_PRICE_MARGIN,DISCOUNT,SALES_PRICE,YEAR_OVER_YEAR,YEAR_1,BASE_PRICE, SERIAL_NO,GREENBOOK,FABLOCATION_ID, TOTAL_COST, TARGET_PRICE, SALES_DISCOUNT_PRICE, TARGET_PRICE_MARGIN, CEILING_PRICE, SALES_DISCOUNT, TAX, EXTENDED_PRICE,PRICE_BENCHMARK_TYPE,TOOL_CONFIGURATION,ANNUAL_BENCHMARK_BOOKING_PRICE,CONTRACT_ID,CONVERT(VARCHAR(10),CONTRACT_VALID_FROM,101) AS [CONTRACT_VALID_FROM],CONVERT(VARCHAR(10),CONTRACT_VALID_TO,101) AS [CONTRACT_VALID_TO],BENCHMARKING_THRESHOLD,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY "+ str(Wh_API_NAMEs)
                                            +") AS ROW, * from SAQICO (NOLOCK) where  QUOTE_ID = '"
                                            + str(qt_rec_id.QUOTE_ID)
                                            + "' AND SERVICE_ID = '"
                                            + str(LineAndEquipIDList)
                                            + "' AND FABLOCATION_ID = '"+str(TreeParam)+"' and LINE_ITEM_ID = '"+str(TreeParentParam.split(' -')[0])+"') m where m.ROW BETWEEN "
                                            + str(Page_start)
                                            + " and "
                                            + str(Page_End)
                                    )
                                    QuryCount_str = (
                                            "select count(*) as cnt FROM SAQICO where  SERVICE_ID = '"+ str(LineAndEquipIDList)+"' and FABLOCATION_ID = '"+str(TreeParam)+"'  and QUOTE_ID = '"+ str(qt_rec_id.QUOTE_ID)+ "' and LINE_ITEM_ID = '"+str(TreeParentParam.split(' -')[0])+"'".format(
                                                LineAndEquipIDList[1],str(TreeParam) ,str(qt_rec_id.QUOTE_ID)))

                        elif str(RECORD_ID) == 'SYOBJR-98799':
                            contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                            qt_rec_id = Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")
                            try:
                                quote_id = qt_rec_id.QUOTE_ID
                            except:
                                quote_id = ""
                            Trace.Write("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            Qury_str = (
                                        "select top "
                                            + str(PerPage)
                                            + " CASE WHEN STATUS = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ acquiring_img_str +"' END AS STATUS, QUOTE_DOCUMENT_RECORD_ID, DOCUMENT_ID,DOCUMENT_NAME,LANGUAGE_ID,LANGUAGE_NAME,CPQTABLEENTRYDATEADDED,QUOTE_RECORD_ID,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY STATUS) AS ROW, * from SAQDOC (NOLOCK) where QUOTE_ID = '"
                                            + str(qt_rec_id.QUOTE_ID)
                                            + "') m where m.ROW BETWEEN "
                                            + str(Page_start)
                                            + " and "
                                            + str(Page_End)
                                    )
                            QuryCount_str = (
                                    "select count(*) as cnt FROM SAQDOC where QUOTE_ID = '{}'".format(
                                        str(qt_rec_id.QUOTE_ID))
                            )
                        
                        elif str(RECORD_ID) == "SYOBJR-00015" and str(TreeParentParam) == "Approval Chain Steps":
                            Qury_str = (
                                " SELECT TOP "
                                + str(PerPage)
                                + " * FROM (SELECT ROW_NUMBER() OVER(ORDER BY APPROVAL_TRACKED_FIELD_RECORD_ID) AS ROW,APPROVAL_TRACKED_FIELD_RECORD_ID,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRACKING_TYPE,ACAPTF.CpqTableEntryId FROM ACAPTF (NOLOCK) INNER JOIN ACACST (NOLOCK) ON ACAPTF.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID WHERE ACACST.APRCHN_RECORD_ID = '"
                                + str(RecAttValue)
                                + "' AND ACACST.APRCHNSTP_NAME = '"
                                + str(TreeParam).split(': ')[1]
                                + "' )m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " "
                            )

                            QuryCount_str = (
                                "SELECT COUNT(APPROVAL_TRACKED_FIELD_RECORD_ID) AS cnt FROM ACAPTF (NOLOCK) INNER JOIN ACACST (NOLOCK) ON ACAPTF.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID WHERE ACACST.APRCHN_RECORD_ID = '"
                                + str(RecAttValue)
                                + "' AND ACACST.APRCHNSTP_NAME = '"
                                + str(TreeParam).split(': ')[1]
                                + "' "
                            )    
                        elif str(RECORD_ID) == "SYOBJR-00014":
                            step_name = TreeParam.split(':')[1].strip()
                            Qury_str = (
                                "select top "
                                + str(PerPage)
                                + " * from ( select ROW_NUMBER() OVER( order by APPROVAL_CHAIN_STEP_APPROVER_RECORD_ID) AS ROW,ACACSA.APPROVAL_CHAIN_STEP_APPROVER_RECORD_ID,ACACSA.APRCHN_ID,ACACSA.APRCHNSTP_APPROVER_ID,ACACSA.APPROVER_SELECTION_METHOD,ACACSA.USERNAME,ACACSA.PROFILE_ID,ACACSA.ROLE_ID,ACACSA.NOTIFICATION_ONLY,ACACSA.CpqTableEntryId from ACACSA (nolock) INNER JOIN ACACST (NOLOCK) ON ACACST.APPROVAL_CHAIN_STEP_RECORD_ID = ACACSA.APRCHNSTP_RECORD_ID WHERE  ACACSA."
                                + str(Wh_API_NAME)
                                + " = '"
                                + str(RecAttValue)
                                + "' AND ACACST.APRCHNSTP_NAME = '"
                                + str(step_name)
                                + "') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " AND "
                                + str(Page_End)
                                + ""
                            )
                            QuryCount_str = (
                                "select count(ACACSA.CpqTableEntryId) as cnt from ACACSA (nolock) INNER JOIN ACACST (NOLOCK) ON ACACST.APPROVAL_CHAIN_STEP_RECORD_ID = ACACSA.APRCHNSTP_RECORD_ID WHERE ACACSA."
                                + str(Wh_API_NAME)
                                + " = '"
                                + str(RecAttValue)
                                + "' AND ACACST.APRCHNSTP_NAME = '"
                                + str(step_name)
                                + "'"
                            )    
                        elif str(RECORD_ID) == "SYOBJR-98822":     
                            if Product.GetGlobal("TreeParentLevel1") == "Contract Items":                                
                                imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                                acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                                
                                Qury_str = (
                                        "SELECT DISTINCT TOP "
                                        + str(PerPage)
                                        + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID,EQUIPMENT_LINE_ID,SERVICE_ID,EQUIPMENT_ID,SERIAL_NO,GREENBOOK,TOTAL_COST,LINE_ITEM_ID,DISCOUNT,TAX,EXTENDED_PRICE,EQUIPMENT_RECORD_ID,SERVICE_RECORD_ID,FABLOCATION_RECORD_ID,EQUIPMENTCATEGORY_RECORD_ID,CONTRACT_RECORD_ID,MNT_PLANT_RECORD_ID,SALESORG_RECORD_ID,GREENBOOK_RECORD_ID,CONTRACT_CURRENCY,CONTRACT_CURRENCY_RECORD_ID,CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from CTCICO (nolock)  where CONTRACT_RECORD_ID ='"+str(RecAttValue)
                                        +"' and GREENBOOK = '"+str(TreeParam)+"') m where m.ROW BETWEEN "
                                        + str(Page_start)
                                        + " AND "
                                        + str(Page_End)
                                    )

                                QuryCount_str = (
                                    "SELECT COUNT(CpqTableEntryId) AS cnt FROM CTCICO (nolock) WHERE CONTRACT_RECORD_ID = '"
                                        + str(RecAttValue)
                                        + "'and GREENBOOK = '"+str(TreeParam)+"'"
                                )  
                            else:    
                                imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                                acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                                qt_rec_id = SqlHelper.GetFirst("SELECT CONTRACT_ID, SERVICE_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID ='" + str(
                                contract_quote_record_id) + "'")
                                LineAndEquipIDList = TreeParam.split(' - ')
                                if qt_rec_id.CONTRACT_ID == '70011556':
                                    SERV_DESC = "Z0091"
                                else:
                                    SERV_DESC = qt_rec_id.SERVICE_ID
                                if TreeParentParam == "Contract Items":                                    
                                    Qury_str = (
                                        "select top "
                                            + str(PerPage)
                                            + " CASE WHEN DISCOUNT = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS EQUIPMENT_STATUS, CONTRACT_ITEM_COVERED_OBJECT_RECORD_ID, EQUIPMENT_LINE_ID, SERVICE_ID, EQUIPMENT_ID,LINE_ITEM_ID,DISCOUNT,SERIAL_NO, GREENBOOK, TOTAL_COST, TAX, EXTENDED_PRICE,CpqTableEntryId from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where CONTRACT_ID = '"
                                            + str(qt_rec_id.CONTRACT_ID)
                                            + "' AND SERVICE_ID = '"
                                            + str(LineAndEquipIDList[1])
                                            + "') m where m.ROW BETWEEN "
                                            + str(Page_start)
                                            + " and "
                                            + str(Page_End)
                                    )
                                    QuryCount_str = (
                                            "select count(*) as cnt FROM CTCICO where SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                                LineAndEquipIDList[1], str(qt_rec_id.CONTRACT_ID))
                                    )
                                else:
                                    Qury_str = (
                                        "select top "
                                            + str(PerPage)
                                            + " * from ( select  ROW_NUMBER() OVER( ORDER BY EQUIPMENT_LINE_ID) AS ROW, * from CTCICO (NOLOCK) where CONTRACT_ID = '"
                                            + str(qt_rec_id.CONTRACT_ID)
                                            + "' AND SERVICE_ID = '"
                                            + str(SERV_DESC)
                                            + "') m where m.ROW BETWEEN "
                                            + str(Page_start)
                                            + " and "
                                            + str(Page_End)
                                    )
                                    QuryCount_str = (
                                            "select count(*) as cnt FROM CTCICO where SERVICE_ID = '{}' and CONTRACT_ID = '{}'".format(
                                                SERV_DESC, str(qt_rec_id.CONTRACT_ID))
                                    )
                        elif str(RECORD_ID) == "SYOBJR-98788":
                            Trace.Write("Test1")
                            contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                            qt_rec_id= Sql.GetFirst("SELECT QUOTE_ID FROM SAQTSV WHERE QUOTE_RECORD_ID ='"+str(contract_quote_record_id)+"'")
                            
                            if TreeParentParam:
                                Qustr = "where QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"' and SERVICE_TYPE = '{}'".format(TreeParam)
                            else:
                                Trace.Write("Next")
                                Qustr = "where QUOTE_ID = '"+str(qt_rec_id.QUOTE_ID)+"'"
                            
                            Qury_str = (
                                "select DISTINCT  " 
                                + str(select_obj_str)
                                + ",CpqTableEntryId from ( select  ROW_NUMBER() OVER(order by "
                                + str(Wh_API_NAMEs)
                                + ") AS ROW, * from "
                                + str(ObjectName)
                                + " (nolock) "
                                + str(Qustr)
                                + " ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + ""
                            )                            
                            QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                        elif str(RECORD_ID) == "SYOBJR-98853" and str(TreeParam) == "Tracked Objects":
                            RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_AC_00063").GetValue()
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + " APPROVAL_TRACKED_FIELD_RECORD_ID,APRCHN_ID,APRCHNSTP,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRACKING_TYPE,CpqTableEntryId from (SELECT ROW_NUMBER() OVER(order by APPROVAL_TRACKED_FIELD_RECORD_ID) AS ROW,ACAPTF.APPROVAL_TRACKED_FIELD_RECORD_ID,ACAPTF.APRCHN_ID,ACAPTF.APRCHNSTP,ACAPTF.TRKOBJ_TRACKEDFIELD_LABEL,ACAPTF.TRKOBJ_NAME,ACAPTF.TRACKING_TYPE,ACAPTF.CpqTableEntryId FROM ACAPTF (NOLOCK) INNER JOIN ACAPTX ON ACAPTF.APRCHN_ID = ACAPTX.APRCHN_ID WHERE ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                                + str(RecAttValue)
                                + "') S where S.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " "
                            )
                            QuryCount_str = (
                                "SELECT count(DISTINCT ACAPTF.APPROVAL_TRACKED_FIELD_RECORD_ID) as cnt FROM ACAPTF (NOLOCK) INNER JOIN ACAPTX ON ACAPTF.APRCHN_ID = ACAPTX.APRCHN_ID WHERE ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                                + str(RecAttValue)                                
                                + "' "
                            )
                        elif str(RECORD_ID) == "SYOBJR-00026" and str(TreeParentParam) == "Tracked Objects":
                            RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_AC_00063").GetValue()
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + " APPROVAL_TRACKED_VALUE_RECORD_ID,APRCHN_ID,APRCHNSTP,TRKOBJ_TRACKEDFIELD_LABEL,TRKOBJ_NAME,TRKOBJ_TRACKEDFIELD_OLDVALUE,TRKOBJ_TRACKEDFIELD_NEWVALUE,TRKOBJ_CPQTABLEENTRYID,CpqTableEntryId from (SELECT ROW_NUMBER() OVER(order by APPROVAL_TRACKED_VALUE_RECORD_ID) AS ROW,ACAPFV.TRKOBJ_TRACKEDFIELD_OLDVALUE,ACAPFV.APPROVAL_TRACKED_VALUE_RECORD_ID,ACAPFV.APRCHN_ID,ACAPFV.APRCHNSTP,ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL,ACAPFV.TRKOBJ_NAME,ACAPFV.TRKOBJ_TRACKEDFIELD_NEWVALUE, ACAPFV.CpqTableEntryId,ACAPFV.TRKOBJ_CPQTABLEENTRYID FROM ACAPFV (NOLOCK) INNER JOIN ACAPTX ON ACAPFV.APRCHN_ID = ACAPTX.APRCHN_ID AND ACAPFV.APPROVAL_ID = ACAPTX.APPROVAL_ID WHERE ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                                + str(RecAttValue)
                                + "' AND ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL= '"
                                + str(TreeParam)                            
                                + "') S where S.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + " "
                            )
                            QuryCount_str = (
                                "SELECT count(DISTINCT ACAPFV.APPROVAL_TRACKED_VALUE_RECORD_ID) as cnt FROM ACAPFV (NOLOCK) INNER JOIN ACAPTX ON ACAPFV.APRCHN_ID = ACAPTX.APRCHN_ID WHERE ACAPTX.APPROVAL_TRANSACTION_RECORD_ID = '"
                                + str(RecAttValue)
                                + "' AND ACAPFV.TRKOBJ_TRACKEDFIELD_LABEL= '"
                                + str(TreeParam)                            
                                + "' "
                            )
                        elif str(RECORD_ID) == "SYOBJR-98816":                            
                            contract_quote_record_id = Quote.GetGlobal("contract_record_id")
                            ct_rec_id= SqlHelper.GetFirst("SELECT CONTRACT_ID FROM CTCTSV WHERE CONTRACT_RECORD_ID ='"+str(contract_quote_record_id)+"'")
                            if TreeParentParam:
                                Qustr = "where  CONTRACT_ID = '"+str(ct_rec_id.CONTRACT_ID)+"' and PRODUCT_TYPE = '{}'".format(TreeParam)
                            else:
                                Qustr = "where  CONTRACT_ID = '"+str(ct_rec_id.CONTRACT_ID)+"'"
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + " "
                                + str(select_obj_str)
                                + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                                + str(Wh_API_NAMEs)
                                + ") AS ROW, * from "
                                + str(ObjectName)
                                + " (nolock) "
                                + str(Qustr)
                                + " ) m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + ""
                            )                            
                            QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                        elif RECORD_ID == 'SYOBJR-00006' and TreeParam == "Quote Preview":                            
                            Qury_str = (
                            "SELECT DISTINCT TOP "
                            + str(PerPage)
                            + "QUOTE_ITEM_FORECAST_PART_RECORD_ID,PART_LINE_ID,PART_NUMBER,PART_DESCRIPTION,BASEUOM_ID,SCHEDULE_MODE,DELIVERY_MODE,MATPRIGRP_ID,UNIT_PRICE,EXTENDED_PRICE,ANNUAL_QUANTITY,PRICING_STATUS,CUSTOMER_PART_NUMBER_RECORD_ID,BASEUOM_RECORD_ID,MATPRIGRP_RECORD_ID,QTEITM_RECORD_ID,QUOTE_RECORD_ID,SALESORG_RECORD_ID,SERVICE_RECORD_ID,PART_RECORD_ID,SALESUOM_RECORD_ID,CpqTableEntryId,TAX,TAX_PERCENTAGE,SERVICE_ID,SRVTAXCLA_DESCRIPTION from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQIFP (nolock)  where QUOTE_RECORD_ID ='"+str(RecAttValue)
                            +"') m where m.ROW BETWEEN "
                            + str(Page_start)
                            + " AND "
                            + str(Page_End)+" "
                            )
                            QuryCount_str = (
                                "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQIFP (nolock) WHERE QUOTE_RECORD_ID = '"
                                + str(RecAttValue)
                                + "'"
                            )
                        elif RECORD_ID == 'SYOBJR-00010':    
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            Qury_str = (
                                "SELECT DISTINCT TOP "
                                + str(PerPage)
                                + "QUOTE_ITEM_FORECAST_PART_RECORD_ID, CASE WHEN PRICING_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' WHEN PRICING_STATUS = 'APPROVAL REQUIRED' THEN '" +exclamation+ "' ELSE '"+ acquiring_img_str +"' END AS PRICING_STATUS,SERVICE_ID,PART_LINE_ID,PART_NUMBER,PART_DESCRIPTION,MATPRIGRP_ID,BASEUOM_ID,SCHEDULE_MODE,DELIVERY_MODE,UNIT_PRICE,EXTENDED_PRICE,ANNUAL_QUANTITY,PRICING_STATUS,CUSTOMER_PART_NUMBER_RECORD_ID,BASEUOM_RECORD_ID,MATPRIGRP_RECORD_ID,QTEITM_RECORD_ID,QUOTE_RECORD_ID,SALESORG_RECORD_ID,SERVICE_RECORD_ID,PART_RECORD_ID,SALESUOM_RECORD_ID,CpqTableEntryId,TAX,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE from ( select ROW_NUMBER() OVER(order by "+ str(Wh_API_NAMEs) +") AS ROW, * from SAQIFP (nolock)  where QUOTE_RECORD_ID ='"+str(RecAttValue)
                                +"') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " AND "
                                + str(Page_End)+" ORDER BY PRICING_STATUS ASC"
                            )
                            QuryCount_str = (
                                "SELECT COUNT(CpqTableEntryId) AS cnt FROM SAQIFP (nolock) WHERE QUOTE_RECORD_ID = '"
                                + str(RecAttValue)
                                + "'"
                            )


                            
                            all_acquired = ["ACQUIRING","APPROVAL REQUIRED","ERROR"]
                            all_error = ["APPROVAL REQUIRED","ACQUIRING","ACQUIERD"]
                            all_required = ["ACQUIERD","ACQUIRING","ERROR"]
                            all_acquiring = ["ACQUIERD","ERROR","APPROVAL REQUIRED"]
                            acq_error = ["ACQUIERD","ERROR"]
                            acq_req = ["ACQUIERD","APPROVAL REQUIRED"]
                            not_acq_req = ["ACQUIRING","ERROR"]
                            acq_error_approval = ["ACQUIERD","ERROR","APPROVAL"]
                            not_acq_error = ["ACQUIRING","APPROVAL REQUIRED"]

                            if "ACQUIRED" in price_status and ('ACQUIRING' not in price_status and 'APPROVAL REQUIRED' not in price_status and 'ERROR' not in price_status):
                                icon = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            elif "ERROR" in price_status and ('ACQUIRED' not in price_status and 'APPROVAL REQUIRED' not in price_status and 'ACQUIRING' not in price_status):
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg'
                            elif "APPROVAL REQUIRED" in price_status and ('ACQUIRED' not in price_status and 'ERROR' not in price_status and 'ACQUIRING' not in price_status):
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            elif "ACQUIRING" in price_status and 'ACQUIRED' not in price_status and 'ERROR' not in price_status and 'APPROVAL REQUIRED' not in price_status:
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            elif ("ACQUIRED" in price_status and "ERROR" in price_status) and ('ACQUIRING' not in price_status and 'APPROVAL REQUIRED' not in price_status):
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg'
                            elif ("ACQUIRED" in price_status and 'ERROR' in price_status and 'APPROVAL REQUIRED' in price_status) and "ACQUIRING" not in price_status :
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg'
                            elif ("ACQUIRING" in price_status and 'APPROVAL REQUIRED' in price_status) and ('ACQUIRED' not in price_status and "ERROR" not in price_status) :
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            else:
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg'
                            Trace.Write("dhshjdd"+str(icon))


                        elif RECORD_ID == 'SYOBJR-00008':
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            exclamation = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'

                            if getyears == 1:
                                col_year =  'YEAR_1'
                            elif getyears == 2:
                                col_year =  'YEAR_1,YEAR_2'
                            elif getyears == 3:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3'
                            elif getyears == 4:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                            else:
                                col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'


                            price_status = []
                            # quote_itm_rec = Sql.GetFirst("SELECT QUOTE_ITEM_RECORD_ID FROM SAQITM (NOLOCK) "+str(Qustr)+"")
                            SAQICO_status = Sql.GetList("SELECT DISTINCT PRICING_STATUS FROM SAQICO (NOLOCK) "+str(Qustr)+"")
                            for pricing_status in SAQICO_status:
                                price_status.append(pricing_status.PRICING_STATUS)
                                
                            
                            all_acquired = ["ACQUIRING","APPROVAL REQUIRED","ERROR"]
                            all_error = ["APPROVAL REQUIRED","ACQUIRING","ACQUIERD"]
                            all_required = ["ACQUIERD","ACQUIRING","ERROR"]
                            all_acquiring = ["ACQUIERD","ERROR","APPROVAL REQUIRED"]
                            acq_error = ["ACQUIERD","ERROR"]
                            acq_req = ["ACQUIERD","APPROVAL REQUIRED"]
                            not_acq_req = ["ACQUIRING","ERROR"]
                            acq_error_approval = ["ACQUIERD","ERROR","APPROVAL"]
                            not_acq_error = ["ACQUIRING","APPROVAL REQUIRED"]

                            if "ACQUIRED" in price_status and ('ACQUIRING' not in price_status and 'APPROVAL REQUIRED' not in price_status and 'ERROR' not in price_status):
                                icon = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            elif "ERROR" in price_status and ('ACQUIRED' not in price_status and 'APPROVAL REQUIRED' not in price_status and 'ACQUIRING' not in price_status):
                                icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg'
                            elif "APPROVAL REQUIRED" in price_status and ('ACQUIRED' not in price_status and 'ERROR' not in price_status and 'ACQUIRING' not in price_status):
                                icon = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            elif "ACQUIRING" in price_status and 'ACQUIRED' not in price_status and 'ERROR' not in price_status and 'APPROVAL REQUIRED' not in price_status:
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            elif ("ACQUIRED" in price_status and "ERROR" in price_status) and ('ACQUIRING' not in price_status and 'APPROVAL REQUIRED' not in price_status):
                                icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg'
                            elif ("ACQUIRED" in price_status and "ACQUIRING" in price_status) and ('ERROR' not in price_status and 'APPROVAL REQUIRED' not in price_status):
                                icon = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            elif ("ACQUIRED" in price_status and "APPROVAL REQUIRED" in price_status) and ('ERROR' not in price_status and 'ACQUIRING' not in price_status):
                                icon = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            elif ("ACQUIRED" in price_status and 'ERROR' in price_status and 'APPROVAL REQUIRED' in price_status) and "ACQUIRING" not in price_status :
                                icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg'
                            elif ("ACQUIRING" in price_status and 'APPROVAL REQUIRED' in price_status) and ('ACQUIRED' not in price_status and "ERROR" not in price_status) :
                                icon = '<img title="Approval Required" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/clock_exe.svg>'
                            else:
                                icon = '<img title="Error" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/exclamation_icon.svg'
                           


                            if TreeParam == "Quote Items":                                
                                Qustr = "where QUOTE_RECORD_ID ='"+str(RecAttValue)+"'"
                                Qury_str = (
                                    "select DISTINCT top "
                                    + str(PerPage)
                                    + " '"+ icon +"' AS PO_NOTES, QUOTE_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, OBJECT_QUANTITY,QUANTITY, TOTAL_COST, SALES_DISCOUNT_PRICE,SRVTAXCLA_DESCRIPTION,TAX_PERCENTAGE,TAX, EXTENDED_PRICE, TARGET_PRICE, CEILING_PRICE, BD_PRICE, BD_PRICE_MARGIN, DISCOUNT, SALES_PRICE, YEAR_OVER_YEAR, "+col_year+" "
                                    + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                                    + str(Wh_API_NAMEs)
                                    + ") AS ROW, * from "
                                    + str(ObjectName)
                                    + " (nolock) "
                                    + str(Qustr)
                                    + " ) m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " and "
                                    + str(Page_End)
                                    + ""
                                )
                                QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                        elif RECORD_ID == 'SYOBJR-00024':
                            
                            quote_obj = Sql.GetFirst("select QUOTE_ID,MASTER_TABLE_QUOTE_RECORD_ID from SAQTMT where MASTER_TABLE_QUOTE_RECORD_ID = '{contract_quote_record_id}'".format(contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")))
                            quote_id = quote_obj.QUOTE_ID
                            TreeParam = Product.GetGlobal("TreeParam")
                            
                            if TreeSuperParentParam == 'Approvals':
                                chain_step_name = subTab.split(':')[1].strip()
                                step_id = chain_step_name.split(' ')[1]
                                round_value = TreeParam.split()[1]
                                TreeParam = Product.GetGlobal("TreeParam")
                                Qury_str = ("""select DISTINCT top {PerPage} * from (select ROW_NUMBER() OVER( ORDER BY ACAPTX.APRCHNSTP_ID) AS ROW,ACAPTX.APPROVAL_TRANSACTION_RECORD_ID, ACAPTX.APPROVAL_ID,ACAPTX.APRCHNSTP_ID,ACAPTX.APRCHNSTP_APPROVER_ID,ACAPTX.APPROVAL_ROUND,ACAPTX.APPROVALSTATUS,ACAPTX.RECIPIENT_COMMENTS,ACAPTX.APRCHNSTP_RECORD_ID,ACAPTX.APPROVAL_RECIPIENT,ACAPTX.CpqTableEntryId FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID and ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHNSTP_ID = '{chain_step_name}' and ACAPTX.APRCHN_ID = '{chain_id}' and ACAPTX.APPROVAL_ROUND = '{step_value}')m where m.ROW BETWEEN """.format(PerPage = PerPage,contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id, chain_step_name = step_id,chain_id = TreeParentParam,step_value = round_value ) + str(Page_start) + " and " + str(Page_End))
                                QuryCount_str = """select count(ACAPTX.CpqTableEntryId) as cnt FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID and  ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHNSTP_ID = '{chain_step_name}' and ACAPTX.APRCHN_ID = '{chain_id}' and ACAPTX.APPROVAL_ROUND = '{step_value}' """.format(contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id,chain_step_name = step_id,chain_id =  TreeParentParam,step_value = round_value)
                            else:
                               
                                Qury_str = ("""select DISTINCT top {PerPage} * from (select ROW_NUMBER() OVER( ORDER BY {Wh_API_NAMEs}) AS ROW,ACAPTX.APPROVAL_TRANSACTION_RECORD_ID, ACAPTX.APPROVAL_ID,ACAPTX.APRCHNSTP_ID,ACAPTX.APRCHNSTP_APPROVER_ID,ACAPTX.APPROVAL_ROUND,ACAPTX.APPROVALSTATUS,ACAPTX.RECIPIENT_COMMENTS,ACAPTX.APRCHNSTP_RECORD_ID,ACAPTX.APPROVAL_RECIPIENT,ACAPTX.CpqTableEntryId FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID  and ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHN_ID = '{Chain}')m where m.ROW BETWEEN """.format(PerPage = PerPage,contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id,Chain = TreeParam,Wh_API_NAMEs = Wh_API_NAMEs ) + str(Page_start) + " and " + str(Page_End))
                                QuryCount_str = """select count(ACAPTX.CpqTableEntryId) as cnt FROM ACAPTX (nolock) inner join ACACST (nolock) on ACAPTX.APRCHNSTP_RECORD_ID = ACACST.APPROVAL_CHAIN_STEP_RECORD_ID and  ACAPTX.APRTRXOBJ_ID = '{Quote_id}' and ACAPTX.APRCHNSTPTRX_ID like '%{Quote_id}%' and ACAPTX.APRCHN_ID = '{Chain}' """.format(contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id"),Quote_id = quote_id,Chain = TreeParam)
                        elif RECORD_ID == 'SYOBJR-98841':
                            imgstr = '<img title="Acquired" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Green_Tick.svg>'
                            acquiring_img_str = '<img title="Acquiring" src=/mt/APPLIEDMATERIALS_TST/Additionalfiles/Cloud_Icon.svg>'
                            
                            if TreeParam == "Contract Items":                                
                                Qury_str = (
                                    "select DISTINCT top "
                                    + str(PerPage)
                                    + "  CASE WHEN ITEM_STATUS = 'ACQUIRED' THEN '"+ imgstr +"' ELSE '"+ imgstr +"' END AS PO_NOTES, CONTRACT_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, QUANTITY, TAX, DISCOUNT, EXTENDED_PRICE"
                                    + ",CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                                    + str(Wh_API_NAMEs)
                                    + ") AS ROW, * from "
                                    + str(ObjectName)
                                    + " (nolock) "
                                    + str(Qustr)
                                    + " ) m where m.ROW BETWEEN "
                                    + str(Page_start)
                                    + " and "
                                    + str(Page_End)
                                    + ""
                                )
                                QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                        ##involved parties equipmemt and tool equipment matrix starts
                        elif (str(RECORD_ID) == "SYOBJR-98858" or str(RECORD_ID) == "SYOBJR-00028") and str(TreeParam) == "Quote Information":
                            account_id = Product.GetGlobal("stp_account_id")
                            
                            Qury_str = ("""select DISTINCT top {PerPage} * from (select ROW_NUMBER() OVER( ORDER BY SAQSTE.{Wh_API_NAMEs}) AS ROW,SAQSTE.* from SAQSTE  inner join SAQSCF(nolock)  on SAQSTE.QUOTE_RECORD_ID = SAQSCF.QUOTE_RECORD_ID and SAQSTE.SRCFBL_ID = SAQSCF.SRCFBL_ID where SAQSTE.QUOTE_RECORD_ID = '{contract_quote_record_id}' and SAQSTE.SRCACC_ID = '{account_id}')m where m.ROW BETWEEN """.format(PerPage = PerPage,account_id = account_id,
                            contract_quote_record_id = str(RecAttValue), Wh_API_NAMEs= str(Wh_API_NAMEs))+ str(Page_start) + " and " + str(Page_End))
                            
                            
                            
                            QuryCount_str = "select count(SAQSTE.CpqTableEntryId) as cnt from SAQSTE  inner join SAQSCF(nolock) on SAQSTE.QUOTE_RECORD_ID = SAQSCF.QUOTE_RECORD_ID and SAQSTE.SRCFBL_ID= SAQSCF.SRCFBL_ID where SAQSTE.QUOTE_RECORD_ID = '{contract_quote_record_id}' and SAQSTE.SRCACC_ID = '{account_id}'".format(account_id = account_id,contract_quote_record_id=str(RecAttValue))
                        ##involved parties equipmemt ends
                        elif RECORD_ID == 'SYOBJR-98792' and str(TreeParam) == "Quote Preview":
                            
                            contract_quote_record_id = Quote.GetGlobal("contract_quote_record_id")
                            Qustr_id = Sql.GetFirst("SELECT QUOTE_ID FROM SAQITM WHERE QUOTE_RECORD_ID ='" + str(
                            contract_quote_record_id) + "'")
                            if getyears == 1:
                                col_year =  'YEAR_1'
                            elif getyears == 2:
                                col_year =  'YEAR_1,YEAR_2'
                            elif getyears == 3:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3'
                            elif getyears == 4:
                                col_year =  'YEAR_1,YEAR_2,YEAR_3,YEAR_4'
                            else:
                                col_year = 'YEAR_1,YEAR_2,YEAR_3,YEAR_4,YEAR_5'
                            if TreeParam:
                                Qustr = "where QUOTE_ID = '"+str(Qustr_id.QUOTE_ID)+"'"
                            Qury_str = (
                                "select DISTINCT top "
                                + str(PerPage)
                                + " QUOTE_ITEM_RECORD_ID, LINE_ITEM_ID, SERVICE_ID, SERVICE_DESCRIPTION, ONSITE_PURCHASE_COMMIT, OBJECT_QUANTITY, TOTAL_COST, SALES_DISCOUNT_PRICE, TAX, EXTENDED_PRICE, QUANTITY, TARGET_PRICE, CEILING_PRICE, BD_PRICE, BD_PRICE_MARGIN, DISCOUNT, SALES_PRICE, YEAR_OVER_YEAR, "+col_year+", SRVTAXCLA_DESCRIPTION, TAX_PERCENTAGE, CpqTableEntryId from ( select TOP 10 ROW_NUMBER() OVER(order by "
                                + str(Wh_API_NAMEs)
                                + ") AS ROW, * from "
                                + str(ObjectName)
                                + " (nolock) "
                                + str(Qustr)
                                + " AND SERVICE_ID NOT LIKE '%BUNDLE%') m where m.ROW BETWEEN "
                                + str(Page_start)
                                + " and "
                                + str(Page_End)
                                + ""
                            )
                            QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)+ " AND SERVICE_ID NOT LIKE '%BUNDLE%' "

                        elif str(RECORD_ID) == "SYOBJR-98815":                            
                            splitTP = TP.split('-')
                            TP = splitTP[1]
                            Qustr = "where SALESORG_ID = '"+str(TP)+"' and SORG_CURRENCY='"+str(PR_CURR)+"'"
                        elif str(RECORD_ID) == "SYOBJR-98862":
                            RecAttValue=Product.Attributes.GetByName("QSTN_SYSEFL_SY_00125").GetValue()
                            Qustr = " WHERE "+str(ATTRIBUTE_VALUE_STR)+" APP_ID = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        elif str(RECORD_ID) == "SYOBJR-98863":
                            RecAttValue=Product.Attributes.GetByName("QSTN_SYSEFL_SY_00125").GetValue()
                            Qustr = " WHERE "+str(ATTRIBUTE_VALUE_STR) +" TAB_ID = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        elif str(RECORD_ID) == "SYOBJR-93123":
                            RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                            Qustr = " WHERE "+str(ATTRIBUTE_VALUE_STR) +" SECTION_NAME = '"+str(TreeParentParam)+"' AND PROFILE_ID ='"+str(RecAttValue)+"' AND OBJECT_NAME = '"+str(ObjectName)+"' "
                        elif str(RECORD_ID) == "SYOBJR-98864":
                            Qustr = " WHERE "+str(ATTRIBUTE_VALUE_STR) +" TAB_NAME = '"+str(TreeParentParam)+"' AND PROFILE_RECORD_ID ='"+str(RecAttValue)+"'"
                        elif str(RECORD_ID) == "SYOBJR-95824" or (str(RECORD_ID) == "SYOBJR-95825" and str(TreeParam)=="Constraints") or str(RECORD_ID) == "SYOBJR-95826" or str(RECORD_ID) == "SYOBJR-95976":
                            RecAttValue = productAttributesGetByName("QSTN_SYSEFL_SY_00701").GetValue()
                            Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                        elif str(RECORD_ID) == "SYOBJR-95825" and str(TreeParentParam) == 'Constraints':
                            RecAttValue = productAttributesGetByName("QSTN_SYSEFL_SY_00701").GetValue()
                            Qustr = "WHERE CONSTRAINT_TYPE = '"+str(TreeParam)+"' AND OBJECT_RECORD_ID='"+str(RecAttValue)+"'"
                        elif str(RECORD_ID) == "SYOBJR-95840": 
                            Wh_API_NAMEs = "PAGEACTION_RECORD_ID"                
                            RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00723").GetValue()       
                            Qustr =  " where SCRIPT_RECORD_ID = '" + str(RecAttValue) + "'"
                        elif str(RECORD_ID) == "SYOBJR-95890": 
                            RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_03295").GetValue()
                            Qustr = " where "+str(ATTRIBUTE_VALUE_STR)+" "+ str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                        elif str(RECORD_ID) == "SYOBJR-93188":
                            Trace.Write('SYOBJR-93188@66666')
                            RecAttValue = Product.Attributes.GetByName("QSTN_SYSEFL_SY_00128").GetValue()
                            GetAppname_query = ""
                            Qustr = " WHERE TAB_NAME = '"+str(TreeParentParam)+"' AND PROFILE_ID ='"+str(RecAttValue)+"'" 
                        elif str(RECORD_ID)== "SYOBJR-98857":
                            Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"   
                            if "SRCFBL_ID" in Wh_API_NAMEs:
                                Wh_API_NAMEs=Wh_API_NAMEs.replace("SRCFBL_ID", "CAST(SRCFBL_ID AS int)")
                                Trace.Write("sort param 3  "+str(Wh_API_NAMEs))
                        elif  str(RECORD_ID) == "SYOBJR-98789" and "Sending Account -" in TreeParam :
                            Qustr += " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "' AND RELOCATION_FAB_TYPE = 'SENDING FAB'"
                        elif  str(RECORD_ID) == "SYOBJR-98789" and "Receiving Account -" in TreeParam :
                            Qustr += " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "' AND RELOCATION_FAB_TYPE = 'RECEIVING FAB'"   
                        else:
                            Qustr = " where " + str(Wh_API_NAME) + " = '" + str(RecAttValue) + "'"
                            Trace.Write("7100"+str(Qustr))
                
                if str(Qury_str) == "" and str(QuryCount_str) == "": 
                    Trace.Write("7105")
                         
                    select_obj_str = select_obj_str.replace("DEFAULT","[DEFAULT]")
                    Qury_str = (
                        "select top "
                        + str(PerPage)
                        + " "
                        + str(select_obj_str)
                        + ",CpqTableEntryId from ( select ROW_NUMBER() OVER(order by "
                        + str(Wh_API_NAMEs)
                        + ") AS ROW, * from "
                        + str(ObjectName)
                        + " (nolock) "
                        + str(Qustr)
                        + " ) m where m.ROW BETWEEN "
                        + str(Page_start)
                        + " and "
                        + str(Page_End)
                        + ""
                    )
                    QuryCount_str = "select count(*) as cnt from " + str(ObjectName) + " (nolock) " + str(Qustr)
                    
                try:
                    Query_Obj = Sql.GetList(Qury_str)
                    Query_CountObj = Sql.GetFirst(QuryCount_str)
                   
                except:
                                    
                    Query_Obj = Sql.GetList(
                        "select top "
                        + str(PerPage)
                        + "  "
                        + str(obj_str)
                        + ",CpqTableEntryId from "
                        + str(ObjectName)
                        + " (nolock) where 1=1"
                    )
                    
                    QuryCount_str = (
                        "select count(" + str(Wh_API_NAME) + ") as cnt from " + str(ObjectName) + " (nolock) where 1=1"
                    )
                    Query_CountObj = Sql.GetFirst(QuryCount_str)                    
                if Query_CountObj is not None:
                    QueryCount = Query_CountObj.cnt
            OBJ_CpqTableEntryId_New = ""
        
            for ik in Query_Obj:
                if str(ObjectName) == "USERS":
                    useridval = ik.ID                    
                primary_view = ""
                product_id = ""
                product_name = ""
                other_tab = ""
                product_id_val = ""                
                module_txt = ""
                tab_val = ""
                try:
                    OBJ_CpqTableEntryId_New = str(ik.CpqTableEntryId)
                except:
                    pass
                Action_str = '<div class="btn-group dropdown"><div class="dropdown" id="ctr_drop"><i data-toggle="dropdown" id="dropdownMenuButton" class="fa fa-sort-desc dropdown-toggle" aria-expanded="false"></i><ul class="dropdown-menu left" aria-labelledby="dropdownMenuButton">'
                for inm in ik:
                   
                    value123 = str(inm).split(",")[0].replace("[", "").lstrip()
                    value1234 = str(inm).split(",")[1].replace("]", "").lstrip()
                    
                    if (
                        str(obj_obj.SAPCPQ_ATTRIBUTE_NAME) == "SYOBJR-30114"
                        or str(obj_obj.SAPCPQ_ATTRIBUTE_NAME) == "SYOBJR-60052"
                        or str(obj_obj.SAPCPQ_ATTRIBUTE_NAME) == "SYOBJR-70085"
                    ):
                        if value123 == objRecName:
                            other_tab = "0"
                            primary_view = value1234                    
                    else:
                        if value123 == objRecName:
                            tab_obj1 = Sql.GetFirst(
                                "SELECT PG.TAB_NAME,PG.TAB_RECORD_ID FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE SE.PRIMARY_OBJECT_NAME='"
                                + str(ObjectName)
                                + "' and SE.SECTION_NAME ='BASIC INFORMATION'"
                            )
                            if tab_obj1 is not None:
                                tab_val = str(tab_obj1.TAB_NAME)
                                if tab_val in list_of_tabs:
                                    primary_view = value1234 + "|" + tab_val
                                else:
                                    product_name = Sql.GetFirst(
                                        "select APP_LABEL from SYTABS (nolock) where RECORD_ID='"
                                        + str(tab_obj1.TAB_RECORD_ID)
                                        + "'"
                                    )
                                    if product_name is not None:
                                        module_txt = str(product_name.APP_LABEL).strip()
                                        product_id = Sql.GetFirst(
                                            "select PRODUCT_ID from products (nolock) where PRODUCT_NAME='"
                                            + str(module_txt)
                                            + "'"
                                        )
                                    if product_id != "" and product_id is not None:
                                        primary_view = value1234 + "|" + tab_val
                                        product_id_val = str(product_id.PRODUCT_ID)
                                        other_tab = "1"
                                    else:
                                        primary_view = ""

                if str(current_tab).upper() == "PROFILE" and (ObjectName == "SYPROF"):
                    Action_str += '<li><a class="dropdown-item" href="#" onclick="profileObjSet(this)" data-target="#viewProfileRelatedList" data-toggle="modal">VIEW<a><li>'
                elif str(current_tab).upper() == "PROFILE" and (ObjectName != "SYPROD"):                    
                    Action_str += '<li><a class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)">VIEW<a><li><li><a class="dropdown-item" href="#" onclick="Commontree_edit_RL(this)">EDIT</a></li>'

                elif str(current_tab).upper() == "ROLE":                    
                    Action_str += '<li><a class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)">VIEW<a><li>'  
                else:
                    Trace.Write('ObjectName--7353----'+str(ObjectName))                  
                    if ObjectName != "SAQIBP" :
                        Action_str += '<li><a class="dropdown-item" href="#" onclick="Commonteree_view_RL(this)">VIEW</a></li>'


                if str(Action_permission.get("Delete")).upper() == "TRUE":
                    Action_str += '<li><a class="dropdown-item" data-target="#cont_viewModalDelete" data-toggle="modal" onclick="cont_delete(this)" href="#">DELETE</a></li>'

                Action_str += "</ul></div></div>"
                new_dict = {}
                seg_pric = {}
                ids = {}
                product_id = ""
                product_name = ""
                lookup_rl_popup = []
                pop_val = {}
                editvalue = {}
                primary = ""
                red_color = ""
                decimal_place = 3
                list_lineup = []
                current_rec_id = ""
                for inm in ik:
                    value123 = str(inm).split(",")[0].replace("[", "").lstrip()
                    value1234 = str(inm).split(",")[1].replace("]", "").lstrip()
                    if value123 == objRecName:
                        #current_rec_id = ""
                        current_rec_id = value1234
                        
                    curr_symbol = ""
                    cur_api_name=None
                    data_type_val = ""
                    formu_data_type_val = ""
                    if cur_api_name is not None:
                        data_type_val = cur_api_name.DATA_TYPE
                        formu_data_type_val = cur_api_name.FORMULA_DATA_TYPE
                    if str(cur_api_name) is not None and (
                        str(data_type_val) == "CURRENCY" or str(formu_data_type_val) == "CURRENCY"
                    ):
                        
                        cur_api_name_obj = Sql.GetFirst(
                            "select CURRENCY_INDEX from  SYOBJD (nolock) where API_NAME = '"
                            + str(value123)
                            + "' and OBJECT_NAME = '"
                            + str(ObjectName)
                            + "' "
                        )
                        
                        if str(ObjectName) == "SAQIBP":
                            contract_quote_record_id = Product.GetGlobal("contract_quote_record_id")
                            curr_symbol_obj = Sql.GetFirst(
                                "select SYMBOL,CURRENCY,DISPLAY_DECIMAL_PLACES from PRCURR (nolock) where CURRENCY_RECORD_ID = (select "
                                + str(cur_api_name_obj.CURRENCY_INDEX)
                                + " from SAQTMT"
                                + " where MASTER_TABLE_QUOTE_RECORD_ID  "
                                + " = '"
                                + str(contract_quote_record_id)
                                + "' ) "
                            )
                        else:
                            curr_symbol_obj = Sql.GetFirst(
                                "select SYMBOL,CURRENCY,DISPLAY_DECIMAL_PLACES from PRCURR (nolock) where CURRENCY_RECORD_ID = (select "
                                + str(cur_api_name_obj.CURRENCY_INDEX)
                                + " from "
                                + str(ObjectName)
                                + " where  "
                                + str(objRecName)
                                + " = '"
                                + str(current_rec_id)
                                + "' ) "
                            )
                        if curr_symbol_obj is not None:
                            curr_symbol = curr_symbol_obj.CURRENCY
                            decimal_place = curr_symbol_obj.DISPLAY_DECIMAL_PLACES
                        if value1234 is not None:
                            if value1234 != "":
                                my_format = "{:,." + str(decimal_place) + "f}"                                
                                value1234 = str(my_format.format(round(float(value1234), int(decimal_place))))
                                if str(value123) == "ANNUAL_BILLING_AMOUNT" and str(ObjectName) == "SAQIBP":
                                    value1234 = value1234
                                else:
                                    value1234 = value1234 + " " + curr_symbol

                    if str(cur_api_name) is not None and (
                        str(data_type_val) == "PERCENT" or str(formu_data_type_val) == "PERCENT"
                    ):
                        decimal_place = 3
                        percentSymbol = "%"
                       
                        if value1234 is not None and value1234 != '':
                            my_format = "{:." + str(decimal_place) + "f}"
                            value1234 = str(my_format.format(round(float(value1234), int(decimal_place)))) + " %"
                    if value123 in lookup_disply_list:
                        for key, value in lookup_list.items():
                            if value == value123:
                                lookup_val = ""
                                lookup_obj = Sql.GetFirst(
                                    "SELECT LOOKUP_OBJECT FROM  SYOBJD (nolock) WHERE OBJECT_NAME = '"
                                    + str(ObjectName)
                                    + "' AND LOOKUP_API_NAME ='"
                                    + str(key)
                                    + "' AND DATA_TYPE = 'LOOKUP'"
                                )
                                if lookup_obj is not None:
                                    lookup_val = str(lookup_obj.LOOKUP_OBJECT)
                                tab_obj = Sql.GetFirst(
                                    "SELECT PG.TAB_NAME,PG.TAB_RECORD_ID FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE SE.PRIMARY_OBJECT_NAME='"
                                    + str(lookup_val)
                                    + "' and SE.SECTION_NAME ='BASIC INFORMATION'"
                                )
                                if tab_obj is not None:
                                    tab_val = str(tab_obj.TAB_NAME)
                                    if tab_val in list_of_tabs:
                                        ids[key] = value1234 + "|" + tab_val
                                        
                                    else:
                                        product_name = Sql.GetFirst(
                                            "select APP_LABEL from SYTABS (nolock) where RECORD_ID='"
                                            + str(tab_obj.TAB_RECORD_ID)
                                            + "'"
                                        )
                                        if product_name is not None:
                                            module_txt = str(product_name.APP_LABEL).strip()
                                            product_id = Sql.GetFirst(
                                                "select PRODUCT_ID from products (nolock) where PRODUCT_NAME='"
                                                + str(module_txt)
                                                + "'"
                                            )
                                        if product_id != "" and product_id is not None:
                                            pop_val[key] = value1234 + "|" + tab_val + "," + str(product_id.PRODUCT_ID)
                                        else:
                                            lookup_obj = Sql.GetFirst(
                                                "SELECT LOOKUP_OBJECT FROM  SYOBJD (nolock) WHERE OBJECT_NAME = '"
                                                + str(ObjectName)
                                                + "' AND LOOKUP_API_NAME ='"
                                                + str(key)
                                                + "' AND DATA_TYPE = 'LOOKUP'"
                                            )
                                            lookup_val = str(lookup_obj.LOOKUP_OBJECT)
                                            pop_val[key] = value1234 + "|" + lookup_val
                                else:
                                    lookup_obj = Sql.GetFirst(
                                        "SELECT LOOKUP_OBJECT FROM  SYOBJD (nolock) WHERE OBJECT_NAME = '"
                                        + str(ObjectName)
                                        + "' AND LOOKUP_API_NAME ='"
                                        + str(key)
                                        + "' AND DATA_TYPE = 'LOOKUP'"
                                    )
                                    lookup_val = str(lookup_obj.LOOKUP_OBJECT)
                                    pop_val[key] = value1234 + "|" + lookup_val
                    elif value123 == objRecName:
                        key_value = str(value1234)
                        if str(ObjectName) == "USERS":                            
                            value1234 = str(ObjectName) + "-" + str(key_value).rjust(6, "0")
                        elif str(ObjectName) == 'SAQDOC' and key_value == 'Pending':
                            value1234 = 'Pending'
                        else:
                            value1234 = str(ObjectName) + "-" + str(OBJ_CpqTableEntryId_New).rjust(6, "0")
                            
                        tab_obj1 = Sql.GetFirst(
                            "SELECT PG.TAB_NAME,PG.TAB_RECORD_ID FROM SYSECT (nolock) SE INNER JOIN SYPAGE (nolock) PG on SE.PAGE_RECORD_ID = PG.RECORD_ID WHERE SE.PRIMARY_OBJECT_NAME='"
                            + str(ObjectName)
                            + "' and SE.SECTION_NAME ='BASIC INFORMATION'"
                        )
                        if tab_obj1 is not None and ObjectName != "PASACS":
                            tab_val = str(tab_obj1.TAB_NAME)
                            if tab_val in list_of_tabs:
                                primary = value1234 + "|" + tab_val 
                                                          
                                new_dict[value123] = (
                                    '<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>"
                                )                                
                            else:
                                product_name = Sql.GetFirst(
                                    "select APP_LABEL from SYTABS (NOLOCK) where RECORD_ID='"
                                    + str(tab_obj1.TAB_RECORD_ID)
                                    + "'"
                                )
                                if product_name is not None:
                                    module_txt = str(product_name.APP_LABEL).strip()
                                    product_id = Sql.GetFirst(
                                        "select PRODUCT_ID from products (NOLOCK) where PRODUCT_NAME='"
                                        + str(module_txt)
                                        + "'"
                                    )
                                if product_id != "" and product_id is not None:                                    
                                    primary = value1234 + "|" + tab_val + "," + str(product_id.PRODUCT_ID)
                                    value1234 = value1234.replace('"', "&quot;")
                                    value1234 = value1234.replace("<p>", " ")
                                    value1234 = value1234.replace("</p>", " ")                                                                     
                                    new_dict[value123] = (
                                        '<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>"
                                    )
                                else:                                                                                                                                             
                                    new_dict[value123] = (
                                        '<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>"
                                    )
                    if value1234.startswith("<img"):
                        # value1234 = value1234.replace('"', "&quot;")
                        value1234 = value1234.replace("<p>", " ")
                        value1234 = value1234.replace("</p>", " ")
                        imgValue = value1234
                        value1234 = value1234.split('"')
                        
                        value1234 = value1234[1]
                    else:                 
                        Trace.Write('at 7306')
                        img_list = ['PO_NOTES','PRICING_STATUS','EQUIPMENT_STATUS']
                        if str(ObjectName) == "SAQIFP":
                            img_list.append('PRICING_STATUS')     
                        if value123 in img_list:
                            
                            new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + imgValue + "</abbr>")
                        # if str(ObjectName) == "SAQIFP":
                        #     image_list = ['SERVICE_ID']
                        #     Trace.Write("cm to obj----")    
                        #     if value123 in image_list:
                        #         Trace.Write("COMING HE"+str(imgValue))
                        #         new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + imgValue + "</abbr>")    
                        else:                         
                                    
                            new_dict[value123] = (
                                '<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>"
                            )
                
                    if value123 in edit_field:                      
                        value1234 = value1234.replace('"', "&quot;")
                        value1234 = value1234.replace("<p>", " ")
                        value1234 = value1234.replace("</p>", " ")                        
                        new_dict[value123] = (
                            '<abbr id ="' + value1234 + '" title="' + value1234 + '">' + value1234 + "</abbr>"
                        )                        

                    else:               
                        if value123 in checkbox_list:
                            new_dict[value123] = value1234
                        else:
                            if (value123 == "SET_NAME" or value123 == "SETMAT_NAME") and (
                                RECORD_ID == "SYOBJR-90016" or RECORD_ID == "SYOBJR-30101"
                            ):
                                new_dict[value123] = (
                                    "<a id='"
                                    + str(primary_view)
                                    + "' onclick='Move_to_parent_obj(this)'>"
                                    + value1234
                                    + "</a>"
                                )
                            else:
                                value1234 = value1234.replace('"', "&quot;")
                                value1234 = value1234.replace("<p>", " ")
                                value1234 = value1234.replace("</p>", " ")

                                if value123 in [
                                    "ERROR",
                                    "MINIMUM_PRICE",
                                    "CATCLC_PRICE_INSORG_CURR",
                                    "INVCLC_UNITPRICE_INSORG_CURR",
                                ]:
                                    new_dict[value123] = value1234
                                    seg_pric[value123] = value1234.replace(curr_symbol, "").replace(" ", "")
                                    seg_pric["PRICE_FACTOR"] = PriceFactor
                                else:                                    
                                    if str(TreeParentParam).upper() == "BRIDGE PRODUCTS" and  str(RECORD_ID) == "SYOBJR-00005" and str(value123) in ['SCHEDULE_MODE','CUSTOMER_ANNUAL_QUANTITY']:
                                        new_dict[value123] = (
                                            '<input id ="' + key_value + '"   value="' + value1234 + '" style="border: 0px solid;" disabled>' + value1234 + "</input>"
                                        )
                                    
                                    else:
                                        
                                        #valueGUID = CPQID.KeyCPQId.GetKEYId(str(ObjectName), str(value1234))
                                       
                                        if str(value123) != "CUSTOMER_ANNUAL_QUANTITY":                                                
                                                precentage_columns = ['SALES_DISCOUNT','BD_DISCOUNT']
                                                if value123 in precentage_columns:
                                                    # perc = Sql.GetList("SELECT DISCOUNT FROM SAQICO WHERE "+str(value123)+" = '"+str(value1234)+"'")
                                                    
                                                    #value1234 = "0.25000"
                                                    string_val = str(value1234)
                                                    #string_val = string_val.replace('0','')
                                                    string_val1 = string_val.split('.')
                                                    str_val = string_val1[0]
                                                    value1234 = str_val
                                                    if value1234 is not None and value1234 != '':
                                                        new_dict[value123] = (
                                                            '<abbr id ="' + key_value + '" title="' + value1234 +'">' + value1234 +  ' %' +  "</abbr>"
                                                        )
                                                    else:
                                                        new_dict[value123] = (
                                                        '<abbr id ="' + key_value + '" title="' + value1234 + '">' + value1234 + "</abbr>"
                                                    )    
                                                else:
                                                    img_list = ['PO_NOTES','PRICING_STATUS','EQUIPMENT_STATUS','STATUS']
                                                    if str(ObjectName) == "SAQIFP":
                                                        img_list.append('PRICING_STATUS')
                                                    if value123 in img_list:
                                                       
                                                        new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + imgValue + "</abbr>")
                                                    # if str(ObjectName) == "SAQIFP":
                                                    #     image_list = ['SERVICE_ID']
                                                      
                                                    #     if value123 in image_list:
                                                
                                                    #         new_dict[value123] = ('<abbr id ="' + key_value + '" title="' + value1234 + '">' + imgValue + "</abbr>")    
                                                    else:    
                                                        new_dict[value123] = value1234                                                        

                    new_dict["ACTIONS"] = Action_str       
                    new_dict["ids"] = ids
                    new_dict["seg_pric"] = seg_pric
                    new_dict["pop_val"] = pop_val
                    new_dict["primary"] = primary
                table_list.append(new_dict)
                footer_str, footer = "", ""
                footer_tot = ""
                
                if ObjectName == "SAQIBP":
                    ContractRecordId = Product.GetGlobal("contract_quote_record_id")
                    gettotaldateamt = Sql.GetList("SELECT BILLING_AMOUNT=SUM(BILLING_AMOUNT),ANNUAL_BILLING_AMOUNT = SUM(ANNUAL_BILLING_AMOUNT),BILLING_DATE FROM SAQIBP WHERE BILLING_DATE in {billing_date_column} and QUOTE_RECORD_ID ='{cq}' group by BILLING_DATE ".format(cq=str(ContractRecordId),billing_date_column=str(tuple(billing_date_column))))
                    if gettotaldateamt:
                        my_format = "{:,." + str(decimal_place) + "f}"
                        for val in gettotaldateamt: 
                            gettotalamt = str(my_format.format(round(float(val.ANNUAL_BILLING_AMOUNT), int(decimal_place))))  
                            
                    if gettotaldateamt:
                        my_format = "{:,." + str(decimal_place) + "f}"
                        footer_tot += '<th colspan="1" class="text-left">{}</th>'.format(curr_symbol)
                        footer_tot += '<th colspan="1" class="text-right">{}</th>'.format(gettotalamt)
                        for val in gettotaldateamt:
                            getamt = str(my_format.format(round(float(val.BILLING_AMOUNT), int(decimal_place))))
                            footer_tot += '<th class="text-right">{}</th>'.format(getamt)
                    
                    
                for key, col_name in enumerate(list(eval(Columns))):                    
                    if ObjectName == 'SAQIBP' and (col_name in billing_date_column or col_name == 'QUOTE_CURRENCY'):                        
                        try:                            
                            if col_name in billing_date_column:                                                
                                my_format = "{:,." + str(decimal_place) + "f}"
                                tovalue = 0.00
                                getamt = ""                        
                                #footer += '<th>{}{}</th>'.format(my_format.(sum([float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0].split(" ")[0].replace(",","")) for data in table_list])) ,curr_symbol)
                                for data in table_list:                                    
                                    tovalue += float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0].replace(",",""))
                                    getamt = str(my_format.format(round(float(tovalue), int(decimal_place))))                               
                                footer += '<th class="text-right">{}</th>'.format(getamt)
                            
                            else:
                                if table_list:
                                    currency_obj = re.search(r'>(.+?)<', table_list[0].get(col_name))
                                    if currency_obj:
                                        footer += '<th colspan="2" class="text-left">{}</th>'.format(currency_obj.group(1))
                                    else:
                                        footer += '<th colspan="2" class="text-left"></th>'
                            #footer += '<th>{}{}</th>'.format(sum([float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0].split(" ")[0].replace(",","")) for data in table_list]),curr_symbol)
                            #footer += '<th>{}</th>'.format(sum([float(re.findall(r'value=["](.*?)["]',data.get(col_name))[0]) for data in table_list]))
                        except Exception:                    
                            footer += '<th>0.00</th>'
        if ObjectName == 'SAQIBP':
            #footer_str = '<tfoot><tr><th colspan="7" id= "getbillyear" class="text-left">{}</th>{}</tr></tfoot>'.format(str(SubTab)+" Total", footer)
            footer_str = '<tfoot><tr><th colspan="7" id= "getbill1year" class="text-left">{}</th>{}</tr><tr></tr></tfoot>'.format("GRAND TOTAL", footer_tot)
            #footer_str = '<tfoot><tr><th colspan="7" id= "getbill1year" class="text-left">{}</th>{}</tr><tr><th colspan="9" id= "getbillyear" class="text-left">{}</th>{}</tr></tfoot>'.format("GRAND TOTAL", footer_tot,str(SubTab)+" Total",footer_tot)
            
        if QueryCount==0:
            Page_start=0
        if QueryCount < int(Page_End):
            PageInformS = str(Page_start) + " - " + str(QueryCount) + " of"
        else:
            PageInformS = str(Page_start) + " - " + str(Page_End) + " of"
        
        return table_list, QueryCount, PageInformS,footer_str


ObjSYLDRTLIST = SYLDRTLIST()
if hasattr(Param, "REC_ID"):
    RECORD_ID = Param.REC_ID
   
    Product.SetGlobal("REC_ID", str(RECORD_ID))
else:
    RECORD_ID = ""
    
ACTION = Param.ACTION
try:
    PerPage = Param.PerPage
    PageInform = Param.PageInform
   

except:
    PerPage = ""
    PageInform = ""
try:
    SortColumn = Param.SortColumn
    SortColumnOrder = Param.SortColumnOrder
except:
    SortColumn = ""
    SortColumnOrder = ""
try:
    subTab = Param.SUBTAB
   
except Exception:
    subTab = "Year 1"
    

try:
    PR_CURR = Param.PR_CURR
    TP = Param.TP
except:
    PR_CURR = ""
    TP= ""

try:
    Currenttab = Param.Currenttab    
except:
    Currenttab = ""
        



if ACTION == "PRODUCT_ONLOAD": 
    ApiResponse = ApiResponseFactory.JsonResponse(ObjSYLDRTLIST.MDYNMICSQLOBJECT(RECORD_ID, PerPage, PageInform, subTab, PR_CURR, TP))
elif ACTION == "PRODUCT_ONLOAD_FILTER":
   
    ATTRIBUTE_NAME = Param.ATTRIBUTE_NAME
    
    ATTRIBUTE_VALUE = Param.ATTRIBUTE_VALUE
    # ATTRIBUTE_VALUES = []
    # for att_val in list(ATTRIBUTE_VALUE):
        
    #     if att_val.startswith("<img"):
            
    #         ATT_VAL = att_val.split(" ")
    #         ATT_VAL = att_val.split("'")
    #         ATT_VAL = ATT_VAL[1]
    #         ATTRIBUTE_VALUES.append(ATT_VAL)
    #     else:
    #         ATTRIBUTE_VALUES.append(att_val)
    # ATTRIBUTE_VALUE = ATTRIBUTE_VALUES
    
    
    if RECORD_ID:
        RECORD_ID = "-".join(RECORD_ID.split("_")[:2])
        ApiResponse = ApiResponseFactory.JsonResponse(
            ObjSYLDRTLIST.MDYNMICSQLOBJECTFILTER(
                RECORD_ID, ATTRIBUTE_NAME, ATTRIBUTE_VALUE, PerPage, PageInform, SortColumn, SortColumnOrder, PR_CURR, TP,subTab
            )
        )
