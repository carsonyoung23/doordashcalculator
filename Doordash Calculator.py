#This is a doordash calculator

#This is where we ask for the users inputs
starting_mileage = float(input("What is your starting mileage?: "))
ending_mileage = float(input("What is your ending mileage?: "))
HoursWorked = float(input("How many hours did you work?: "))
AmountMade = float(input("How much money did you make?: "))
CarMPG = float(input("What is your Car's MPG?: "))
GasPrice = float(input("What is the current gas price?: "))

#This is where we do calculations
Gross_EPH = AmountMade / HoursWorked
Total_Mileage = ending_mileage - starting_mileage
GasUsed = Total_Mileage / CarMPG
GasCost = GasUsed * GasPrice
TotalDailyMade = (Gross_EPH * HoursWorked) - GasCost
Adjusted_EPH = TotalDailyMade / HoursWorked

#More Calculations
GasCost2 = "$" + str(GasCost) 
GasUsed2 = str(GasUsed) + " Gallons"
Mileage_Driven = str(Total_Mileage) + " Miles"
TotalDailyMade2 = "$" + str(TotalDailyMade)
Adjusted_EPH2 = "$" + str(Adjusted_EPH)
Gross_EPH2 = "$" + str(Gross_EPH)


#Output
print("                                                                                                                                     ")
print("Gross Earnings Per Hour: " , Gross_EPH2)
print("Adjusted Earnings Per Hour: " , Adjusted_EPH2)
print("Total Miles Driven: " , Mileage_Driven)
print("Amount of Gas Used: " , GasUsed2)
print("Total Gas Cost: ", GasCost2)
print("Total Daily Made: " , TotalDailyMade2)

