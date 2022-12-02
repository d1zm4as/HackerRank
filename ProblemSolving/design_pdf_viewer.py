def designerPdfViewer(h, word):
    alfa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    pao = []
    for x in word:
        indexo = alfa.index(x)
        pao.append(h[indexo])
    return max(pao)*len(word)
