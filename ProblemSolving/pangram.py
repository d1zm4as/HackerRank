def pangrams(s):
    tira = s.lower()
    a = "qwertyuiopasdfghjklzxcvbnm"
    
    for x in a:
        if x not in tira:
            return "not pangram"
    return "pangram"
