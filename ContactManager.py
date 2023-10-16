import os
#Create file for containing text files if it does not already exist.
#Before anything else executes load the file containing all of the text files/contacts stored.


#Some preemptive comments to this sections of code!! *** IMPORTANT *** Since Shuniya is doing the file saving and loading, 
#the amount of work I can do on this function is relatively limited. Wether we choose to save contacts as individual text files or not will change how this code will run.
#For purposes of getting this function done I will use placeholder file names and the assumption that individual text files will be created for each contact.

#search_contact() works

def save_contact():
            file_root = os.path.dirname(__file__)  #gets the folder directory name for current program(whereever the contactmanager.py is saved)
            global name
            global phone
            global email

            contact_dict=[name ,email, phone]
            with open(file_root + "\\" + name + ".txt",'w') as file: #concatenates the folder directory name, the input name, and .txt; a file is created here. (IF THIS FILE EXISTS, THEN IT WILL BE DELETED!!!!!!)
                file.write(str(contact_dict))



def search_contact():

    os.system('cls')

    global contact_search
    global contact_file
    global search_again

    contact_search = input("Enter Contact Name: ")
    
    #Validate Input

    os.system('cls')    

    correct_input = input("You are searching for contact "+ contact_search +". Is this correct? Y or N? ")

    #Validate Input
    
    if correct_input == ("Y" or "y" or "Yes" or "yes"):
        file_root = os.path.dirname(__file__)

        global name
        global phone
        global email
        global search_file_path

        search_file_path = os.path.dirname(__file__) + "\\" + contact_search + ".txt"

        os.system('cls')
    
        try:

            

            with open(file_root + "\\" + contact_search + ".txt", "r") as file:

                contact_file = file.read()

                info_list = contact_file.strip('][').split(', ')
        
        except:
            
            search_contact_fail = input("""
            This Contact Does Not Exist.
                                        
            Search Contact Again (1)
            Return to Home Screen (2)
                  
            """)

            if search_contact_fail == '1':

                search_contact()

            if search_contact_fail == '2':

                home_screen()

            

        name = info_list[0]
        phone = info_list[1]
        email = info_list[2]

        print (f"Contact found.\nPhone number: "+ name +", Name: "+ phone +", Email: "+ email +".")

        search_again = input("""
        
        Search for Another Contact (1)
        Edit Contact (2)
        Delete Contact (3)                 
        Return to Home Screen (4) 
                             
        """)

        #Validate Inputs

        if search_again == '1':

            search_contact()

        if search_again == '2':

            edit_contact()

        if search_again == '3':

            remove_contact()

        if search_again == '4':

            home_screen()

        else:
            print("test")

            input("Press Enter to Return to Home Screen.")
            home_screen()

    else:
        search_contact()

#add_contact() works
def add_contact():

    os.system('cls')

    global correct_input
    global name
    global phone
    global email

    def input_name():
        
        os.system('cls')
       
        global name 
        
        name = input("Enter Name: ")
        
        if name.replace(" ", "").isalpha():
            
            print("Hello, " + name)
        
        else:
            
            print("Invalid name. Please, use only letters and spaces (e.g. John Doe)")
            
            input_name()
    input_name()

    def input_phone():
    
        global phone

        os.system('cls')

        phone = input("Enter your phone number: ")

        no_hyphen = phone.replace("-", "")

        ##checks to see if only digits and hyphens were entered.

        if no_hyphen.isdigit() and len(no_hyphen) == 10:

        ##reformatting of the phone number

            phone = no_hyphen[0] + no_hyphen[1] + no_hyphen[2] + "-" + no_hyphen[3] + no_hyphen[4] + no_hyphen[5] + "-" + no_hyphen[6] + no_hyphen[7] + no_hyphen[8] + no_hyphen[9]

            print("Your number is: " + phone)
        
        else:
        
            print("Invalid phone number. Please, use the following format: 123-456-7890")
        
            input_phone()
    input_phone()
        
    def input_email():
    
        global email

        os.system('cls')

        email = input("Enter your email: ")

        if email.count("@") == 1:

            if email.count(".") < 1:

                print("Invalid email. Please check that your email is typed in correctly. The email requires at least one period.")
                input_email()

        else:
    
            print("Invalid email. Please check that your email is typed in correctly. The email requires a single amperstand.")

            input_email()
    input_email()
    

    os.system('cls')

    print (f"You entered. Phone number: "+ name +", Name: "+ phone +", Email: "+ email +".")

    correct_input = input("Is this information correct? Y or N? ")

    #Validate Inputs

    #Save to dict if Information is correct. 

    if correct_input == ('Y'):
            
        os.system('cls')
        
    #Here you would save the info to a file, which I believe Shuniya volunteered to do. #saves the array as a string.

        save_contact()
        
        print("Saved information to Contacts.")

        #Below function works to go through the function again if incorrect information is entered.

    else:

        os.system('cls')

        input("Invalid Input Please Press Enter to Return.")

        add_contact()

#Edit_contact() works
def edit_contact():

    global name
    global phone
    global email

    os.system('cls')

    print (f"Pending changes:\nPhone number: "+ name +", Name: "+ phone +", Email: "+ email +".")

    change_contact_edit = input(

    """What part of the contact would you like to change?
                                            
    Name (1)
    Email (2)
    Phone Number (3)
    Confirm Changes (4)

    """)

        #Validate inputs

    if change_contact_edit == '1':
        name = input("Input new name: ")
        edit_contact()
    

    if change_contact_edit == '2':
        phone = input("Input new phone number: ")
        edit_contact()        
       

    if change_contact_edit == '3':
        email = input("Input new email: ")
        edit_contact()
    

    if change_contact_edit == '4':  #********THIS DOES NOT OVERWRITE THE ORIGINAL FILE. IT WILL SAVE A NEW FILE USING NAME.TXT********
                                #LIKELY WE WILL NEED TO USE THE os.remove() FUNTION TO DELETE THE OLD FILE
        save_contact()


def remove_contact():
    os.system('cls')
    
    global search_file_path
    global name

    print(search_file_path)

    correct_input = input("You Chose Contact "+ name +" is this Correct? Y or N? ")

    #Validate Input

    if correct_input.lower == "y":
        
        os.system('cls')

        print ("Deleting Contact "+ name +"...")

        os.remove(search_file_path)

        input("Press Enter to Return to Home Screen.")

    else:

        remove_contact()

#home_screen() works
def home_screen():

    global home_selection_choice

    os.system('cls')

    home_selection_choice = input("""Welcome to Contact Manager    
                                  

    Add Contact (1)
    Search Contact (2)
    Exit (3)

    """)

    #Input Validation

    if home_selection_choice == '1':
        
        add_contact()

        home_screen()

    if home_selection_choice == '2':

        search_contact()

        home_screen()

    if home_selection_choice == '3':

        #Close the file that houses all of the contacts.

        exit()


home_screen()
