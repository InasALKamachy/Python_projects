class Grade:
  minimum_passing = 65 # is a variable that’s the same for every instance of the class
  name = "Jan van Eyck"
Grade_1 = Grade() # convert class to object
print(Grade_1.minimum_passing)
print(Grade_1.name)

#Methods are functions that are defined as part of a class. The first argument in a method is always the object that is calling the method.
# #Convention recommends that we name this first argument self. Methods always have at least this one argument.
class Dog:
    dog_time_dilation = 7

    def time_explanation(self):
        print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))


pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."
