infile='infile.txt'
outfile='outfile.csv'
# open infile as read
infile=open(infile,'r')
# open outfile as write
outfile=open(outfile,'w')
#true questions number
count=0
#add user name
username=input('enter your name: ')
for i in infile:
    print(i[:i.index('= ')])
    answer=input('enter answer: ')
    if answer == i[i.index('a')+7:].rstrip():
        count+=1
print(count,'answers is true from 20')
outfile.write(username+","+str(count)+' true from 20')
infile.close()
outfile.close()
