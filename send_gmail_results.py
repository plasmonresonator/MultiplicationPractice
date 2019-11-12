
from __future__ import print_function
from __future__ import unicode_literals
from datetime import datetime
from credentials import app_password, matt_email, maddie_email, krista_email

import logging, os, unittest
from email.mime.base import MIMEBase

from gmail import GMail, GMailWorker, GMailHandler, Message


curr_time = datetime.now()
time = curr_time.strftime('%Y-%m-%d, %H%M')
def send_email(recipient=matt_email, msg='test'):
	try:
		gmail = GMail(maddie_email, app_password)
		msg1 = Message(f"Maddie's Math Results from {time}",
			to=recipient,
			text = msg
			)

		gmail.send(msg1)
		print("Message sent!")
	except Exception as e:
		print(f"Error sending email results. Error message: \n {e}")