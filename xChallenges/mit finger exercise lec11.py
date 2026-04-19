#mit6_100l_f22_ex11

def remove_and_sort(Lin, k):
    """
    Lin is a list of ints
    k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list
    Does not return anything.
    """
    # Your code here
    if len(Lin) <= k:
        Lin.clear()
        return
    for i in range(k):
        del(Lin[0])
    #Lin.sort()
        
    #Lin.sort() replaces the codeblock below    
    Lin_copy = Lin[:]
    Lin.clear()
    order=min(Lin_copy)
    while order in Lin_copy:
        Lin.append(order)
        a = 0
        b = 0
        for i in Lin_copy:
            if order == i:
                a = b
            b += 1
        Lin_copy.pop(a)
        if Lin_copy == []:
            continue
        else:
            order=min(Lin_copy)

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)    # prints the list [3, 6]

P = [5,4,4,8,9,5,3,4,0]
q = 5
remove_and_sort(P, q)
print(P)    # prints the list [0, 3, 4, 5]
