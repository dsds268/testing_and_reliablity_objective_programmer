# Input A
A = int(input('Enter Input 1 (A): '))

# Input B
B = int(input('Enter Input 2 (B): '))

# All possible operators
valid_opr = ['+', '-', '*']

# Iterate through all possible combinations of operators
for op1 in valid_opr:
    for op2 in valid_opr:
        for op3 in valid_opr:
            # Construct the first expression (A = (A + B) * B)
            expression1 = f"({A} {op1} {B}) {op2} {B}"
            
            modified_A = eval(expression1)
                
            # Construct the second expression (C = A - 5)
            expression2 = f"{modified_A} {op3} 5"
                
            # Evaluate the second expression to get the final result C
            C = eval(expression2)

            #PrintOutput of the expression   
            print(f"Operators: {op1}, {op2}, {op3} Producing: {C}")