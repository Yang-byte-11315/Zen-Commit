import time
import sys
import random

def run_simulation():
    print("\n" + "="*50)
    print(f"   [System] Zen-Commit Simulation Started")
    print("="*50 + "\n")
    
    print(">> Developer is typing code...")
    time.sleep(1)
    
    print(f" git add .")
    time.sleep(0.5)
    
    print(f" git commit -m 'Fix critical bug'")
    print("   [main 8f3a12] Fix critical bug")
    print("   1 file changed, 12 insertions(+)\n")
    time.sleep(1)

    print(f" git push origin main")
    time.sleep(0.5)
    
    print(f"\n [Git Hook Triggered] Checking Vital Signs...")
    time.sleep(1)

    print(f"\n[Simulation Control]")
    print("1: ANGRY (Push Blocked)")
    print("2: CALM (Push Success)")
    # 원래는 웨어러블 API랑 연동이 되도록 해야 했는데 git 없으면 안되서 
    # 그냥 demo 파일 만들어서 진행함
    choice = input(" Enter number (1 or 2): ")

    if choice == '1':
        bpm = random.randint(101, 140) 
    else:
        bpm = random.randint(60, 95)

    print(f"\nMeasuring Heart Rate...")
    time.sleep(1)
    print(f" Heart Rate: {bpm} BPM")
    time.sleep(0.5)

    if bpm > 100:
        print(f"\n[X] PUSH BLOCKED! High Stress Detected.")
        print(f"    Reason: Heart rate ({bpm}) > 100.")
        print(f"    Action: Git push cancelled.")
        print("-" * 50)
        print(f"    Advice: Take a deep breath.")
    else:
        print(f"\n[V] ZEN STATE CONFIRMED.")
        print(f"    Writing objects: 100% (3/3), done.")
        print(f"    To github.com:user/project.git")
        print(f"    * [new branch]      main -> main")

    print("\n" + "="*50)
    print("   Simulation Finished.")
    print("="*50)

    input("\n(Press Enter to exit)")

if __name__ == "__main__":
    run_simulation()