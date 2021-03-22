def check_permutation(a,b):
    if len(a)!=len(b) :
        return False
    
    a=sorted(a)
    b=sorted(b)
    #print(a,b)
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True

def check_permutation2(a,b):
    if len(a)!=len(b):
        return False
    
    #assuming ASCII characters
    #counter_a=[0]*128
    #counter_b=[0]*128
    counter=[0]*128

    for char in a:
        counter[ord(char)]+=1

    for i in range(len(b)):
        counter[ord(b[i])]-=1
        if counter[ord(b[i])]<0:
            return False
    return True

    """for char in a:
        counter_a[ord(char)]+=1
    
    for char in b:
        counter_b[ord(char)]+=1
    
    # comparing the arrays
    for i in range(len(counter_a)):
        if counter_a[i]!=counter_b[i]:
            return False
    
    return True"""
    

print(check_permutation("Dog", "God                  "))
print(check_permutation("dog","god"))
print(check_permutation("  Dog","God  "))
print(check_permutation("  Dog","goD  "))
print(check_permutation("test","estt"))

print("+++++++++++++++++++++++++++++++++++++++")

print(check_permutation2("Dog", "God                  "))
print(check_permutation2("dog","god"))
print(check_permutation2("  Dog","God  "))
print(check_permutation2("  Dog","goD  "))
print(check_permutation2("test","estt"))