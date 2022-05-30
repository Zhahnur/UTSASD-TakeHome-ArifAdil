# Nama  : Muhammad Zhahnur Arif & Adil Firdausy Firmansyah
# NIM   : 1204210075 & 1204210048
# Kelas : IS 04-02

print()
def fact(n):
    if n==0:
        return 1
    else :
        fact1=1
        for i in range (1, n+1):
            fact1=fact1*i
        return fact1
    
x=float(input("Masukkan X = "))
n=int(input("Masukkan Jumlah Term = "))
n=n+1
hasil=0

for i in range (n):
    hasil=hasil+(x**i)/fact(i)
print("Hasil= ",hasil)
print()