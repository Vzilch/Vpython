import V
import time

def afunc():
    scr = V.ipo()
    out = ""
    arr = scr.windowlist()
    string = "this is example code..."
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

