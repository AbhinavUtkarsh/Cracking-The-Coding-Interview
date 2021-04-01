def string_rotation(a,b):

    a.lower()
    b.lower()

    b=''.join(list(b)+list(b))
    
    if b.find(a)!=-1:
        return True
    else:
        return False



print(string_rotation("apple","pplea"))
print(string_rotation("waterbottle","erbottlewat"))

