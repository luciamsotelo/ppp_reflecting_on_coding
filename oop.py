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


# Example usage:
# Create an instance of Podracer
podracer1 = Podracer(500, "perfect", 1000)
print("Podracer 1 - Condition:", podracer1.condition)

# Use repair method on podracer1
podracer1.repair()
print("Podracer 1 after repair - Condition:", podracer1.condition)

# Create an instance of AnakinsPod
anakins_pod = AnakinsPod(800, "trashed", 2000)
print("Anakin's Pod - Max Speed:", anakins_pod.max_speed)

# Use boost method on anakins_pod
anakins_pod.boost()
print("Anakin's Pod after boost - Max Speed:", anakins_pod.max_speed)

# Create another instance of Podracer
podracer2 = Podracer(600, "perfect", 1500)
print("Podracer 2 - Condition:", podracer2.condition)

# Create an instance of SebulbasPod
sebulbas_pod = SebulbasPod(700, "perfect", 1800)
print("Sebulba's Pod - Condition:", sebulbas_pod.condition)


# ONCE AN OBJECT ORIENTED SOLUTION HAS BEEN IMPLEMENTED, ANSWER THE FOLLOWING QUESTIONS:
# how does this solution demonstrate the four pillars of OOP? (this may not demonstrate all of them describe only those that apply)

# ENCAPSULATION- is demonstrated here because it bundles the data together 

#ABSTRACTION- this code hides unnecessary information 

#ABSTRACTION - both the AnakisPod and the SebulbasPod inherit from the Podracer class. the child classes can inherit attributes from the parent class and reuses code where possible


#would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# its possible to use a different code style, however, OOP keeps the code dry and organizes, easy to follow and read 


#HOW IN PARTICULAR DID OOP ASSIST IN THE SOLVING OF THIS PROBLEM?
#it provided structure, the way it was coded helped show the different parts of podracing and its attributes. Using classes and inheritance helped to not duplicate code which kept it cleaner and easy to read and understand