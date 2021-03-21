def isUnique(string):
    if len(string)>128:
        return False
    booleanmap=[False]*128
    for char in string:
        if booleanmap[ord(char)]==True:
            booleanmap[ord(char)]=False
            return False
        booleanmap[ord(char)]=True
    return True

def isUniqueBit(string):
	if len(string)>128:
		return False
	total_bits=0
	for char in string:
		current_char=ord(char)-ord("a")
		if(total_bits & (1<<current_char)>0):
			return False

		total_bits = total_bits | 1<<current_char
	return True




print(isUnique("abhinav"))
print(isUnique("utkarsh"))
print(isUnique("test"))
print("+++++++++++++++++++++++++++++")
print(isUniqueBit("abhinav"))
print(isUniqueBit("utkarsh"))
print(isUniqueBit("test"))