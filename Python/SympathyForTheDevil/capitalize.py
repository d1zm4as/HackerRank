def solve(s):
    input_list = [i[0].upper()+i[1:] if len(i)>=1 else i for i in s.rsplit(' ')]
    return ' '.join(input_list)
