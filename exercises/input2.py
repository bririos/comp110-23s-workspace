"""Example enviroment diagram program."""

age: int = 21
year: int = 2024
age_in_2043: int = 2043 - year + age
print ("In 2043, you'll be " + str(age_in_2043))

age = age + 1
year = year + 1 
print("In " + str(year) + ", you'll be " + str(age))