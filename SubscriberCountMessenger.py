import urllib.request 
import json
import smtplib
import imghdr
from email.message import EmailMessage

with open("SubCountStorage.txt", 'r') as file:
    var = file.read()
    file.close()
    pass

name = "Input Channel Id"
key = "Input API Key"

data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
control = int(subs) - int(var)
print(name + " has " + "{:,d}".format(int(subs)) + " subscribers!🎉")
if control > 0:
    msg = EmailMessage()
    msg['Subject'] = 'Subscriber Update!'
    #msg['Subject'] = 'Test mail- with attachment'
    msg['From'] = 'Input Your Email'
    msg['To'] = 'Input Recipients Email'
    Total = "Congrats! You have gained " + str(control) + " subscriber(s)!"
    msg.set_content(Total)
#msg.set_content('Check out this really cute puppy!')

#files = ['puppy.jpg']
#
# for file in files:
#       with open(file, 'rb') as f:
#           file_data = f.read()
#           file_type = imghdr.what(f.name)
#           file_name = f.name
#
#       msg.add_attachment(file_data,maintype='image',subtype=file_type,filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
           smtp.login('Input Your Email', 'Input Your Email Password')
           smtp.send_message(msg)
elif control < 0:
    check = abs(int(control))
    msg = EmailMessage()
    msg['Subject'] = 'Subscriber Update!'
    #msg['Subject'] = 'Test mail- with attachment'
    msg['From'] = 'Input Your Email'
    msg['To'] = 'Input Recipitents Email'
    Total = "Sorry! You have lost " + str(check) + " subscriber(s)!"
    msg.set_content(Total)
#msg.set_content('Check out this really cute puppy!')

#files = ['puppy.jpg']
#
# for file in files:
#       with open(file, 'rb') as f:
#           file_data = f.read()
#           file_type = imghdr.what(f.name)
#           file_name = f.name
#
#       msg.add_attachment(file_data,maintype='image',subtype=file_type,filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
           smtp.login('Input Your Email', 'Input Your Email Password')
           smtp.send_message(msg)


elif control == 0:
    msg = EmailMessage()
    msg['Subject'] = 'Subscriber Update!'
    #msg['Subject'] = 'Test mail- with attachment'
    msg['From'] = 'Input Your Email'
    msg['To'] = 'Input Recipitents Email'
    Total = "Hello! No additional subscribers were lost or made!"
    msg.set_content(Total)
#msg.set_content('Check out this really cute puppy!')

#files = ['puppy.jpg']
#
# for file in files:
#       with open(file, 'rb') as f:
#           file_data = f.read()
#           file_type = imghdr.what(f.name)
#           file_name = f.name
#
#       msg.add_attachment(file_data,maintype='image',subtype=file_type,filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
           smtp.login('Input Your Email', 'Input Your Email Password')
           smtp.send_message(msg)
    
with open("SubCountStorage.txt", 'w') as file:
    var = file.write(subs)
    file.close()
    pass

    
