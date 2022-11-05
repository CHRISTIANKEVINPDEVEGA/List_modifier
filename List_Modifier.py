def Main():
    Array=[1, 4, 3, 4, 4, 5, 6, 2, 8, 26, 4, 50, 8, 32, 97 ,8 ,3 ,1 ,1 ,13 ,22 ,2 ,6 ,2 ,60 ,65 ,2 ,76 ,62 ,0 ,57 ,23 ,53 ,8]
    
    def Menu_Intro(Array):
        
        print("Good day! this is my List Modifier program")
        print(f"This is the Initial List: {Array}")
        print("Menu:")
        print("1 -> Add an element")
        print("2 -> Insert an element")
        print("3 -> Count the number of an element")
        print("4 -> Delete an element")
        print("5 -> Arrange in ascending order")
        print("6 -> Arrange in descending order")
        return 

    def User_Input(Array):
        Users_num_input=int(input("What do you want to do? (1-6): "))
        if Users_num_input == 1:
                print("You chose the Add an element option")
                user_add=int(input("Add an element to the list: "))
                Array.append(user_add)
                print(Array)
        if Users_num_input == 2:
                print("You chose the Insert an element option")
                user_element=int(input("enter the element to be added: "))
                user_Index=int(input("enter the index for the element: "))
                Array.insert(user_Index,user_element)
                print(Array)
        if Users_num_input == 3:
                print("You chose the Count the number of an element option")
                user_count=int(input("Pick an element to be counted: "))
                Array_counter=Array.count(user_count)
                print(Array_counter)                
        if Users_num_input == 4:
                print("You chose the Delete an element option")
                user_add=int(input("Add an element to the list: "))
        if Users_num_input == 5:
                print("You chose the Arrange in ascending order option")
                user_add=int(input("Add an element to the list: "))
        if Users_num_input == 6:
                print("You chose Arrange in descending order option")
                user_add=int(input("Add an element to the list: "))
        return 
    return Menu_Intro(Array), User_Input(Array)



Main()