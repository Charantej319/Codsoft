import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['1','2','3','4','5','6','7','8','9','0',]
symbol = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+','*','/']

print("Welcome to the Password generator !!!")
n_letter = int(input("Enter the no. of letters required in your password..?\n"))
n_number = int(input("Enter the no. of numbers required in your password..?\n"))
n_symbol = int(input("Enter the no. of symbols required in your password..?\n"))
pswd = []
for i in range(1,n_letter + 1):
    char = random.choice(letter)
    pswd += char
for i in range(1,n_number + 1):
    char = random.choice(number)
    pswd += char
for i in range(1,n_symbol + 1):
    char = random.choice(symbol)
    pswd += char

random.shuffle(pswd)

password = ""
for i in pswd:
    password += i

print(password)
