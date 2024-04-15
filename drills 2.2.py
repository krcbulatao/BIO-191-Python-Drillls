age = int(input("Please enter your age: "))
born = str(input("Are you anatural born citizen of the U.S.? yes or no  "))
resided = int(input("Ho many years have you resided in the USA? "))
eligible = True

if age < 35:
    eligible = False
if born == 'no':
    eligible = False
if resided >= 15:
    eligible = True
if eligible:
    print ("You can for president of USA.")
else:
    print ("You cannot run for president of USA.")