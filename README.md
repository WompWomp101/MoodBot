# 🤖 MoodBot

MoodBot is a fun AI chatbot built using **Python, Streamlit, LangChain, and Groq APIs**.
It allows users to interact with different AI personalities with dynamic behavior switching and real-time conversations.

## ✨ Features

* 😡 RageBot — angry and rude responses
* 🤣 JokeBot — replies with jokes and humor
* 😢 SadBot — melancholic and emotional responses
* 💬 Interactive chat UI using Streamlit
* 🧠 Conversation memory using Streamlit session state
* ⚡ Fast responses powered by Groq LLMs
* 🔄 Dynamic personality switching

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* dotenv

---

## 📂 Project Structure

```bash
mood-chatbot/
│
├── moodbot.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd mood-chatbot
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add environment variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Run the application

```bash
streamlit run moodbot.py
```

---

## 📸 Preview

MoodBot provides a clean chat interface where users can select different AI personalities and have interactive conversations in real time.

---

## 🎯 Future Improvements

* Voice input/output
* Chat history export
* More AI personalities
* Dark mode UI
* RAG-based knowledge integration
* Multi-agent support

---

## 👨‍💻 Author

Built by Aadya using GenAI + Streamlit 🚀
