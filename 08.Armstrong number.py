def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)

    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_digits == number:
        return True
    else:
        return False
number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
