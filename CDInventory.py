#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Deborah C, 2022-Nov-20, Modified File to Add Functions
# Deborah C. 2022-Nov-23, Began Modifications to Add Error Handling & Pickling
# Deborah C. 2022-Nov-27, Work on Error Handling & Pickling
# Deborah C. 2022-Nov-23, Program Re-Creation and Editing
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # List of dictionaries to hold data
dicRow = {}  # Dictionary of data as a row
strFileName = 'CDInventory.dat'  # Data storage file
objFile = None  # File object
strID = '' # User-generated CD number
strTitle = '' # CD Title
stArtist = '' # CD Artist/s

import pickle
pickling = open('CDInventory.dat', 'rb+')
pickle.dump(lstTbl, pickling)
pickling.close()
print('\nUnpickling the Table')
lstTbl = open('CDInventory.dat', 'rb+')
pickling.close()

# -- PROCESSING -- #
class DataProcessor:
    """Processing the data provided by the user"""
    # TODONE add functions for processing here
    
    @staticmethod
    def update_table():
        """
        Takes the three pieces of new data provided by the user, the CD's user-generated ID, its title, and its artist/s, and then adds them into the 2D table known as lstTbl.

        Args:
            None

        Returns:
            None

        """
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        lstTbl.append(dicRow) 
       
    @staticmethod
    def delete_cd(numchoice):
        """
        Deletes the CD chosen by the user, via accessing each using the the user-generated ID number provided.

        Args:
            numchoice (string): The ID number of the CD

        Returns:
            None

        """
        global blnCDRemoved
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
                
class FileProcessor:
    """Processing the data to and from text file"""
    
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None
        """
        # table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'rb')
        for line in objFile:
            data = line.strip()#.split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        # TODONE Add code here   
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()      

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None

        Returns:
            None
        """
        print('\nMenu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] dIsplay Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to File\n[x] eXit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None

        Returns:
            choice (string): A lower case string of the user's input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dicts): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None

        """
        print('\n======= The Current Inventory: =======\n')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by: {})'.format(*row.values()))
        print('======================================\n')

    @staticmethod
    def add_cd(idnum, title, artist):
        """
        Adds a new CD using data provided by the user. This includes three pieces of data: a user-generated ID number, a CD Title, and the Artist/'s\' name.

        Args:
            idnum (String): Represents the ID Number
            title (String): Represents the CD's Title'
            artist (String): Represents the Artist/s Name

        Returns:
            None

        """
        global strID
        global strTitle
        global stArtist
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()


    # TODONE add I/O functions as needed

# 1. When program starts, read in the currently saved Inventory

FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.\n')
        strYesNo = input('Type \'yes\' to continue and reload from the data file. Otherwise, reload will be canceled. ')
        if strYesNo.lower() == 'yes':
            FileProcessor.read_file(strFileName, lstTbl)
            print('\nLoaded.\n')
            IO.show_inventory(lstTbl)
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the Main Menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 ask user for new ID, CD Title and Artist
        # TODONE move IO code into function

        IO.add_cd(strID, strTitle, stArtist)

        # 3.3.2 Add item to the table
        # TODONE move processing code into function
        DataProcessor.update_table()
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('\nWhich ID number would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        # TODONE move processing code into function
        DataProcessor.delete_cd(intIDDel) 
        IO.show_inventory(lstTbl)
        if blnCDRemoved:
            print('\nThe CD was removed.\n')
        else:
            print('Could not find this CD!\n\n')
        continue  # start loop back at top
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODONE move processing code into function
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')


# pickling = open('CDInventory.dat', 'ab')
# pickle.dump(lstTbl, pickling)
# pickling.close()

# print('\nUnpickling the Table')
# lstTbl = open('CDInventory.dat', 'ab')
# pickling.close()