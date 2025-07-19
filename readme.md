# WltpDiscordBot

🇰🇷 **WLTP 디스코드 커뮤니티** 전용 기능을 지원하는 다기능 Discord 봇입니다.  
🇺🇸 A multi-functional Discord bot made for the **WLTP Discord community**, offering typing practice, server notice sync, and convenience features.

---

## 🧠 주요 기능 / Features

| 기능 이름 / Feature | 설명 (한국어) | Description (English) |
|---------------------|----------------|------------------------|
| `타자연습` (Typing Practice) | 타자 실력 테스트 가능 | Test your typing skill via interaction |
| `주사위` (Dice Game) | 봇과 주사위 대결 가능 | Play dice games with the bot |
| `청소` (Clean Messages) | 메시지 일괄 삭제 | Bulk delete messages |
| `ping` | 봇의 응답 시간 표시 | Shows bot response time |
| `서버와 연동` (Website Notices) | 마인크래프트 서버 공지 연동 | Sync server notices from the website |

---

## 🧑‍💻 개발 환경 / Development Environment

| 항목 / Item | 기술 / Tech |
|-------------|-------------|
| 언어 / Language | Python 3.10+ |
| 라이브러리 / Libraries | `discord.py`, `aiohttp`, `python-dotenv` |
| 패키징 / Packaging | `venv`, `requirements.txt` |
| 테스트 서버 / Test Server | 지세 커뮤니티 (Jise Community) |
| 운영체제 / OS | Ubuntu 24.04 |
| 실행 방식 / Run Method | `python main.py` |

---

## 🌐 API 출처 / API Source

- `https://www.wltp.world/api/important_notices/`
- `https://www.wltp.world/api/normal_notices/`
- `https://www.wltp.world/api/archived_notices/`

🇰🇷 JSON 형식의 공지 데이터를 받아와 표시합니다.  
🇺🇸 Fetches and displays notices in JSON format.

---

## ⚙️ 설치 및 실행 / Setup & Run

### 1. 환경 설정 / Environment Setup

```bash
git clone https://github.com/yourusername/WltpDiscordBot.git
cd WltpDiscordBot
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
