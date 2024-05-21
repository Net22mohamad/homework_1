#empty list to reverse the binary for LSB
l=[]
while True:
    binary=input('enter binary: ')
    if binary.isdigit():
        #binary to decimal algorithm
        dec=0
        for i in binary:
            l.append(int(i))
        #reverse the list to make input is right to computaion
        l.reverse()
        for i in range(len(l)):
            dec+=l[i]*2**i
        print(dec)
    else:
        print("error input")
    s=input('do you want to continue? for yes enter y no enter n: ')
    if s=='y':
        #clear list items
        l=[]
    elif s=="n":
        break
    else:
        print('error, good bye')
        break
