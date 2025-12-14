# install.py
import os
import stat

# 우리가 만들 파일의 경로: .git/hooks/pre-push
HOOK_PATH = os.path.join(".git", "hooks", "pre-push")

# 파일에 들어갈 내용 (쉘 스크립트)
# $PYTHON_EXEC은 현재 실행 중인 파이썬 경로를 자동으로 찾음
SCRIPT_CONTENT = f"""#!/bin/sh
echo " [Zen-Commit] Hook Triggered!"
python3 src/zen_guard.py
"""

def install():
    if not os.path.exists(".git"):
        print("Error: git init을 먼저 하세요.")
        return

    # 1. 파일 쓰기
    with open(HOOK_PATH, "w", encoding="utf-8") as f:
        f.write(SCRIPT_CONTENT)
    
    # 2. 실행 권한 주기 (이게 없으면 실행 안 됨!)
    st = os.stat(HOOK_PATH)
    os.chmod(HOOK_PATH, st.st_mode | stat.S_IEXEC)
    
    print(f"Installed to {HOOK_PATH}")

if __name__ == "__main__":
    install()

#위의 코드는 전부 다 git이 깔려 있다는 것을 전제로 해서 만들었는데 평가하는 사람들의 환경을 몰라서 
#install.py는 그냥 남기기로 했습니다.