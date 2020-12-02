class Person:
    age = 0
    def __init__(self,initialAge):
        #  run some checks on initialAge
        if initialAge < 0:
            print ("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    def amIOld(self):
        #  print out the correct statement to the console
        if self.age < 13:
            print ("You are young.")
        elif self.age >= 13 and self.age < 18:
            print ("You are a teenager.")
        else:
            print ("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
