import pyinputplus as pyip

types = ['str', 'num', 'choice', 'menu', 'time',
         'yesno', 'bool', 'email', 'filepath', 'password']
choices = ['McMuffin', 'Hashbrown', 'Pancakes']


for i, theType in enumerate(types):
    print()
    print(f'pyinputplus.{theType}():')
    if theType == 'str':
        pyip.inputStr("Enter a String: ")
    elif theType == 'num':
        pyip.inputNum("Enter a number: ", min=1)
    elif theType == 'choice':
        pyip.inputChoice(choices)
    elif theType == 'menu':
        pyip.inputMenu(choices, lettered=True)
    elif theType == 'time':
        pyip.inputTime("Enter a time [xx:xx]: ")
    elif theType == 'yesno':
        pyip.inputYesNo("Enter Yes or No: ")
    elif theType == 'bool':
        pyip.inputBool("Enter a boolean: ")
    elif theType == 'email':
        pyip.inputEmail("Enter an email: ")
    elif theType == 'filepath':
        pyip.inputFilepath("Enter a filepath: ")
    elif theType == 'password':
        pyip.inputPassword("Enter a password: ")