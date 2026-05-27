order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print()
    print("""===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình""")
    
    choose = int(input("Mời bạn nhập lựa chọn: "))

    match choose:
        case 1:
            for i, name in enumerate(order_list, start=1):
                if not order_list:
                    print("Danh sách đơn hàng hiện đang trống.")
                else:
                    print(f"{i}. {name}")

        case 2:
            while True:
                print()
                print("""----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
1. Thêm đơn hàng mới
2. Sửa đơn hàng theo vị trí
3. Xóa đơn hàng theo vị trí
4. Quay lại menu chính
 """)
                option = int(input("Mời bạn nhập lựa chọn: "))

                # Thêm
                if option == 1:
                    add_code = input("Nhập mã đơn hàng: ").strip().upper() 
                    add_status = input("Nhập trạng thái: ").strip().upper()
                    add_order = f"{add_code} - {add_status}"
                    order_list.append(add_order)
                    print("Thêm đơn hàng mới thành công")
                    for i, name in enumerate(order_list, start=1):
                        print(f"{i}. {name}")
                
                # Sửa
                elif option == 2:
                    update_poisition = input("Nhập vị trí cần sửa: ")
                    if not update_poisition.isdigit():
                        print("Vị trí không hợp lệ")
                        continue
                    update_poisition = int(update_poisition)
                    
                    if update_poisition < 1 or update_poisition > len(order_list):
                        print("Lựa chọn không hợp lệ")
                        continue
                    update_code = input("Nhập mã mới: ").strip().upper()
                    update_status = input("Nhập trạng thái mới: ").strip().upper()
                    order_list[update_poisition - 1] = f"{update_code} - {update_status}"
                    for i, name in enumerate(order_list, start=1):
                        print(f"{i}. {name}")
                # Xóa
                elif option == 3:
                    delete_poisition = input("Nhập vị trí cần xóa: ")
                    if not delete_poisition.isdigit():
                        print("Vị trí không hợp lệ")
                        continue
                    delete_poisition = int(delete_poisition)
                    
                    if delete_poisition < 1 or delete_poisition > len(order_list):
                        print("Lựa chọn không hợp lệ")
                    delete = order_list.pop(delete_poisition - 1)
                    print("Đã xóa", delete)
                    for i, name in enumerate(order_list, start=1):
                        print(f"{i}. {name}")
                        

                elif option == 4:
                    break

                else:
                    print("Lựa chọn không hợp lệ")
        
        case 3:
            pending = 0
            delivering = 0
            completed = 0
            cancelled = 0
            for order in order_list:
                data = order.split("-")
                if data[1].strip() == "PENDING":
                    pending += 1
                elif data[1].strip() == "DELIVERING":
                    delivering += 1
                elif data[1].strip() == "COMPLETED":
                    completed += 1
                elif data[1].strip() == "CANCELLED":
                    cancelled += 1
            print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
            print("PENDING: ", pending)
            print("DELIVERING: ", delivering)
            print("COMPLETED: ", completed)
            print("CANCELLED: ", cancelled)
            print("Tổng số đơn hàng: ", len(order_list))

        case 4:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ")