def string_compression(string):

    compressed=[]
    counter=0

    for i in range(len(string)):
        
        if i!=0 and string[i]!=string[i-1]:
            compressed.append(string[i-1]+str(counter))
            counter=0
        counter+=1
    
    if counter:
        compressed.append(string[-1]+str(counter))


    return min(string, "".join(compressed), key=len)




print(string_compression("aaaaabbbbccccfeghhhhh"))
print(string_compression("aabbccdd"))
print(string_compression("aaaab"))
print(string_compression("a"))
print(string_compression(""))