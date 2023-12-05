# 1a) Write a Python function to find the maximum of three numbers
# NOTE: do not utilize built-in functions to accomplish this
# instead, opt for conditionals
def maximum(2, 3, 4): 
 
    if (2 >= 3) and (2 >= 4): 
        largest = 2 
 
    elif (3>= 2) and (3 >= 4): 
        largest = 3 
    else: 
        largest = 4 
         
    return largest 
 


# 1b) use this function to find the max of the 3 vars below
a = float("inf")
b = float("-inf")
c = 100000000
max_value = find_maximum(a, b, c)
print(max_value)


# 2a) Write a Python program to reverse a string
def reverse(str):
    str=str[::-1]
    return str


# 2b) Use this function to reverse the string saved in the name below
word = "racecar"
print("racecar")
reversed_string= reverse(word)
print(reversed_string)


# 3a) Write a Python function to multiply all the numbers in a list.
def var(my_list):
    result=1
    for x in my_list:
        result= result * x
    return result

# 3b) Use this function to find the product of the list below
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(var(nums))


# 4a) Write a Python function that finds the maximum value of a list
# NOTE: do not use built-in Python functions. Instead use a for-loop and
# a conditional
def max(my_list):
    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value    

# 4b) Use this function to find the product of the list below
nums = [100, 491, 592, 58, 3, 59, -100]
print(max(nums))
