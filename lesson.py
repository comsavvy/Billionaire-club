def am(age, money, output_name):

    if ((age >= 20 and money >= 500000) or (age<= 20 and money >= 2000000)) is True:

        return True

    else:

        return False


def male():

    if am(age, money, output_name) is True:

        print(f'Mr {output_name}you are allow to enter😎')

    else:

        print(f'Mr {output_name}please go and hustle.')




def female():

    if am(age, money, output_name) is True:

        print(f'Mrs {output_name}you are allow to enter😎')

    else:

        print(f'Mrs {output_name}please go and hustle.')



# Question


print('\t \tBILLIONAIRE CLUB')


try:

    name= input('Name: ').split()
    
    capitalize_name= [cpa.capitalize() for cpa in name]
    
    output_name= ''
    
    for cpl in capitalize_name:
        
        output_name += cpl + ' '
        
    

    age= int(input('Please Enter your Age: '))

    money= int(input('How much do you have in your account? '))

    gender = input('Male(M) or Female(F): ').capitalize()

 
# Conditional Statement

    if gender == 'M' or gender== 'Male':

        male()

    elif gender == 'F' or gender == 'Female':

        female()

    else:

        print('Invalid gender')

except ValueError:

    print('Check the input!')