'''

file: extractor.py

This program separates the odd and even numbers into categorized text files.

1. Look for numbers.txt file
2. Iterate through every number from numbers.txt
    - If even, store it on even.txt
    - If odd, store it on odd.txt
3. Remember to close the txt file! (Use with operator for a foolproof execution!)

'''


def open_file_and_extract():

    # Look for numbers.txt file
    try:
        with open('numbers.txt', 'r') as numbers:
            # Iterate through every number from numbers.txt
            numbers = numbers.readlines()

            for index, number in enumerate(numbers):
                # If number is even
                if(int(number.strip()) % 2 == 0):
                    store_to_file(str(number), 'even')
                # If number is odd
                else:
                    store_to_file(str(number), 'odd')
    except FileNotFoundError:
        return 'File numbers.txt is not found'

def store_to_file(number, mode):

    global first_odd, first_even

    # Determine divisor according to mode
    divisor = 1 if mode == 'odd' else 0

    # If number is first on list, create a new file or overwrite existing
    if not (first_odd and first_even):
        # These will determine whether there the first odd or even have already been identified
        if not first_odd and mode == 'odd':
            first_odd = True
        
        if not first_even and mode == 'even':
            first_even = True

        with open(f'{mode}.txt', 'w') as odd_or_even_file:
            odd_or_even_file.write(str(number))
    else:
        with open(f'{mode}.txt', 'a') as odd_or_even_file:
            odd_or_even_file.write(str(number))

first_odd = False
first_even = False

print(open_file_and_extract())