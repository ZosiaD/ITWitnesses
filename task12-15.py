'''
Question 1 
Write a program that asks the user to enter a weight in kilogram
The program should convert it to pounds, printing the answer rounded
to the nearest tenth of a pound.
'''
#1 kg = 2.2046 Pounds
kg = float(input('Enter weight in Kg to convert into pounds:'))
pounds = kg*2.2046
print(kg, 'Kg =', round(pounds,1), 'Pounds')
