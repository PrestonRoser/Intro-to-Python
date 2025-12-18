# Basic CLI calculator with 3 operators
# Notable elements:
#   - .stip() to remove any spaces from the input
#   - int(input(*)) to change the input from a set of characters to an integer
#   - raise to throw an exception when an operator falls outside the realm of accepted inputs
#   - def main() and if __name__ * to ensure proper program initiation

def calc():
    val_x = int(input("What is your first value? ").strip())
    val_opp = input("What operator will we use? + - * ").strip()
    val_y = int(input("What is your second value? ").strip())
    output:float

    if val_opp == "+":
        output = val_x + val_y
    elif val_opp == "-":
        output = val_x - val_y
    elif val_opp == "*":
        output = val_x * val_y
    else:
        raise ValueError("Operator must be either +, -, or *")
    
    return output


def main():
    out = calc()
    print(out)

if __name__ == "__main__":
    main()