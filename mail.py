import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("e-mail_id","passwd")
subject="Sending email using python"
body="Hey ! Hope you are doing well and keeping safe ! Have a great day ahead ! Thanks ..."
message="subject:{}\n\n{}".format(subject,body)
ob.sendmail("sender's_e-mail_id","receiver's_e-mail_id",message)
print("Sent successfully..")ishash2310@gmail.com
ob.quit()
