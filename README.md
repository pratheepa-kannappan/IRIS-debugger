# 🐛 IRIS AI — Python Visual Debugger 

> Understand Python errors instantly. Paste your traceback, get a clear explanation, root causes, and a working fix — powered by LLM inference via Groq.

---

## 📸 Preview

```
Traceback (most recent call last):
  File "app.py", line 5, in <module>
    print(user['email'])
KeyError: 'email'
```

↓ IRIS AI returns:

| Section | Output |
|---|---|
| 📘 Meaning | The key `'email'` does not exist in the dictionary |
| ⚠️ Causes | Missing key, typo in key name, unexpected data shape |
| 🛠 Fix | Check key existence with `.get()` or `in` before access |
| 💡 Example | Corrected Python code snippet |

---

## 🚀 Features

- Paste any Python error traceback and get an instant structured analysis
- Four-panel output: Meaning, Causes, Fix, and Code Example
- Sub-2-second response times powered by Groq's LPU hardware
- Clean, minimal light UI built with Streamlit
- Response time displayed for every request

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | Streamlit |
| LLM Provider | Groq API |
| Model | LLaMA 3 / Mixtral (via Groq) |
| Language | Python 3.9+ |
| Output Format | Structured JSON parsed from LLM response |

### Why Groq?

Groq runs open-source LLMs on custom **LPU (Language Processing Unit)** hardware, delivering response times of **1–3 seconds** — significantly faster than GPU-based providers. This makes it ideal for developer tools where speed matters.

---

## 📁 Project Structure

```
iris-ai/
├── app.py                  # Main Streamlit application
├── utils/
│   ├── llm_client.py       # Groq API wrapper (LLMClient)
│   └── prompt_builder.py   # Prompt engineering logic
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/iris-ai.git
cd iris-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Groq API key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at [console.groq.com](https://console.groq.com)

### 5. Run the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📦 Requirements

```txt
streamlit
groq
python-dotenv
```

Or install directly:

```bash
pip install streamlit groq python-dotenv
```

---

## 🔧 How It Works

The app follows a simple, single-turn LLM pipeline:

```
User pastes error traceback
        ↓
build_prompt()  →  formats error into a structured prompt
        ↓
LLMClient.get_response()  →  single HTTP call to Groq API
        ↓
Groq runs LLaMA/Mixtral on LPU  →  returns structured JSON
        ↓
json.loads()  →  parses meaning, causes, fix, example
        ↓
Streamlit renders the 4-panel result card
```

### Prompt Strategy

The `build_prompt()` function instructs the model to return a strict JSON object:

```json
{
  "meaning": "Clear explanation of the error",
  "causes": ["Cause 1", "Cause 2", "Cause 3"],
  "fix": "Concrete fix recommendation",
  "example": "# Corrected Python code"
}
```

This structured output approach ensures consistent, parseable responses every time.

---

## 💡 Example Errors to Try

**NameError**
```
NameError: name 'mesage' is not defined
```

**TypeError**
```
TypeError: can only concatenate str (not "int") to str
```

**KeyError**
```
KeyError: 'email'
```

**Dependency conflict**
```
ERROR: pip's dependency resolver conflict — numpy 2.4.4 incompatible with numba, opencv-python, tensorflow-intel
```

---

## 🗺 Roadmap

- [ ] Code execution sandbox — run buggy code and capture live errors
- [ ] Support for JavaScript, Java, and Rust error analysis if you change the prompt_builder
- [ ] Agentic mode — model autonomously searches docs and retries fixes

---


## 👨‍💻 Author

Built with ❤️ using Streamlit + Groq API.  
Star ⭐ the repo if you found it helpful!
