# 🧟‍♂️ Zombie Shooting Game

A fast-paced arcade-style shooting game built with **Pygame**, featuring multiple zombie types, combo scoring, sound effects, and dynamic difficulty.

---

## 🎮 Overview

This project is a 2D shooting game where the player controls a weapon to defeat incoming zombies while avoiding special red zombies. Players earn points, build combos, collect extra lives, and try to achieve the highest score before losing all health.

The game showcases the use of:

* Sprite-based animation
* Collision detection
* Sound effects and background music
* Multiple enemy behaviors
* Custom fonts and UI rendering

(All gameplay logic is implemented in `game.py` .)

---

## 📂 Project Structure

```
Zombie-Shooting-Game/
│── game.py                 # Main game script (logic, rendering, physics)
│── img/                    # Image assets
│     ├── player.png
│     ├── brownzombie.png
│     ├── redzombie.png
│     ├── yellowzombie.png
│     ├── bullet.png
│     └── life-x.png
│── sound/                  # Audio assets
│     ├── background_music.mp3
│     ├── gunshot.mp3
│     ├── die.mp3
│     └── 1up.mp3
└── Butcherman-Regular.ttf  # Custom font used in the UI
```

---

## 🕹️ How to Play

### Controls

| Key                           | Action            |
| ----------------------------- | ----------------- |
| **← / →**                     | Move left / right |
| **Space**                     | Shoot bullets     |
| **Any key (at start screen)** | Begin game        |

### Objective

* Shoot **brown** and **yellow** zombies to gain points
* Build combos by hitting zombies consecutively
* **Avoid red zombies** — shooting them reduces your life
* Maintain life points (displayed with icons)
* Try to beat the **Highest Score**

---

## 🧟 Enemy Types

| Zombie            | Behavior            | Points     | Effect                                             |
| ----------------- | ------------------- | ---------- | -------------------------------------------------- |
| **Brown Zombie**  | Standard fall speed | 10 × combo | Normal damage on contact                           |
| **Yellow Zombie** | Faster than brown   | 20 × combo | Normal damage on contact                           |
| **Red Zombie**    | Dangerous zombie    | None       | Shooting it reduces life; hitting it gives +2 life |

Each zombie type inherits unique movement patterns and collision effects (implemented with Pygame sprite classes).

---

## 🔊 Audio & Visual Features

* Background music loop
* Distinct gunshot and death sound effects
* Custom UI font for score display
* Animated life bar that updates in real time

---

## 🛠️ Installation & Setup

### 1. Install Python

Make sure Python 3.8+ is installed.

### 2. Install Pygame

```
pip install pygame
```

### 3. Run the Game

```
python game.py
```

---

## 📘 Code Highlights

✔ Object-oriented design using Pygame’s `Sprite` classes
✔ Modularized entities: Player, Bullet, Zombie, Zombie2, Zombie3, Life bar
✔ Collision detection using `groupcollide()` and `spritecollide()`
✔ Custom scoring system with combo mechanics
✔ Use of mixer module for sound effects and BGM

