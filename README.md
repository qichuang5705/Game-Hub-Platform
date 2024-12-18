IDEA OF PROJECT: Game Hub Platform gồm: *Chu y: Mỗi giao diện có logi game hub bên trái trên cùng để người nhập vào và quay lại trang chủ game. *Kéo xuống dưới cùng luôn có các thông tin nhóm như tên nhóm thành viên, fb, ins, git, ytb...

Giao diện đăng nhập, đăng kí, quên mật khẩu, nút xác nhận Guest (ấn vô để vô trang chủ game không cần tài khoản)
-Giao diện trang chủ game: A

nơi chứa các hình ảnh trò chơi, có nút play hay cái đó để người các user nhấp vào chơi. Mỗi thao tác nhấn chơi sẽ chuyển một frontend cho các developer tạo ra
Ấn vào nút view sẽ hiện thông tin, đánh giá, bảnh xếp
Có nút hình icon của tài khoản để xem profile hay đăng xuất
Chèn quảng cáo nếu cần
Ô nạp vip premium cho tài khoản (trừ role guest)
Giao diện từng vai trò kế thừa A (Giao diện trang chủ game: @Guest: -không có ô hiện bảng xếp hạng từng game @Player: -Có ô hiện bảng xếp hạng từng game -Ô hiện điểm thưởng từ việc chơi game

@Development: -Có nút chuyển qua giao diện đăng tải xoá game

@Designer -Có nút chuyển qua gaio diện đăng tải các tài nguyên

@System Admin -Có nút chuyển qua giao duyệt nâng cấp tài khoản -Có nút chuyển qua giao diện thống kê lượt chơi, rate of game của từng development để trả công cho họ

#GameHUb/
    ├── GameHUb         #App gốc(root)
    ├── accounts      # App quản lý tài khoản 
    ├── games          # App quản lý trò chơi
    ├── assets         # App quản lý tài sản  
    ├── reviews        # App cho Player review
    ├── rewards         # App quản lý hệ thống tích điểm thưởng
    ├── payments        # App quản lý thanh toán và giao dịch
    ├── administrator  # App dành cho System admin
