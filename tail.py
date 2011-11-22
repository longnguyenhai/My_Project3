import sys
import time

def tail_n(n,file):
    fo = open(file,'r')
    n= int(number_lines)    # number of lines need show
    lines = fo.readlines()     
    nlines = len(lines)     
    if n > nlines:
        n = nlines
    for i in range(nlines - n, nlines):
            print lines[i],
            
def tail_f(fo):
    fo = open(file,'r')
    fo.seek(0,2)
    while True:
        lines =fo.readlines()
        if not lines:
            time.sleep(0.1)
            continue
        yield lines
        

if sys.argv[1]=='-n':
    number_lines=sys.argv[2]
    file = sys.argv[3]
    tail_n(sys.argv[2],sys.argv[3])

elif sys.argv[1]=='-f':
    number_lines=10
    file = sys.argv[2]
    for lines in tail_f(tail_n):
        tail_n(10,sys.argv[2])
        print lines
   