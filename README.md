# CAP fhL 2025: Hands-On AI – Running and Building with Local LLMs

## Overview
AI isn’t just for research teams—it’s for every developer. This hands-on session is designed to help developers, managers, and product owners learn how to **run multiple local LLMs, compare responses, and integrate AI into real-world applications.**

## What You’ll Learn
- How to set up and run **local LLMs** using [Ollama](https://ollama.ai)
- How to compare model responses to understand their strengths and weaknesses
- How to write scripts for **theming, summarization, and AI-aware features**
- How to start incorporating **agentic scenarios** in your products—no prior AI expertise required

## Prerequisites
To get the most out of this session, please ensure you have the following installed on your laptop:

### **Required Software**

1. **Ollama** (Required) | [Download](https://ollama.ai/download)
2. **Python 3.10+** (Required) | [Windows download](https://www.python.org/downloads/windows/) | [Mac download](https://www.python.org/downloads/mac-osx/)

Install as admin and update PATH

<img src="https://github.com/user-attachments/assets/a44cefb7-dfde-43ff-af6b-03dd425e12a9" width="400" />



### **Clone the Session Repository**
Run the following command to clone the repository containing example scripts:
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/ollama-learning-session.git
cd ollama-learning-session
```

## Getting Started
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Pull Ollama models:
   ```sh
   ollama run phi
   ollama run llama3.2:1b
   ollama run deepseek-r1:1.5b
   ```
3. Create a temprary folder:
   ```sh
   mkdir temp
   ```
5. Run temporary local web server
   ```sh
   cd temp
   python -m http.server 8000
   ```
3. Run the example summarization script:
   ```sh
   python summarize.py --input "sample_text.txt"
   ```

## Ollama Usage Guide
Ollama provides a CLI for managing and running models. Here are some key commands:

| Command               | Description |
|-----------------------|-------------|
| `ollama help`        | Show help menu |
| `ollama ps`          | List running models |
| `ollama list`        | List available models |
| `ollama run <model>` | Run a model |
| `ollama stop <model>` | Stop a running model |
| `ollama rm <model>`  | Remove a model |
| `/bye` | Exit the chat |
## Resources



- [Ollama Documentation](https://ollama.ai/docs)
- [Python Basics for AI](https://docs.python.org/3/tutorial/)
- [Introduction to Agentic AI](https://example.com/agentic-ai-guide) *(Replace with actual link)*

## Contact
If you have any issues or questions, feel free to open an issue in the GitHub repository or reach out via Teams.

📢 **Bring your laptop, follow along, and start building with AI!**

