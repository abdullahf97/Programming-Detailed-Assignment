print('Practice Problem 3.3')
year = eval(input('Enter a year to check if its a leap year: '))
if year%4 ==0:
    print(year, 'could be a leap year.')
else:
        print(year, 'is definitely not a leap year.')

lottery = [20, 35, 40, 50, 60, 55]
ticket = eval(input('Enter the ticket numbers: '))

if ticket in lottery:
    print('You won!')
else:
    print('Better luck next time')
