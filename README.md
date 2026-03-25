<div align="center">

# 🗂️ Smart File Organizer

### *Your downloads folder deserves better.*

**An AI-powered file automation tool that sorts, classifies, and renames your files — instantly.**

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![AI Powered](https://img.shields.io/badge/AI-OpenAI%20GPT-412991?style=for-the-badge&logo=openai&logoColor=white)
![Automation](https://img.shields.io/badge/Type-Automation%20Tool-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

<br/>

> 💡 *Combining rule-based logic and AI intelligence to bring order to digital chaos.*

</div>

---

## ⚡ The Problem → The Solution

| ❌ The Problem | ✅ The Solution |
|---|---|
| Downloads folder is a chaotic mess | Automatically sorts files into clean category folders |
| Hours wasted manually organizing files | One command sorts everything in seconds |
| Hard to find files buried in clutter | Structured folders make every file instantly locatable |
| Cryptic filenames like `doc_final_v3_REAL.pdf` | AI suggests meaningful, descriptive file names |
| Unknown file types sit unhandled | AI classifies unknown extensions and places them correctly |

---

## 🔥 Features

<table>
<tr>
<td width="50%">

**📂 Automatic File Sorting**
Rules-based engine instantly routes known file types into the right folders — zero configuration needed.

</td>
<td width="50%">

**🤖 AI-Based Classification**
Unknown files are sent to GPT, which predicts the best category based on content and context.

</td>
</tr>
<tr>
<td width="50%">

**🏷️ Smart File Renaming**
AI suggests clean, descriptive filenames that actually tell you what's inside.

</td>
<td width="50%">

**⚡ Fast Folder Cleanup**
Scans and organizes entire directories in milliseconds — even with hundreds of files.

</td>
</tr>
<tr>
<td width="50%">

**🧠 Hybrid Intelligence Engine**
Combines instant rule-based sorting with AI fallback for complete coverage.

</td>
<td width="50%">

**📁 Unknown File Handling**
No file gets left behind. Every extension gets classified, moved, and renamed.

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```
📁 Input Folder
        │
        ▼
┌──────────────────┐
│   File Scanner   │  ← Reads all files in target directory
└──────────────────┘
        │
        ▼
┌──────────────────────┐
│  Extension Checker   │  ← Matches against known type registry
└──────────────────────┘
        │
   ┌────┴────┐
   │         │
   ▼         ▼
Known?      Unknown?
   │         │
   ▼         ▼
Move to   ┌──────────────────────────┐
Category  │   AI Classification      │
Folder    │   Engine (OpenAI GPT)    │
          └──────────────────────────┘
                      │
                      ▼
          ┌──────────────────────────┐
          │  Category + Better Name  │
          └──────────────────────────┘
                      │
                      ▼
              Move & Rename File ✅
```

---

## 🔄 How It Works

```
Step 1 → User provides a folder path as input
Step 2 → System scans all files in that directory
Step 3 → Known extensions are instantly sorted (Images, Docs, Videos, etc.)
Step 4 → Unrecognized files are packaged and sent to the AI engine
Step 5 → GPT predicts the best category and a cleaner filename
Step 6 → All files land in organized folders with meaningful names
```

That's it. **One command. Zero clutter.**

---

## 🛠️ Tech Stack

| Tool | Role |
|---|---|
| `Python 3.10+` | Core language — clean, fast, and widely supported |
| `os` | Directory traversal and file path management |
| `shutil` | Safe file moving and renaming operations |
| `python-dotenv` | Secure loading of API keys from `.env` |
| `OpenAI API` | GPT-powered classification and filename suggestions |

---

## 🧠 Core Intelligence — Hybrid Logic

This project uses a **two-layer intelligence system** designed for speed and coverage.

### Layer 1 — Rule-Based Engine (Fast Path)

- Instantly maps common extensions to categories
- Zero API calls, zero latency
- Covers: Images, Documents, Videos, Audio, Archives, Code, and more
- Handles ~90% of real-world files with no external dependency

### Layer 2 — AI Classification Engine (Smart Path)

- Activated only for unknown or ambiguous file types
- Sends file metadata to OpenAI GPT with a structured prompt
- Returns: *predicted category* + *suggested clean filename*
- Handles edge cases that rigid rules can't cover

> **Result:** Fast for common files. Smart for everything else.

---

## 📊 Why This Project Matters

```
✦  Students       →  Stop drowning in assignment downloads
✦  Designers      →  Auto-sort assets, PSDs, exports, and references
✦  Developers     →  Clean up project folders and code archives
✦  Professionals  →  Reclaim hours lost to manual file management
✦  Everyone       →  Less clutter. More focus. Better productivity.
```

Digital clutter is a silent productivity killer. Smart File Organizer eliminates it at the source — automatically.

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/RTGamerz009/smart-file-organizer.git
cd smart-file-organizer

# Install dependencies
pip install -r requirements.txt

# Set up your OpenAI API key
cp .env.example .env
# → Add your OPENAI_API_KEY to .env

# Run the organizer
python main.py --path "/path/to/your/folder"
```

---

## 🔮 Future Scope

| Upgrade | Description |
|---|---|
| 🖥️ **GUI Version** | Drag-and-drop desktop interface for non-technical users |
| 👁️ **File Previews** | Thumbnail previews before committing to organization |
| 🔁 **Duplicate Detection** | Find and flag identical files across directories |
| 🔍 **Smart Search** | Natural language file search powered by embeddings |
| ⏰ **Auto-Scheduling** | Run on a schedule — folders stay clean automatically |
| 🧠 **Advanced AI Models** | Support for local models (Ollama, LLaMA) as OpenAI alternatives |
| ☁️ **Cloud Sync** | Organize files across Google Drive, Dropbox, OneDrive |

---

## 📌 Get Involved

<div align="center">

**If this project saved you even 5 minutes — give it a star. It means everything.**

[![Star this repo](https://img.shields.io/badge/⭐%20Star%20This%20Repo-yellow?style=for-the-badge)](https://github.com/your-username/smart-file-organizer)
[![Fork it](https://img.shields.io/badge/🍴%20Fork%20It-blue?style=for-the-badge)](https://github.com/your-username/smart-file-organizer/fork)
[![Open Issues](https://img.shields.io/badge/🐛%20Report%20a%20Bug-red?style=for-the-badge)](https://github.com/your-username/smart-file-organizer/issues)
[![Contribute](https://img.shields.io/badge/🚀%20Contribute-brightgreen?style=for-the-badge)](https://github.com/your-username/smart-file-organizer/pulls)

</div>

---

<div align="center">

*Built with Python, OpenAI, and a deep hatred of messy download folders.*

</div>

---

## 💡 Appendix

### A. Banner Image Suggestion

Use a **dark-themed, minimal design** featuring:
- A folder icon splitting open into organized sub-folders (Documents, Images, Videos, etc.)
- A subtle AI/neural network overlay on one side of the folder
- Typography: `Smart File Organizer` in a clean sans-serif (Inter or Geist)
- Color palette: Deep navy background `#0D1117` with electric blue `#58A6FF` and white accents

Tools: Figma, Canva, or Midjourney prompt — *"minimalist dark-mode tech banner, folder organization, AI classification, clean UI concept art"*

---

### B. Resume / Portfolio Positioning

> *"Built an AI-powered file automation tool that combines a rule-based classification engine with OpenAI GPT to automatically sort, rename, and organize files — reducing manual effort and improving digital productivity."*

Highlight: **Python · OpenAI API · Automation · AI Integration · File System Engineering**

---

### C. Suggested Upgrades to Strengthen the Project

| # | Upgrade | Impact |
|---|---|---|
| 1 | **Add a web UI with Flask or FastAPI** | Makes it accessible without CLI knowledge — dramatically increases perceived value |
| 2 | **Persist organization history to SQLite** | Enables undo, audit trails, and analytics on your own files |
| 3 | **Batch mode + progress bar with `tqdm`** | Transforms it from a script into a polished developer tool |
