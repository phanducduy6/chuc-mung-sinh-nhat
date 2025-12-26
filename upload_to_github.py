import os
import subprocess

# --- CẤU HÌNH THÔNG TIN ---
REPO_URL = "https://github.com/USER_CUA_BAN/TEN_REPO.git"  # Thay link của bạn vào đây
FILE_NAME = "unlock_code.py"
COMMIT_MESSAGE = "Upload code mo khoa 26122025"

# --- 1. TẠO FILE CODE NỘI DUNG ---
content = f"""
# Code mo khoa giao dien Among Us
# Password: 26122025

def unlock():
    print("Dang mo khoa voi mat ma: 26122025")
    # Gia lap thao tac go phim
    import pyautogui
    pyautogui.sleep(2)
    pyautogui.typewrite('26122025')

if __name__ == "__main__":
    unlock()
"""

with open(FILE_NAME, "w", encoding="utf-8") as f:
    f.write(content)

# --- 2. CHẠY CÁC LỆNH GIT ĐỂ TẢI LÊN ---
def run_git_commands():
    try:
        # Khoi tao git neu chua co
        subprocess.run(["git", "init"], check=True)
        
        # Add file
        subprocess.run(["git", "add", FILE_NAME], check=True)
        
        # Commit
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True)
        
        # Dat ten nhanh chinh la main
        subprocess.run(["git", "branch", "-M", "main"], check=True)
        
        # Them remote (neu da ton tai thi thong bao)
        subprocess.run(["git", "remote", "add", "origin", REPO_URL], stderr=subprocess.DEVNULL)
        
        # Push len GitHub
        print("Dang tai code len GitHub...")
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        
        print("--- THANH CONG! Code cua ban da co tren GitHub. ---")
    except Exception as e:
        print(f"Co loi xay ra: {e}")

if __name__ == "__main__":
    run_git_commands()
