#!/usr/bin/env python3
import binascii
import re
import sys

# --- الهوية الرمزية للمهندس إحسان ---
EHSAN_BANNER = r"""
      Capturing Data... 
             !
             !
             ^
            / \
           /___\
          |=   =|
          |  E  |
          |  H  |
          |  S  |
          |  A  |
          |  N  |
          |     |
          |_____|
          |/ \ / \
          ((   ))
         ((  +  ))
        ((   +   ))
       ((    +    ))
      ---------------------------------------
      ENG. EHSAN - CYBER SECURITY ROCKET v1.0
      ---------------------------------------
"""

def read_firmware(file_path):
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[-] Error: {file_path} not found!")
        return None

def analyze_hex_data(data):
    hex_data = binascii.hexlify(data)
    # البحث عن نمط سداسي عشر (Hex) يشبه كلمات المرور أو المفاتيح
    passwords = re.findall(b'[0-9a-fA-F]{8,16}', hex_data)
    return hex_data, passwords

def main():
    # طباعة الهوية عند التشغيل
    print(EHSAN_BANNER)
    
    file_path = 'firmware.bin'
    data = read_firmware(file_path)
    
    if data:
        hex_data, passwords = analyze_hex_data(data)
        print(f"[*] Analyzing: {file_path}")
        print(f"[*] Result: Found {len(passwords)} potential Hex strings.\n")
        
        print(f"{'INDEX':<8} | {'HEX DATA':<18} | {'OFFSET'}")
        print("-" * 45)
        
        for i, pwd in enumerate(passwords):
            offset = hex_data.find(pwd)
            print(f"{i+1:<8} | {pwd.decode():<18} | {hex(offset)}")
        
        print("\n" + "="*45)
        print("Done. Ready for GitHub Upload, Eng. Ehsan!")
        print("="*45)
    else:
        print("[-] Please create 'firmware.bin' to start analysis.")

if __name__ == "__main__":
    main()
