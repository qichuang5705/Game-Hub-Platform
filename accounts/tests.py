import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from time import sleep

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("--no-sandbox")  # Tắt sandbox nếu cần
        self.browser = webdriver.Edge(options=options)

    def tearDown(self):
        self.browser.quit()

    def test_user_can_login(self):
        # Đảm bảo URL đúng
        self.browser.get('http://127.0.0.1:8000/loginas')
        
        # Kiểm tra tiêu đề trang (cập nhật nếu cần)
        self.assertIn('Login', self.browser.title)

        # Tìm các trường nhập liệu
        username = self.browser.find_element(By.NAME, 'username')
        password = self.browser.find_element(By.NAME, 'password')

        # Nhập thông tin và gửi
        username.send_keys('admin1')
        password.send_keys('123456')
        password.send_keys(Keys.RETURN)
        sleep(5)
        
        # Kiểm tra kết quả đăng nhập
        self.assertIn('Welcome, test1', self.browser.page_source)
        

if __name__ == "__main__":
    unittest.main()
