#Input A
A = int(input('Enter Input 1 (A): '))

#Input B
B = int(input('Enter Input 2 (B): '))

#All possible operators
valid_opr = ['+', '-', '*'] 

for op1 in valid_opr:
    for op2 in valid_opr:
        for op3 in valid_opr:
            statement = f"(({A} {op1} {B}) {op2} {B} ) {op3} 5"
            result = eval(statement)
            print(f"The following operators were used: {op1}, {op2}, {op3}: Producing: {result}")
