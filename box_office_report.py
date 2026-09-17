movie = input("Enter movie name here:")
adulttickets = int(input("Enter amount of adult tickets sold:"))
childtickets = int(input("Enter amount of child tickets sold:"))
adultprice = int(10)
childprice = int(6)
adulttotal = adultprice * adulttickets
childtotal = childprice * childtickets
gross = adulttotal + childtotal
distibutorcut = gross * .80
netpay = gross - distibutorcut 
print("Gross box office profit:", gross)
print("Net box office profit", netpay)
print("Distributor cut: ", distibutorcut)