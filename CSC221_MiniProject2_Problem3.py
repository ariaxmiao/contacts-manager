def store_name(user_name): # Define a method for storing names from user input
    # Assume names are inputted in the format 'First Last'; standardize
    user_name = user_name.strip().lower().title()
    name_list = user_name.split()
    name_dict = {'last': None, 'first': None}

    # To distinguish between first and last, store name values in a dict
    # that will compose one dimension of the three-dimensional master list
    if len(name_list) == 2:
        for i in range(len(name_list)):
            if i == 0:
                name_dict['first'] = name_list[i]
            else:
                name_dict['last'] = name_list[i]
    else:
        print('\nERROR: Please enter name in the format "First Last."\n')
        quit() # Program doesn't allow for names three words and above

    return name_dict


def store_phone(user_phone): # Define a method for storing phone numbers from user input
    # Assume phone numbers are inputted as a string of 10 digits without delimiters    
    if (user_phone.isdigit()):
        user_phone = int(user_phone)
        
        # Fetch the various components and standardize their format,
        # then store as an f-string that unlike name_dict doesn't
        # occupy its own dimension
        if user_phone // 10000000000 == 0:
            area_code = user_phone // 10000000
            prefix = (user_phone // 10000) % 1000
            line_number = user_phone % 10000

            full_phone = f'({area_code}) {prefix}-{line_number}'
        
        else:
            print('\nERROR: Please enter phone number as ten unbroken digits.\n')
            quit()

    else:
        print('\nERROR: Please enter phone number as ten unbroken digits.\n')
        quit()

    return full_phone


def store_address(user_address): # Define a method for storing addresses from user input
    # Assume addresses are inputted in the format 'Street, City, State Zip'; standardize
    user_address = user_address.strip().lower().title()
    address_list = user_address.split(',')
    # List comprehension for stripping hanging spaces after commas are removed
    address_list = [i.strip() for i in address_list]

    # Since state and zip aren't separated by a comma,
    # some extra steps to extract both pieces of data
    state_plus_zip = address_list.pop(-1)
    state_zip_list = state_plus_zip.split()
    address_list.extend(state_zip_list)

    address_dict = {'street': None, 'city': None, 'state': None, 'zip': None}

    # Populate a dict that distinguishes between the different parts of an address,
    # its own dimension in the master list
    if len(address_list) == 4:
        for i in range(len(address_list)):
            if i == 0:
                address_dict['street'] = address_list[i]
            elif i == 1:
                address_dict['city'] = address_list[i]
            elif i == 2:
                address_dict['state'] = address_list[i].upper()
            else:
                address_dict['zip'] = address_list[i]
    else:
        print('\nERROR: Please enter address in the format "Street, City, State Zip."\n')
        quit() # Program doesn't allow for more specific addresses (e.g., apt. #, etc.)

    return address_dict


# Define a method for aggregating all data relevant to one person
# in one container, the second dimension in the 3D master list
def create_contact(name, phone, email, address):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    return contact


# Define a method for printing the complete contacts list as a table
def print_full_table(user_contacts):
    print('\nContacts for This Session') # Print header
    print(f'{"CONTACT #":<15}{"NAME":<30}{"PHONE NUMBER":<20}{"EMAIL ADDRESS":<35}{"PHYSICAL ADDRESS"}')

    for i in range(1, len(user_contacts)): # Loop through the contact elements
        # Access data using layered index references; 2D locations require two indices
        # while 3D locations require three
        name = f'{user_contacts[i]["name"]["first"]} {user_contacts[i]["name"]["last"]}'
        phone = f'{user_contacts[i]["phone"]}'
        email = f'{user_contacts[i]["email"]}'

        street_plus_city = f'{user_contacts[i]["address"]["street"]}, {user_contacts[i]["address"]["city"]}'
        state_plus_zip = f'{user_contacts[i]["address"]["state"]} {user_contacts[i]["address"]["zip"]}'
        address = f'{street_plus_city}, {state_plus_zip}'

        print(f'{i:<15}{name:<30}{phone:<20}{email:<35}{address}')
    
    print()


# Define a method for printing just phone numbers (plus names) as a table
def print_phone_table(user_contacts):
    print('\nPhone Numbers for This Session')
    print(f'{"CONTACT #":<15}{"NAME":<30}{"PHONE NUMBER":<20}')

    for i in range(1, len(user_contacts)):
        name = f'{user_contacts[i]["name"]["first"]} {user_contacts[i]["name"]["last"]}'
        phone = f'{user_contacts[i]["phone"]}'

        print(f'{i:<15}{name:<30}{phone:<20}')
    
    print()


# Define a method for printing just cities and states (plus names) as a table;
# this is where the differentiated address components come into effect
def print_place_table(user_contacts):
    print('\nLocations for This Session')
    print(f'{"CONTACT #":<15}{"NAME":<30}{"LOCATION"}')

    for i in range(1, len(user_contacts)):
        name = f'{user_contacts[i]["name"]["first"]} {user_contacts[i]["name"]["last"]}'
        city_plus_state = f'{user_contacts[i]["address"]["city"]}, {user_contacts[i]["address"]["state"]}'

        print(f'{i:<15}{name:<30}{city_plus_state}')
    
    print()


# Define a method for printing just a phone number given the contact's full name
def print_phone_given_name(user_contacts, user_name):
    user_name = user_name.strip().lower().title()
    name_list = user_name.split()

    found = False

# Since all info for one contact is stored in the same first-dimension location,
# I can drill down to any other data (phone) given one piece of data (name)
    for i in range(1, len(user_contacts)):
        if (name_list[0] == user_contacts[i]['name']['first']):
            if (name_list[1] == user_contacts[i]['name']['last']):
                found = True
                print()
                print(user_contacts[i]['phone'])
    print()

    if found == False:
        print('ERROR: No match found. Try again.\n')


# Define a method for printing just an address given the contact's first name
# using the same method as above
def print_address_given_first(user_contacts, first_name):
    first_name = first_name.strip().lower().title()

    found = False

    for i in range(1, len(user_contacts)):
        if (first_name == user_contacts[i]['name']['first']):
            found = True

            street_plus_city = f'{user_contacts[i]["address"]["street"]}, {user_contacts[i]["address"]["city"]}'
            state_plus_zip = f'{user_contacts[i]["address"]["state"]} {user_contacts[i]["address"]["zip"]}'
            address = f'{street_plus_city}, {state_plus_zip}'

            print()
            print(address)
    print()

    if (found == False) and (first_name != 'Quit'):
        print('ERROR: No match found. Try again.\n')


if __name__ == '__main__':
    # Initialize the master container ContactList with some sample info at index 0,
    # to visualize the format of a 3D list
    ContactList = [
        {
            'name': {'last': 'Doe', 'first': 'Jane'},
            'phone': '(888) 888-8888',
            'email': 'janedoe@gmail.com',
            'address': {'street': '111 Main St', 'city': 'Greenville', 'state': 'AK', 'zip': '12345'}
        }
    ]

    iteration = 1 # Initialize count variable
    check = 1 # Initialize sentinel value check
    print('\nLet\'s get started by adding your first contact.\n')

    while check != 0: # Sentinel value is 0
        print(f'CONTACT {iteration}')
        # Store all data for one contact separately
        user_name = store_name(input('Enter first and last name: '))
        user_phone = store_phone(input('Enter phone number: '))
        user_email = input('Enter email address: ')
        user_address = store_address(input('Enter physical address: '))

        # Then aggregate them in a temporary dict that is appended to the master list
        curr_contact = create_contact(user_name, user_phone, user_email, user_address)
        ContactList.append(curr_contact)

        iteration += 1
        # Allow user to decide when to stop entering
        check = int(input('\nKeep going? Type 1 for yes and 0 for no: '))
        print()

    next_step = None # Initialize sentinel value check

    while next_step != 'quit': # Sentinel value is 'quit'
        # Allow user to decide how they want to view the data
        next_step = input(
            'What next? Choose from the list of options below:\n\n' \
            '\t(type "ALL") Display all contacts from this session\n' \
            '\t(type "PHONE") List all phone numbers from this session\n' \
            '\t(type "PLACES") List all locations from this session\n' \
            '\t(enter FULL NAME) Display one person\'s phone number\n' \
            '\t(enter FIRST NAME) Display one person\'s address\n' \
            '\t(type "QUIT") End the session\n\n'
        )
        if next_step.lower() == 'all':
            print_full_table(ContactList)
        elif next_step.lower() == 'phone':
            print_phone_table(ContactList)
        elif next_step.lower() == 'places':
            print_place_table(ContactList)
        elif len(next_step.split()) == 2:
            print_phone_given_name(ContactList, next_step)
        elif len(next_step.split()) == 1:
            print_address_given_first(ContactList, next_step)
        elif next_step.lower() == 'quit':
            break
        else:
            print('\nERROR: Please choose from the list of options.\n')