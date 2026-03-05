def flatten(L):
    """
    L: a list
    Returns a copy of L, which is a flattened version of L
    """
    #L=[list] or [[list]] or [[[list]]] or ...
    if len(L)==1:
        if not type(L[0])==list:
            return L
        else:
            return flatten(L[0])
    #L=[list1,list2,list3,...]
    elif not type(L[0])==list:
        return [L[0]]+flatten(L[1:])
    #L=[[list1],[list2],[...]]
    else:
        return flatten(L[0])+flatten(L[1:])
    
#Examples:
Li=[[1,4,[6],2],[[[3]],2],4,5]

print(flatten(Li)) #prints [1, 4, 6, 2, 3, 2, 4, 5]