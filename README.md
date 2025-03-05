# **T.Prompt – The Ultimate Teleprompter App**  
🚀 **Smooth. Modular. Feature-Rich.**  

[![GitHub](https://img.shields.io/badge/GitHub-T.Prompt-blue?logo=github)](https://github.com/sathya-py/teleprompt)  

**T.Prompt** is a **modern teleprompter** application designed for smooth, distraction-free reading. Whether you're a presenter, content creator, or speaker, T.Prompt provides **seamless scrolling**, customizable layouts, and **Markdown-powered script formatting**.  

---

## **🔗 Repository**
📌 **GitHub**: [sathya-py/teleprompt](https://github.com/sathya-py/teleprompt)  

📌 **Executable Name**: `t.prompt`  

📌 **Developed By**: **Sathya**  

---

## **🔥 Features**
✅ **Live Configuration Updates** – Change settings in `config.json` without restarting.  
✅ **Smooth Scrolling** – Pixel-based movement with fade-in/out transparency effects.  
✅ **Markdown `.prom` File Support** – Use headings, bold, italics, and speaker cues.  
✅ **Draggable Toolbar** – Move the app freely without window decorations.  
✅ **Customizable UI** – Change font size, background color, and text alignment.  
✅ **Mirroring Support** – Flip text horizontally or vertically for teleprompter glass.  
✅ **Hotkeys & Shortcuts** – Control scrolling, font size, and more with keyboard shortcuts.  

---

## **📥 Installation**
### **🔹 Prerequisites**
Make sure you have **Python 3.8+** installed. You also need the following dependencies:

```sh
pip install pygame mistune watchdog
```

### **🔹 Clone & Run**
```sh
git clone https://github.com/sathya-py/teleprompt.git
cd teleprompt
python tprom.py
```

---

## **🖥️ Usage**
### **🚀 Running T.Prompt**
```sh
python tprom.py
```
- Open a `.prom` or `.txt` file to start reading.
- Use **keyboard shortcuts** to control scrolling, font size, and alignment.
- Modify `config.json` for custom settings.

### **🎯 Keyboard Shortcuts**
| Action               | Shortcut  |
|----------------------|----------|
| Scroll Up           | ↑        |
| Scroll Down         | ↓        |
| Increase Font Size  | `+`      |
| Decrease Font Size  | `-`      |
| Toggle Horizontal Mirror | `H` |
| Toggle Vertical Mirror | `V` |
| Change Background Color | `B` |
| Quit | `Q` |

---

## **📜 File Format – `.prom`**
T.Prompt supports `.prom` files, an **enhanced text format** with Markdown-like syntax:

### **🔹 Supported Features**
- **Headings** (`# Heading`)
- **Bold & Italics** (`**bold**`, `*italics*`)
- **Code Blocks** (```python ... ```)
- **Speaker Names** (`[Speaker: John]`)
- **Emphasis & Expressions** (`[sarcasm]`, `[angry]`)

### **🔹 Example**
```md
# Introduction  
[Speaker: Alice]  
Hello, **everyone**!  

[Speaker: Bob]  
This is a *test script* for T.Prompt.  
```

---

## **🛠️ Configuration (`config.json`)**
Modify **T.Prompt** settings on the fly!

```json
{
  "display": { "screen_width": 800, "screen_height": 600, "bg_color": [0, 0, 0] },
  "font": { "font_size": 30, "text_alignment": "left" },
  "scrolling": { "scroll_speed": 1 }
}
```
✅ **No restart required**! Changes apply **instantly**.

---

## **🤝 Contributing**
🔹 **Fork the repo**  
🔹 **Create a feature branch**  
🔹 **Submit a pull request**  

**Issues & suggestions?** [Open a GitHub issue](https://github.com/sathya-py/teleprompt/issues).  

---

## **📜 License**
T.Prompt is released under the **MIT License**.  

---

## **📢 Shoutout**
🎙️ Built with ❤️ by **Sathya**.  

Happy prompting! 🚀
