# FUNCTIONAL PROMPT -implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    flattened = sum(array, [])
    return sorted(flattened)
  
array = [[3, 2, 1], [7, 9, 8], [6, 5, 4]]
result = flatten_and_sort(array)
print(result)

# ANSWER THE FOLLOWING QUESTIONS: 
# 1) HOW DOES THIS SOLUTION ENSURE DATA IMMUTABILITY?
# The solution ensures data immutability because it creates a new list without changing the original data. It also sorts the function and returns a new sorted list that does not change the input list. The solution does not alter the original data.


# 2) IS THIS SOLUTION A PURE FUNCTION? WHY OR WHY NOT?
# yes the solution is a pure function because it does not produce or rely on side effects and its output purely depends on it input. also the function must not change the input value or any external values


# 3) IS THIS SOLUTION A HIGHER ORDER FUNCTION? WHY OR WHY NOT?
# No, this solution is not a higher-order function because it does not accept one or more functions as an argument and it does not return a function it is operating solely on the input array.


# 4) WOULD IT HAVE BEEN EASIER TO SOLVE THIS PROBLEM USING A DIFFERENT PROGRAMMING STYLE?
# i think it would have been the same an example of an OOP would look like this:

# def flatten_and_sort(array):
#     flattened = []
#     for sublist in array:
#         for item in sublist:
#             flattened.append(item)
#     flattened.sort()
#     return flattened

# array = [[3, 2, 1], [7, 9, 8], [6, 5, 4]]
# result = flatten_and_sort(array)
# print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



# 5) WHY IN PARTICULAR IS FUNCTIONAL PROGRAMMING A HELPFUL PARADIGM WHEN SOLVING THIS PROBLEM?
# it is helpful because it keeps the code unchanged or immutable. it makes writing the functions in the same way to make it easier to understand and have less mistakes/

# OBJECT ORIENTED PROMPT

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_pod):
        other_pod.condition = "trashed"

# ONCE AN OBJECT ORIENTED SOLUTION HAS BEEN IMPLEMENTED, ANSWER THE FOLLOWING QUESTIONS:
# how does this solution demonstrate the four pillars of OOP? (this may not demonstrate all of them describe only those that apply)
# 
