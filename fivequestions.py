#QUESTION 1

def hello_name(user_name):
    """Says Hello to a user"""
    print('Hello ' + user_name.title() + "!")

hello_name('ashley')

#QUESTION 2

def first_odds(start, end):
    """prints odd numers in a range"""
    for num in range(start, end):
        if num % 2 != 0:
            print(num)
        
            

start= 1
end = 100

   # adding print return none?     
print(first_odds(start,end))


#QUESTION 3

def max_num_in_list(a_list):
    """Returns the max number in a list"""
    maxnum = max(a_list)
    print(maxnum)

a_list = [2, 4, 6, 22, 44, 400, 8]


max_num_in_list(a_list)
   

#QUESTION 4 Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """returns if the given year is a leap year"""
    if (a_year % 4 == 0 )and (a_year % 100 != 0):
         print ("It's a Leap year!")
    elif (a_year % 400 == 0) and (a_year % 100 != 0):
        print ("It's a Leap year!")

    else:
        print("Not a Leap Year")

is_leap_year(2009)
is_leap_year(2004)

#QUESTION 5

def is_consecutive(a_list):
    """ check to see if all numbers in list are consecutive numbers. """
    return sorted(a_list) == list(range(min(a_list), max(a_list)+ 1))

numlist = [1, 2, 3, 4, 5]
numlist2 = [5, 3, 2, 8, 9]
numlist3 = [44, 455, 56, 12, 9]
numlist4= [9, 8, 7]

print(is_consecutive(numlist))
print(is_consecutive(numlist2))
print(is_consecutive(numlist3))
print(is_consecutive(numlist4))