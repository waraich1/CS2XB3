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


