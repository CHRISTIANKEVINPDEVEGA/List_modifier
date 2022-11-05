import os


def Main(Array):
    def Menu_Intro(Array):
        print(f"This is the List: {Array}")
        print("Menu:")
        print("1 -> Add an element")
        print("2 -> Insert an element")
        print("3 -> Count the number of an element")
        print("4 -> Delete an element")
        print("5 -> Arrange in ascending order")
        print("6 -> Arrange in descending order")
        print("7 -> Modify an element")
        print("8 -> Close the program")
        return 


    def User_Input(Array):
        Users_num_input=int(input("What do you want to do? (1-8): "))
        if Users_num_input == 1:
                print("You chose the Add an element option")     
                for tries in range(1000):
                    user_add=int(input("Add an element to the list: "))
                    os.system('cls')
                    Array.append(user_add)
                    print(Array)
                    User_path=str(input("Do you want to add another element? "))
                    if User_path=="yes":
                        continue
                    elif User_path=="no":
                        User_Menu_Input=input("Do you wish to go back to Menu? Enter yes or no: ")
                        if User_Menu_Input == "yes":
                            Main(Array)
                        elif User_Menu_Input == "no":
                         print("Thank you for using List Modifier program.")
                        break
                    else:
                        print("error")
                        break
        elif Users_num_input == 2:
                print("You chose the Insert an element option")
                for tries in range(1000):
                    user_element=int(input("enter the element to be added: "))
                    user_Index=int(input("enter the index for the element: "))
                    os.system('cls')
                    Array.insert(user_Index,user_element)
                    print(Array)
                    User_path=str(input("Do you want to insert another element? "))
                    if User_path=="yes":
                            continue
                    elif User_path=="no":
                        User_Menu_Input=input("Do you wish to go back to Menu? Enter yes or no: ")
                        if User_Menu_Input == "yes":
                                Main(Array)
                        elif User_Menu_Input == "no":
                            print("Thank you for using List Modifier program.")
                            break
                    else:
                            print("error")
                            break
        elif Users_num_input == 3:
                print("You chose the Count the number of an element option")
                for tries in range(1000):
                    user_count=int(input("Pick an element to be counted: "))
                    os.system('cls')
                    Array_counter=Array.count(user_count)
                    print(Array_counter)   
                    User_path=str(input("Do you want to count another element? "))
                    if User_path=="yes":
                            continue
                    elif User_path=="no":
                        User_Menu_Input=input("Do you wish to go back to Menu? Enter yes or no: ")
                        if User_Menu_Input == "yes":
                                Main(Array)
                        elif User_Menu_Input == "no":
                            print("Thank you for using List Modifier program.")
                            break
                    else:
                            print("error")
                            break             
        elif Users_num_input == 4:
                print("You chose the Delete an element option")
                for tries in range(1000):
                    user_delete=int(input("Pick an element to be deleted from the list: "))
                    os.system('cls')
                    Array.remove(user_delete)
                    print(Array)
                    User_path=str(input("Do you want to deleted another element? "))
                    if User_path=="yes":
                            continue
                    elif User_path=="no":
                        User_Menu_Input=input("Do you wish to go back to Menu? Enter yes or no: ")
                        if User_Menu_Input == "yes":
                                Main(Array)
                        elif User_Menu_Input == "no":
                            print("Thank you for using List Modifier program.")
                            break
                    else:
                            print("error")
                            break
        elif Users_num_input == 5:
                print("You chose the Arrange in ascending order option")
                input("Enter any key to arrange the elements in ascending order ")
                os.system('cls')
                Array.sort()
                print(Array)
                User_Menu_Input=input("Do you wish to go back to Menu? Enter yes or no: ")
                if User_Menu_Input == "yes":
                        Main(Array)
                elif User_Menu_Input == "no":
                        print("Thank you for using List Modifier program.")
        elif Users_num_input == 6:
                print("You chose the Arrange in descending order option")
                input("Enter any key to arrange the elements in descending order ")
                os.system('cls')
                Array.sort(reverse=True)
                print(Array)
                User_Menu_Input=input("Do you wish to go back to Menu? Enter yes or no: ")
                if User_Menu_Input == "yes":
                        Main(Array)
                elif User_Menu_Input == "no":
                        print("Thank you for using List Modifier program.")
        elif Users_num_input == 7:
                print("You chose the Modify an element option")
                for tries in range(1000):
                    user_replace=int(input("enter the element to replace: "))
                    user_index=int(input("enter the index of the element to be replaced: "))
                    os.system('cls')
                    Array.pop(user_index);Array.insert(user_index,user_replace)
                    print(Array)
                    User_path=str(input("Do you to modify another element? "))
                    if User_path=="yes":
                            continue
                    elif User_path=="no":
                        User_Menu_Input=input("Do you wish to go back to Menu? Enter yes or no: ")
                        if User_Menu_Input == "yes":
                                Main(Array)
                        elif User_Menu_Input == "no":
                            print("Thank you for using List Modifier program.")
                            break
                    else:
                            print("error")
                            break
        elif Users_num_input == 8:
            print("Thank you for using List Modifier program.")
        else :
            User_Input(Array)               
        return 
    return Menu_Intro(Array), User_Input(Array)


Array=[1, 4, 3, 4, 4, 5, 6, 2, 8, 26, 4, 50, 8, 32, 97 ,8 ,3 ,1 ,1 ,13 ,22 ,2 ,6 ,2 ,60 ,65 ,2 ,76 ,62 ,0 ,57 ,23 ,53 ,8]
print("Good day! this is my List Modifier program") 
Main(Array)