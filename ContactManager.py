#Import the required libraries for the program to function.
import os
import copy

#Declare variables that are used in multiple functions and do not require user input to be generated.
old_contact_name = 0
file_root = os.path.dirname(__file__)



def after_edit():

    #Remove old contact file.
    os.remove(file_root + "\\" + old_contact_name + ".txt")

    save_contact()


def save_contact():

        global name    
        global phone
        global email

        contact_dict=[name ,email, phone]
        with open(file_root + "\\" + name.replace("'","") + ".txt",'w') as file: #concatenates the folder directory name, the input name, and .txt; a file is created here. (IF THIS FILE EXISTS, THEN IT WILL BE DELETED!!!!!!)
            file.write(str(contact_dict))
        
        os.system('cls')

        input("Contact Saved Press Enter to Return.")

        home_screen()



def search_fail():

    os.system('cls')

    global search_contact_fail

    search_contact_fail = input("""
    This Contact Does Not Exist or Was Not Attempted to be Accessed.
                                            
    Search Contact Again (1)
    Return to Home Screen (2)
                    
    """)

    if search_contact_fail == '1':

        search_contact()

    if search_contact_fail == '2':

        home_screen()
                
    else:
                    
        os.system('cls')

        input("Invalid Input Press Enter to Continue.")

        search_fail()



def search_contact():

    file_root = os.path.dirname(__file__)

    os.system('cls')

    global old_contact_name
    global contact_search
    global contact_file

    contact_search = input("Enter Contact Name: ")
    
    if os.path.exists(file_root + "\\" + contact_search + ".txt"):

        os.system('cls')    

        correct_input = input("You are searching for contact "+ contact_search +". Is this correct? Y or N? ")

        if correct_input == 'Y':

            global name
            global phone
            global email
            global search_file_path

            search_file_path = os.path.dirname(__file__) + "\\" + contact_search + ".txt"

            os.system('cls')

        else:

            os.system('cls')

            input("Please Press Enter to Return.")

            search_fail()

        try:

            with open(file_root + "\\" + contact_search + ".txt", "r") as file:

                contact_file = file.read()

                info_list = contact_file.replace('"','').strip('][').split(', ')

                name = info_list[0]
                email = info_list[1]
                phone = info_list[2]

        except:

            search_fail()

    else:

        os.system('cls')
        def inc_spelling():

            incorrect_spelling = input("""
                
                The File """ + contact_search + " Does Not Exist, Please Check Spelling. "
                
                """\n
                Search Again (1)  
                Go to Home Menu (2)  
                
                """)
            
            if incorrect_spelling == '1':

                search_contact()

            if incorrect_spelling == '2':

                home_screen()

            else:

                input("Invalid Input Press Enter to Continue")

                inc_spelling()
        
        inc_spelling()

    def search_again_menu():

        os.system('cls')

        print (f"Contact found.\nName: "+ name.replace("'","") +", Phone Number: "+ phone.replace("'","") +", Email: "+ email.replace("'","") +".")

        search_again = input("""
            
        Search for Another Contact (1)
        Edit Contact (2)
        Delete Contact (3)                 
        Return to Home Screen (4) 
                                
        """)


        if search_again == '1':

            search_contact()

        if search_again == '2':

            edit_contact()

        if search_again == '3':

            remove_contact()

        if search_again == '4':

            home_screen()

        else:

            os.system('cls')

            input("Press Enter to Return.")

            search_again_menu()

    search_again_menu()

def add_contact():

    os.system('cls')

    global name
    global phone
    global email

    
    input_name()

    input_phone()

    input_email()
    

    os.system('cls')

    def cor_input():

        global correct_input

        os.system('cls')

        print (f"You entered. Name: "+ name +", Phone Number: "+ phone +", Email: "+ email +".")

        correct_input = input("Is this information correct? Y or N? ")

        if correct_input == ('Y'):
            
            os.system('cls')

            save_contact()

            home_screen()
        
        else:

            os.system('cls')

            input("Invalid Input Please Press Enter to Return.")

            cor_input()

    cor_input()


def edit_contact():

    global old_contact_name
    global name
    global phone
    global email

    old_contact_name = copy.deepcopy(contact_search)

    os.system('cls')

    print (f"Pending changes:\nName: "  + name.replace("'","") + ", Phone Number: "+ phone.replace("'","") +", Email: "+ email.replace("'","") +".")

    change_contact_edit = input("""

    What part of the contact would you like to change?
                                            
    Name (1)
    Phone Number (2)
    Email (3)
    Confirm Changes (4)

    """)

    if change_contact_edit == '1':
        #name = input("Input new name: ")

        input_name()
        
        edit_contact()
    

    if change_contact_edit == '2':
        #phone = input("Input new phone number: ")

        input_phone()

        edit_contact()        
       

    if change_contact_edit == '3':
        #email = input("Input new email: ")

        input_email()

        edit_contact()
    

    if change_contact_edit == '4':  
                    
        after_edit()



def remove_contact():
    os.system('cls')
    
    global search_file_path
    global name


    correct_input = input("You Chose to Delete Contact "+ name +" is this Correct? Y or N? ")

    if correct_input == 'Y':
        
        os.system('cls')

        print ("Deleting Contact "+ name +"...")

        os.remove(search_file_path)

        input("Press Enter to Return to Home Screen.")

        home_screen()

    else:
        def bypass():
            
            os.system('cls')

            bypass_input = input(""" 
                
                Bypassing Deletion 

                Remove Different Contact (1)
                Go to Home Screen (2)
                
                """)
            
            if bypass_input == '1':

                search_contact()
            
            if bypass_input == '2':

                home_screen()
            
            else:

                input("Invalid Input Press Enter to Continue")

                bypass()
        
        bypass()



def home_screen():

    global home_selection_choice

    os.system('cls')

    home_selection_choice = input("""Welcome to Contact Manager    
                                  

    Add Contact (1)
    Search Contact (2)
    Exit (3)

    """)

    if home_selection_choice == '1':
        
        add_contact()

        home_screen()

    if home_selection_choice == '2':

        search_contact()

        home_screen()

    if home_selection_choice == '3':

        exit()
    
    else:

        os.system('cls')

        input("Invalid Input Press Enter to Continue")

        home_screen()

def input_name():
    
    os.system('cls')
       
    global name 
        
    name = input("Enter Name: ")
        
    if name.replace(" ", "").isalpha():
            
        print("Hello, " + name)
        
    else:
            
        print("Invalid name. Please, use only letters and spaces (e.g. John Doe)")
            
        input_name()
    
def input_phone():
    global phone

    os.system('cls')

    phone = input("Enter phone number: ")

    no_hyphen = phone.replace("-", "")

    ##checks to see if only digits and hyphens were entered.

    if no_hyphen.isdigit() and len(no_hyphen) == 10:

    ##reformatting of the phone number

        phone = no_hyphen[0] + no_hyphen[1] + no_hyphen[2] + "-" + no_hyphen[3] + no_hyphen[4] + no_hyphen[5] + "-" + no_hyphen[6] + no_hyphen[7] + no_hyphen[8] + no_hyphen[9]

        print("Your number is: " + phone)
        
    else:
        
        print("Invalid phone number. Please, use the following format: 123-456-7890")
        
        input_phone()
        
def input_email():
    
    global email

    os.system('cls')

    email = input("Enter email: ")

    if email.count("@") == 1:

        if email.count(".") < 1:

            print("Invalid email. Please check that your email is typed in correctly. The email requires at least one period.")
            input_email()

    else:
    
        print("Invalid email. Please check that your email is typed in correctly. The email requires a single amperstand.")

        input_email()
    

home_screen()


