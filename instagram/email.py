from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
def send_welcome_email(name,receiver):
  subject = 'Welcome to Instagram'
  sender = 'egesacollins92@gmail.com'
  text_content = render('email/email.txt',{"name": name})
  html_content = render('email/email.html',{"name": name})

  msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
  msg.attach_alternative(html_content,'text/html')
  msg.send()