import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("--no-sandbox")  # Tắt sandbox nếu cần
        self.browser = webdriver.Edge(options=options)

    def tearDown(self):
        self.browser.quit()

    def test_user_can_login(self):
        # Đảm bảo URL đúng
        self.browser.get('http://127.0.0.1:8000/login')
        
        # Kiểm tra tiêu đề trang (cập nhật nếu cần)
        self.assertIn('GameHub', self.browser.title)

        # Tìm các trường nhập liệu
        username = self.browser.find_element(By.NAME, 'username')
        password = self.browser.find_element(By.NAME, 'password')

        # Nhập thông tin và gửi
        username.send_keys('test1')
        password.send_keys('hahahaha1234')
        password.send_keys(Keys.RETURN)

        # Chờ đến khi URL thay đổi (chắc chắn rằng người dùng đã đăng nhập thành công)
        WebDriverWait(self.browser, 10).until(
            EC.url_changes('http://127.0.0.1:8000/login')  # Đợi URL thay đổi
        )

        # Kiểm tra rằng URL đã chuyển sang trang chủ hoặc trang người dùng
        self.assertNotEqual(self.browser.current_url, 'http://127.0.0.1:8000/login')

        # Kiểm tra phần tử "Đăng xuất" xuất hiện trên trang, đảm bảo người dùng đã đăng nhập
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='logout-button']"))
        )

        # Kiểm tra rằng nút "Đăng xuất" có mặt trên trang
        self.assertIn('Đăng xuất', self.browser.page_source)

if __name__ == "__main__":
    unittest.main()
