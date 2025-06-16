def  mixlist(list1,indexlist,index,list1len):
    if index == 0:
        for i in range(list1len):
            if cheklist(indexlist,i) == True:
                o= 0
                list3 = [None]*list1len
                indexlist.append(i)             
                for k in range(list1len):
                    list3[indexlist[k]] = list1[o]
                    o += 1
                indexlist.pop()
                return list3
    else:
        list3 =[]
        for i in range(list1len):
            if cheklist(indexlist,i) == True:
                indexlist.append(i)
                if index == 1:
                    list3.append(mixlist(list1,indexlist,index+-1,list1len)) 
                else:
                    for j in mixlist(list1,indexlist,index-1,list1len):
                        list3.append(j)
                indexlist.pop()
        return list3
def cheklist(indexlist,index):   
    for i in range(len(indexlist)):
        if indexlist[i] == index:
            return False
    return True
def findtheemptyslot(list1,index,value):
    for i in range(len(list1)):
        if list1[i] == -1:
            if i == index: list1[index] = value
            elif i < index: return -1
            elif i > index: pushbigger(list1,index,value,i)
            break
def pushbigger(list1,index,value,indexemptyplace):
    temp= value
    for i in range(index, indexemptyplace+1):
        temp = list1[i]
        list1[i] = value
        value = temp
def pushsmaller(list1,index,value,indexemptyplace):
    temp = value
    for i in range(indexemptyplace, index-1):
        temp = list1[i]
        list1[i] = value
        value = temp
    return list1
#print(pushsmaller([1,2,-1,4,5,6], 3, 4, 2))
a = [i for i in range(100)]
print(mixlist(a,[],len(a)-1,len(a)))