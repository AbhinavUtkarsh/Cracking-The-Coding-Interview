def one_away(string1,string2):

    counter=0
    larger=""
    smaller=""

    if len(string1)>=len(string2):
        larger=string1
        smaller=string2
    else:
        larger=string2
        smaller=string1

    i=0
    j=0
    for c in range(len(smaller)):
        if larger[i]!=smaller[j] and len(larger)!=len(smaller):
            counter+=1
            i+=1
        elif larger[i]!=smaller[j] and len(larger)==len(smaller):
            i+=1
            j+=1
            counter+=1

        else:
            i+=1
            j+=1
            

    if counter<=1:
        return True
    else:
        return False
        
def one_away_OPT(string1,string2):

    if abs(len(string1) - len(string2)) >1:
        return False
    
    s2= string2 if len(string2) > len(string1)  else string1 #longer
    s1= string1 if len(string2) > len(string1)  else string2 #shorter

    index1=0
    index2=0
    flag=False

    while(index1 < len(s1) and index2 < len(s2)):

        if (s1[index1]!=s2[index2]):
            
            if(flag!=True):
                return False
            flag = True

            if (len(s1)==len(s2)):
                index1+=1
        else:
            index1+=1
        index2+=1
    return True


print(one_away("pale","ple"))
print(one_away("pales","pale"))
print(one_away("pale","bale"))
print(one_away("pale","bake"))
print(one_away("palee","balee"))
print("+++++++++++++++++++++++++++++")
print(one_away("pale","ple"))
print(one_away("pales","pale"))
print(one_away("pale","bale"))
print(one_away("pale","bake"))
print(one_away("palee","balee"))