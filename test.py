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