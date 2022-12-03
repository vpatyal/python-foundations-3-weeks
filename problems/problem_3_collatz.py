"""
Collatz sequence:
    - Starting at a number, n
    - If n is even, divide it by 2
    - If n is odd, multiply it by 3 and add 1
    - Repeat the process until you reach 1

Print the Collatz sequence for each number from 1 to 100.
"""

# Todo: determine next number in sequence
def next_num(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n*3) + 1


# Test for the logic in next_num
def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected} but got {actual}"


assert_equals(next_num(2), 1)
assert_equals(next_num(3), 10)
assert_equals(next_num(4), 2)
assert_equals(next_num(5), 16)


# Todo: print the Collatz sequence for a given number
def collatz(num):
    x = num
    while num >= 1:
        list_of_nums.append(num)
        if num == 1:            
            print(f"collatz list for {x} is {list_of_nums}")
            break
        else:
            num = next_num(num)

# Todo: print the Collatz sequence for each number from 1 - 100
for n in range(100, 1, -1):
    list_of_nums = []
    collatz(n)
