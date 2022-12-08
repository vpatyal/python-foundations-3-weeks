import random as rd

# Todo: Create a c_to_f(temp) function
def c_to_f(temp):
    return ((temp * 9/5) + 32)

# Todo: Create a list of reminders
reminders = ['1. Prepare Coffee', '2. Carry Airpods', '3. Check train schedule before starting']

# Todo: Get some input from the user
name = input("\nHi, what is your name? : ")
temp_in_c = rd.randint(3,20)
temp_in_f = c_to_f(temp_in_c)

# Todo: Create a string with email content that includes:
#       - A greeting
#       - The day's weather + temp in c and f
#       - Some reminders
#       - 1-2 more items based on APIs that you've found


# def weather_report(temp_in_c, temp_in_f):
#     if temp_in_c <= 14:
#         return f"\nThe temperature outside is cold: {temp_in_c} °C ({temp_in_f}) °F"
#     elif 14 < temp_in_c < 25:
#         return f"\nThe temperature outside is pleasant: {temp_in_c} °C ({temp_in_f} °F)"
#     else:
#         return f"\nThe temperature outside is warm: {temp_in_c} °C ({temp_in_f} °F)"

# weather_msg = weather_report(temp_in_c, temp_in_f)
# reminders_1 = ''
# for item in reminders:
#     reminders_1 += f"\n{item}"

# email_msg = f"""\nHi {name}, wish you a super day ahead. \n{weather_msg}.
# \nDon't forget to: {reminders_1}"""
# print(email_msg)

# me = 'vinodpatyal@onmail.com'
# you = 'vinodpatyal@onmail.com'
# msg = EmailMessage()
# msg.set_content(email_msg)
# msg['Subject'] = f'Daily weather report'
# msg['From'] = me
# msg['To'] = you

# Send the message via our own SMTP server.
# s = smtplib.SMTP('localhost')
# s.send_message(msg)
# s.quit()

# Todo: Print the content to the console

print(f"\nHi {name}, wish you a super day ahead.")
if temp_in_c <= 14:
    print(f"\nThe temperature outside is cold: {temp_in_c} °C ({temp_in_f} °F)")
elif 14 < temp_in_c < 25:
    print(
        f"\nThe temperature outside is pleasant: {temp_in_c} °C ({temp_in_f} °F)")
else:
    print(f"\nThe temperature outside is warm: {temp_in_c} °C ({temp_in_f} °F)")

print("\nDon't forget to:")
for item in reminders:
    print(item)

print("\n")
