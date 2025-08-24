import numpy as np
import math

#Bài 1:
ArrayBai1 = [-2, 6, 3, 10, 15, 48]
print(ArrayBai1[2:4])
print(ArrayBai1[1::2])
print(ArrayBai1[3::])
print(ArrayBai1[:2:-1])

#Bài 2:
ArayBai2 = np.random.randint(0, 30, (3, 3))
print(ArayBai2)
print(ArayBai2.max()) #lấy giá trị lớn nhất mảng
print(ArayBai2.max(0)) #lấy giá trị lớn nhất từng cột trong mảng
print(ArayBai2.max(1)) #lấy giá trị lớn nhất từng hàng trong mảng

#Bài 3:
def pt_bac1(a, b):
    if(a == 0):
        if(b == 0): print("Phương trình bậc 1 vô số nghiệm")
        else: print("Phương trình bậc 1 vô nghiệm")
    else:
        x = float(-b / a)
        print("Phương trình có nghiệm x = ", x)

def pt_bac2(a, b, c):
    if(a == 0):
        pt_bac1(b, c)
    else:
        delta = float(b**2 - 4 * a * c)
        #print(delta)
        if(delta > 0):
            x1 = float(-b + math.sqrt(delta)) / (2 * a)
            x2 = float(-b - math.sqrt(delta)) / (2 * a)
            print("Phương trình bậc 2 có 2 nghiệm x1 = ",x1, ", x2 = ",x2)
        elif(delta == 0):
            x = float(-b / (2 * a))
            print("Phương trình bậc 2 có nghiệm x = ", x)
        else:
            print("Phương trình bậc 2 vô nghiệm")

ArrayBai3 = list(map(int, input("Nhập các hệ số phương trình: ").split()))
count = len(ArrayBai3)

if(count == 2):
    a = ArrayBai3[0]
    b = ArrayBai3[1]
    pt_bac1(a, b)
elif(count == 3):
    a = ArrayBai3[0]
    b = ArrayBai3[1]
    c = ArrayBai3[2]
    pt_bac2(a, b, c)
else: print("Hãy nhập 2 hệ số cho pt bậc 1 và 3 hệ số cho pt bậc 2")

#Bài 4: Code có tham khảo từ trang: https://pythonforundergradengineers.com/creating-taylor-series-functions-with-python.html
x = math.radians(int(input("Nhập giá trị góc x: ")))
i = 0
cosx = 0
while(i <= 20):
   a = 2 * i
   b = math.factorial(a)
   cosx += ((-1)**i) * (x**a) / b
   i += 1

print("cos(x) có giá trị: ", cosx)

#Bài 5:
bang_diem = {23110151: {'Điện tử căn bản': 8.25, 'Thể chất 3': 7, 'Kỹ thuật máy tính': 4.75},
             23110152: {'Điện tử căn bản': 6.5, 'Thể chất 3': 4, 'Kỹ thuật máy tính': 3.25},
             23110157: {'Điện tử căn bản': 4.5, 'Thể chất 3': 7, 'Kỹ thuật máy tính': 8}
             }
x = int(input("Hãy nhập mã số sinh viên: "))
ArrayBai5 = []

if(x in bang_diem):
    for subj, diem in bang_diem[x].items():
        if(diem < 5): ArrayBai5.append(subj)
    print(ArrayBai5)
else: print("Mã số sinh viên không tồn tại")