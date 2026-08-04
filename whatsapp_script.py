import pywhatkit


phone_numbers = ["+27799953644"]  # Add more numbers as needed

for i in phone_numbers:
    pywhatkit.sendwhatmsg_instantly(i, "HELLOW I AM UNDA DA WATA",15,True,3)

print("Message sent successfully!")