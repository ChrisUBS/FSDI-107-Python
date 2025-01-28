print("hello world!")

# Variables
name = "Chris"
last_name = "Bonilla"
age = 20
found = False
print(name)

# If statements
if age < 100:
    print("Don't worry, your not that old")
    print("I'm using the indentation")
    print("I'm in of the if statement")
elif age == 100: # Else if
    print("Wow, you are a century!")
else:
    print("Seems that you are really old")

# Functions
def say_hello():
    print("Hello World!")

def say_goodbye(name):
    print(f"Goodbye, {name}!")

# Call functions
say_hello()
say_goodbye("Chris")

# Arrays are called lists
color = ["red", "green", "blue", "yellow"]

# Add an element to the list
color.append("pink")
print(color)
print(color[0])
color.remove("yellow")
print(color)

# For loop
for item in color:
    print(item)
# for(let i = 0; i < color.length; i++)
# let temp = color[i]
# print(temp)

# Dictionaries
me = {
    "name": "Chris",
    "last_name": "Bonilla",
    "age": 20
}

print(me["last_name"])
me["last_name"] = "Doe"
print(me)

ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]

# Print the sum of all numbers
def example1():
    sum = 0
    for age in ages:
        sum += age
    print(sum)

# Count how many users are equal or older than 21
def example2():
    count = 0
    for age in ages:
        if(age >= 21):
            count += 1
    print(count)

# How many users are between 30 and 40 years old
def example3():
    counter = 0
    for age in ages:
        if age >= 30 and age <= 40:
            counter += 1
    print(counter)

# Call the functions
example1()
example2()
example3()
