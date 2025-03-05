# 🚀 CAP fhL 2025: Hands-On AI – Running and Building with Local LLMs  

## 🔹 Overview  
AI isn’t just for research teams—it’s for every developer. This **hands-on session** will help **developers, managers, and product owners** learn how to:  

✅ **Run multiple local LLMs**  
✅ **Compare AI model responses**  
✅ **Integrate AI into real-world applications**  

---

## 🎯 What You’ll Learn  

✔️ **Set up & run local LLMs** using [Ollama](https://ollama.ai)  
✔️ **Compare model responses** to understand their strengths & weaknesses  
✔️ **Write scripts** for theming, summarization, & AI-aware features  
✔️ **Explore agentic scenarios** – no prior AI expertise required!  

---

## 🛠️ Prerequisites  

To **get the most out of this session**, please install the following **beforehand**:  

### **Required Software**  

| Software | Download Link |
|----------|--------------|
| **Ollama** | [Download](https://ollama.ai/download) |
| **Python 3.10+** | [Windows](https://www.python.org/downloads/windows/) \| [Mac](https://www.python.org/downloads/mac-osx/) |

⚡ **Pro Tip:** Install as **admin** and update `PATH`!  

<img src="https://github.com/user-attachments/assets/a44cefb7-dfde-43ff-af6b-03dd425e12a9" width="400" />

---


# 🏗️ Hands-On Exercises  

## 🏁 **Exercise 1: Running Your First Local LLM**  

🔹 **Goal:** Download and run your first model, and interact with an LLM using the command line.  

### **1️⃣ Pull & Run Your First Model**  
```sh
ollama run llama3.2:1b
```

### **2️⃣ Interact with the Model in the Terminal**  
Ask a question, such as "Is hotdog a sandwich?"

Be creative and ask it questions or chat with it.

You now have the powers of a scaled down chatgpt running on your local computer.

💡 **Tip:** Input `/bye` to exit the chat.

---

## 💬 **Exercise 2: Build a Simple Web-Based Chatbot**  

🔹 **Goal:** Create a basic **web interface** to interact with an LLM.  

### 📌 What You’ll Do:  
✅ Set up a **simple HTML & JavaScript** front-end  
✅ Connect your chatbot to **Ollama's API**  

### **1️⃣ Create a Working Directory**  
```sh
mkdir llm
cd llm
```

### **2️⃣ Download the Chatbot Web Page**  
Download **[single-llm.html](https://github.com/whizamit/llm/blob/main/single-llm.html)** into the `llm` folder.  

### **3️⃣ Start a Temporary Web Server**  
| OS | Command |
|----|---------|
| **Windows** | `python -m http.server 8000` |
| **Mac** | `python3 -m http.server 8000` |

### **4️⃣ Open in Your Browser**  
Go to **http://localhost:8000/single-llm.html** in your web browser.  

---

## 🔄 **Exercise 3: Compare Multiple LLMs in a Chatbot**  

🔹 **Goal:** Build a **more advanced chatbot** that compares multiple LLM responses side by side.  

📌 **What You’ll Do:**  
✅ Query multiple LLMs **at once**  
✅ Display responses **side by side**  
✅ Analyze **differences in model outputs**  

---

### **1️⃣ Understanding LLM Sizes & System Limitations**  

💡 **Not all LLMs are the same size!** Some require more memory and computing power, affecting performance.  

🔹 **Windows Users:**  
- Windows laptops **lack unified memory** (which Apple Silicon uses to share RAM between CPU & GPU).  
- Running **larger models (7B-14B)** can be **slow or impossible** due to memory limits.  
- **Solution:** Use **smaller models (1B-3B)** that require less RAM.  

🔹 **Mac Users:**  
- Macs with **M1/M2/M3 chips** can run **larger models** due to **unified memory**.  
- If you have a Mac with **16GB+ RAM**, you can try **larger models (7B-14B)** for better results.  

---

### 🧠 **Choosing the Right Model**  

#### 🔹 **Smaller, Lightweight Models (Best for Windows & Low-Memory Macs) -- Recommended**  

| Model ID | Run Command |
|----------|------------|
| `llama3.2:1b` | `ollama run llama3.2:1b` |
| `phi3` | `ollama run phi3:3.8b` |
| `gemma2:2b` | `ollama run gemma2:2b` |
| `deepseek-r1:1.5b` | `ollama run deepseek-r1:1.5b` |

#### 🔹 **Larger, More Powerful Models (Best for Macs with 16GB+ RAM)**  

| Model ID | Run Command |
|----------|------------|
| `llama3.2:latest` | `ollama run llama3.2:latest` |
| `phi4` | `ollama run phi4:14b` |
| `gemma2:9b` | `ollama run gemma2:9b` |
| `deepseek-r1` | `ollama run deepseek-r1:7b` |

---

### **2️⃣ Download the Multiple Chatbot Web Page**  
Download **[multiple-llm.html](https://github.com/whizamit/llm/blob/main/multiple-llm.html)** into the `llm` folder.  

### **3️⃣ Open in Your Browser**  
Go to **http://localhost:8000/multiple-llm.html**  

💡 **Tip:** Compare different models on various topics!  

---

## 📊 **Exercise 4: AI-Powered Thematic Analysis & Summarization**  

🔹 **Goal:** Use Python to **analyze themes** and **summarize discussions** from a recent AMA with **Satya Nadella**.  

📌 **What You’ll Do:**  
✅ Use AI to **extract key topics**  
✅ Use AI to **summarize**  

### **1️⃣ Download the Multiple Chatbot Web Page**  
Download the following into the `llm` folder.  
[summarize.py](https://github.com/whizamit/llm/blob/main/summarize.py)
| 
[sample.csv](https://github.com/whizamit/llm/blob/main/sample.csv)

### **2️⃣ Run the script**  

(Windows) `python summarize.py sample.csv`
(Mac) `python3 summarize.py sample.csv`

### **3️⃣ View the output**  
Open the file 'output.csv' to see the summary and theme of each sample question.

---
---

## 📚 Resources  

📖 [Ollama Models](https://ollama.com/search)  
🐍 [Python Basics for AI](https://docs.python.org/3/tutorial/)  
🤖 [Introduction to LLMs by Andrej Karpathy](https://www.youtube.com/playlist?list=PLAqhIrjkxbuW9U8-vZ_s_cjKPT_FqRStI) 


### ✨ Cleanup
Remove all local llms 

(Windows) `ollama list | ForEach-Object { ollama rm $_.Split(" ")[0] }`

(Mac) `ollama list | awk '{print $1}' | xargs -I {} ollama rm {}`
## 📩 Contact  

💡 **Questions?** Open an issue in the GitHub repository or reach out via **Teams** @amigupta, @sasitara


