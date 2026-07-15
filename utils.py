from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import config
from twocaptcha import TwoCaptcha

class BrowserManager:
    """Quản lý browser automation"""
    
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def init_driver(self):
        """Khởi tạo Chrome driver"""
        options = webdriver.ChromeOptions()
        if config.HEADLESS_MODE:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, config.DEFAULT_TIMEOUT)
        return self.driver
    
    def close_driver(self):
        """Đóng driver"""
        if self.driver:
            self.driver.quit()
    
    def solve_captcha(self, captcha_type='recaptcha'):
        """Giải captcha dùng 2Captcha"""
        if not config.TWO_CAPTCHA_API_KEY:
            print("⚠️ Chưa set TWO_CAPTCHA_API_KEY")
            return None
        
        try:
            solver = TwoCaptcha(config.TWO_CAPTCHA_API_KEY)
            result = solver.recaptcha(sitekey='', pageurl=self.driver.current_url)
            return result
        except Exception as e:
            print(f"❌ Lỗi giải captcha: {e}")
            return None
    
    def wait_for_element(self, by, selector, timeout=None):
        """Chờ element xuất hiện"""
        timeout = timeout or config.DEFAULT_TIMEOUT
        return self.wait.until(EC.presence_of_element_located((by, selector)))
    
    def click_element(self, by, selector):
        """Click vào element"""
        element = self.wait_for_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        element.click()
    
    def simulate_human_interaction(self):
        """Mô phỏng tương tác con người (scroll, click ngẫu nhiên)"""
        actions = ActionChains(self.driver)
        # Scroll up-down
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.5)
        self.driver.execute_script("window.scrollBy(0, -150);")
        time.sleep(0.5)

class LinkProcessor:
    """Xử lý links rút gọn"""
    
    def __init__(self):
        self.browser = BrowserManager()
        self.browser.init_driver()
    
    def process_link(self, url):
        """Xử lý một link rút gọn"""
        print(f"🔗 Processing: {url}")
        try:
            self.browser.driver.get(url)
            time.sleep(2)
            
            # Bước 1: Chờ captcha
            print("⏳ Chờ captcha...")
            # TODO: Implement captcha solving
            
            # Bước 2: Chờ countdown
            print("⏳ Chờ countdown...")
            self.browser.simulate_human_interaction()
            
            # Bước 3: Lấy nhiệm vụ
            print("📋 Lấy nhiệm vụ...")
            
            return True
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            return False
    
    def close(self):
        """Đóng browser"""
        self.browser.close_driver()
