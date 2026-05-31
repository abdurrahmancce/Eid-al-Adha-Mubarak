# 🌙 Eid al-Adha Mubarak App

A beautiful and festive **Eid al-Adha** greeting application built with Python and Tkinter.

This desktop application displays an animated Eid al-Adha celebration screen featuring a glowing crescent moon, twinkling stars, a mosque silhouette, bilingual greetings, and an interactive "Send Wishes" popup — all with zero external dependencies.

---

## 🚀 Features

### 🕌 Visual Elements
- Animated crescent moon with golden glow
- 60 individually twinkling stars
- Teal mosque silhouette with domes and minarets
- Smooth dark green gradient background sky

### 🎨 Animations
- Pulsing title brightness effect
- Gently swaying `✦ Eid Mubarak ✦` banner
- Real-time star twinkle using sine wave phases

### 🌍 Bilingual Greetings
- Arabic: **عيد الأضحى مبارك**
- Arabic closing: **تقبل الله منا ومنكم**
- English blessings and Eid messages

### 🎁 Interactive
- **Send Eid Wishes** button opens a blessing popup
- Wish counter tracks how many wishes you've sent
- Smooth popup with full Eid blessing message

---

## ✨ Key Features

- Zero External Dependencies (pure Tkinter)
- Animated Canvas Graphics
- Crescent Moon with Glow Effect
- Mosque Silhouette Artwork
- Real-Time Star Twinkling
- Bilingual Arabic & English Text
- Interactive Wishes Popup
- Wish Send Counter
- Fixed 700×580 Window Layout
- OOP-Based Code Structure

---

## 📸 Screenshots

<img width="843" height="701" alt="image" src="https://github.com/user-attachments/assets/853a3132-785f-4f7b-8a8b-69630a9394cd" />

## ```Send Eid Wishes```

<img width="474" height="303" alt="image" src="https://github.com/user-attachments/assets/7c3694b6-2419-48a0-84fa-17daa44b2310" />

---

## 🛠 Technologies Used

- Python 3
- Tkinter
- Canvas Widget
- `math` module (sine-wave animations)
- `random` module (star placement)
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
EidAlAdha/
│
├── eid_al_adha.py
├── README.md
│
└── assets/
    └── screenshot.png
```

---

## ⚙ Requirements

- Python 3.6 or higher
- Tkinter (included with Python)

> ⚠️ On some Linux systems, install Tkinter separately:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## ▶ Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/eid-al-adha-app.git
```

### Navigate to the Project Directory
```bash
cd eid-al-adha-app
```

### Run the Application
```bash
python eid_al_adha.py
```

---

## 🖥 Usage

1. Launch the application.
2. Enjoy the animated Eid greeting screen.
3. Watch the stars twinkle and the title pulse.
4. Click **🌙 Send Eid Wishes 🌙** to open the blessing popup.
5. Read the full Eid al-Adha blessing message.
6. Click **Close** to dismiss the popup.
7. Check the wish counter below the button.
8. Send as many wishes as you like! 🕊️

---

## 🎨 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Background | `#0a0f0a` | Dark near-black green sky |
| Teal | `#00c9a7` | Mosque, button, subtitle |
| Gold | `#f5c518` | Moon, Arabic text, blessings |
| White | `#f0f0f0` | Stars, main title |
| Dim Green | `#2a3a2a` | Divider line |

---

## 🧩 App Structure — `EidApp` Class

| Method | Description |
|--------|-------------|
| `_draw_static_bg()` | Renders pixel-by-pixel vertical gradient background |
| `_draw_mosque()` | Draws teal mosque with arcs, rectangles, and polygons |
| `_draw_stars()` | Places 60 random stars with unique animation phases |
| `_draw_moon()` | Draws crescent moon with glow rings and star shape |
| `_draw_text()` | Renders Arabic heading, English title, and blessings |
| `_draw_button()` | Places the Send Wishes button and wish counter |
| `_send_wishes()` | Opens Toplevel popup with blessings; increments counter |
| `_animate()` | Main loop (50ms): twinkles stars, pulses title, sways banner |

---

## 🔄 Animation Loop

The app uses `self.after(50, self._animate)` — a non-blocking recursive timer that runs every 50 milliseconds:

- **Stars** — each star has a unique sine phase for natural, unsynchronized twinkle
- **Title** — brightness pulses using `sin(t × 0.7)`
- **Banner** — sways left and right using `sin(t × 0.5)`

---

## 📊 Example Interactions

| Action | Result |
|--------|--------|
| Launch app | Full animated Eid screen loads |
| Watch idle | Stars twinkle, title pulses, banner sways |
| Click Send Wishes | Popup opens with Arabic & English blessings |
| Close popup | Counter increments: `1 wishes sent 🕊️` |
| Click again | Counter increments: `2 wishes sent 🕊️` |

---

## 🧠 Concepts Practiced

- Tkinter Canvas Drawing
- Trigonometric Animations (`math.sin`)
- Object-Oriented Programming (OOP)
- Recursive Event Loops (`after()`)
- Toplevel Popup Windows
- Polygon & Arc Shape Drawing
- Dynamic Color Manipulation
- UI Layout with `place()`

---

## 🎯 Learning Outcomes

By studying this project, you will learn:

- Drawing custom shapes with `tkinter.Canvas`
- Building smooth animations without external libraries
- Using `math.sin` for natural motion effects
- Structuring a GUI app with OOP in Python
- Creating popup windows with `Toplevel`
- Managing dynamic widget states (counter, labels)

---

## 🙏 Eid Blessings

> *May your sacrifice be accepted.*
> *May Allah fill your home with joy,*
> *your heart with peace,*
> *and your life with blessings.*
>
> **تقبل الله منا ومنكم**

---

## 👨‍💻 Author

**Abdur Rahman**

Computer & Communication Engineering Student

---

## 📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute this project for educational and personal purposes.

---

## ⭐ Support

If you found this project helpful:
- Star the repository
- Fork the project
- Share it with others
- Contribute improvements

Eid Mubarak! 🌙🕌
