from concurrent import futures

def am(age, money, output_name):
    if ((age >= 20 and money >= 500000) or (age <= 20 and money >= 2000000)):
        return True
    else:
        return False

def gender(gen, age, money, output_name):
    if gen.startswith("M"):
        if am(age, money, output_name):
            print(f'Mr {output_name}\b, you are allow to enter😎')
        else:
            print(f'Mr {output_name}\b, please go and hustle.')
    elif gen.startswith("F"):
        if am(age, money, output_name) is True:
       		print(f'Mrs {output_name}\b, you are allow to enter😎')
        else:
            print(f'Mrs {output_name}\b, please go and hustle.')
    else:
        print("Invalid gender")


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
	    gend = input('Male(M) or Female(F): ').capitalize()
	# Conditional Statement
	    gender(gend, age, money, output_name)
	except ValueError:
	    print('Check the input!')


if __name__ == '__main__':
    with futures.ThreadPoolExecutor(max_workers= 2) as executor:
        executor.submit(main)
