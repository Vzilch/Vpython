

#to do - .out(), .println(), graph(), .treechart()

class ipo:
    
    def __init__(self, l = 37, w = 80):
        self.l = l
        self.w = w

    # I, inputs
    def ins(self, n = 1, it = 0):
        o = list(range(n))
        while n != 0:
            a = input()
            o[it] = a
            n -= 1
            it += 1
        return o

    #clearscreen
    def cls(self):
        a = self.l
        clear = ""
        while a > 0:
            print("")
            a -= 1

    #Nav function for IPO, I>P
    def usrwait(self, prompt = "Continue"):
        a = input(prompt)
        if a == "quitp":
            return False
        else:
            return a

    # Breaksdown text into chartypes, P
    def breakdown(self, string = ""):
        convention = ["base10", "letter", "bodmas"]
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        base10_str = "0123456789"
        letters_str = " AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        bodmas_str = "()^/*+-"
        
        onum = []
        ochar = []
        obod = []
        stringlen = len(string)
        while stringlen > 0:
            onum += [None]
            obod += [None]
            ochar += [None]
            stringlen -= 1
        
        oindex = 0
        for i in string:
            index = 0
            for x in base10_str:
                if i == x:
                    onum[oindex] = [nums[index], index, "number"]
                    oindex += 1
                index += 1

            index = 0
            for x in letters_str:
                if i == x:
                    ochar[oindex] = [i, index, "letter"]
                    oindex += 1
                index += 1

            index = 0
            for x in bodmas_str:
                if i == x:
                    obod[oindex] = [i, index, "bodmas"]
                    oindex += 1
                index += 1

            olist = [onum, ochar, obod]
        return olist

    #list generator, G
    def nlist(self, length = 1, depth = 1, ns = 1):
        a = []
        b = []
        copy = ns

        #set number of "none" vals in each indice
        while ns > 0:
            a += [None]
            ns -= 1
        #set depth/dimensions/brackets
        while depth - 1 > 0:
            a = [a]
            depth -= 1
        #length of list
        while length > 0:
            b += a
            length -= 1
        
        return b

    #makes list for window sized outputs, G
    def windowlist(self, filler = " ", typ = 0):
        out = []
        count = self.w * self.l + self.l
        width = self.w + 1
        it = 0
        
        if typ == 1:
            while count > 0:
                if it % width == 0:
                    out += "\n"
                else:
                    out += [None]
                it += 1
                count -= 1
        
        else:
            while count > 0:
                if it % width == 0:
                    out += "\n"
                else:
                    out += filler
                it += 1
                count -= 1
        out[0] = "Window\n"
        return out

    #for adding char in o arr, p
    def putone(self, char, rc = [1, 1], arr = []):
        pos = rc[0] + (rc[1] - 1) * (self.w + 1)
        arr[pos] = char[0]
        return arr

    #for adding line in O array, P
    def posput(self, iterable = [], rc = [2, 2], arr = []):
        pos = rc[0] + (rc[1] - 1) * (self.w + 1)
        #self,w + 1 because, newlines in prev func
        end = len(arr)
        x = 0
        n = len(iterable)
        while n > 0:
            if pos % (self.w + 1) == 0:
                pos += 1
            try:
                arr[pos] = iterable[x]
            except IndexError:
                break
            x += 1
            pos += 1
            n -= 1

    def vremove(self, iterable = " ", rc = [1, 1], arr = []):
        pos = rc[0] + (rc[1] - 1) * (self.w + 1)
        end = len(arr)

        for i in iterable:
            if pos > end:
                pos = 5
            arr[pos] = " "
            pos += 1
            if pos % (self.w + 1) == 0:
                pos += 1
            
        return arr



    #Adds up items in a list, P
    def windowstr(self, inlist = [None], filler = " "):
        out = ""
        for i in inlist:
            try:
                out += i
            except TypeError:
                out += filler
        return out

    #generates a list of lists of chars, G
    def awin(self):
        l = self.l
        w = self.w
        out = []
        while l > 0:
            out += [[" "] * w]
            l -= 1
        return out

    #concatenates list if lists of chars into one string, P>O
    def o(self, a = [], typ = 0):
        out = ""
        for i in a:
            for x in i:
                out += x
            out += "\n"
        if typ == 0:
            print(out)
        else:
            return out

    #adds a sequence of chars to a list of lists, P
    def vinserts(self, iterable = "", x = 1, y = 1, lis = []):
        l = self.l
        w = self.w

        for item in iterable:
            lis[y][x] = item
            #print(y, x, lis[y][x])
            if x >= w:
                x = 0
                y += 1
            if y >= l:
                y = 0
            
            x += 1


    #queue displacement, P
    def dis(self, a = [], typ = 0):
        off = a[0]
        z = len(a) - 1
        s = z
        n = 1
        while s > 0:
            a[n-1] = a[n]
            n += 1
            s -= 1
        a[z] = None
        if typ == 0:
            return a
        elif typ == 1:
            return off
        else:
            return [a, off]

    # queue displacement cycle, P
    def discyc(self, a = [], times = 1, typ = 0):
        x = 0
        lena = len(a)
        outlist = list(range(lena))
        z = lena - 1
        for i in range(times):
            outlist[x] = a[0]
            s = z
            n = 1
            while s > 0:
                a[n-1] = a[n]
                n += 1
                s -= 1
            a[z] = None
            n += 1
            x += 1
        if typ == 1:
            return outlist
        elif typ == 0:
            return [a, outlist]
        else:
            return None

    
    def incoord(self, n = 1, prompt = "Enter coordinate\t"):
            xc = list(range(n+1))
            yc = list(range(n+1))
            clist = list(range(n+1))
            it = 0
            
            while n > 0:
                try:
                    x = int(input(prompt))
                    y = int(input(prompt))
                    print("\n")
                except ValueError:
                    print("\n\tsomething wrong with input\n")
                    continue
                clist[it] = [x, y]
                xc[it] = x
                yc[it] = y
                it += 1
                n -= 1

            it = 0

            for i in xc:
                it = 0
                for x in xc:
                    if x > xc[0]:
                        xc[0] = i
                        it += 1
                    else:
                        it += 1
                
                it = 0
                for ycoord in yc:
                    if ycoord > yc[0]:
                        yc[0] = ycoord
                        it += 1
                    else:
                        it += 1
                    
            return [clist, xc, yc, [xc[0], yc[0]]]
                
            
    def treechart(self):
        print("incomplete")


