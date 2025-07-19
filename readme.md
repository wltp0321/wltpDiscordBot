# 🪐 WltpDiscordBot

**WLTP 디스코드 커뮤니티** 전용 다기능 Discord 봇입니다.  
타자 연습, 서버 공지 연동, 커뮤니티 기능을 지원합니다.

> 🌍 [English version available below](#-wltpdiscordbot-en)

---

## 🧠 주요 기능 (Features)

| 기능 이름         | 설명                                         |
|------------------|--------------------------------------------|
| `타자연습`        | 봇과의 인터랙션을 통해 타자 실력 테스트 가능                  |
| `주사위`          | 사용자 간 주사위 대결 가능                                 |
| `청소`           | 명령어를 통해 지정한 개수만큼 메시지 삭제 가능                     |
| `핑` (`ping`)     | 봇의 반응 속도 측정                                   |
| `공지 연동`        | 웹사이트 공지사항 API와 실시간 연동                           |

---

## 🧑‍💻 개발 환경 (Dev Environment)

| 항목         | 내용                                                                 |
|--------------|----------------------------------------------------------------------|
| 언어         | Python 3.10+                                                         |
| 라이브러리   | `discord.py`, `aiohttp`, `python-dotenv`                             |
| 패키징       | `venv`, `requirements.txt`                                           |
| 서버 환경    | Ubuntu 24.04                                                         |
| 배포 방식    | `python main.py` 직접 실행                                             |

---

## 🌐 API 출처 (API Sources)

- [`/api/important_notices/`](https://www.wltp.world/api/important_notices/)
- [`/api/normal_notices/`](https://www.wltp.world/api/normal_notices/)
- [`/api/archived_notices/`](https://www.wltp.world/api/archived_notices/)

> JSON 형식의 공지 데이터를 디스코드에 출력합니다.

---

## ⚙️ 설치 및 실행 (Install & Run)

### 1. 저장소 클론 및 환경 설정

```bash
git clone https://github.com/yourusername/WltpDiscordBot.git
cd WltpDiscordBot
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate
pip install -r requirements.txt
