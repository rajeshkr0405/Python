# list = [2,1,3]
# list.append(4)#adds one element at the end [2,1,3,4]
# list.sort #sorts in accending order [1,2,3]
# list.sort(reverse=True) #short in decending order [3,2,1]
# list.reverse()#reverses list [3,2,1]
# list.insert(idx,el) #insert element at index
list=[2,1,3]
list.append(4)
print(list) 
list.remove(4)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(1,5)
print(list)
list.remove(1)
print(list)
list.pop(1)
print(list)