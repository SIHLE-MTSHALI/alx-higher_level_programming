#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from a string.
    Returns the new string.
    """
    return ''.join(char for char in my_string if char not in 'cC')


if __name__ == "__main__":
    # Sample use
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
