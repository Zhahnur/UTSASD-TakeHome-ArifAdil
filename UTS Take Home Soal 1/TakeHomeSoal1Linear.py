# Nama  : Muhammad Zhahnur Arif & Adil Firdausy Firmansyah
# NIM   : 1204210075 & 1204210048
# Kelas : IS 04-02

# linier Search
print()
from timeit import default_timer as timer
start = timer()
def linearsearch(arr, n, x):
 
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

arr = [0,8,7,8,5,0,8,6,6,1,8,2]
x = 8
n = len(arr)
position = linearsearch(arr, n, x)
if(position == -1):
    print("Index tidak ditemukan!!!")
else:
    print("Index ditemukan =", position)
end = timer()
print("Waktu yang diperlukan :", end - start)
print()