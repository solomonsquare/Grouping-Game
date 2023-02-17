from Grouping import Group#imorting the Group Class created for grouping the list of names from the Grouping.py flie  

#i = 1
j = 0
everyone = []#Global empty list variable that would hold everyone
names = []#Global empty list of strings variable 
group_number = 0
number_of_people = 0

def user_inputs():
    i = 1
    while True:#this is used to catch an invalid value exception.
        try:#captures user input and checks if it's an integer.
            globals()['group_number'] = int(input("Please enter number of groups: "))
            globals()['number_of_people'] = int(input("Please enter the number of people:  "))
            break
        except ValueError:#if user's input is not an integer, it throws "ValueError" and prints the message bellow.
            print("please enter correct value")#it prints this message if the users input is not an integer

    while i <= number_of_people:
    
    
        names = list(input("Please enter names of everyone: "))#takes the names of everyone as string type
    
       
        while True:        #''.join(names[i])
            try:
                str(everyone.append(''.join(names)))#appends the names to a list seperated by "'" and ","
                break
            except ValueError:
                print("names must not contain a number")
        i = i + 1
    return group_number, number_of_people

user_inputs()

while int(len(everyone) % group_number) != 0:
    print("Cannot divide {0} people into {1} groups!".format(len(everyone), group_number))

    everyone = []
    names = []
    user_inputs()
grp = Group(everyone, group_number, number_of_people)#creating an object of the Group Class called grp
grp.divide_into_group(everyone, group_number)#calls the method divide_into_groups with the parameters to shuffle the names accurately.
    

#grp = Group(everyone, group_number, number_of_people)#creating an object of the Group Class called grp
#grp.divide_into_group(everyone, group_number)#calls the method divide_into_groups with the parameters to shuffle the names accurately.

