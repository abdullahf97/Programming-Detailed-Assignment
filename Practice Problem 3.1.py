print("Abdullah Farooq")
print("18B-104-CS-A")
print("Practice Problem 3.1")

age = eval(input("Enter your age: "))
if age > 62:
    print("You can get your pension benefits.")

name = input("Enter a baseball player's name: ")
list = ['Musial', 'Aaraon', ' Williams', 'Gehrig', 'Ruth']
if name in list:
    print('One of the top 5 baseball player, ever!')

hits = eval(input('Enter the number of hits taken: '))
shields = eval(input('Enter the number of shields: '))
if hits >10 and shields ==0:
    print('You are dead...')


direction = input("Enter a direction: ")
list = ['North', 'South', 'West', 'East']
if direction in list:
    print('I can escape.')

print('Practice problem 3.3')

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
