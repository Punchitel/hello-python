import sys

# vvv - modify this function to return greetings to the person called "name"
# e.g. if "name" is "Karel", the whole output should be "Hello, Karel!"
def greet(name):
    return "Hello... someone?"
# ^^^

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "world"

if __name__ == "__main__":
    print(greet(name))