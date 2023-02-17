import random #importing random makes you able to use the random module which has the ability to shuffle items randomly with its shuffle method.

#groups_list = []
all_names = list()


class Group(object): # A "Group" class to professionally hold the variables and functions of the program
    
    #all_names = list()
    #groups_list = []
    
    def __init__(self, all_names, number_of_groups, number_of_people): #Initializing the Class so it can be called as an object
        self.allnames = all_names                   #variable to hold all the names of poeple in the group
        self.number_of_groups = number_of_groups    #variable to hold the number of groups
        self.number_of_people = number_of_people    #variable to hold the number of people in the group

    
    def divide_into_group(self, all_names, number_of_groups):#method that divides list of people into groups, with two parameters: all_names and number_of_groups as inputs 
        a = 1
        #number_of_groups -= 1
        #for j in list(range(0, len(all_names))):
            
            #all_names.append(all_names[j])
            
            #j = j + 1
        print(all_names)#prints all the names to show users the order they entered the names
        random.shuffle(all_names) #shuffles the names randomly with the shuffle method in the random module
      
                
        
        sliced = int(len(all_names)/number_of_groups)#calculates the number the list of people will be divided into.
        chunk = [all_names[i:i + sliced] for i in range(0, len(all_names), sliced)]#using list comprehension to create a list of the shuffled  group inside the list of all names entered
        print(chunk)#printing the result
        
        
