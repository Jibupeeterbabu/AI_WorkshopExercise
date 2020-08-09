'''
python program for printing fibonacci series
sample :
  fibonacci series: 0, 1, 1, 2, 3, 5,
logic:
  Nth number = (n-1)th + (n-2)th
'''


firstNumber = 0
secondNumber = 1

n = int(input("How many numbers have to be displayed: "))

if(n == 2):
    print(firstNumber, secondNumber, sep=' ', end=' ' )
elif n == 1:
    print(fistNumber)
elif n < 0:
    print("Enter a positive number!!")
else:
    print(firstNumber, secondNumber, sep=' ', end=' ' )
    for i in range(2, n):
        nextNumber = firstNumber + secondNumber
        print(nextNumber, end=' ')
        firstNumber = secondNumber
        secondNumber = nextNumber
