def palindrome_P(P_string):

    table=[0 for _ in range(ord("z")-ord("a")+1)]
    oddcounter=0

    for char in P_string:
        location=number(char)
        
        if location!=-1:
            table[location]+=1

            if table[location]%2==1:
                oddcounter+=1
            else:
                oddcounter-=1



    return oddcounter <=1

def palindrome_P_B(P_string):

    bitvector=0
    for char in P_string:
        value=number(char)
        if value!=-1:
            mask = 1<<value
            if bitvector & mask == 0:
                bitvector |= mask
            else:
                bitvector &= ~mask

    #print(bin(bitvector))
    # check for only one 1 bit in bitvector
    if (((bitvector - 1) & bitvector)==0):
        return True
    else:
        return False



def number(char):
    a=ord("a")
    z=ord("z")

    A=ord("A")
    Z=ord("Z")

    value=ord(char)

    if a<=value<=z:
        return value-a
    
    if A<=value<=Z:
        return value-A
    
    return -1






print(palindrome_P("aabb"))
print(palindrome_P("aabbCD"))
print(palindrome_P("iTopiNon   AvevanoN   ipoti"))

print("+++++++++++++++++++++++++++++")

print(palindrome_P_B("aabb"))
print(palindrome_P_B("aabbCD"))
print(palindrome_P_B("iTopiNon   AvevanoN   ipoti"))
