def am(age, money, name):
    if (age >= 20 and money >= 500000) or (age<= 20 and money >= 2000000):
        return True
    else:
        return False
    
    
def male():
    if am(age, money, name) is True:
        print(f'Mr {name}, you are allow to enter😎')
    else:
        print(f'Mr {name}, please go and hustle.')
        

def female():
    if am(age, money, name) is True:
        print(f'Mrs {name}, you are allow to enter😎')
    else:
        print(f'Mrs {name}, please go and hustle.')

# Question
print('\t \tBILLIONAIRE CLUB')
name= input('Name: ').capitalize()
age= int(input('Please Enter your Age: '))
gender = input('Male(M) or Female(F): ').capitalize()
money= int(input('How much do you have in your account? '))

# Conditional Statement   
if gender == 'M':
    male()
elif gender == 'F':
    female()
else:
    print('Invalid gender')
    