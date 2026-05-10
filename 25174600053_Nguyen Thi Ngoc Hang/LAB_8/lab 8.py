print("bài 8.1")
ds_cap = []
for n in range(2, 999):
    la_ngt1 = True
    if n < 2:
        la_ngt1 = False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                la_ngt1 = False
                break
            i += 1
    n2 = n + 2
    la_ngt2 = True
    if n2 < 2:
        la_ngt2 = False
    else:
        i = 2
        while i * i <= n2:
            if n2 % i == 0:
                la_ngt2 = False
                break
            i += 1
    if la_ngt1 and la_ngt2:
        ds_cap.append((n, n2))
print("Các cặp số nguyên tố sinh đôi < 1000:")
for cap in ds_cap:
    print(" ", cap)

print("bài 8.2")
n = int(input("Nhập số nguyên dương: "))
gt = 1
for i in range(2, n + 1):
    gt *= i
print(str(n) + "! =", gt)

print("bài 8.3")
n = int(input("Nhập n: "))
r = int(input("Nhập r (r <= n): "))
gt_n = 1
for i in range(2, n + 1):
    gt_n *= i
gt_r = 1
for i in range(2, r + 1):
    gt_r *= i
gt_nr = 1
for i in range(2, (n - r) + 1):
    gt_nr *= i
hoan_vi = gt_n
to_hop = gt_n // (gt_r * gt_nr)
print("Hoán vị P(" + str(n) + ") =", hoan_vi)
print("Tổ hợp C(" + str(n) + "," + str(r) + ") =", to_hop)

print("bài 8.4")
n = int(input("Nhập số nguyên: "))
tong = 0
so_tam = n
while so_tam > 0:
    tong += (so_tam % 10) ** 3
    so_tam //= 10
print("Tổng lập phương các chữ số của", n, ":", tong)

print("bài 8.5")
ds_armstrong = []
for num in range(1, 1000):
    tong = 0
    so_tam = num
    while so_tam > 0:
        tong += (so_tam % 10) ** 3
        so_tam //= 10
    if tong == num:
        ds_armstrong.append(num)
print("Số Armstrong (dùng cubesum):", ds_armstrong)

print("bài 8.6")
n = int(input("Nhập số nguyên dương: "))
tong_uoc = 0
for i in range(1, n):
    if n % i == 0:
        tong_uoc += i
print("Tổng ước thực sự của", n, ":", tong_uoc)

print("bài 8.7")
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
tong_a = 0
for i in range(1, a):
    if a % i == 0:
        tong_a += i
tong_b = 0
for i in range(1, b):
    if b % i == 0:
        tong_b += i
if tong_a == b and tong_b == a and a != b:
    print("(" + str(a) + ",", str(b) + ") là cặp số Amicable.")
else:
    print("(" + str(a) + ",", str(b) + ") không phải cặp số Amicable.")

print("bài 8.8")
n = int(input("Nhập số phần tử: "))
mang = []
for i in range(n):
    mang.append(int(input("Phần tử " + str(i+1) + ": ")))
chan = list(filter(lambda x: x % 2 == 0, mang))
le = list(filter(lambda x: x % 2 != 0, mang))
print("Nhóm số chẵn:", chan)
print("Nhóm số lẻ:", le)

print("bài 8.9")
n = int(input("Nhập số phần tử: "))
mang = []
for i in range(n):
    mang.append(int(input("Phần tử " + str(i+1) + ": ")))
binh_phuong = list(map(lambda x: x ** 2, mang))
print("Mảng gốc:", mang)
print("Mảng bình phương:", binh_phuong)

print("bài 8.10")
n = int(input("Nhập số phần tử: "))
mang = []
for i in range(n):
    mang.append(int(input("Phần tử " + str(i+1) + ": ")))
chan = list(filter(lambda x: x % 2 == 0, mang))
le = list(filter(lambda x: x % 2 != 0, mang))
lap_phuong_chan = list(map(lambda x: x ** 3, chan))
binh_phuong_le = list(map(lambda x: x ** 2, le))
print("Lập phương số chẵn:", lap_phuong_chan)
print("Bình phương số lẻ:", binh_phuong_le)