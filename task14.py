'''
Question 3
Write a program that asks the user to enter a power.
Then find the last two digits of 2 raised to that power.
'''
power = int(input('Enter power:'))
ans = 2**power
print('2 raised to that power:', ans)
print('The last two digits of 2 raised to that power:', ans % 100)
