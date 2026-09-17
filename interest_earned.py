#Justin ventura
#CMP 131
#Week 3 
#Lab 1 
#interst earned
#9/17/26
principal = int(input("What is the Starting amount:" ))
interestrate = float(input("What is the interest rate: "))
timescompound = int(input("What is the number of times compounded: "))
interestrate2 = interestrate / 100
interest = principal * interestrate2
totalamount = interest + principal
print("Interst rate:", interestrate, "%")
print("number of times copmounded: ", timescompound)
print("principal:", principal)
print("Interest: ", interest)
print("Amount in savings: ", totalamount)

