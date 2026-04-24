#Palindrome Checker with Wildcard

def replace_wildcards(wildcard, char):
    """
    param wildcard is a string
    param char is a wildcard character
    Replaces '*' in wildcard by one of its character
    Return a string 
    """
    replace_word = ""
    if not char == '*':
        for asterick in wildcard:
            if asterick == '*':
                replace_word += char
            else:
                replace_word += asterick
        
    return replace_word


def is_palindrome(check):
    """
    param check is a string or tuple or list
    Compares the word to its reverse and returns boolean
    Returns if word same as its reverse then True otherwise Talse
    """
    string = check
    
    return string == string[::-1]

        
def is_wildcard_palindrome(text):
    """
    param text is an all lowercase string or all uppercase string
    
    Determines if the string is a palindrome by calling is
    is_palindrome(text) and replace_wildcards(text) functions
    
    The string may contain a wildcard '*' character
    Returns True if string is a palindrome otherwise False
    """
    if is_palindrome(text):
        return True
    
    if not '*' in text:
        return False
        
    for letter in text:
        if not letter == '*':
            if is_palindrome(replace_wildcards(text, letter)):
                return True
                       
    return False
    
print("PALINDROME CHECKER WITH WILDCARD")
#str_text = input("Type a string text: ")
#print(is_wildcard_palindrome(str_text))

print(is_wildcard_palindrome("racecar"))  # True
print(is_wildcard_palindrome("r*cecar"))
print(is_wildcard_palindrome("r*cec*r"))
print(is_wildcard_palindrome("a*"))
print(is_wildcard_palindrome("*"))
print(is_wildcard_palindrome("A**"))
print(is_wildcard_palindrome("hello")) # False
print(is_wildcard_palindrome("h*llo"))
