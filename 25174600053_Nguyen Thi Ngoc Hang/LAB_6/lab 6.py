print("bài 6.1")
n = int(input("Nhập n: "))
mang = []
for i in range(n):
    mang.append(int(input("Phần tử " + str(i+1) + ": ")))
chan = []
le = []
for x in mang:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)
tong_chan = 0
for x in chan:
    tong_chan += x
tong_le = 0
for x in le:
    tong_le += x
print("Số chẵn:", chan, "- tổng:", tong_chan)
print("Số lẻ:", le, "- tổng:", tong_le)

print("bài 6.2")
n = int(input("Nhập n: "))
mang = []
for i in range(n):
    mang.append(int(input("Phần tử " + str(i+1) + ": ")))
ket_qua = []
for x in mang:
    la_ngt = False
    if x >= 2:
        la_ngt = True
        i = 2
        while i * i <= x:
            if x % i == 0:
                la_ngt = False
                break
            i += 1
    la_hoan_hao = False
    if x >= 2:
        tong_uoc = 1
        i = 2
        while i * i <= x:
            if x % i == 0:
                tong_uoc += i
                if i != x // i:
                    tong_uoc += x // i
            i += 1
        if tong_uoc == x:
            la_hoan_hao = True
    if la_ngt or la_hoan_hao:
        ket_qua.append(x)
print("Kết quả:", ket_qua)

print("bài 6.3")
n = int(input("Nhập số lượng phần tử: "))
day = []
for i in range(n):
    day.append(float(input("Phần tử " + str(i+1) + ": ")))
lon_nhat = day[0]
nho_nhat = day[0]
for x in day:
    if x > lon_nhat:
        lon_nhat = x
    if x < nho_nhat:
        nho_nhat = x
print("Lớn nhất:", lon_nhat)
print("Nhỏ nhất:", nho_nhat)

print("bài 6.4")
n = int(input("Nhập n: "))
fib = []
a = 0
b = 1
for i in range(n):
    fib.append(a)
    temp = a + b
    a = b
    b = temp
print(str(n) + " số Fibonacci đầu tiên:", fib)

print("bài 6.5")
ds_ngt = []
for so in range(2, 100):
    la_ngt = True
    i = 2
    while i * i <= so:
        if so % i == 0:
            la_ngt = False
            break
        i += 1
    if la_ngt:
        ds_ngt.append(so)
print("Số nguyên tố < 100:", ds_ngt)

print("bài 6.6")
n = int(input("Nhập số lượng phần tử: "))
day = []
for i in range(n):
    day.append(int(input("Phần tử " + str(i+1) + ": ")))
if n < 2:
    print("Cần ít nhất 2 phần tử.")
else:
    cong_sai = day[1] - day[0]
    la_csc = True
    for i in range(2, n):
        if day[i] - day[i - 1] != cong_sai:
            la_csc = False
            break
    if la_csc:
        print("Dãy là cấp số cộng với d =", cong_sai)
    else:
        print("Dãy không phải cấp số cộng.")

print("bài 6.7")
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        hang.append(int(input("[" + str(i+1) + "][" + str(j+1) + "]: ")))
    ma_tran.append(hang)
tong = 0
for i in range(m):
    for j in range(n):
        tong += ma_tran[i][j]
print("Ma trận:")
for hang in ma_tran:
    print(hang)
print("Tổng:", tong)

print("bài 6.8")
n = int(input("Nhập kích thước ma trận vuông n: "))
a = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(int(input("A[" + str(i+1) + "][" + str(j+1) + "]: ")))
    a.append(hang)
b = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(int(input("B[" + str(i+1) + "][" + str(j+1) + "]: ")))
    b.append(hang)
tich = []
for i in range(n):
    hang = []
    for j in range(n):
        s = 0
        for k in range(n):
            s += a[i][k] * b[k][j]
        hang.append(s)
    tich.append(hang)
print("Tích A x B:")
for hang in tich:
    print(hang)

print("bài 6.9")
n = int(input("Nhập kích thước ma trận vuông n: "))
mt = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(int(input("[" + str(i+1) + "][" + str(j+1) + "]: ")))
    mt.append(hang)
chuyen_vi = []
for j in range(n):
    hang = []
    for i in range(n):
        hang.append(mt[i][j])
    chuyen_vi.append(hang)
print("Ma trận chuyển vị:")
for hang in chuyen_vi:
    print(hang)
doi_xung = True
for i in range(n):
    for j in range(n):
        if mt[i][j] != chuyen_vi[i][j]:
            doi_xung = False
            break
if doi_xung:
    print("Ma trận đối xứng.")
else:
    print("Ma trận không đối xứng.")

print("bài 6.10")
n = int(input("Nhập kích thước ma trận vuông n: "))
mt = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(float(input("[" + str(i+1) + "][" + str(j+1) + "]: ")))
    mt.append(hang)

stack_mt = [mt]
stack_sz = [n]
stack_results = []
stack_col = []
stack_i = []

