import copy

def comma(list):
    #Function takes a list and returns a string with items separated by a comma and a space (', '),
    # with ('and ') inserted before the last item
    if len(list) == 0:
        return list
    else:
        editedList = []
        for i in list:
            if len(list) != list.index(i) + 1:
                editedList.append(list[list.index(i)])
                editedList.append(', ')
            else:
                editedList.append('and ')
                editedList.append(list[list.index(i)])
        
        for i in editedList:
            print(editedList[editedList.index(i)], end='')
            if(len(editedList) == editedList.index(i) + 1 ):
                print()

        return editedList


comma(["one", "two", "three", "four", "five"])