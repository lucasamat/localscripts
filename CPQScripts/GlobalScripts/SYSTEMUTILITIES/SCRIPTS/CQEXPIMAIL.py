from SYDATABASE import SQL
import Webcom.Configurator.Scripting.Test.TestProduct
import SYCNGEGUID as CPQ
from datetime import *
import datetime
from System.Net import CookieContainer, NetworkCredential, Mail
from System.Net.Mail import SmtpClient, MailAddress, Attachment, MailMessage
Sql = SQL()
Param = Param



def mailtrigger(self):
    Subject = "TEST"
    mailBody = "HI This Is TeST MAIl"
    recepient = "joe.ebenezer@bostonharborconsulting.com"
    try:
        LOGIN_CRE = Sql.GetFirst("SELECT USER_NAME,PASSWORD FROM SYCONF (NOLOCK) where Domain ='SUPPORT_MAIL'")
        mailClient = SmtpClient()
        mailClient.Host = "smtp.gmail.com"
        mailClient.Port = 587
        mailClient.EnableSsl = "true"
        mailCred = NetworkCredential()
        mailCred.UserName = str(LOGIN_CRE.USER_NAME)
        mailCred.Password = str(LOGIN_CRE.PASSWORD)
        mailClient.Credentials = mailCred
        toEmail = MailAddress(str(recepient))
        fromEmail = MailAddress(str(LOGIN_CRE.USER_NAME))
        msg = MailMessage(fromEmail, toEmail)
        msg.Subject = Subject
        msg.IsBodyHtml = True
        msg.Body = mailBody
        # copyEmail1 = MailAddress("mayura.priya@bostonharborconsulting.com")
        # msg.CC.Add(copyEmail1)
        #copyEmail2 = MailAddress("wasim.abdul@bostonharborconsulting.com")
        #msg.CC.Add(copyEmail2)
        # copyEmail2 = MailAddress("sathyabama.akhala@bostonharborconsulting.com")
        # msg.CC.Add(copyEmail2)
        #copyEmail4 = MailAddress("aditya.shivkumar@bostonharborconsulting.com")
        #msg.CC.Add(copyEmail4)
        #copyEmail5 = MailAddress("namrata.sivakumar@bostonharborconsulting.com")
        #msg.CC.Add(copyEmail5)    
        mailClient.Send(msg)
        Trace.Write("Mail Sent Successfully")
        Quote.GetCustomField("quote_expiration_mail").Content = "TRUE"
        # quote_expiration_mail = "FALSE"
    except Exception, e:
        self.exceptMessage = "SYCONUPDAL : mailtrigger : EXCEPTION : UNABLE TO TRIGGER E-EMAIL : EXCEPTION E : " + str(e)
        Trace.Write(self.exceptMessage)
    return True



now = datetime.datetime.now()
current_date_obj = str(now).split(" ")[0].strip()
today_date = datetime.datetime.strptime(str(current_date_obj),"%Y-%m-%d")
today_date_string = str(today_date).split(" ")[0].strip()
Trace.Write("Today_date "+str(today_date_string))
today_date_string = "2023-03-07"
quote_expiration_date = Quote.GetCustomField('QuoteExpirationDate').Content
quote_expiration_date_obj = datetime.datetime.strptime(str(quote_expiration_date),"%Y-%m-%d")
mail_trigger_date = quote_expiration_date_obj - timedelta(days=14)
mail_trigger_date = str(mail_trigger_date).split(" ")[0].strip()

# try:
# 	if quote_expiration_mail:
# 		quote_expiration_mail = quote_expiration_mail
# 	else:
# 		quote_expiration_mail = "TRUE"
# except:
# 	Trace.Write("EXCEPT: quote_expiration_mail")
# 	quote_expiration_mail = "FALSE"

if str(today_date_string) == str(mail_trigger_date):
	if Quote.GetCustomField("quote_expiration_mail").Content == "TRUE":
		ApiResponse = ApiResponseFactory.JsonResponse(mailtrigger())