# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")

greet_with("max", "nowhere")
greet_with(location="NOWHERE", name="max")