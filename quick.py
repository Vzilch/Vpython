import V
import time

def arandom():
    scr = V.ipo()
    out = "g"
    arr = scr.windowlist()
    string = "my name is \n who know\n i know\n it is \nv\nstar..."
    a = 20
    b = 30
    for i in range(40):
        scr.posput(string, [a, b], arr)
        out = scr.windowstr(arr)
        scr.vremove(string, [a, b], arr)
        print(out)
        time.sleep(0.05)
        b += 1


z = V.ipo()
a = z.awin()
my = "hi bye"
z.vinserts(my, 1, 1, a)
z.o(a)

