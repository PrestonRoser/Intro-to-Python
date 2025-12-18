import math

"""
Takes user input recursively; appends it to the list.
"""
def get_input(number_set: list) -> list:
    
    while True:
        user_input: str = input('Please enter a number you\'d like to calculate (enter \'q\' to quit):\n')

        if (user_input.lower() == 'q'):
            break
        else:
            try:
                val: float = float(user_input)  # Try converting input to a number
            except ValueError:
                print("Cannot calculate. The character you have entered is not a number and cannot be computed.")
            
            number_set.append(float(user_input)) # Changes the user_input from a str to a float and appends it
    
    return number_set
       
def calculate(number_set: list) -> int:
    size: int = len(number_set)
    if ((not number_set) or (size == 1)):
        raise Exception('Cannot calculate. You did not enter enough numbers to calculate Standard Deviation.')
    elif not check(number_set):
        raise Exception('Cannot calculate. The max value entered is equal to 1 and cannot be computed.')
    
    x_sum: float = 0.0
    sum_squares: float = 0.0
    for i in range(size):
        x_sum += number_set[i]
        sum_squares += pow(number_set[i],2)
    quotient: float = (size*(sum_squares)-(pow((x_sum),2)))/(size*(size-1))
    value: float = math.sqrt(quotient)
    return value

def check(number_set: list) -> bool:
    max_val: float = 0.0
    for i in range(len(number_set)):
        if (number_set[i] >= max_val):
            max_val = number_set[i]
    
    if max_val <= 1.0:
        return False
    
    return True

"""
Asks for user input and prints it
"""
def main() -> None:
    number_set: list = []
    print(f'\n--The purpose of this program is to calculate standard deviation--\n')
    num: float = calculate(get_input(number_set))
    print(f'The standard deviation for the set {number_set} is: \n {num}')

main()