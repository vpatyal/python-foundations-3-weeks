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
            print(f"\ncollatz list for {x} is {list_of_nums}")
            print(f"length of list: {len(list_of_nums)}, maximum number in list: {max(list_of_nums)}")
            return [len(list_of_nums), max(list_of_nums)]
            break
        else:
            num = next_num(num)

# Todo: print the Collatz sequence for each number from 1 - 100
a = [0, 0]  # list to hold the maximum number of elements from collatz list of 1 -100
b = [0, 0]  # list to hold the largest number from collatz list of 1 - 100
for n in range(100, 1, -1):
    list_of_nums = []
    ret_list_next_num = collatz(n)
    if ret_list_next_num[0] > a[1]:
        a[0] = n
        a[1] = ret_list_next_num[0]
    if ret_list_next_num[1] > b[1]:
        b[0] = n
        b[1] = ret_list_next_num[1]

print(f"\n\n\nNumber {a[0]} has the maximum number of elements ({a[1]}) in collatz list")
print(f"Number {b[0]} has the largest element ({b[1]}) in collatz lists for numbers 1-100")
