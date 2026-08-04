import pywhatkit

numbers = ["+27794975184", "+27794975185", "+27794975186"]  # Add more numbers as needed

for number in numbers:
    pywhatkit.sendwhatmsg_instantly(number, "message",15,True,3)

print("Message sent successfully!")