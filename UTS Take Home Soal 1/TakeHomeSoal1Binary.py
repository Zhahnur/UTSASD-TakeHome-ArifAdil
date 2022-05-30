# Nama  : Muhammad Zhahnur Arif & Adil Firdausy Firmansyah
# NIM   : 1204210075 & 1204210048
# Kelas : IS 04-02

# Binary Search
print()
from timeit import default_timer as timer
start = timer()
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# Jika X lebih besar, abaikan setengah kiri
		if arr[mid] < x:
			low = mid + 1
		# Jika X lebih kecil, abaikan setengah kanan
		elif arr[mid] > x:
			high = mid - 1
		else:
			return mid

	return -1

# Test Array
arr = [0,8,7,8,5,0,8,6,6,1,8,2]
arr.sort()
print(arr)
x = 8

# Memanggil Fungsi
result = binary_search(arr, x)

if result != -1:
	print("Index ditemukan =", str(result))
else:
	print("Index tidak ditemukan!!!")
end = timer()
print("Waktu yang diperlukan :", end - start)
print()