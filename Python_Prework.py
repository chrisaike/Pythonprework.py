# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_username():
	print("Hello_USERNAME!")

hello_username()

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds(n):
    return [x for x in range(1,n+1) if x % 2 ==1]
print(first_odds(100))
    
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list( a_list ):
    max = a_list[ 0 ]
    for q in a_list:
        if q > max:
            max = q
    return max
print(max_num_in_list([8700, 73000, 425, 3, 85, 69, 77000, 58000])) 

# Question 3 alternative answer:
a_list = [8700, 73000, 425, 3, 85, 69, 77000, 58000]
max_num_in_list = max(a_list)
print(max_num_in_list)  

# Question 4
# Write a function to return if the given year is a leap yaer. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false)
input_year = int(input("Enter a year:"))
def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    
    return False
    
if is_leap(input_year):
    print("True") 
else:
    print("False") 


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
numbers = [1, 6, 3, 8, 9]

output = "False"
for i in range(0, len(numbers)-1):
    if numbers[i]+1 == numbers[i+1] or numbers[i]-1 == numbers[i+1]:
        output = "True"
    else:
        output = "False"
        break
print(output) 