import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

class EmailUtilities:

    def __init__(self, login_id, login_password):
        self.login_id = login_id
        self.login_password = login_password

    def send_email(self, receiver_email_id, email_subject='', email_body='', email_body_type='plain',
                   attachment_file_name=None, attachment_file_source_path=None):

        msg = MIMEMultipart()
        msg['From'] = self.login_id

        if isinstance(receiver_email_id, str):
            msg['To'] = receiver_email_id

        elif isinstance(receiver_email_id, list):
            msg['To'] = ','.join(receiver_email_id)

        msg['Subject'] = email_subject

        msg.attach(MIMEText(email_body, email_body_type))

        if attachment_file_name !=None and attachment_file_source_path!=None:
            # ATTACHMENT PART OF THE CODE IS HERE
            attachment = open(attachment_file_source_path, 'rb')
            part = MIMEBase('application', "octet-stream")
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_file_name)
            msg.attach(part)

        server = smtplib.SMTP('smtp.office365.com', 587)  ### put your relevant SMTP here
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.login_id, self.login_password)  ### if applicable
        server.send_message(msg)
        server.quit()
