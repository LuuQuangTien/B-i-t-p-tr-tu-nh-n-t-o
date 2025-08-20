def YesNo(bool):
    if bool == "y":
        bool = True
    elif bool == "n":
        bool = False
    else:
        bool = YesNo(input("Vui lồng nhập lại (y/n): "))
    return bool

daudau = YesNo(input("Bạn có bị đau đầu không? (y/n) "))
metmoi = YesNo(input("Bạn có mệt môi không? (y/n) "))
somui = YesNo(input("Bạn có bị sổ mủi không? (y/n) "))

if daudau and metmoi and somui:
    print("Bạn bị cảm cúm, hãy uống thuốc và nghỉ ngơi")
elif daudau and metmoi:
    print("Nguy cơ bị bệnh, xin hãy đi khám")
elif somui:
    print("Nguy cơ bị cảm cúm, xin hãy tránh tiếp xúc ngoài trời")
elif metmoi or daudau:
    print("Xin hãy nằm nghỉ")
else:
    print("Bạn bình thường")