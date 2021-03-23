def URlify(string,length):

    char_array=list(string)
    string=""

    newindex=(len(char_array))

    for i in range(length-1,-1,-1):
        #replacing spaces
        if char_array[i]==" ":
            char_array[newindex-3:newindex]="%20"
            newindex=newindex-3
        else:
            #moving characters
            char_array[newindex-1]=char_array[i]
            newindex=newindex-1
    return string.join(char_array)




print(URlify("Mr John Smith    ",13))