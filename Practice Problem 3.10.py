print('Practice Problem 3.10')
string1 = input('Enter a word and I will return True if it does not have vowels: ')
def noVowel(string1):
    for i in string1:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            return('False')
        else:
           return('True')
print(noVowel(string1))
