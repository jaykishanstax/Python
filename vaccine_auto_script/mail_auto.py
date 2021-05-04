import json
import random
import requests
import smtplib, ssl
import time
from datetime import datetime


def sendmail():
  port = 465  # For SSL
  password = "yourpassword"
  sender_email = "jaykishanss23@gmail.com"
  receiver_email = "jaykishanss23@gmail.com"
  message = "test available"

  # Create a secure SSL context
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login("jaykishanss23@gmail.com", password)
      server.sendmail(sender_email, receiver_email, message)
      # TODO: Send email here

def main():  
  while 1 == 1:
      process()

def process():

  url = 'https://findslot.in/api/getPincodeWiseVaccineCentersApi.php?pincode=380016'
  headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }
  # headers = {‘Content-Type’: ‘application/json; charset=utf-8’}
  r = requests.get(url, headers=headers)
  files = r.json()
  print(files)
  print(len(files))
  #resp_dict = json.loads(r)
  print(files['centers'])
  print(len(files['centers']))
  print(datetime.now())

  if len(files['centers']) > 0 :
      sendmail()
  time.sleep(120)

if __name__== "__main__":
  main()
