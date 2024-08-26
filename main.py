from functools import reduce

def process_numbers(numbers):

    even_positive_numbers = filter(lambda x: x > 0 and x % 2 == 0, numbers)

    squared_numbers = map(lambda x: x ** 2, even_positive_numbers)

    sum_of_squares = reduce(lambda x, y: x + y, squared_numbers, 0)

    return sum_of_squares