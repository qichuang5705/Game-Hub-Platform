from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://localhost:8000")  # Cập nhật URL nếu cần


openuser = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "open1")))
openuser.click()
print("open1 oke")


login_button_opne = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "open2222")))
login_button_opne.click()
print("open2222 oke")


username_input = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "login1")))
password_input = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "pass1")))
login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "but1")))


username_input.send_keys("testing")
password_input.send_keys("huy123123")
login_button.click()

dashboard_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "ncanscn"))
)
assert dashboard_element is not None
print("Đăng nhập thành công, vào dashboard!")


openuser = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "open2")))
openuser.click()
print("open1 oke")


doi_thuong_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "doithuong"))
)
doi_thuong_button.click()
print("Đã ấn nút Đổi thưởng!")

WebDriverWait(browser, 10).until(EC.url_contains("/bag"))
print("Đã vào trang Đổi thưởng!")