print("Enter Marks Obtained in 4 subjects:")
english= int(input("english :"))
sc= int(input("sc :"))
ssc= int(input("ssc :"))
msc= int(input("msc :"))
 
sum = english+sc+ssc+msc
print("sum of subjects = ", sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)