def value_of(number: int) -> str:
    message = ""
    if is_divisible_by_both(number):
        message = "fizzbuzz"
    elif is_divisible_by_five(number):
        message = "buzz"
    elif is_divisible_by_three(number):
        message = "fizz"
    else:
        message = str(number)
    return message


def is_divisible_by_both(number: int) -> bool:
    return is_divisible_by_three(number) and is_divisible_by_five(number)


def is_divisible_by_five(number: int) -> bool:
    return number % 5 == 0


def is_divisible_by_three(number: int) -> bool:
    return number % 3 == 0
