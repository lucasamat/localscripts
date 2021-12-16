# =========================================================================================================================================
#   __script_name : CQSPBLKUPL.PY
#   __script_description : THIS SCRIPT IS USED TO SHOW BULK INSERT MODEL(POP-UP)
#   __primary_author__ : AYYAPPAN SUBRAMANIYAN
#   __create_date :09-10-2020
#   © BOSTON HARBOR TECHNOLOGY LLC - ALL RIGHTS RESERVED
# ==========================================================================================================================================
import Webcom.Configurator.Scripting.Test.TestProduct
try:
    ACTION = Param.ACTION
except:
    ACTION = "" 
if ACTION == "BULKUPLOADDATA":
    model_html = """ <div class="row modulebnr brdr ma_mar_btm">UPLOAD PARTS LIST<button type="button" class="close flt_rt" onclick="closepopup_scrl()" data-dismiss="modal">X</button></div>
                    <div class="col-md-12 padlftrhtnone">
                        <div class="row pad-10 bg-lt-wt brdr" id="seginnerbnr">
                        <img style="height: 40px; margin-top: -1px; margin-left: -1px; float: left;" src="/mt/APPLIEDMATERIALS_TST/Additionalfiles/Secondary Icon.svg">
                        <div class="product_txt_div_child secondary_highlight" style="display: block;text-align: left;">
                            <div class="product_txt_child"><abbr title="Upload Parts List">Upload Parts List</abbr></div>
                            <div class="product_txt_to_top_child"><abbr title="Please upload your edited Excel file to replace and update your Parts List...">Please upload your edited Excel file to replace and update your Parts List...</abbr></div>
                        </div>
                        </div>
                    </div>
                    <div class="col-md-12">
                            <p class="p-0">Please ensure the file you're uploading exactly matches the format of the downloaded parts list.</p>
                    </div>
                    <div class="col-md-12 d-flex align-items-center">
                        <div class="partno-lbl col-md-4">File Name</div>
                        <div class="txt-col-sec col-md-4"><input id="uploadsheet" class="light_yellow" style="width: 100%;" disabled></div>
                        <div class="col-md-4">
                            <label for="file-input">
                                <img src="https://sandbox.webcomcpq.com/mt/APPLIEDMATERIALS_TST/Additionalfiles/document_upload_icon.svg">
                            </label>
                            <input id="file-input" style="display:none" type="file">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button id="bulkaddpopupcancel" class="btn btn-list-cust" data-dismiss="modal" aria-hidden="true">CANCEL</button>
                        <button onclick="bulkUploadSave()" id="bulkuploadsave" data-dismiss="modal" class="btn btn-list-cust">SAVE</button>
                    </div> """
    ApiResponse = ApiResponseFactory.JsonResponse([model_html])
else:
    model_html = """
        <div class='row modulebnr brdr ma_mar_btm'>BULK ADD<button type='button' class='close flt_rt' onclick='closepopup_scrl()' data-dismiss='modal'>X</button></div>
        <div id='container' class='g4 pad-10 brdr except_sec spare-parts-bulk-add-ctnr-out'>
            <textarea id='spare-parts-bulk-add-ctnr' name='spare-parts-bulk-add-ctnr' class='form-control txtArea' rows='100' cols='100' tabindex='7' style='width: 100%;height: 200px;'></textarea>
        </div>
        <div id='spare-parts-bulk-add-model-footer'>
            <button type='button' class='btnconfig' data-dismiss='modal' onclick='closepopup_scrl()'>CANCEL</button>    
            <button type='button' id='spare-parts-bulk-add-save-btn' class='btnconfig' onclick='bulkAddSpareParts()' data-dismiss='modal'>ADD</button>                
        </div>
        """
    ApiResponse = ApiResponseFactory.JsonResponse([model_html])