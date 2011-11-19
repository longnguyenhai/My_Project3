import sys
fo = open(sys.argv[3],"r")
lines = fo.readlines()
count_line=0
#print len(lines)
number = sys.argv[2]
char = sys.argv[1]

if char ==  '-n'    :
    
    for i in lines:
    #print len(i)
    
        count_line +=1
#print c
        if count_line > (len(lines) - int(number)) and count_line <= (len(lines)):
            print i,
            
else:
    print 'Nhap vao n '
    
    

   