# ✦ Notevix AI

> Transform any text into structured study material instantly.
> Powered by Groq's LLaMA 3.1 — built for students who study smarter.

## 🔗 Live Application
**[Launch Notevix AI →](https://hassaan-shariq.github.io/notevix/)**

---

## 📸 Preview

![Notevix AI](screenshot.png)

---

## What Is Notevix?

Notevix AI is a full-stack AI-powered study tool that converts 
any text — lecture notes, articles, textbook chapters — into 
10 different learning formats simultaneously.

Instead of reading the same paragraph five times, paste it once 
and get a summary, flashcards, quiz, exam notes, and more in seconds.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📝 Summarize | Concise 3-5 sentence summary |
| 📋 Detailed Summary | Comprehensive structured analysis |
| • Bullet Summary | 8 scannable key bullets |
| 🔑 Key Points | 5 exam-focused concepts explained |
| 🃏 Flashcards | 5 Q&A cards for active recall |
| ❓ Practice Quiz | 4 MCQ questions with answers |
| 💡 ELI5 | Complex ideas explained simply |
| 📚 Exam Notes | Complete revision sheet |
| 📖 Important Terms | Definitions with context |
| ✅ Action Items | Tasks categorized by urgency |
| 💬 FAQs | 5 questions students actually ask |
| 📸 Image Upload | Extract text from photos of notes |

---

## 🏗️ Architecture
Frontend (GitHub Pages) Backend (Railway)
index.html → notevix_api.py
HTML/CSS/JS FastAPI + Python
fetch() calls ← JSON responses
↓
Groq API
LLaMA 3.1 8B Instant


**Separation of concerns:**
- `index.html` handles all UI and user interaction
- `notevix_api.py` handles all AI logic and API calls
- Each layer deployable and updatable independently

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | HTML, CSS, JavaScript | User interface |
| Backend | Python, FastAPI | API server |
| AI Model | Groq / LLaMA 3.1 8B | Text generation |
| Vision | Groq / Qwen 3.6 27B | Image text extraction |
| Deployment (FE) | GitHub Pages | Static hosting |
| Deployment (BE) | Railway | Python server hosting |
| Version Control | Git / GitHub | Code management |

---

## 🚀 Run Locally

### Prerequisites
- Python 3.11+
- Groq API key (free at [console.groq.com](https://console.groq.com))

### Backend Setup

```bash
# Clone repository
git clone https://github.com/hassaan-shariq/notevix.git
cd notevix

# Install dependencies
pip install -r requirements.txt

# Create environment file
echo "GROQ_API_KEY=your_key_here" > .env

# Start server
uvicorn notevix_api:app --reload
```

Backend runs at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

### Frontend Setup

```bash
# Update API URL in index.html
# Change Railway URL to: http://localhost:8000

# Open in browser
open index.html
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/summarize` | Generate concise summary |
| POST | `/detailed-summary` | Generate comprehensive summary |
| POST | `/bullet-summary` | Convert to bullet points |
| POST | `/key-points` | Extract 5 key concepts |
| POST | `/flashcards` | Generate 5 flashcards |
| POST | `/quiz` | Create 4 MCQ questions |
| POST | `/eli5` | Simplify explanation |
| POST | `/exam-notes` | Create revision notes |
| POST | `/important-terms` | Extract terminology |
| POST | `/action-items` | Extract tasks by priority |
| POST | `/faq` | Generate FAQ |
| POST | `/extract-from-image` | OCR from uploaded image |

**Request format (all text endpoints):**
```json
{ "text": "Your study material here" }
```

**Response format:**
```json
{ "summary": "AI generated content here" }
```

---

## 🗂️ Project Structure

notevix/
├── notevix_api.py # FastAPI backend — all AI logic
├── index.html # Frontend — UI and API calls
├── requirements.txt # Python dependencies
├── Procfile # Railway deployment config
├── runtime.txt # Python version for Railway
├── .env # API keys (never committed)
├── .gitignore # Excludes sensitive files
└── README.md # This file

---

## 🔒 Security

- API keys stored in environment variables only
- `.env` file excluded from version control
- CORS configured for cross-origin requests
- No user data stored or logged

---

## 🗺️ Roadmap

- [ ] PDF and DOCX file upload
- [ ] User accounts and history
- [ ] Download results as PDF
- [ ] Multiple language support
- [ ] Chrome extension

---

## 👨‍💻 About

Built by **Hassaan Shariq** — a self-taught AI Engineer from 
Karachi, Pakistan, building AI-powered products independently.

- GitHub: [hassaan-shariq](https://github.com/hassaan-shariq)
- Live: [Neon Circuit Story Engine](https://neon-circuit-story-engine-6zpjyefgkpkxbdkwn48s2d.streamlit.app/)

---

*Notevix AI — Built from scratch. Deployed independently. 
No frameworks used beyond what the problem required.*
