# Nama  : Muhammad Zhahnur Arif & Adil Firdausy Firmansyah
# NIM   : 1204210075 & 1204210048
# Kelas : IS 04-02

# Jump Search
print()
from timeit import default_timer as timer
start = timer()

import math
def jump_search (mylist, value, length) :
    step = int (math.sqrt(len(mylist)))
    prev = 0
    while (mylist[min(step, length) - 1] < value):
        prev = step
        step = step + int(math.sqrt(len(mylist)))
        if (prev >= length):
            return -1
    while (mylist[prev] < value):
        prev = prev + 1
        if(prev == min(step, length)):
            return -1
    if (mylist[prev] == value):
        return prev
    return -1

mylist = [0,8,7,8,5,0,8,6,6,1,8,2]
mylist.sort()
print(mylist)
number = 8
index = jump_search(mylist, number, len(mylist))
if(index != -1 ):
    print("Index ditemukan =", index)
else :
    print("Index tidak ditemukan!!!")

end = timer()
print("Waktu yang diperlukan :", end - start)
print()