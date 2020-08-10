from concurrent import futures

def am(age, money, output_name):
    if ((age >= 20 and money >= 500000) or (age <= 20 and money >= 2000000)):
        return True
    else:
        return False


def male(age, money, output_name):
    if am(age, money, output_name):
        print(f'Mr {output_name}\b, you are allow to enter😎')
    else:
        print(f'Mr {output_name}\b, please go and hustle.')


def female(age, money, output_name):
    if am(age, money, output_name) is True:
        print(f'Mrs {output_name}\b, you are allow to enter😎')
    else:
        print(f'Mrs {output_name}\b, please go and hustle.')


def main():
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
	    if gender.startswith('M'):
	        male(age, money, output_name)
	    elif gender.startswith('F'):
	        female(age, money, output_name)
	    else:
	        print('Invalid gender')
	except ValueError:
	    print('Check the input!')


if __name__ == '__main__':
    with futures.ThreadPoolExecutor(max_workers= 2) as executor:
        executor.submit(main)
