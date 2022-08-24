'''
Date         : 2022-08-24 11:49:45
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-08-24 12:35:41
LastEditors  : BDFD
Description  : 
FilePath     : \test.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
import autoscript as ats

email_receiver = 'davidchen014@gmail.com'
# Set the subject and body of the email
subject = 'Hello World2'
body = """
This is auto test msg send from info email
"""
# ats.gmail(email_receiver=email_receiver,gmail_subject=subject,gmail_body=body)
ats.work_mail(email_receiver=email_receiver,workmail_subject=subject,workmail_body=body)