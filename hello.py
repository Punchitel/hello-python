import sys

# vvv - modify this function to output greetings to the person called "name"
# e.g. if "name" is "Karel", the whole output should be "Hello, Karel!"
def greet(name):
    print("Hello... someone?")
# ^^^

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "world"

if __name__ == "__main__":
    greet(name)