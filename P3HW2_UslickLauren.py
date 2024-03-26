# Lauren Uslick
#

em = input("Enter employee's name: ")
hrs = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))
print('-'*37)
print("Employee name:", em)
print()
hw = "Hours Worked"
pr = 'Pay Rate'
ov = 'Overtime'
op = 'Overtime Pay'
rp = 'RegHour Pay'
gp = 'Gross Pay'
print(hw'   'pr,ov,op,rp,gp)

print('-'*80)

ovt_hours = 0
ovt_pay = 0
if hrs > 40:
    reg_pay = rate * 40
    ovt_hours = hrs - 40
    ovt_rate = 1.5 * rate
    ovt_pay = ovt_hours * ovt_rate
    gross_pay = ovt_pay + reg_pay
else:
    reg_pay = rate * hrs
    gross_pay = ovt_pay + reg_pay

print(hrs)
print(rate)
print(ovt_hours)
print(ovt_pay)
print(reg_pay)
print(gross_pay)
