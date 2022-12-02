def gradingStudents(grades):
    res = []
    for x in grades:
        if x >= 38:
            mod5 = x % 5
            if mod5>=3:
                x += (5-mod5)
        res.append(x)
    return res
