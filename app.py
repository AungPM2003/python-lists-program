import sys

## [["kyaw",["apple","orange"]],["soe",["apple","orange"]],["moe",["apple","orange"]]]
## ["moe",["apple","orange"]]
##  ["kyaw",["apple","orange",]]

ppl_lists = []
print(" welcome from your ppl lists")

choice = ""
while choice != "4":
    print("""
      What do you want to do your lists
      1.Add-people  2.show your list 3.delete the list 4.quit
      """)

    choice = input("Please select one of the above \n")

    if choice == "1":
        ppl_name = input("what's the name you want to add,sir? \n")
        while True:
            ppl_lists += [ppl_name]
            more = input("Do you wanna add more? Y/N ")
            if more == "Y":
                ppl_name = input("what's the name you want to add,sir? \n")
            elif more == "N":
                break
            else:
                print("please enter Y or N only")

    elif choice == "2":
        print("Here is the lists")
        
        for i in range(len(ppl_lists)):
            i += 1
            print(f'{i}.{ppl_lists[i - 1]} \n')

        quit = input("Want to Quit? Y/N")
        if quit == "Y":
            break
        elif quit == "N":
            pass

    elif choice == "3":

        while True:
            delete_people = input("Enter the name of the people you want to remove? ")
            if delete_people in ppl_lists:
                ppl_lists.remove(delete_people)
                
            else:
                print(f'The name {delete_people} was not found')

            find = input("Do you still wanna find and remove? Y/N ")
            if find == "Y":
                pass
            elif find == "N":
                break
            else:
                print("Please enter only Y/N")
                
    elif choice == "4":
        sys.exit()
    else:
        print("i dont know what u choose  ")
