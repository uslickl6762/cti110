# Calculate a students average for grades entered
## Decision structures

# get grades from user, add grades together for a total
# divide tota; by number of grades entered to get average
# Use average to determine letter grade

grade1 = int(input("Enter the first grade: "))
grade2 = int(input("Enter the second grade: "))
grade3 = int(input("Enter the third grade: "))
grade4 = int(input("Enter the fourth grade: "))
grade5 = int(input("Enter the fifth grade: "))

total = grade1 + grade2 + grade3 + grade4 + grade5
ave = total/5

# figure out letter grade that correspond with the numeric grade
# use a decision structure

if ave >= 89.5:
    letter= "A"
else:
    if ave >= 79.5:
        letter= "B"
    else:
        if ave >= 69.5:
            letter= "C"
        else:        
            if ave >= 59.5:
                letter= "D"
            else:
                    letter= "F"

##if ave >= 89.5:
##    letter= "A"
##elif ave >= 79.5:
##        letter= "B"
##elif ave >= 69.5:
##            letter= "C"
##elif ave >= 59.5:
##                letter= "D"
##else:
##    letter= "F"


print(ave)
print(letter)



