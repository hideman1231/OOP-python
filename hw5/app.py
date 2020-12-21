from classes import AddressBook


def main():
    # CTRL + /
    address_book = AddressBook('address_book.csv')
    print('Address book initialized. Source is:'.format(address_book.fp))

    while True:
        command = input('What you want to do? ADD, SHOW, FIND, EXIT:')
        """
        Validate input to check that input in these four: ADD, SHOW, FIND, EXIT
        1. Exit: close the program
        2. Add: add record
        3. Show: display records
        4. Find: find records
        """
        if command == 'ADD':
            """
            Ask user what type he want to add (org, person)
            based on this, ask required fields and check field uniqueness if required.
            After adding record show success message in console
            """
            type_ = 'Organization'
            data = {'phone_number': 77777, 'address': '', 'name': 'Volya', 'category': 'razvod', 'first_name': '',
                    'last_name': '', 'email': ''}
            address_book.add_record(type_, data)
        if command == 'SHOW':
            """
            Ask type of records to show: org, person, all
            print records
            """
            type_ = 'all'
            address_book.get_records(type_)
        if command == 'FIND':
            """
            Ask for type of records to find: org, person, all
            Ask for string to find any text, at least 5 symbols
            print results
            """
            type_ = 'all'
            search_term = 'iVAn'
            address_book.find_record(type_, search_term)
        if command == 'EXIT':
            raise KeyboardInterrupt


if __name__ == '__main__':
    # Add try/except block to log every unhandled exception. (same as for lesson 4)
    try:
    	main()
    except Exception as err:
    	print(err)
