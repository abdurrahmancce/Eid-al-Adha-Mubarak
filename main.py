import tkinter as tk
from tkinter import font
import math
import time
import random

# ── colour palette ──────────────────────────────────────────────────────────
BG        = "#0a0f0a"
TEAL      = "#00c9a7"
GOLD      = "#f5c518"
WHITE     = "#f0f0f0"
DIM       = "#2a3a2a"
MOON_COL  = "#f5c518"

class EidApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eid al-Adha Mubarak")
        self.configure(bg=BG)
        self.resizable(False, False)

        W, H = 700, 580
        self.geometry(f"{W}x{H}")

        self.canvas = tk.Canvas(self, width=W, height=H, bg=BG,
                                highlightthickness=0)
        self.canvas.pack()

        self._stars   = []
        self._tick    = 0
        self._sparkles= []

        self._draw_static_bg(W, H)
        self._draw_mosque(W, H)
        self._draw_stars(W, H)
        self._draw_moon(W, H)
        self._draw_text(W, H)
        self._draw_button(W, H)

        self._animate()

    # ── static background ────────────────────────────────────────────────────
    def _draw_static_bg(self, W, H):
        for i in range(H):
            r1, g1, b1 = 10, 15, 10
            r2, g2, b2 = 5, 25, 20
            t = i / H
            r = int(r1 + (r2-r1)*t)
            g = int(g1 + (g2-g1)*t)
            b = int(b1 + (b2-b1)*t)
            self.canvas.create_line(0, i, W, i, fill=f"#{r:02x}{g:02x}{b:02x}")

    # ── mosque silhouette ────────────────────────────────────────────────────
    def _draw_mosque(self, W, H):
        c   = self.canvas
        col = "#00c9a7"
        # ground bar
        c.create_rectangle(0, H-60, W, H, fill=col, outline="")

        def dome(cx, base_y, wd, ht, col):
            c.create_arc(cx-wd//2, base_y-ht, cx+wd//2, base_y+ht,
                         start=0, extent=180, fill=col, outline="")
            c.create_rectangle(cx-wd//2, base_y, cx+wd//2, base_y+ht//2,
                                fill=col, outline="")

        def minaret(cx, top_y, wd, ht, col):
            c.create_rectangle(cx-wd//2, top_y, cx+wd//2, top_y+ht,
                                fill=col, outline="")
            c.create_polygon(cx-wd//2-4, top_y,
                             cx+wd//2+4, top_y,
                             cx, top_y-18, fill=col, outline="")

        base = H - 60
        # main dome
        dome(W//2, base, 200, 90, col)
        # side domes
        dome(W//2-130, base, 100, 55, col)
        dome(W//2+130, base, 100, 55, col)
        # minarets
        minaret(W//2-220, base-130, 22, 130, col)
        minaret(W//2+220, base-130, 22, 130, col)
        minaret(W//2-155, base-90,  16,  90, col)
        minaret(W//2+155, base-90,  16,  90, col)

    # ── twinkling stars ──────────────────────────────────────────────────────
    def _draw_stars(self, W, H):
        random.seed(42)
        for _ in range(60):
            x = random.randint(0, W)
            y = random.randint(0, H - 200)
            r = random.uniform(1, 2.5)
            phase = random.uniform(0, 2*math.pi)
            oid = self.canvas.create_oval(x-r, y-r, x+r, y+r,
                                          fill=WHITE, outline="")
            self._stars.append((oid, phase))

    # ── crescent moon ────────────────────────────────────────────────────────
    def _draw_moon(self, W, H):
        c  = self.canvas
        cx, cy, R = 580, 90, 44
        # glow
        for g in range(20, 0, -1):
            alpha = int(255 * (g/20) * 0.12)
            col = f"#{int(0xf5*(g/20)):02x}{int(0xc5*(g/20)):02x}{int(0x18*(g/20)):02x}"
            c.create_oval(cx-R-g, cy-R-g, cx+R+g, cy+R+g,
                          fill="", outline=col)
        # full circle
        c.create_oval(cx-R, cy-R, cx+R, cy+R, fill=MOON_COL, outline="")
        # cutout (makes crescent)
        c.create_oval(cx-R+14, cy-R-8, cx+R+14, cy+R-8, fill=BG, outline=BG)
        # small star near moon
        self._star_shape(c, cx+30, cy-28, 6, MOON_COL)

    def _star_shape(self, c, cx, cy, r, col):
        pts = []
        for i in range(10):
            angle = math.pi/2 + i * 2*math.pi/10
            radius = r if i % 2 == 0 else r*0.4
            pts += [cx + radius*math.cos(angle),
                    cy - radius*math.sin(angle)]
        c.create_polygon(pts, fill=col, outline="")

    # ── text ─────────────────────────────────────────────────────────────────
    def _draw_text(self, W, H):
        c = self.canvas
        # Arabic-style heading
        c.create_text(W//2, 55,
                      text="عيد الأضحى مبارك",
                      font=("Georgia", 22, "bold"),
                      fill=GOLD, anchor="center")

        # Big English title  (animated later via tag)
        c.create_text(W//2, 120,
                      text="Eid al-Adha",
                      font=("Georgia", 48, "bold"),
                      fill=WHITE, anchor="center",
                      tags="title")

        c.create_text(W//2, 175,
                      text="M U B A R A K",
                      font=("Courier", 16, "bold"),
                      fill=TEAL, anchor="center",
                      tags="subtitle")

        # Divider line
        c.create_line(W//2-180, 200, W//2+180, 200, fill=DIM, width=1)

        # Blessing text
        c.create_text(W//2, 230,
                      text="🌙  May Allah accept your sacrifice  🌙",
                      font=("Georgia", 13),
                      fill=GOLD, anchor="center")

        c.create_text(W//2, 262,
                      text="May Allah bless us in this world & the hereafter",
                      font=("Georgia", 12, "italic"),
                      fill="#aaccaa", anchor="center")

        # ASCII-art banner frame
        banner = "✦  Eid Mubarak  ✦"
        c.create_text(W//2, 305,
                      text=banner,
                      font=("Courier", 15, "bold"),
                      fill=TEAL, anchor="center",
                      tags="banner")

    # ── send-wishes button ───────────────────────────────────────────────────
    def _draw_button(self, W, H):
        btn_frame = tk.Frame(self, bg=TEAL, bd=0)
        btn = tk.Button(btn_frame,
                        text="🌙  Send Eid Wishes  🌙",
                        font=("Georgia", 13, "bold"),
                        bg=TEAL, fg=BG,
                        activebackground=GOLD, activeforeground=BG,
                        relief="flat", bd=0, padx=28, pady=10,
                        cursor="hand2",
                        command=self._send_wishes)
        btn.pack()
        btn_frame.place(x=W//2, y=360, anchor="center")

        # counter label
        self._counter_var = tk.StringVar(value="")
        self._counter_lbl = tk.Label(self,
                                     textvariable=self._counter_var,
                                     font=("Courier", 11),
                                     bg=BG, fg=GOLD)
        self._counter_lbl.place(x=W//2, y=400, anchor="center")

    # ── wishes popup ─────────────────────────────────────────────────────────
    def _send_wishes(self):
        pop = tk.Toplevel(self)
        pop.title("Eid Wishes")
        pop.configure(bg=BG)
        pop.resizable(False, False)
        pop.geometry("420x260")
        pop.grab_set()

        msgs = [
            "🌙  Eid al-Adha Mubarak! 🌙",
            "May your sacrifice be accepted.",
            "May Allah fill your home with joy,",
            "your heart with peace,",
            "and your life with blessings.",
            "",
            "تقبل الله منا ومنكم",
        ]

        for i, m in enumerate(msgs):
            col = GOLD if i in (0, len(msgs)-1) else WHITE
            tk.Label(pop, text=m,
                     font=("Georgia", 11 + (2 if i==0 else 0),
                           "bold" if i==0 else "normal"),
                     bg=BG, fg=col).pack(pady=(10 if i==0 else 2))

        tk.Button(pop, text="Close", font=("Georgia", 10),
                  bg=TEAL, fg=BG, relief="flat", padx=20, pady=6,
                  command=pop.destroy).pack(pady=12)

        # bump counter
        cur = self._counter_var.get()
        n = int(cur.split()[0]) + 1 if cur else 1
        self._counter_var.set(f"{n} wishes sent 🕊️")

    # ── animation loop ────────────────────────────────────────────────────────
    def _animate(self):
        t = self._tick * 0.05
        self._tick += 1

        # twinkle stars
        for oid, phase in self._stars:
            brightness = 0.4 + 0.6 * (0.5 + 0.5 * math.sin(t + phase))
            v = int(brightness * 255)
            col = f"#{v:02x}{v:02x}{v:02x}"
            self.canvas.itemconfig(oid, fill=col)

        # pulse title colour
        r_val = int(200 + 55 * math.sin(t * 0.7))
        self.canvas.itemconfig("title",
                               fill=f"#{r_val:02x}{r_val:02x}{r_val:02x}")

        # scroll banner
        offset = int(10 * math.sin(t * 0.5))
        self.canvas.moveto("banner", 350 + offset - 350//2, 295)   # nudge

        self.after(50, self._animate)


if __name__ == "__main__":
    app = EidApp()
    app.mainloop()