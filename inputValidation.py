import pyinputplus as pyip

types = ['str', 'num', 'choice', 'menu', 'time',
         'yesno', 'bool', 'email', 'filepath', 'password']
choices = ['McMuffin', 'Hashbrown', 'Quarter Pounder']


for i, theType in enumerate(types):
    print(f'Enter a  {theType}')
    if theType == 'str':
        pyip.inputStr()
    elif theType == 'num':
        pyip.inputNum()
    elif theType == 'choice':
        pyip.inputChoice(choices)
    elif theType == 'menu':
        pyip.inputMenu(choices, lettered=True)
    elif theType == 'time':
        pyip.inputTime()
    elif theType == 'yesno':
        pyip.inputYesNo()
    elif theType == 'bool':
        pyip.inputBool()
    elif theType == 'email':
        pyip.inputEmail()
    elif theType == 'filepath':
        pyip.inputFilepath()
    elif theType == 'password':
        pyip.inputPassword()