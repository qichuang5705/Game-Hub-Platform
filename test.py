import os
import zipfile
import random

def extract_with_unique_folder(zip_path, extract_to):
    """
    Giải nén file .zip và đảm bảo thư mục không bị trùng tên.
    zip_path: Đường dẫn tới file .zip
    extract_to: Thư mục đích để giải nén
    """
    # Lấy tên file .zip (không có đuôi)
    file_name = os.path.basename(zip_path)[:-4]  # Bỏ ".zip", ví dụ: "z.zip" -> "z"

    # Kiểm tra thư mục đích
    dest_folder = os.path.join(extract_to, file_name)
    while os.path.exists(dest_folder):
        random_suffix = str(random.randint(100, 999))  # Tạo hậu tố ngẫu nhiên
        dest_folder = os.path.join(extract_to, f"{file_name}_{random_suffix}")

    # Tạo thư mục đích mới
    os.makedirs(dest_folder, exist_ok=True)

    # Giải nén file .zip vào thư mục mới
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)

    print(f"Đã giải nén {zip_path} vào {dest_folder}")
    return dest_folder
# Đường dẫn file cũ
file = "C:\\Users\\Huy Le\\Desktop\\Projects\\gamehub\\catch_the_ball_709.z111ip"
new = os.rename(file, 'ab')

print(new)