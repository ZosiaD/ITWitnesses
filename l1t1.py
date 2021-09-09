"""Write a program that asks the user to enter three numbers:
the day of birth, the month of birth and the year of birth
(use three separate input statements).
Print out the total number of days from birth."""

days = int(input("day of birth = "))
month = int(input("month of birth = "))
year = int(input("year of birth = "))

print("total days from birth = ", (year*365 + month*30 + days))
