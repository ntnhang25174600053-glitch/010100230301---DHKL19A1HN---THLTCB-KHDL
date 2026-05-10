print("bài 5.1")
n = int(input("Nhập số nguyên dương: "))
ket_qua = ""
so_tam = n
if so_tam == 0:
    ket_qua = "0"
else:
    while so_tam > 0:
        ket_qua = str(so_tam % 2) + ket_qua
        so_tam = so_tam // 2
print("Kết quả:", ket_qua)
 
print("bài 5.2")
str1 = input("Nhập str1: ")
str2 = input("Nhập str2: ")
chuoi_ngan = ""
do_dai_ngan = -1
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuoi_con = str1[i:j]
        if chuoi_con in str2:
            if do_dai_ngan == -1 or len(chuoi_con) < do_dai_ngan:
                do_dai_ngan = len(chuoi_con)
                chuoi_ngan = chuoi_con
if do_dai_ngan == -1:
    print("Không có chuỗi con chung.")
else:
    print("Chuỗi con chung ngắn nhất:", chuoi_ngan, "- độ dài:", do_dai_ngan)
 
print("bài 5.3")
chuoi = input("Nhập chuỗi văn bản: ")
tu_khoa = input("Nhập từ khóa: ")
vi_tri_list = []
for i in range(len(chuoi) - len(tu_khoa) + 1):
    if chuoi[i:i + len(tu_khoa)] == tu_khoa:
        vi_tri_list.append(i)
print("Vị trí xuất hiện:", vi_tri_list)
print("Số lần xuất hiện:", len(vi_tri_list))
ky_tu_list = []
so_lan_list = []
for ky_tu in chuoi:
    if ky_tu == " ":
        continue
    da_co = False
    for k in range(len(ky_tu_list)):
        if ky_tu_list[k] == ky_tu:
            so_lan_list[k] += 1
            da_co = True
            break
    if not da_co:
        ky_tu_list.append(ky_tu)
        so_lan_list.append(1)
tan_suat_max = 0
ky_tu_pho_bien = ""
for k in range(len(so_lan_list)):
    if so_lan_list[k] > tan_suat_max:
        tan_suat_max = so_lan_list[k]
        ky_tu_pho_bien = ky_tu_list[k]
print("Ký tự xuất hiện nhiều nhất:", ky_tu_pho_bien, "-", tan_suat_max, "lần")
 
print("bài 5.4")
chuoi = input("Nhập chuỗi: ")
chuoi_so = ""
for ky_tu in chuoi:
    if '0' <= ky_tu <= '9':
        chuoi_so += ky_tu
print("Chuỗi sau lọc:", chuoi_so)
if chuoi_so == "":
    print("Không có chữ số nào.")
else:
    so = int(chuoi_so)
    print("Số nguyên:", so)
    if so < 2:
        print(so, "không phải số nguyên tố.")
    else:
        la_ngt = True
        i = 2
        while i * i <= so:
            if so % i == 0:
                la_ngt = False
                break
            i += 1
        if la_ngt:
            print(so, "là số nguyên tố.")
        else:
            print(so, "không phải số nguyên tố.")
 
print("bài 5.5")
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
ket_qua = ""
do_dai_max = len(str1) if len(str1) > len(str2) else len(str2)
for i in range(do_dai_max):
    if i < len(str1):
        if ket_qua != "":
            ket_qua += "-"
        ket_qua += str1[i]
    if i < len(str2):
        if ket_qua != "":
            ket_qua += "-"
        ket_qua += str2[i]
print("Chuỗi sau khi trộn:", ket_qua)
 
print("bài 5.6")
chuoi = input("Nhập chuỗi: ")
so_dac_biet = 0
for ky_tu in chuoi:
    la_chu = ('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z')
    la_so = '0' <= ky_tu <= '9'
    if not la_chu and not la_so:
        so_dac_biet += 1
print("Số ký tự đặc biệt:", so_dac_biet)
if len(chuoi) > 0:
    print("Tỷ lệ:", round((so_dac_biet / len(chuoi)) * 100, 2), "%")
 
print("bài 5.7")
chuoi = input("Nhập chuỗi: ")
chu_thuong = 0
chu_hoa = 0
chu_so = 0
dac_biet = 0
for ky_tu in chuoi:
    if 'a' <= ky_tu <= 'z':
        chu_thuong += 1
    elif 'A' <= ky_tu <= 'Z':
        chu_hoa += 1
    elif '0' <= ky_tu <= '9':
        chu_so += 1
    else:
        dac_biet += 1
print("Chữ thường:", chu_thuong)
print("Chữ hoa:", chu_hoa)
print("Chữ số:", chu_so)
print("Ký tự đặc biệt:", dac_biet)
 
print("bài 5.8")
chuoi = input("Nhập chuỗi (> 10 ký tự): ")
if len(chuoi) <= 10:
    print("Chuỗi phải dài hơn 10 ký tự!")
else:
    print("Vị trí 2 đến 8:", chuoi[1:8])
    print("5 ký tự từ vị trí 5:", chuoi[4:9])
    print("3 ký tự cuối:", chuoi[-3:])
    chuoi_hoa = ""
    for c in chuoi:
        if 'a' <= c <= 'z':
            chuoi_hoa += chr(ord(c) - 32)
        else:
            chuoi_hoa += c
    print("Chữ hoa:", chuoi_hoa)
    chuoi_thuong = ""
    for c in chuoi:
        if 'A' <= c <= 'Z':
            chuoi_thuong += chr(ord(c) + 32)
        else:
            chuoi_thuong += c
    print("Chữ thường:", chuoi_thuong)
    chuoi_dao = ""
    for i in range(len(chuoi) - 1, -1, -1):
        chuoi_dao += chuoi[i]
    print("Đảo ngược:", chuoi_dao)
 
print("bài 5.9")
nguon = input("Chuỗi ban đầu: ")
muc_tieu = input("Chuỗi mục tiêu: ")
m = len(nguon)
n = len(muc_tieu)
dp = []
for i in range(m + 1):
    hang = []
    for j in range(n + 1):
        hang.append(0)
    dp.append(hang)
for i in range(m + 1):
    dp[i][0] = i
for j in range(n + 1):
    dp[0][j] = j
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if nguon[i - 1] == muc_tieu[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            a = dp[i - 1][j - 1] + 1
            b = dp[i - 1][j] + 1
            c = dp[i][j - 1] + 1
            if a <= b and a <= c:
                dp[i][j] = a
            elif b <= c:
                dp[i][j] = b
            else:
                dp[i][j] = c
print("Số thao tác tối thiểu:", dp[m][n])
 
print("bài 5.10")
chuoi = input("Nhập chuỗi: ")
ket_qua = ""
for ky_tu in chuoi:
    if ky_tu != " " and ky_tu != "\t":
        ket_qua += ky_tu
print("Gốc:", chuoi)
print("Kết quả:", ket_qua)
 