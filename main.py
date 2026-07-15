#!/usr/bin/env python3
"""
Auto Link Bypass Tool
Tự động hóa vượt qua link rút gọn
"""

import sys
import time
from utils import LinkProcessor

def main():
    print("="*50)
    print("🚀 AUTO LINK BYPASS TOOL")
    print("="*50)
    
    # Danh sách links cần xử lý
    links = [
        "https://layma.net/1ct9Ble0b?session_token=d467db29b8c1e3ecc5e3f0d5df197018275a807cdbafc2e5622a8b5d5e742c59",
        "https://taplayma.com/link/6xk6Jj4xbk/?session_token=5f07f2ce5d2c98fb0e14f66f32601266264194203a0620b4861e3aa6f51e627a",
        "https://link4m.net/go/JKNY9Rv",
    ]
    
    processor = LinkProcessor()
    
    try:
        for idx, link in enumerate(links, 1):
            print(f"\n[{idx}/{len(links)}] Processing...")
            processor.process_link(link)
            time.sleep(2)  # Delay giữa các requests
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Người dùng dừng chương trình")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
    finally:
        processor.close()
        print("\n✅ Hoàn thành!")

if __name__ == "__main__":
    main()
