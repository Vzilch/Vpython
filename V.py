
#I>P>O is input then processing then output
#the class methods are sequenced in the above formate with only one exception
#G, indicates that the function makes/generates something and returns it comes P

import time

class ipo:
    
    def __init__(self, l = 37, w = 80):
        self.l = l
        self.w = w

    # I, reurns a list of inputs
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
        print("\n" * (self.l - 1))

    #Nav function for IPO, I>P>O
    def usrwait(self, prompt = "Continue"):
        a = input(prompt)
        if a == "quitp":
            print("\n\nprogram off")
            return False
        else:
            return a

    #nested list generator, P>G
    def nlist(self, n = 2):
        n += 1
        out = [None] * n
        x = 1
        print([out[x]])
        while x < n:
            out[x] = [out[x - 1]]
            x += 1
        return out[n - 1]

    #generates a list of lists of whitespaces, P>G
    def awin(self):
        l = self.l
        w = self.w
        out = []
        while l > 0:
            out += [[" "] * w]
            l -= 1
        return out

    #adds a sequence of chars to a list of lists, P
    def vinsert(self, iterable = "", x = 1, y = 1, lis = [], typ = "", fill = " "):
        l = self.l
        w = self.w

        if typ == "del":
            iterable = fill[0] * len(iterable)

        for item in iterable:
            if x >= w:
                x = 0
                y += 1
            if y >= l or y <= -l:
                continue
            lis[y][x] = item
            #print(y, x, lis[y][x])
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

    #displaces all items in a ques by n indexes, P
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

    #concatenates list if lists of chars into one string, P>O
    def o(self, a = [], wait = 0.00, typ = 0):
        out = ""
        index = 0
        for i in a:
            for x in i:
                out += x
                
            if index == self.l - 1:
                break
            
            out += "\n"
            index += 1
        
        if typ == 1:
            return out
        else:
            print(out)
            if wait > 0.00:
                time.sleep(wait)

    #this is the example of a bad function as it does two things not one and is messed up
    #takes a set of coordinates as input and returns a lists of data (max val xcoord and ycoord)
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


#for sorking on strings
class vstring:

    def __init__(self, ins):
        self.ins = ins

    def breakdown(self, string = ""):
        convention = ["base10", "letter", "bodmas"]
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        base10_str = "0123456789"
        letters_str = " AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        bodmas_str = "()^/*+-"
        
        gen = []
        stringlen = len(string)
        while stringlen > 0:
            gen += [None]
            stringlen -= 1
        
        oindex = 0
        for i in string:
            index = 0
            for x in base10_str:
                if i == x:
                    gen[oindex] = [nums[index], oindex, "number"]
                    oindex += 1
                index += 1

            index = 0
            for x in letters_str:
                if i == x:
                    gen[oindex] = [i, oindex, "ascii"]
                    oindex += 1
                index += 1

            index = 0
            for x in bodmas_str:
                if i == x:
                    gen[oindex] = [i, oindex, "bodmas"]
                    oindex += 1
                index += 1
        return gen

    
    def getwrds(selfstring = ""): 
        bre = breakdown(string)
        wrds = []
        x = 0
        wrd = ""
        for i in string:
            if bre[x][2] == "ascii":
                if bre[x][0] == " ":
                    wrds += [wrd]
                    #print(x)
                    wrd = ""
                else:
                    wrd += bre[x][0]
            x += 1
        wrds += [wrd]
        return wrds
