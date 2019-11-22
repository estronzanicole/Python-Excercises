def bottleform(n):
    if n == 0:
        return " no more bottles "
    elif n == 1:
        return str(n) + "bottle"
    else: 
        return str(n) + "bottles"

def printlyrics(n=99):
    if(n==0):
        return bottleform(n) + " beer on the wall," + bottleform(n) + " of beer\ngo to the store and buy some more," + bottleform(99) + " of beer on the wall"
    else:
        return (bottleform(n) + " beer on the wall, " + bottleform(n) + " of beer\nTake one down and pass it around, "  + printlyrics(n-1))

    

print(printlyrics(99))