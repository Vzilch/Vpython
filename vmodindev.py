#vmod_indev
#basic functions for a window (object)


class window:
        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.arr = [[["","","",""]] * self.x] * self.y  #note: rgb+d   

        #hex format: #00000000, (rgb+d)
        def update_pt(self, x = int, y = int, hex = str):
                self.arr[y][x][0] = hex[1:3]
                self.arr[y][x][1] = hex[3:5]
                self.arr[y][x][2] = hex[5:7]
                self.arr[y][x][3] = hex[7:9]

        def hexof(self, x = int, y = int):
                return "#" + "".join(val for val in self.arr[y][x])