# Java Study Pack Generator 🤖☕

A one-shot agentic workflow built with **Python and Backboard.io** for generating Java study materials automatically.

Give it a Java topic, and the agent creates a complete study pack containing an explanation, Java examples, practice questions, and a quiz.

## 🚀 How It Works

The workflow runs through five AI-powered steps:

1. **Explain** — Explains the Java topic in beginner-friendly language.
2. **Examples** — Generates 3 progressively harder Java code examples.
3. **Practice** — Creates 10 practice questions from beginner to challenging.
4. **Quiz** — Creates a 5-question multiple-choice quiz with an answer key.
5. **Save** — Saves everything into a Markdown study pack.

### Workflow

`Java Topic → Explain → Examples → Practice → Quiz → Markdown File`

## 🛠️ Technologies

* Python
* Backboard API
* `backboard-sdk`
* AI Agent / Agentic Workflow
* Markdown

## 📁 Output

The workflow generates a file such as:

```text
study-pack-java-arrays.md
```

The generated study pack contains:

* Beginner explanation
* Java syntax
* Java code examples
* 10 practice questions
* 5-question quiz
* Answer key

## ⚙️ Setup

Set your Backboard API key as an environment variable.

### Windows PowerShell

```powershell
$env:BACKBOARD_API_KEY="YOUR_API_KEY"
```

Then run:

```bash
python study_pack.py "Java arrays"
```

You can replace `"Java arrays"` with any Java topic.

For example:

```bash
python study_pack.py "Java loops"
```

```bash
python study_pack.py "Java methods"
```

```bash
python study_pack.py "Java inheritance"
```

## 🎯 Challenge

This project was created for **MLH Global Hack Week: Agents — Challenge 5: One-Shot an Agentic Workflow**.

The challenge demonstrates how a detailed prompt can instruct an AI agent to build and execute an entire multi-step workflow without iterative implementation instructions.

## 👤 Author

**Thinali Walpola**

Built as part of the Global Hack Week: Agents challenges.   can you create project for me/code
