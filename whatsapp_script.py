import pywhatkit


phone_numbers = ["+27823468282"]  # Add more numbers as needed

for i in phone_numbers:
    pywhatkit.sendwhatmsg_instantly(i, "Automatic Messager",15,True,3)

print("Message sent successfully!")