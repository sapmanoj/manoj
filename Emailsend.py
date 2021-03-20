import smtplib

msz="hello this is message from ncitday19"
a=smtplib.SMTP('smtp.gmail.com',587)
a.ehlo()
a.starttls()
mail.login('manojsapkota764@gmail.com','itsme1234')
mail.sendmail('manojsapkota764@gmail.com','dhirajpyakurel@gmail.com',msz)
mail.close()

 