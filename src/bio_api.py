# src/bio_api.py
import random
import time

class BioMonitor:
    def get_heart_rate(self):
        # 센서 연결되는 모션을 구현하기
        print("[Sensor] Connecting to pulse meter...", end=" ", flush=True)
        time.sleep(0.5) 
        print("Connected.")
        
        # 2. 60~120 사이의 랜덤값 리턴 (화난 상태 시뮬레이션)
        return random.randint(60, 120)
    #실제 데이터를 불러오는 코드는 