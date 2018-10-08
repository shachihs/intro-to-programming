def run(input):
    if _is_divisible_by_3_and_5(input):
        return "fizzbuzz"
    elif _is_divisible_by_3(input):
        return "fizz"
    elif _is_divisible_by_5(input): 
        return "buzz"
    else:
        return input 

def _is_divisible_by_3_and_5(input):
    return input % 3 == 0 and input % 5 == 0 

def _is_divisible_by_3(input):
    return input % 3 == 0 

def _is_divisible_by_5(input):
    return input % 5 == 0

