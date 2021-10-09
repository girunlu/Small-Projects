def alphabet_position(text):
    import string
    alph = string.ascii_lowercase
    alp = {}
    alp1 = []
    alp2 = []
    for i,l in enumerate(alph):
        alp1.append(i+1)
        alp2.append(l)
    alp = dict(zip(alp2, alp1))
    txt = []
    for i in text:
        if i in alph or i.lower() in alph:
            txt.append(i.lower())
    final = ""
    for i in txt:
        final += str(alp.get(i))+" "
    asd = final[:-1]
    return asd

while True:
   x = str(input("enter your text to find its letters position "))
   print(alphabet_position(x))
