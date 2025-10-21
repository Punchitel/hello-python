from hello import greet

def test_greet_world():
    assert greet("world") == "Hello, world!"

def test_greet_python():
    assert greet("Python") == "Hello, Python!"

def test_greet_karel():
    assert greet("Karel") == "Hello, Karel!"
