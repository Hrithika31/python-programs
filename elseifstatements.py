numbofstudents = int(input("enter the number of students:"))
numbofgirls = int(input("enter the number of girls:"))
numbofboys = numbofstudents - numbofgirls

if numbofstudents > 40:
    print("the population of the class is good")


elif numbofboys > numbofgirls:
    print("increase the number of girl students")
