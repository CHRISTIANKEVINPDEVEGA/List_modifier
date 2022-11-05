def Main():
    Array=[1, 4, 3, 4, 4, 5, 6 ,2 ,8,26,4,50,8,32,97,8,3,1,1,13,22,2,6,2,60,65,2,76,62,0,57,23,53,8]
    
    def Menu_Intro(Array):
        
        print("Good day! this is my List Modifier program")
        print(f"This is the Initial List: {Array}")
        print("Menu:")
        print("1 -> Add an element")
        print("2 -> Insert an element")
        print("3 -> Modify an element")
        print("4 -> Delete an element")
        print("5 -> Arrange in ascending order")
        print("6 -> Arrange in descending order")
        return 

    def User_Input(Array):
        Users_num_input=input("What do you want to do? (1-6): ")
        return Users_num_input

    return Menu_Intro(Array), User_Input(Array)



Main()