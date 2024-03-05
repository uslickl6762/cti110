#Lauren Uslick
#3/5/2024
#P2HW2
#





module1 = float(input('Enter grade for Module 1: '))
module2 = float(input('Enter grade for Module 2: '))
module3 = float(input('Enter grade for Module 3: '))
module4 = float(input('Enter grade for Module 4: '))
module5 = float(input('Enter grade for Module 5: '))
module6 = float(input('Enter grade for Module 6: '))
print()

grades=[module1,module2,module3,module4,module5,module6]

print('-'*12 + "Results" + 12*'-')
low=min(grades)
high=max(grades)
sum1=sum(grades)
length=len(grades)
average=sum1/length
print('Lowest Grade:'.ljust(7),f'{low:.1f}') 
print('Highest Grade:'.ljust(7),f'{high:.1f}') 
print('Sum of Grades:'.ljust(7),f'{sum1:.1f}') 
print('Average:'.ljust(7),f'{average:.2f}') 
print('-'*40)



