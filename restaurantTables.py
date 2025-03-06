# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]



#Bonus level
def nice_format(number, size):
    if size == 0:
        print(f'We have found a free table at table {number}.')
    else:
        print(f'We have found a free table at table {number}, which holds {size} people.')




#Level 1
def find_empty_seats(table_list, timeslot, print_fancy):
    open_tables = []
    letter_order = 1
    i = 0
    for table in table_list[timeslot]:                  #looks at all elements in the time slot.
        if table == 'o':                                  #checks if the table is free
            open_tables.append(table_list[0][i])            #adds free tables to a list
            for character in table_list[0][i]:              #checks every character in the table of the "o"
                if character.isnumeric():                   #checks if the character has a numerical value
                    if letter_order == 1:                       #makes sure the number it's looking at is the table number
                        table_number = int(character)           #ensures the table number is an integer
                        letter_order = 2                    #says the next number will be the capacity
                        if print_fancy:                         #since this function is used in level 2, printing is optional
                            nice_format(table_number, 0)        #prints all free tables in the nice format
                    else:                                   #in case the number was the capacity:
                        letter_order = 1                #says the nect number will be the table number
        i += 1
    return open_tables                              #returns the actual list of open tables for other functions to build on




#Level 2
def capacity_table(size):
    free_tables = find_empty_seats(restaurant_tables2, time_request, False)
    letter_order = 1
    for word in free_tables:                        #singles out each element in the list
        for character in word:                      #singles out each digit in the element
            if character.isnumeric():                   #if the digit holds a number value:
                capacity = int(character)                   #force it to be an integer type.
                if letter_order == 2:                           #if it's the second number in the element(capacity):
                    letter_order =  1                       #in the next element, the first number will be seen as a table number
                    if capacity >= size:                        #check if the capacity is big enough
                        nice_format(table_number, capacity)     #prints the capacity and table number nicely
                        return capacity                         #ensures the function only prints one table, by ending it.
                else:                                       #if it's the first number in the element(table number):
                    table_number = capacity                 #saves the table number IN CASE the capacity is big enough.
                    letter_order = 2                        #in the next element, the first number will be seen as a capacity




#Level 3
def capacity_poly_tables(list, size, time):
    table_count = 0
    letter_order = 1
    for word in list[0]:                                #isolates each table in the header row
        if word != 0:                                   #makes sure it starts on a table insteas of the orgin
            for character in word:                          #isolates each digit in the table
                if character.isnumeric():                   #checks if the digit has a number value
                    capacity = int(character)                   #forces the digit to be an integer
                    if letter_order == 2:                       #checks if the digit is a capacity
                        letter_order = 1                            #the next element's first number will be seen as a table number.
                        if capacity>=size and list[time][table_count]=='o':     #checks if the table is big enough AND free
                            nice_format(table_number, capacity)             #nicely prints the table number and capacity
                    else:                                           #if the digit was a table number:
                        table_number = capacity                     #save the table number in a variable
                        letter_order = 2                            #the next element's first number will be seen as a table number.
        table_count += 1                                        #moves to next table/element
                



'''
The link to my brainstorming whiteboard (Miro) is here:
https://miro.com/app/board/uXjVIfuT-Ys=/?share_link_id=465671883638
Please reach out to me at noelle.rangel15@gmail.com if it doesnt work once logged in to Miro.
'''
time_request = int(input('What time slot would you like to be seated in? '))

#add a hashtag to the levels you dont wanna test, the bonus level is called in each function.
find_empty_seats(restaurant_tables2, time_request, True)                #Level 1, prints all available tables in the timeslot.
party_size = int(input('How many people does your party contain? '))            #not needed for level 1.
capacity_table(party_size)                                             #Level 2, prints table that can fit the party size.
capacity_poly_tables(restaurant_tables2, party_size, time_request)     #Level 3, prints all tables that can fit the party size.