#email
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("iramfathima99@gmail.com", "IramFathima1")
msg="hello"
server.sendmail("iramfathima99@gmail.com","iramfathima99@gmail.com",msg)
print("sent")
server.quit()

