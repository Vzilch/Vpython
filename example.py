import V
import time

def arandom():
    scr = V.ipo()
    out = "g"
    arr = scr.windowlist()
    string = "sample code..."
    a = 20
    b = 30
    for i in range(40):
        scr.posput(string, [a, b], arr)
        out = scr.windowstr(arr)
        scr.vremove(string, [a, b], arr)
        print(out)
        time.sleep(0.05)
        b += 1

#example program with Vpy module
        #startin v module objects and other basics
z = V.ipo()
win = z.awin()
swich = True

# code
while swich == True:
    z.cls()
    
    x = int(input("enter x\t"))
    y = int(input("enter y\t"))
    filler = "*" * (x * y)

    swich = z.usrwait() #if user enters quitp it terminates the loop
    z.vinsert(filler, x, y, win)
    z.o(win, 0.8)



    

