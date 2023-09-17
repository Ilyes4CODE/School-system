def equal(text1:str, text2:str)->bool:
    if text1 == text2:
        return True
    else:
        return False

def verify(user,group)->bool:
    if equal(user.groups.get,group) == True:
        return True
    else:
        return False
    

