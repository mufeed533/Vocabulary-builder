#!/usr/bin/python
import random
import time
from datetime import datetime
from pythonzenity import Message

#open vocabulary file and read all the contents
file = open('vocabulary.txt','r')
f = file.readlines()
file.close()

#create an array to store line numbers of all the blak lines, 1 for first word
myList = [1]
for num, line in enumerate(f,1):
    if line in ['\n', '\r\n']:
        myList.append(num+1)
    last_line = num

# get the number of times the words are displayed
count  = 1

#to skip examples getting counted
print_flag = 0

#display the words when called
def display(count,print_flag):
    #select random line number(to print randm line) from myList
    k = random.choice(myList)
    #get the exact last line of previous word
    k = k-1
    flag = 0
    for i in f:
        #if ever reach last line start iterating again
        if k == last_line:
            flag = 0
            break
        else:
            n = f[k]
            if n in ['\n', '\r\n']:
                flag = 0
                time.sleep(600)
                break
            else:
                if flag == 0:
                    v = n.split(' ', 1)[0]
                    flag = 1
                if print_flag == 0:
                    print count,n
                    count = count+1
                print_flag = 1
                print datetime.now().strftime('%H:%M:%S')
                Message(title= v,text= n)
                k = k+1
    return count

while True:
    count  = display(count,print_flag)
