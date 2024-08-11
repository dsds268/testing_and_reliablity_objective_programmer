def BooleanInput(input):
    return input.lower() in ['true', 't', 'yes', 'y']

#Retrive the values of A if Known
print('Is the value of A Known? (T/F): ')
AKnown = BooleanInput(input())

if AKnown:
    A = int(input('Enter Input 1 (A): '))

#Retrive the values of B if Known
print('Is the value of B Known? (T/F): ')
BKnown = BooleanInput(input())

if BKnown:
    B = int(input('Enter Input 2 (B): '))

valid_opr = ['+', '-', '*'] 

if AKnown and BKnown:  #Calculation with both values known
    for op1 in valid_opr:
        for op2 in valid_opr:
            for op3 in valid_opr:
                statement = f"(({A} {op1} {B}) {op2} {B} ) {op3} 5"
                result = eval(statement)
                print(f"The following operators were used: {op1}, {op2}, {op3}: Producing: {result}")

elif AKnown or BKnown:
    print('Retriving all possible values of A so that the concrete test case can be generated')

else:
    print('You must have at least one value known to proceed')