while len(stack_mt) > 0:
    cur_mt = stack_mt[-1]
    cur_sz = stack_sz[-1]
    if cur_sz == 1:
        stack_results.append(cur_mt[0][0])
        stack_mt.pop()
        stack_sz.pop()
        if len(stack_col) > 0:
            col = stack_col.pop()
            parent_mt = stack_i.pop()
            val = stack_results.pop()
            dau = 1 if col % 2 == 0 else -1
            parent_mt[0] += dau * parent_mt[1][0][col] * val
            if col + 1 < len(parent_mt[1][0]):
                next_col = col + 1
                sub = []
                for r in range(1, len(parent_mt[1])):
                    hr = []
                    for c in range(len(parent_mt[1][0])):
                        if c != next_col:
                            hr.append(parent_mt[1][r][c])
                    sub.append(hr)
                stack_col.append(next_col)
                stack_i.append(parent_mt)
                stack_mt.append(sub)
                stack_sz.append(len(sub))
            else:
                stack_results.append(parent_mt[0])
    elif cur_sz == 2:
        stack_results.append(cur_mt[0][0] * cur_mt[1][1] - cur_mt[0][1] * cur_mt[1][0])
        stack_mt.pop()
        stack_sz.pop()
        if len(stack_col) > 0:
            col = stack_col.pop()
            parent_mt = stack_i.pop()
            val = stack_results.pop()
            dau = 1 if col % 2 == 0 else -1
            parent_mt[0] += dau * parent_mt[1][0][col] * val
            if col + 1 < len(parent_mt[1][0]):
                next_col = col + 1
                sub = []
                for r in range(1, len(parent_mt[1])):
                    hr = []
                    for c in range(len(parent_mt[1][0])):
                        if c != next_col:
                            hr.append(parent_mt[1][r][c])
                    sub.append(hr)
                stack_col.append(next_col)
                stack_i.append(parent_mt)
                stack_mt.append(sub)
                stack_sz.append(len(sub))
            else:
                stack_results.append(parent_mt[0])
    else:
        sub = []
        for r in range(1, cur_sz):
            hr = []
            for c in range(cur_sz):
                if c != 0:
                    hr.append(cur_mt[r][c])
            sub.append(hr)
        holder = [0, cur_mt]
        stack_col.append(0)
        stack_i.append(holder)
        stack_mt.append(sub)
        stack_sz.append(cur_sz - 1)

det = stack_results[-1]
if det == 0:
    print("Ma trận không khả nghịch (định thức = 0).")
else:
    nghich_dao = []
    for i in range(n):
        hang = []
        for j in range(n):
            sub2 = []
            for r in range(n):
                if r == i:
                    continue
                hr = []
                for c in range(n):
                    if c == j:
                        continue
                    hr.append(mt[r][c])
                sub2.append(hr)
            if len(sub2) == 1:
                minor = sub2[0][0]
            elif len(sub2) == 2:
                minor = sub2[0][0] * sub2[1][1] - sub2[0][1] * sub2[1][0]
            else:
                stk_m = [sub2]
                stk_s = [len(sub2)]
                stk_r = []
                stk_c = []
                stk_p = []
                while len(stk_m) > 0:
                    cm = stk_m[-1]
                    cs = stk_s[-1]
                    if cs == 1:
                        stk_r.append(cm[0][0])
                        stk_m.pop()
                        stk_s.pop()
                        if len(stk_c) > 0:
                            cc = stk_c.pop()
                            pp = stk_p.pop()
                            vv = stk_r.pop()
                            dd = 1 if cc % 2 == 0 else -1
                            pp[0] += dd * pp[1][0][cc] * vv
                            if cc + 1 < len(pp[1][0]):
                                nc = cc + 1
                                ns = []
                                for rr in range(1, len(pp[1])):
                                    nh = []
                                    for hc in range(len(pp[1][0])):
                                        if hc != nc:
                                            nh.append(pp[1][rr][hc])
                                    ns.append(nh)
                                stk_c.append(nc)
                                stk_p.append(pp)
                                stk_m.append(ns)
                                stk_s.append(len(ns))
                            else:
                                stk_r.append(pp[0])
                    elif cs == 2:
                        stk_r.append(cm[0][0]*cm[1][1] - cm[0][1]*cm[1][0])
                        stk_m.pop()
                        stk_s.pop()
                        if len(stk_c) > 0:
                            cc = stk_c.pop()
                            pp = stk_p.pop()
                            vv = stk_r.pop()
                            dd = 1 if cc % 2 == 0 else -1
                            pp[0] += dd * pp[1][0][cc] * vv
                            if cc + 1 < len(pp[1][0]):
                                nc = cc + 1
                                ns = []
                                for rr in range(1, len(pp[1])):
                                    nh = []
                                    for hc in range(len(pp[1][0])):
                                        if hc != nc:
                                            nh.append(pp[1][rr][hc])
                                    ns.append(nh)
                                stk_c.append(nc)
                                stk_p.append(pp)
                                stk_m.append(ns)
                                stk_s.append(len(ns))
                            else:
                                stk_r.append(pp[0])
                    else:
                        ns = []
                        for rr in range(1, cs):
                            nh = []
                            for hc in range(cs):
                                if hc != 0:
                                    nh.append(cm[rr][hc])
                            ns.append(nh)
                        hh = [0, cm]
                        stk_c.append(0)
                        stk_p.append(hh)
                        stk_m.append(ns)
                        stk_s.append(cs - 1)
                minor = stk_r[-1]
            dau = 1 if (i + j) % 2 == 0 else -1
            hang.append(dau * minor / det)
        nghich_dao.append(hang)
    nghich_dao_T = []
    for j in range(n):
        hang = []
        for i in range(n):
            hang.append(nghich_dao[i][j])
        nghich_dao_T.append(hang)
    print("Ma trận nghịch đảo:")
    for hang in nghich_dao_T:
        dong = []
        for x in hang:
            dong.append(round(x, 4))
        print(dong)