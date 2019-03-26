import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='hemanthmadala75@gmail.com'
reciever='madalahemanth007@gmail.com'
msg='gud ni8'
s.login(sender,'')
s.sendmail(sender,reciever,msg)
print("msg sent successfully")
s.quit()