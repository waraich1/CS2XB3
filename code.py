def are_valid_groups(a, b):
    for i in a:
        indicate = 0
        for j in b:
            if i in j:
                indicate = 1
                break
        if indicate == 0:
            return False

    return True
  


#print(are_valid_groups(["1", "2"], [["1", "3"], ["2", "4"]]))
#print(are_valid_groups(["1", "2"], [["5", "3"], ["2", "4"]]))
