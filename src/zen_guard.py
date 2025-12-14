# src/zen_guard.py
import sys
from bio_api import BioMonitor

MAX_BPM = 100  # 기준값 설정

def main():
    monitor = BioMonitor()
    bpm = monitor.get_heart_rate()
    
    print(f"Current Heart Rate: {bpm} BPM")
    
    if bpm > MAX_BPM:
        print("DANGER: You are too angry to code!")
        print("Push Blocked by Zen-Commit.")
        sys.exit(1)  # Git에게 "멈춰!" 신호 보냄
    else:
        print("Peace: You are calm.")
        sys.exit(0)  # Git에게 "통과!" 신호 보냄

if __name__ == "__main__":
    main()