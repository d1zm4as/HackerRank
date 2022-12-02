def plusMinus(arr):
    zeros = 0
    positivos = 0
    negativos = 0
    lista = [arr]
    for x in arr:
        if x == 0 :
            zeros += 1
        if x > 0:
            positivos += 1
        if x < 0:
            negativos += 1
            
    m_p = positivos/len(arr)
    m_n = negativos/len(arr)  
    m_z = zeros/len(arr)
    print(m_p)
    print(m_n)
    print(m_z)
