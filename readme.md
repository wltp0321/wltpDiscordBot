# WltpDiscordBot

**WLTP 디스코드 커뮤니티** 전용 기능을 지원하는 다기능 Discord 봇입니다.  
타자 연습, 마인크래프트 서버 공지 연동, 유저 편의 기능을 제공합니다.

---

## 🧠 주요 기능

| 기능 이름    | 설명                        |
|----------|---------------------------|
| `타자연습`   | 봇과의 인터랙션을 통해 타자 실력 테스트 가능 |
| `주사위`    | 봇과 원하는 범위로 주사위 대결 가능      |
| `청소`     | 원하는 만큼 메세지 지우기 가능         |
| `ping`   | 봇의 처리 시간 계산 가능            |
| `서버와 연동` | 웹사이트 공지사항 연동              |

---

## 🧑‍💻 개발 환경

| 항목 | 사용 기술                                    |
|------|------------------------------------------|
| 언어 | Python 3.10+                             |
| 라이브러리 | `discord.py`, `aiohttp`, `python-dotenv` |
| 패키징 | `venv`, `requirements.txt`               |
| 테스트 서버 | 지세 커뮤니티                                  |
| 운영체제 | Ubuntu 24.04                             |
| 배포 방식 | python main.py                           |



## 🌐 API 출처

- `https://www.wltp.world/api/important_notices/`
- `https://www.wltp.world/api/normal_notices/`
- `https://www.wltp.world/api/archived_notices/`

JSON 형식의 공지 데이터를 받아와 표시합니다.


## ⚙️ 설치 및 실행

### 1. 환경 설정

```bash
git clone https://github.com/yourusername/WltpDiscordBot.git
cd WltpDiscordBot
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate
pip install -r requirements.txt
