age = int(input("What is your age? "))
license = str (input("Do you have a fishing license? yes or no "))
parents = str (input("Does your parent have a fishing license in MN? yes or no "))

if age <= 15 and license == 'yes':
    print ("You are legal to fish in MN.")
elif parents == 'yes':
    print ("You are legal to fish in MN.")
else:
    print ("You are not legal to fish in MN.")
