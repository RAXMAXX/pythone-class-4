num = int(input("Enter number of days:"))

year  = int(num/365)
week =  int((num%365)/7)
days =  int((num%365)%7)

print("Number of Years: ", year)
print("Number of Weeks: ", week)
print("Number of Days: ", days)