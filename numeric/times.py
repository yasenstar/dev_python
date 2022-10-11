import sys
import random
print("Play on Times for up to 10")
k=1
count=0
correct=0
want_to_quit = 0
first_time_correct = 1
while want_to_quit != 1:

    if k == 1:
        a = int(round(random.random()*10,0))
        b = int(round(random.random()*10,0))

        print("Please try", a, " x ", b, " = ?")
        if int(input()) == a * b:
            print("Correct!\n")
            k=1
            count = count + 1
            if first_time_correct == 1:
                correct=correct+1
            first_time_correct = 1
            if count % 5 == 0:
                print("continue? (y or n)")
                if input() == "n":
                    want_to_quit = 1
                    exit
        else:
            print("Try again...")
            k=0
            first_time_correct = 0

    else:

        print("Please try", a, " x ", b, " = ?")
        if int(input()) == a * b:
            print("Correct!")
            k=1
            count = count + 1
            if first_time_correct == 1:
                correct=correct+1
            first_time_correct = 1
            if count % 5 == 0:
                print("Continue? (y or n)")
                if input() == "n":
                    want_to_quit = 1
                    exit                   
        else:
            print("Try again...")
            k=0
            first_time_correct = 0
print("Total: ",count, ", # of correct are: ",correct,", Correction Rate is",round(correct/count,3)*100,"%, Great Job!")