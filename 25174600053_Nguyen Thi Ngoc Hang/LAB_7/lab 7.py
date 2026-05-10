print("bài 7.1")
N = int(input("Nhập N: "))
tu_dien = {}
for x in range(1, N + 1):
    tu_dien[x] = x ** 3
print("Từ điển:", tu_dien)

print("bài 7.2")
n = int(input("Nhập số sinh viên: "))
tu_dien = {}
for i in range(n):
    ten = input("Tên sinh viên " + str(i+1) + ": ")
    diem = float(input("Điểm của " + ten + ": "))
    if diem >= 9.0:
        xep_loai = 'A'
    elif diem >= 8.0:
        xep_loai = 'B'
    elif diem >= 7.0:
        xep_loai = 'C'
    elif diem >= 5.0:
        xep_loai = 'D'
    else:
        xep_loai = 'F'
    tu_dien[ten] = xep_loai
print("Kết quả xếp loại:")
for ten in tu_dien:
    print(" ", ten, ":", tu_dien[ten])

print("bài 7.3")
n = int(input("Nhập số sinh viên: "))
tu_dien_sv = {}
for i in range(n):
    ten = input("Tên sinh viên " + str(i+1) + ": ")
    diem = float(input("Điểm của " + ten + ": "))
    if diem >= 9.0:
        xep_loai = 'A'
    elif diem >= 8.0:
        xep_loai = 'B'
    elif diem >= 7.0:
        xep_loai = 'C'
    elif diem >= 5.0:
        xep_loai = 'D'
    else:
        xep_loai = 'F'
    tu_dien_sv[ten] = xep_loai
dem = {}
for ten in tu_dien_sv:
    loai = tu_dien_sv[ten]
    if loai in dem:
        dem[loai] += 1
    else:
        dem[loai] = 1
print("Số sinh viên theo từng mức:")
for loai in dem:
    print("  Loại", loai, ":", dem[loai], "sinh viên")

print("bài 7.4")
van_ban = input("Nhập đoạn văn bản tiếng Anh: ")
van_ban_sach = ""
for c in van_ban:
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == ' ':
        if 'A' <= c <= 'Z':
            van_ban_sach += chr(ord(c) + 32)
        else:
            van_ban_sach += c
    else:
        van_ban_sach += ' '
tu_vung = {}
tu_hien_tai = ""
for c in van_ban_sach + " ":
    if c != ' ':
        tu_hien_tai += c
    else:
        if tu_hien_tai != "":
            if tu_hien_tai in tu_vung:
                tu_vung[tu_hien_tai] += 1
            else:
                tu_vung[tu_hien_tai] = 1
            tu_hien_tai = ""
print("Tần suất từ vựng:")
for tu in tu_vung:
    print(" ", tu, ":", tu_vung[tu])

print("bài 7.5")
van_ban = input("Nhập văn bản: ")
van_ban_sach = ""
for c in van_ban:
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == ' ':
        if 'A' <= c <= 'Z':
            van_ban_sach += chr(ord(c) + 32)
        else:
            van_ban_sach += c
    else:
        van_ban_sach += ' '
tu_vung = {}
tu_hien_tai = ""
for c in van_ban_sach + " ":
    if c != ' ':
        tu_hien_tai += c
    else:
        if tu_hien_tai != "":
            if tu_hien_tai in tu_vung:
                tu_vung[tu_hien_tai] += 1
            else:
                tu_vung[tu_hien_tai] = 1
            tu_hien_tai = ""
tu_cao = ""
tu_thap = ""
max_sl = -1
min_sl = -1
for tu in tu_vung:
    sl = tu_vung[tu]
    if sl > max_sl:
        max_sl = sl
        tu_cao = tu
    if min_sl == -1 or sl < min_sl:
        min_sl = sl
        tu_thap = tu
print("Từ tần suất cao nhất:", tu_cao, "-", max_sl, "lần")
print("Từ tần suất thấp nhất:", tu_thap, "-", min_sl, "lần")

print("bài 7.6")
inventory = {"gold": 100, "backpack": ["sword", "shield", "potion"]}
inventory["pocket"] = ["key", "map"]
inventory["gold"] += 50
print("Inventory:", inventory)

print("bài 7.7")
inventory = {"gold": 150, "backpack": ["sword", "apple", "map", "shield"], "pocket": ["key", "map"]}
ds = []
for vat_pham in inventory["backpack"]:
    ds.append(vat_pham)
for i in range(len(ds)):
    for j in range(i + 1, len(ds)):
        if ds[i] > ds[j]:
            tam = ds[i]
            ds[i] = ds[j]
            ds[j] = tam
vat_pham_xoa = input("Nhập tên vật phẩm cần xóa khỏi backpack: ")
ds_moi = []
for vat_pham in ds:
    if vat_pham != vat_pham_xoa:
        ds_moi.append(vat_pham)
inventory["backpack"] = ds_moi
print("Backpack sau khi sắp xếp và xóa:", inventory["backpack"])

print("bài 7.8")
n = int(input("Nhập số mặt hàng: "))
kho = {}
for i in range(n):
    ten = input("Tên mặt hàng " + str(i+1) + ": ")
    so_luong = int(input("  Số lượng: "))
    don_gia = float(input("  Đơn giá: "))
    kho[ten] = [so_luong, don_gia]
print("===== HÓA ĐƠN =====")
tong = 0
for ten in kho:
    chi_phi = kho[ten][0] * kho[ten][1]
    tong += chi_phi
    print(" ", ten, ":", kho[ten][0], "x", kho[ten][1], "=", chi_phi, "VNĐ")
print("Tổng:", tong, "VNĐ")

print("bài 7.9")
n = int(input("Nhập số mặt hàng: "))
kho = {}
for i in range(n):
    ten = input("Tên mặt hàng " + str(i+1) + ": ")
    so_luong = int(input("  Số lượng: "))
    kho[ten] = so_luong
chay = True
while chay:
    ten = input("Tên hàng giao dịch (nhập 'xong' để kết thúc): ")
    if ten == "xong":
        chay = False
    elif ten not in kho:
        print("Không có mặt hàng này.")
    else:
        so_ban = int(input("Số lượng bán (" + str(kho[ten]) + " hiện có): "))
        if so_ban > kho[ten]:
            print("Không đủ hàng!")
        else:
            kho[ten] -= so_ban
            print("Thành công. Còn lại:", kho[ten])
print("Báo cáo tồn kho:")
for ten in kho:
    print(" ", ten, ":", kho[ten])

print("bài 7.10")
kho_hang = set()
n = int(input("Số mặt hàng trong kho: "))
for i in range(n):
    kho_hang.add(input("  Mặt hàng " + str(i+1) + ": "))
khach_da_chon = set()
m = int(input("Số mặt hàng khách đã chọn: "))
for i in range(m):
    khach_da_chon.add(input("  Khách chọn " + str(i+1) + ": "))
chua_duoc_chon = kho_hang - khach_da_chon
print("Mặt hàng chưa được chọn:", chua_duoc_chon)