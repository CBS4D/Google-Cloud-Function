import smtplib
import mimetypes

from io import IOBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(request):
    """
    """
    try:
        json_data = request.get_json()
        if not json_data:
            print("No data provided")
            return

        if not json_data.get('recipient_email'):
            print('recipient email is not provided')
            return
        if not json_data.get('sender_email'):
            print('sender email is not provided')
            return

        if not json_data.get('email_body'):
            print('email body is not provided')
            return
        
        body = json_data.get('email_body')
        message = MIMEText(body, 'plain', 'utf-8')
        username = json_data.get('sender_email')
        password = json_data.get('password')
        smtphost = 'smtp.gmail.com'
        port = 465

        from_email = json_data.get('sender_email')
        to_addresses = json_data.get('recipient_email')
        message['Subject'] = json_data.get('subject')
        message['From'] = formataddr(('Google Cound Email Function', from_email))
        message['To'] = to_addresses

        smtp = smtplib.SMTP_SSL(smtphost, port)
        try:
            smtp.login(username, password)
            smtp.sendmail(from_email, to_addresses, message.as_string())
            print("SENT")
        except Exception as e:
            print(e)
        finally:
            smtp.quit()
    except Exception as e:
        print(e)
