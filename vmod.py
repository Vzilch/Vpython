#vmod
#has bugs

import tkinter as tk
class ipo():
    def __init__(self, x, y, arr):
        self.x = x
        self.y = y
        arr = [[0]*self.x]*self.y
        self.arr = arr

    def arrout(self):
        for cols in self.arr:
            out = ""
            for pts in cols:
                out += str(pts)
            print(out)

def mov(count, canvas):
    count = 0
    z = 0
    print("d")
    if count < 10:
        print(count)
        z += 100
        canvas.create_rectangle(50, 50, z, 200, fill="red")
        mw.after(10, mov, count + 1, canvas) # Call again after 1 second
    else:
        pass

scr = []
a = ipo(500, 500, scr)
mw = tk.Tk()
canvas = tk.Canvas(mw, width=a.x, height=a.y, bg="black")
canvas.pack()
mw.title("MAIN")
geo = str(a.x) + "x" + str(a.y)
mw.geometry(geo)
z = 0
