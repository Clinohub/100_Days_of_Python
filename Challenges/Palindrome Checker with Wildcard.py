#Palindrome Checker with Wildcard

def wild_pos_list(astericks):
    count = 0
    pos = []
    for asterick in astericks:
        if asterick == '*':
            pos.append(count)
            count +=1
    return pos



def replace_wildcards(wildcardList,empty_wildcardList,n):
    count = 0
    asterick_positions = []
    for wild_card in wildcardList:
        if wild_card == '*':
            asterick_positions.append(count)
        count +=1
    
    for position in asterick_positions:
        wildcardList[position] = empty_wildcardList[n]
        
    return wildcardList


def is_palindrome(check):
    checkList =[]
    for i in check:
        checkList.append(i)
    reverse_checkList=checkList[:]
    reverse_checkList.reverse()
    
    return checkList == reverse_checkList

        
def is_wildcard_palindrome(text):
    if is_palindrome(text) == True:
        return True
    elif '*' in text:
        text_as_list = []
        removeWild = []
        for char in text:
            text_as_list.append(char)
            if not char == '*':
                removeWild.append(char)
                
        for number in range(len(removeWild)):
            copy_text_as_list=text_as_list[:]
            if is_palindrome(replace_wildcards(copy_text_as_list,removeWild,number))==True:
                return True
        return False
    else:
        return False

    
print("PALINDROME CHECKER WITH WILDCARD")
str_text = input("Type a string text: ")
print(is_wildcard_palindrome(str_text))