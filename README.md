# Hands-On AI — Running and Building with Local LLMs

## Overview

AI is no longer limited to research teams — it's becoming an essential tool for every developer. This **hands-on session** introduces practical ways to:

- Run local LLMs efficiently
- Compare model responses
- Integrate AI into everyday applications

---

## What You’ll Learn

By the end of this session, you will be able to:

- Set up and run local LLMs using [Ollama](https://ollama.ai)
- Compare model behavior to assess capabilities and trade-offs
- Write scripts for summarization, theming, and lightweight AI-driven experiences
- Explore agentic and automation scenarios without prior AI expertise

---

## Prerequisites

To fully participate, please install the following software **before the session**:

| Software     | Download Link |
|--------------|----------------|
| Ollama       | [Download](https://ollama.ai/download) |
| Python 3.10+ | [Windows](https://www.python.org/downloads/windows/) &#124; [Mac](https://www.python.org/downloads/mac-osx/) |

> **Note:** Install Python as an administrator and ensure it’s added to your system PATH.

---

## Hands-On Exercises

### Exercise 1: Running Your First Local LLM

**Objective:** Install and interact with a lightweight local model via the command line.

```sh
ollama run llama3.2:1b
```

Ask a few question such as:  
`Is a hotdog a sandwich?`

> Type `/bye` to exit the session.

---

### Exercise 2: Build a Simple Web-Based Chatbot

**Objective:** Create a basic chatbot using HTML and JavaScript, connected to Ollama's API.

Steps:

1. Clone the sample project:  
   ```sh
   git clone https://github.com/AITrekker/ollama.git
   ```

2. Start a local web server:  
   - Windows: `python -m http.server 8000`  
   - Mac: `python3 -m http.server 8000`

3. Open your browser to:  
   [http://localhost:8000/single-llm.html](http://localhost:8000/single-llm.html)

4. Ask a question and watch the LLM return a response

---

### Exercise 3: Compare Multiple LLMs

**Objective:** Build a chatbot that displays responses from multiple models side by side.

#### Considerations by Platform:

- **Windows:** Limited RAM; prefer models between 1B–3B.
- **Mac (M1/M2/M3/M4):** Unified memory allows for running larger models (7B–14B), ideally with 16GB+ RAM.

#### Suggested Models

| Model | Run Command |
|-------|-------------|
| llama3.2:1b | `ollama run llama3.2:1b` |
| phi3:3.8b   | `ollama run phi3:3.8b` |
| gemma2:2b   | `ollama run gemma2:2b` |
| deepseek-r1:1.5b | `ollama run deepseek-r1:1.5b` |

Larger models (Mac only):

| Model | Run Command |
|-------|-------------|
| llama3.2:latest | `ollama run llama3.2:latest` |
| phi4:14b        | `ollama run phi4:14b` |
| gemma2:9b       | `ollama run gemma2:9b` |
| deepseek-r1:7b  | `ollama run deepseek-r1:7b` |

Next steps:

- Download 4 models from above
- Launch the multi-model chatbot: [http://localhost:8000/multiple-llm.html](http://localhost:8000/multiple-llm.html)

---

### Exercise 4: Thematic Analysis & Summarization

**Objective:** Use a local LLM to summarize and extract themes from a CEO AMA dataset.

Steps:

1. Run the summarization script:  
   - Windows: `python summarize.py sample.csv`  
   - Mac: `python3 summarize.py sample.csv`

2. Open `output.csv` to view themes and summaries.

3. To experiment, modify `LLM_NAME` in the script and rerun with other downloaded models.

4. Try a few different prompts and compare the output of the different LLMs

---

## Additional Resources

- [Explore Ollama Models](https://ollama.com/search)  
- [Python Tutorial](https://docs.python.org/3/tutorial/)

---

## Optional: Cleanup

To remove all downloaded models:

- **Windows:**
  ```powershell
  ollama list | ForEach-Object { ollama rm $_.Split(" ")[0] }
  ```

- **Mac:**
  ```bash
  ollama list | awk '{print $1}' | xargs -I {} ollama rm {}
  ```

---

## Contact

For questions or support:  
- Submit an issue on GitHub  
- Connect on [LinkedIn](https://www.linkedin.com/in/agupta11/)