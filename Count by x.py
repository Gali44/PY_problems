# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

    print(count_by(10))
    """
    Return a sequence of numbers counting by `x` `n` times. Example (2,5) 2*1=2, 2*2+4... 5 times
    """


def count_by(x, n):
    arr = []
    for num in range(1, n + 1):
        result = x * num
        arr.append(result)
    return arr

print(count_by(1, 10))
print(count_by(2, 5))
print(count_by(50, 5))


def count_by(x, n):
    multiples_of_x = []
    for number in range(1, n + 1):
        multiples_of_x.append(number * x)

    return multiples_of_x

#Create list from string

def string_to_array(string):
    return string.split(" ")

print(string_to_array("Good day"))

#Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are strictly positive numbers.

def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:  # use n both times!
        return True
    else:
        return False
#Or in short:

def is_divisible(n, x, y):
    return n % x == n % y == 0