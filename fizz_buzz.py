def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        print("FizzBuzz")
    if(input % 3 == 0):
        print("Fizz")
    if(input % 5 == 0):
        print("Buzz")
    return input

fizz_buzz(6)