print("1. Change Celsius to Fahrenheit")
print("2. Change Fahrenheit to Celsius")

choice = int(input("nhập vào lựa chọn: "))
if choice == 1: 
    c = float(input("Nhập vào nhiệt độ C: "))
    f = c * 9/5 + 32
    print("Nhiệt độ F là:", f)
elif choice == 2:
    f = float(input("Nhập vào nhiệt độ F: "))
    c = (f -32)*5/9
    print("Nhiệt độ C là:", c)
else:
    print("Lựa chọn không hợp lệ")
