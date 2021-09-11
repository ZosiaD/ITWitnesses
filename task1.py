'''
Write short scripts to print the results of the following expressions. In 
most places, changing integers to floating point produces a notably different 
result. For example (296/167)^2 and(296.0/167.0)^2$. 
Use long as well as complex types to see the differences.
'''

# info
a = 355.113 * (1 - 0.0003/3522)
b = 22/17 + 37/47 + 88/83
c = (553/312)**2
ai = int(a)
bi = int(b)
ci = int(c)
# input
print('choose which of the tasks you want to solve(1,2,3)')
print('1. 355.113 * (1 - 0.0003/3522) '
      '2. 22/17 + 37/47 + 88/83  '
      '3.(553/312)**2')
x = int(input())
# main
if x == 1:
    print('float : ', a)
    print('integer : ', ai)
    print('difference between float and integer : ', a-ai)
elif x == 2:
    print('float : ', b)
    print('integer : ', bi)
    print('difference between float and integer : ', a-ai)
elif x == 3:
    print('float : ', c)
    print('integer : ', ci)
    print('difference between float and integer : ', a-ai)
else:
    print('try again')

