"""
A program that prints a greeting:
    Good morning, {name}!
    Today is going to be {condition} and {temp_c} °C ({high_f} °F).

Scenario 2 practice
"""

# Todo: Get some input from the user
name = input("What is your name : ")
weather = input(f"Hi {name}, How is the weather today ? ")
temp_hi = float(input("High Temp in C: "))
temp_low = float(input("Low temp in C: "))

# Todo: Convert the temperatures
def temp_c_to_f(temp_c):
    return (temp_c * 9 / 5 + 32)

# Todo: Print the greeting
greetings = f"""Good morning, {name}!
Today is going to be {weather} weather.
High: {temp_hi} C ({temp_c_to_f(temp_hi)} F)  
Low:  {temp_low} C ({(temp_c_to_f(temp_low))} F)"""

print(greetings)