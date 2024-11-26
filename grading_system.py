print("Enter Your Marks Here: ")

mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

total = mark1+mark2+mark3+mark4+mark5
average = total/5

if average >= 91 and average<=100:
    print("You got an A1")

elif average>= 81 and average <91:
    print("You got an A2")

elif average>= 71 and average <81:
    print("You got an B1")

elif average >= 61 and average <71:
    print("You got a B2")

elif average >= 51 and average< 61:
    print("You got a C1")

elif average >= 41 and average<51 :
    print("You got a C2")

elif average >= 33 and average< 41:
    print("You got a D ")

elif average >= 21 and average < 33:
    print("You got E1")

elif  average >= 0 and average < 21:
    print("You got E2")

else:
    print("Invalid Input!!")
    