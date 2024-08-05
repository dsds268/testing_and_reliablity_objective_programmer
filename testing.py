
print('Enter Input 1 (A): ')
A = int(input())

print('Enter Input 2 (B): ')
B = int(input())


valid_opr = ['+', '-', '*'] 

for op1 in valid_opr:
    for op2 in valid_opr:
        for op3 in valid_opr:

            statement = f"(({A} {op1} {B}) {op2} {B} ) {op3} 5"

            result = eval(statement)
            print(f"The following operators were used: {op1}, {op2}, {op3}: Producing: {result}")


