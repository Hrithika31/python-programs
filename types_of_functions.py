#type 1

def greet(name):
    print(f"hi {name}")

greet("hrithika")

#type 2

def get_greet(name):
    return f"hi {name}"

get_greet("rahul")

message = get_greet("rahul")
print(message)