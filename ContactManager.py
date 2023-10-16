import os
import os.path 
path='contacts'
check_file=os.path.isfile(path)

print(check_file)


contact_manager=open('contacts', "w" ) 

#Create file for containing text files if it does not already exist.
#Before anything else executes load the file containing all of the text files/contacts stored.

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


def add_contact():

    os.system('cls')

    global contact_dict
    global correct_input
    global name
    global phone
    global email

    input_name()
    input_phone()
    input_email()


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
    
    

    os.system('cls')

    print (f"You entered. Phone number: "+ name +", Name: "+ phone +", Email: "+ email +".")

    correct_input = input("Is this information correct? Y or N? ")

    #Validate Inputs

    #Save to dict if Information is correct. 

    if correct_input == ("Y" or "y" or "Yes" or "yes"):
            
        os.system('cls')
        
    #Here you would save the info to a file, which I believe Shuniya volunteered to do.
        def save_contact():
            file_root = os.path.dirname(__file__)  #gets the folder directory name for current program(whereever the contactmanager.py is saved)
            global name
            global phone
            global email

            contact_dict=[name ,email, phone]
            with open(file_root + "\\" + name + ".txt",'w') as file: #concatenates the folder directory name, the input name, and .txt; a file is created here. (IF THIS FILE EXISTS, THEN IT WILL BE DELETED!!!!!!)
                file.write(str(contact_dict)) #saves the array as a string.

        save_contact()
        
        print("Saved information to Contacts.")

        #Below function works to go through the function again if incorrect information is entered.

    else:

        os.system('cls')

        input("Invalid Input Please Press Enter to Return.")

        add_contact()


#Some preemptive comments to this sections of code!! *** IMPORTANT *** Since Shuniya is doing the file saving and loading, 
#the amount of work I can do on this function is relatively limited. Wether we choose to save contacts as individual text files or not will change how this code will run.
#For purposes of getting this function done I will use placeholder file names and the assumption that individual text files will be created for each contact.

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
        
        os.system('cls')
        
        contact_file = open(+contact_search+".txt", "r")
        
        print(contact_file.read())

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

            input("Press Enter to Return to Home Screen.")

    else:
        search_contact()


def edit_contact():

    global contact_file_edit
    global contact_search
    global correct_input
    global change_contact

    os.system('cls')

    contact_search = input("Please Enter the Name of Contact you Wish to Edit: ")
    
    #Validate input

    os.system('cls')    

    correct_input = input("You are searching for contact "+ contact_search +". Is this correct? Y or N? ")
    
    #Validate input

    if correct_input == ("Y" or "y" or "Yes" or "yes"):
        
        os.system('cls')

        with open(+contact_search+".txt", "w") as oldcontact:

            print(oldcontact.read())

            #Here needs to be a way to convert the file information to dictionary form or pull it directly as dictionary form, seperating it into the three variables: name, email, phone number.
        
        change_contact = input(

        """What part of the contact would you like to change?
                                            
        Name (1)
        Email (2)
        Phone Number (3)
        Cancel Changes (4)

        """)

        #Validate inputs

        if change_contact == '1':

            os.system('cls')
        
        print("Saved information to Contacts.")

            print("thisisaplaceholder")
            #Here needs to be added the ability to change specific parts of the file in accordance with user request (name).
            print("Here is the current name of the contact")
            print(name)
            new_name=input("please enter the new name ")
            contact_dict[name]=new_name
        if change_contact == '2':

            os.system('cls')

            print("thisisaplaceholder")
            #Here needs to be added the ability to change specific parts of the file in accordance with user request (email).
            contact_dict[name,email,phone]
            print('this is the current email in tha contact')
            print(email)
            new_email= input("please neter the new email")
            contact_dict[email]=new_email
        if change_contact == '3':

            os.system('cls')

            print("thisisaplaceholder")
            #Here needs to be added the ability to change specific parts of the file in accordance with user request (phone number).
            contact_dict[name,email,phone]
            print('this is the current phone number in the contact')
            print(phone)
            new_phone=input('please enter the new phone number')
            contact_dict[phone]=new_phone
        else:
            os.system('cls')
            input("Press Enter to Return to Home Screen.")
            home_screen()




def remove_contact():

    os.system('cls')

    global contact_removal
    global correct_input

    contact_removal = input("Enter Name of Contact you wish to Remove: ")

    #Validate Input

    os.system('cls')

    correct_input = input("You Chose Contact "+ contact_removal +" is this Correct? Y or N? ")

    #Validate Input

    if correct_input == ("Y" or "y" or "Yes" or "yes"):
        
        os.system('cls')

        print ("Deleting Contact "+ contact_removal +"...")

        os.remove(+contact_removal+".txt")

        input("Press Enter to Return to Home Screen.")

    else:

        remove_contact()
