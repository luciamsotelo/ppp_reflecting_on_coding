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

# ENCAPSULATION- is demonstrated here because it bundles the data together 

#ABSTRACTION- this code hides unnecessary information 

#ABSTRACTION - both the AnakisPod and the SebulbasPod inherit from the Podracer class. the child classes can inherit attributes from the parent class and reuses code where possible


#would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# its possible to use a different code style, however, OOP keeps the code dry and organizes, easy to follow and read 


#HOW IN PARTICULAR DID OOP ASSIST IN THE SOLVING OF THIS PROBLEM?
#it provided structure, the way it was coded helped show the different parts of podracing and its attributes. Using classes and inheritance helped to not duplicate code which kept it cleaner and easy to read and understand