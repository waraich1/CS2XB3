def are_valid_groups(a, b):
    hashTable = set()
    for i in b:
        for j in i:
            hashTable.add(j)
    for k in a:
        if k not in hashTable:
            return False
    return True	
  


#print(are_valid_groups(["1", "2"], [["1", "3"], ["2", "4"]]))
#print(are_valid_groups(["1", "2"], [["5", "3"], ["2", "4"]]))
