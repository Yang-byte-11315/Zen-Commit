Zen-Commit/
├── demo.py           평가용 시뮬레이터 (Git 없이 작동)
├── install.py        [실제 구현] Git Hook 자동 설치 스크립트
├── requirements.txt  의존성 패키지 목록
└── src/
    ├── zen_guard.py  심박수 판단 및 차단 로직 
    └── bio_api.py    생체 신호 데이터 처리 모듈
"개발자의 심리적/신체적 상태는 코드의 **품질**과 직결됩니다. 특히 마감 압박이나 스트레스 상황에서 작성된 코드는 논리적 오류(Bug)를 포함할 확률이 매우 높습니다. 이 프로젝트는 단순한 코드 검사를 넘어, 개발자의 생체 신호(심박수)를 분석하여 평온한 상태에서만 배포(Push)를 허용함으로써, 감정적인 실수로 인한 프로덕션 장애를 원천 차단하는 **'생체학적 안전장치'**를 구축하고자 기획했습니다.
# Zen-Commit: The Biological Firewall

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git Hook](https://img.shields.io/badge/Tech-Git_Hook-F05032?style=for-the-badge&logo=git&logoColor=white)
![Status](https://img.shields.io/badge/Status-Simulation_Ready-green?style=for-the-badge)

> **"Don't push code when you are angry. Bugs are born from rage."**
> (화난 상태로 코드를 배포하지 마십시오. 버그는 분노에서 태어납니다.)

---

## [필독] 평가자님을 위한 가이드 (For Reviewers)

이 프로젝트는 본래 `Git Hook`과 `웨어러블 API`를 연동하여 작동하지만, **평가 환경에서 쉽게 테스트하실 수 있도록 시뮬레이션 모드**를 제공합니다. 복잡한 설치 없이 아래 명령어로 즉시 시연 가능합니다.

## 3초 만에 실행하기 (Simulation Mode)
터미널(CMD, PowerShell, VS Code)에서 아래 명령어를 입력하세요. visualStudio에서는 위에 ...부분에서 terminal을 찾고 새로운 것에다가 아래의 코드 입력하기

```bash
python demo.py

##  개발 과정에서의 시행착오 

1. Git Hook 권한 문제: 처음에 `install.py`를 만들었는데 실행이 안 돼서 한참 헤맸습니다. 알고 보니 윈도우랑 맥에서 파일 권한(chmod) 주는 방식이 달라서, 파이썬의 `os.chmod`를 사용해서 해결했습니다.

2. 터미널 색상 깨짐:
   집 컴퓨터 CMD에서는 색깔이 잘 나오는데, 친구 컴퓨터 파워셸에서는 이상한 문자가 나왔습니다. 그래서 `colorama` 라이브러리를 써서 호환성 문제를 해결했습니다.
   
3. 무한 루프:
   처음엔 심박수를 계속 체크하느라 프로그램이 안 꺼지는 버그가 있었는데, `sys.exit()`으로 명확하게 종료 시점을 잡아서 해결했습니다.
4. 처음에 생각한 코드는 웨어러블 데이터를 받아서 실시간으로 만드는 프로그램이었는데 git이 설치가 안 되어 있으면 안되서

   그냥 demo.py 만들어서 진행했습니다.
'''





![화면 캡처 2025-12-14 150546](https://github.com/user-attachments/assets/a6296a74-0999-4537-ac5a-79bdadcace23)





![화면 캡처 2025-12-14 150604](https://github.com/user-attachments/assets/d3b38e06-069a-409a-905e-75e94778e1ca)
'''





