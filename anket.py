import codecs
from msvcrt import getch

#anket sorularının olduğu txt belgesindeki bütün soruları okuyup her bir soruyu
#cevaplarken cevabı ile birlikte yeni txt dosyasına yazdırma


def ans(x):
    f = codecs.open("cevaplar.txt","a","utf8")
    #y = int(input())
    b = getch().decode("cp437")
    
    if b == "1":
        f.write(x+"Evet\n\n")
    elif b == "2":
        f.write(x+"Hayır\n\n")
    elif b == "3":
        f.write(x+"IDK\n\n")
    f.close()
   


with codecs.open("metin.txt","r","utf8") as f:
    for i in f:
        print(i)
        ans(i)
    
