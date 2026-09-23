# MIKE-PROMPTS-BP

**English** | [Tiếng Việt](README.vi.md)

> ⚡ Red Team / Penetration Testing toolkit for AI & LLM security — **41 Attack Types · 13 Payload Encodings · 21 AI Target Profiles · 7 Luxury Themes · OWASP LLM Top 10 2026 · Live API Test · Multi-turn Attack · Effectiveness Stats**

<p align="center">
  <img src="docs/screenshots/03-logo.jpg" width="200" alt="MIKE-PROMPTS-BP Logo">
</p>

![Screenshot 1](docs/screenshots/screenshot-1.png)

![Screenshot 2](docs/screenshots/screenshot-2.png)

![Screenshot 3](docs/screenshots/screenshot-3.png)

![Screenshot 4](docs/screenshots/screenshot-4.png)

## ⚠️ Disclaimer

**This tool is intended for authorized security testing and AI safety research only.** Unauthorized use against systems you do not own or have explicit permission to test is illegal. The author assumes no liability for misuse.

## ✨ Features

### 🎯 AI Target Intelligence (21 Profiles)
Detailed defense profiles for **ChatGPT, Claude, Gemini, Grok, DeepSeek, Cursor, Devin, Windsurf, Codex, Perplexity, Kimi, Replit, Lovable, v0, Manus, Llama, Mistral, Qwen, Command R+, Phi, Copilot** — including versions, defenses, weaknesses, recommended attacks, and tactical notes.

### ⚔️ Attack Categories (7 × 41 Types)
| Category | Types | Description |
|----------|-------|-------------|
| **OVERRIDE** | Direct, Jailbreak, DevMode, Skeleton Key, System Override v2 | Direct system prompt override |
| **STEALTH** | Indirect, Payload, Token Smuggle, Multimodal Inject, RAG Poison, Tool-Call Smuggle | Hide payload in trusted data |
| **EVASION** | Multilingual, Few-Shot, Virtualization, Context, Flip Attack, Low-Resource Lang, Poetic Format, Emoji Cipher | Bypass filters |
| **HYBRID** | WormGPT, Persona Layer, Prompt Chain, Crescendo, TAP, GOAT, Self-Replicate | Multi-step / multi-layer |
| **RECON** | System Leak, Hierarchy Confusion, Hidden Context, Training Data Extract, Package Hallucination | System intelligence gathering |
| **AGENTIC** | Confused Deputy, Permission Escalation, MCP Tool Abuse, Indirect via RAG, Execution Loop, Memory Poison | AI agent exploitation |
| **SAFETY** | Do Not Answer, Real Toxicity, XSS via Output, SQL via Output | Safety alignment benchmarks |

### 🏷️ OWASP LLM Top 10 2026 Compliance
Every attack type is mapped to the OWASP LLM Top 10 (2026 Edition) — from LLM01 (Prompt Injection) to LLM10 (Improper Output Handling). OWASP badges are displayed in the output for compliance tracking.

### 🔐 Payload Encoding (13 Types)
`Base64` · `Obfuscate Hex` · `Unicode Escape` · `ROT13` · `Homoglyph` · `Stealth Embed (Zero-Width)` · `Token Split` · `Markdown Inject` · `Morse Code` · `Braille Unicode` · `Pig Latin` · `Reverse Text` · `Leetspeak` — combine multiple encodings for maximum evasion.

### 📊 Export (4 Formats)
`TXT` · `JSON (structured report)` · `HTML (styled Obsidian & Gold report)` · `CSV` — professional reporting for security audits.

### 🎨 7 Luxury Themes
`🌑 Obsidian & Gold` · `💎 Midnight Sapphire` · `🌹 Eclipse Rose` · `🍀 Emerald Noir` · `❄️ Arctic Silver` · `🖤 Dark Pro` · `☀️ Light Mode`

### 🌐 Bilingual UI
Full **Vietnamese / English** interface with one-click language switching.

### 🛡️ Stealth Steganography
Hide entire attack payloads inside innocent-looking text using zero-width Unicode characters — completely invisible to the naked eye.

### 💡 Smart Recommendations
Select an AI target → get instant recommendations for optimal attack types and encodings based on real-world testing data.

### 🧪 Live API Test (v8.0)
Send generated payloads directly to AI APIs (OpenAI, Anthropic, Google, OpenRouter) — test effectiveness in real-time with automatic **BYPASSED / BLOCKED / UNCERTAIN** scoring.

### 🔄 Multi-turn Attack Simulation (v8.0)
Automate multi-step attack strategies: **Escalation**, **Persistence**, and **Context Poisoning** — simulate real-world adversarial conversations.

### 📈 Effectiveness Stats Dashboard (v8.0)
Track bypass rates, best-performing attacks and encodings per AI target — data-driven red teaming.

### 🔄 Batch Processing (v8.0)
Import targets from CSV/JSON, generate payloads in bulk, and export results — streamline large-scale testing.

### 🎨 Custom Attack Templates (v8.0)
Create, save, and manage your own attack templates (CRUD JSON) — extend the arsenal with domain-specific techniques.

## 📦 Download

Download `MikePromptsBP.exe` from the [**Releases**](https://github.com/mikeTran99/MIKE-PROMPTS-BP/releases) page.

> **Portable** — No installation needed. Just download and run on Windows.

## 🚀 Quick Start

1. **Select AI Target** — Choose from 21 AI profiles (or leave on Auto)
2. **Enter Target Role** — The identity to force on the AI
3. **Enter System Override** — Override command (optional)
4. **Select Attack Type** — Pick from 7 category tabs × 41 types
5. **Select Encoding** — Optional, combine multiple for layered evasion
6. **Click ⚡ GENERATE PAYLOAD** — Get your crafted prompt
7. **Copy or Export** — TXT, JSON, or HTML Report

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+C` | Copy payload to clipboard |
| `Ctrl+Shift+S` | Export payload as .txt file |

## 🛠️ Tech Stack

- **Python 3.14** — Core runtime
- **CustomTkinter** — Modern dark-themed GUI framework
- **Pillow** — Image processing for app icons
- **PyInstaller** — Single-file `.exe` packaging

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**mikeTran99** — [GitHub](https://github.com/mikeTran99)

---

<p align="center">
  <b>MIKE-PROMPTS-BP v8.0</b> — Luxury Edition<br>
  <i>For authorized security testing only.</i>
</p>
