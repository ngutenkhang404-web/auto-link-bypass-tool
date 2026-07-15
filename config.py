import os
from dotenv import load_dotenv

load_dotenv()

# 2Captcha API Key
TWO_CAPTCHA_API_KEY = os.getenv('TWO_CAPTCHA_API_KEY', '')

# Browser settings
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH', '/usr/local/bin/chromedriver')
HEADLESS_MODE = os.getenv('HEADLESS_MODE', 'False').lower() == 'true'

# Timeouts (seconds)
DEFAULT_TIMEOUT = 30
CAPTCHA_TIMEOUT = 120
COUNTDOWN_TIMEOUT = 60

# Target links
TARGET_LINKS = [
    'layma.net',
    'taplayma.com',
    'link4m.net'
]
