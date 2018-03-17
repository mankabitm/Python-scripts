import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('from@gmail.com','password')
conn.sendmail('from@gmail.com','to@gmail.com','Subject: subject \n\n -sender')
print('Done')
conn.quit();