# Minecraft Distance Calculator

A free tool for Windows that tells you how far away anything is in Minecraft. Type where you are, add the places you care about (your house, a village, a portal, a stronghold) and it shows the distance, the direction to walk, how long the trip takes, and a live map. It works in the **Overworld**, the **Nether** and **The End**, and it knows how to measure between them.

No account, no Excel, no internet connection and no Minecraft mods needed.

---

## Table of contents

1. [Read this first: you must convert it](#read-this-first-you-must-convert-it)
2. [Download](#download)
3. [Convert it to an .exe (step by step)](#convert-it-to-an-exe-step-by-step)
4. [Where is my .exe?](#where-is-my-exe)
5. [Opening the app](#opening-the-app)
6. [How to use it](#how-to-use-it)
7. [Reading a waypoint card](#reading-a-waypoint-card)
8. [The map](#the-map)
9. [Dimensions: Overworld, Nether and The End](#dimensions-overworld-nether-and-the-end)
10. [Travel methods and speeds](#travel-methods-and-speeds)
11. [Worlds, seeds and finders](#worlds-seeds-and-finders)
12. [The built-in guide](#the-built-in-guide)
13. [How it works (the math)](#how-it-works-the-math)
14. [How the conversion works](#how-the-conversion-works)
15. [Project files](#project-files)
16. [Troubleshooting](#troubleshooting)
17. [FAQ](#faq)
18. [Privacy](#privacy)

---

## Read this first: you must convert it

> **The calculator only works after you convert it into an .exe.**
> If you open the `.html` file in a web browser, the calculator **locks itself** and only shows a "Please use the .exe version" message. It only unlocks inside the app that `build.bat` creates.
> You have to run **`build.bat`** first. It does the conversion for you, and it only takes a few minutes. After that, you use the `.exe` it creates.

You only need to convert **once**. After that you can open the `.exe` whenever you want.

---

## Download

**Get the files from the [Releases tab](../../releases) of this repository, not from the green "Code" button.**

1. Open the **Releases** tab on the right side of this page (or click the link above).
2. Find the newest release at the top.
3. Under **Assets**, click the `.zip` file to download it.
4. **Extract the zip.** Right-click it, choose **Extract All...**, then **Extract**. Do not run anything from inside the zip, because it will fail.

After extracting you will have a folder with these three files:

```
minecraft_distance_calculator.html
app.py
build.bat
```

Keep all three **together in the same folder**. Moving only one of them will break the conversion.

---

## Before you start: install Python (one time)

`build.bat` uses **Python** to create the app, so Python must be installed on your computer.

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3 for Windows.
2. Run the installer and **tick "Add python.exe to PATH"** on the first screen, then click **Install Now**.
3. You also need an **internet connection while converting** (it downloads two small helper packages). You do not need internet afterwards.

Already have Python? Open a Command Prompt, type `python --version` and press Enter. If it prints a version number, you are ready.

---

## Convert it to an .exe (step by step)

### 1. Open the folder

Open the folder you extracted. You should see the three files listed above.

### 2. Double-click `build.bat`

`build.bat` is the converter. Double-click it.

### 3. If a popup appears, press **Run**

Windows sometimes shows a warning when you open a `.bat` file you downloaded, for example **"Open File - Security Warning"** or **"Windows protected your PC"**. This is normal for any downloaded script.

- If you see **"Open File - Security Warning"**, click **Run**.
- If you see **"Windows protected your PC"** (blue window), click **More info**, then click **Run anyway**.

You can read `build.bat` and `app.py` in any text editor (Notepad is fine) before you run them. They are short.

### 4. Wait for the black window to finish

A black window (Command Prompt) opens and text scrolls by. It is creating a clean workspace, downloading the helper packages and packing everything into one file. **Do not close it yet** and do not click inside it. Be patient, it can take a few minutes, and it may look like nothing is happening for a while. That is normal.

### 5. When it says **Done**, close the window

When you see this, the conversion has finished:

```
Done. Your exe is in the "dist" folder.
Press any key to continue . . .
```

**Close the black window** (click the X, or press any key) and you are finished converting.

> The word **Done** is printed at the end even if something went wrong earlier. If you see red error text above it, or there is no `dist` folder, see [Troubleshooting](#troubleshooting).

---

## Where is my .exe?

When the conversion is finished, the new `.exe` is in a folder that `build.bat` creates **next to the files you downloaded**. Look for a folder named **`dist`** inside the folder you extracted:

```
your-folder\
├── minecraft_distance_calculator.html
├── app.py
├── build.bat
├── MinecraftDistanceCalculator.spec
├── build\
├── venv\
└── dist\
    └── MinecraftDistanceCalculator.exe   <-- this is the one
```

Open the `dist` folder and double-click **`MinecraftDistanceCalculator.exe`**.

**Tip:** Right-click the `.exe` and choose **Send to > Desktop (create shortcut)** so you can open it from your desktop. You can also move the `.exe` anywhere you like, because everything it needs is inside it.

The other items (`build`, `venv` and the `.spec` file) are leftovers from the conversion. They are safe to delete once you have your `.exe`.

---

## Opening the app

1. Double-click the `.exe`.
2. If Windows shows **"Windows protected your PC"**, click **More info**, then **Run anyway**. This appears because the program was made on your own computer and is not signed by a big publisher. It is safe, and you built it yourself from the files in this repository.
3. The calculator opens in its own window (no browser needed).

The app needs the **Microsoft Edge WebView2 Runtime**, which comes with Windows 11 and with up-to-date Windows 10. If the window stays blank or does not open, install it from [Microsoft's WebView2 page](https://developer.microsoft.com/microsoft-edge/webview2/) (choose the **Evergreen Bootstrapper**).

---

## How to use it

The app has two pages, selected with the tabs at the top: **Calculator** and **How to use**.

### Step 1: find your coordinates in Minecraft

- **Java Edition:** press **F3** and read the line that starts with **XYZ**.
- **Bedrock Edition** (phone, console, Windows): turn on **Show Coordinates** in the world settings and read the top-left corner.

You get three numbers: X, Y and Z. You only need **X** (first) and **Z** (third). **Y is height and is ignored.** Decimals are fine.

### Step 2: tell the calculator where you are

1. Under **Your position**, press the button for the dimension you are standing in: **Overworld**, **Nether** or **The End**.
2. Type your **X** and **Z**.

The calculator remembers a separate position for each dimension, so when you switch dimension and come back, the old numbers are still there.

### Step 3: add the places you want to measure

Every place is a **waypoint**. Each one has:

| Box | What to type |
| --- | --- |
| **Name** | Anything you like: house, base, village, portal |
| **Dimension** | The dimension where that place is |
| **X** and **Z** | The coordinates exactly as the game shows them in that dimension |

Press **+ Add waypoint** to add more, and the **x** button to remove one. A **Spawn** waypoint at 0, 0 is added for you. The real world spawn is usually close to 0, 0 but not always, so change it if yours is different.

> **Important:** always type coordinates exactly as the game shows them in the dimension where the place is. **Never convert Nether coordinates yourself.** The calculator multiplies and divides for you.

### Step 4: read the results

Every waypoint card updates instantly as you type. The card with the **Closest** badge is the nearest place in your dimension, and the **Closest** panel at the top names it.

---

## Reading a waypoint card

| Item | What it means |
| --- | --- |
| **Compass** | The needle points toward the place. North is up. |
| **Big number** | Straight-line distance in blocks, with a bar that compares it with your farthest waypoint. |
| **Chunks** | Distance divided by 16 (a chunk is 16 blocks wide). |
| **Head toward** | The direction name: North, North-East, East, South-East, South, South-West, West or North-West. |
| **Bearing** | The exact direction in degrees, clockwise from North (90 is East, 180 is South, 270 is West). |
| **Walking / Sprinting** | Travel time at 4.317 and 5.612 blocks per second. |
| **Travel method** | Travel time for the method you picked (boat, elytra, horse and so on). |
| **Nether / Overworld (X, Z)** | Where the matching spot is in the other dimension. |
| **In the Nether** | How far the same trip is if you go through the Nether (distance divided by 8). |
| **Nether walking** | How long that Nether trip takes on foot. |

If something shows a dash (-), a number is missing. Check that you typed both your X and Z and the waypoint's X and Z.

---

## The map

Under the position panel there is a live top-down **map**. **North is up and East is right.**

| What you see | Meaning |
| --- | --- |
| Pulsing **blue dot** | You |
| **Green / red / purple dots** | Waypoints in the Overworld / Nether / The End |
| **Gold ring** and **dashed blue line** | The closest place in your dimension |
| **Dashed-outline dots** | Places from the other dimension, drawn where they would be on your map (multiplied or divided by 8) |
| **Dotted circles** | Distance rings around you, labelled in blocks |
| **Arrow on the edge** | A place is off screen that way. Click it to jump there. |
| **Scale bar** | Bottom-left corner |

Controls:

- **Drag** to move the map.
- **Mouse wheel** (or **pinch** on a touch screen) to zoom.
- **Hover or click a dot** to see its details and an orange line with the distance. A button in the popup jumps to its waypoint card.
- **Click empty ground** to drop a **pin**. It shows the coordinates, the distance from you and the walking time. Type a name and press **Add as waypoint** to save it.
- **Fit all** zooms to show everything. **Center on me** centers on your dot.
- Keyboard (click the map first): arrow keys move, **+** and **-** zoom, **0** fits everything.
- Untick **Show places from the other dimension** to hide the dashed dots.

Until you move or zoom the map yourself, it re-fits automatically whenever you add or change something.

---

## Dimensions: Overworld, Nether and The End

The Nether is squeezed 8 to 1: one block in the Nether covers **8 blocks** in the Overworld. That is why people travel through the Nether to cross long distances quickly.

| You are in | The place is in | What the calculator does |
| --- | --- | --- |
| Same dimension | Same dimension | Measures directly. |
| Overworld | Nether | Converts the place to Overworld coordinates (X x 8, Z x 8), then measures. |
| Nether | Overworld | Converts the place to Nether coordinates (X / 8, Z / 8, rounded down), then measures. |
| Anything else | The End | **No distance.** The End is a separate world that lines up with nothing. A message explains how to travel instead. |
| The End | The End | Measures directly. |

Notes:

- Distances in the Nether are in **Nether blocks**. The card also shows the Overworld equivalent.
- The game rounds **down** when it divides by 8, and the calculator does the same.
- When you go through a portal, the game links to the nearest portal inside a search area (16 blocks going to the Nether in Java, 128 in Bedrock, and 128 coming back to the Overworld). You can arrive a few blocks from the matching spot, so treat the numbers as a target.
- The page color theme changes with your dimension. You can also pick a theme with the three squares at the top right.

---

## Travel methods and speeds

Use **Also show travel by** to pick a method. The card shows the time for it next to walking and sprinting. You can type your own speed in **Its speed (blocks/s)**, and the label then shows **(custom)**.

| Method | Blocks per second |
| --- | --- |
| Walking | 4.317 |
| Sprinting | 5.612 |
| Boat on water | 8 |
| Boat on ice | 40 |
| Boat on blue ice | 72.73 |
| Minecart (powered rails) | 8 |
| Horse (average) | 9.49 (up to about 14.57) |
| Elytra (level glide) | 30 |
| Elytra + rockets | 33.5 |
| Swimming | 2.2 |
| Sprint-swimming | 3.918 |
| Creative flying | 11 |
| Creative sprint-flying | 22 |

Speeds come from the Minecraft Wiki (flat ground, no Speed or Slowness effects). Real trips are slower because of hills, turns and obstacles. Walking and sprinting speeds can be changed under **Speeds (blocks per second)**.

---

## Worlds, seeds and finders

At the top of the calculator there is a **World** box. Each world keeps its own spawn, waypoints, seed and edition, so you can play on several Minecraft worlds without mixing them up. Use **+ New world** to add one, the drop-down to switch, and **Delete** to remove one. Everything is saved on your computer.

If you type your **world seed** (and pick your **Edition**), two extra tools appear on the map:

- **Slime chunks**: tick the box and slime chunks are drawn in green. Hover the map to see if a chunk is a slime chunk.
- **Strongholds**: shows the 3 strongholds closest to you, with distance, direction and walking time. Each has a **Show** button (centers the map on it) and a **+ Waypoint** button.

**Editions:**

| Edition | Slime chunks | Strongholds |
|---|---|---|
| Java 1.19.3 or newer | Exact | All 128 positions, exact before the game adjusts them |
| Java 1.9 to 1.19.2 | Exact | Only stronghold 1 is exact. Strongholds 2 and 3 are shown as a direction and a distance range |
| Bedrock | Not supported (Bedrock slime chunks do not depend on the seed) | Not supported |

**Accuracy:** I checked the slime chunk and stronghold math against the reference library *cubiomes* on several seeds. The game moves each stronghold to a fitting biome, so the real one can be up to about **112 blocks** away from its dot. Get close, then throw an eye of ender. This has not been compared with a real Minecraft world yet, so treat the dots as very good estimates.

Leaving the seed empty changes nothing: the calculator works as before.

---

## The built-in guide

The **How to use** tab is a full animated tutorial with 14 sections:

1. Quick start
2. How coordinates work
3. The math, step by step (an interactive lab with a clickable map)
4. Bearing and direction (a compass trainer)
5. Travel time (a race between travel methods)
6. The 8 to 1 Nether scale
7. Crossing dimensions
8. The map
9. Worlds, seeds and finders
10. Every number explained
11. Accuracy and limits
12. Questions and fixes
13. Test yourself (a short quiz)
14. Cheat sheet

Press **Load a ready-made example** at the top of the guide to fill the calculator with sample data and see how everything looks.

---

## How it works (the math)

Everything uses only X and Z (the flat ground). Height is ignored.

**1. The two gaps**

```
dx = place X - your X
dz = place Z - your Z
```

**2. Distance** (the Pythagorean theorem, a straight line)

```
distance = square root of (dx*dx + dz*dz)
```

Example: you at 0, 0 and a base at 300, 400 gives `sqrt(300*300 + 400*400) = sqrt(250000) = 500` blocks. Adding the gaps (700) is wrong because a straight line is shorter than walking the two sides.

**3. Chunks**

```
chunks = distance / 16
```

**4. Travel time**

```
seconds = distance / speed
```

shown as minutes and seconds.

**5. Bearing** (direction in degrees, clockwise from North)

```
bearing = atan2(dx, -dz) in degrees, add 360 if negative
```

North is **-Z**, East is **+X**, South is **+Z**, West is **-X**.

**6. Direction name**

```
name = list[ round(bearing / 45) mod 8 ]
list = North, North-East, East, South-East, South, South-West, West, North-West
```

**7. Crossing between the Overworld and the Nether**

```
Overworld -> Nether :  X / 8, Z / 8   (rounded down)
Nether -> Overworld :  X x 8, Z x 8
Same trip, Nether blocks     = Overworld distance / 8
Same trip, Overworld blocks  = Nether distance x 8
```

The place is converted into **your** dimension first, and then the normal distance formula is used.

---

## How the conversion works

The calculator itself is a single web page (`minecraft_distance_calculator.html`). It contains all of its own code and needs no internet.

- **`app.py`** is a small launcher. It uses [pywebview](https://pywebview.flowrl.com/) to open the page in its own window and keeps your entries between launches.
- **`build.bat`** creates a clean Python environment (`venv`), installs `pywebview` and `PyInstaller`, and then uses PyInstaller to pack the launcher and the page into one `MinecraftDistanceCalculator.exe`. It is a windowed app, so no black console window appears when you run it.
- The page itself checks that it is running inside the app window. In a normal browser it shows "Please use the .exe version" instead of the calculator.

That is why you run `build.bat` once, and why the `.html` file on its own does not work.

---

## Project files

| File | What it is |
| --- | --- |
| `minecraft_distance_calculator.html` | The calculator and the tutorial (one self-contained page). |
| `app.py` | The launcher that opens the calculator in a window. |
| `build.bat` | The converter. Double-click it to create the `.exe`. |

Created by `build.bat`: `venv\` (temporary workspace), `build\` (temporary files), `MinecraftDistanceCalculator.spec` (PyInstaller settings) and `dist\MinecraftDistanceCalculator.exe` (your app).

---

## Troubleshooting

**It says "python is not recognized" (or similar).**
Python is not installed, or it was installed without **"Add python.exe to PATH"**. Install it again from [python.org](https://www.python.org/downloads/) and tick that box, then run `build.bat` again.

**There are red errors, or there is no `dist` folder after Done.**
Make sure you **extracted** the zip first and that `build.bat`, `app.py` and the `.html` file are in the **same folder**. Check that you are online, then run `build.bat` again. If it still fails, take a screenshot of the black window and open an issue with it.

**I opened the .html and it says "Please use the .exe version".**
That is intended. Follow the steps above to convert it and use the `.exe`.

**The app window is blank or does not open.**
Install the Microsoft Edge WebView2 Runtime (see [Opening the app](#opening-the-app)).

**Windows says "Windows protected your PC".**
Click **More info**, then **Run anyway**. This happens with any program that is not signed by a large publisher.

**A popup asks me to confirm when I open `build.bat`.**
Click **Run**.

**My antivirus flags the `.exe`.**
Programs packaged with PyInstaller are sometimes flagged by mistake. You built it yourself from the files in this repository, which you can read in any text editor. If you are unsure, you can add the folder to your antivirus exceptions.

**I can't find the `.exe`.**
Look in the **`dist`** folder next to `build.bat`, for the file named `MinecraftDistanceCalculator.exe`. See [Where is my .exe?](#where-is-my-exe).

**The numbers show dashes.**
A value is missing. Type both **Your X** and **Your Z** for the dimension you are in, and both **X** and **Z** on the waypoint.

**I just used a portal. What now?**
Press the button for the new dimension and type the coordinates the game shows there.

**My entries disappeared.**
Entries are saved on your computer in `%APPDATA%\MinecraftDistanceCalculator`. The **Reset everything** button clears them on purpose, and deleting that folder does too.

**I want to build it again.**
Just run `build.bat` again. It replaces the old `venv` automatically. You can delete the `dist` and `build` folders first if you want a fresh start.

---

## FAQ

**Do I need to install anything to use the `.exe`?**
Only to convert it: Python, once. After that the `.exe` runs on its own (on Windows 10 or 11 with WebView2).

**Do I need internet?**
No, the app works offline.

**Does it work with Java and Bedrock?**
Yes. Both show X and Z the same way. Only the way you display coordinates differs (F3 in Java, Show Coordinates in Bedrock).

**Does height (Y) matter?**
No. Distances only use X and Z.

**Why is The End different?**
It is a separate world that lines up with no other dimension, so a distance between it and another dimension means nothing. You enter through an End portal in a stronghold and return through the exit portal. Two places that are both in The End are measured normally.

**Does it work on Mac or Linux?**
`build.bat` is a Windows script, so the `.exe` is for Windows.

**How do I find my world's spawn?**
A compass points at the world spawn in the Overworld. With cheats on, `/setworldspawn` while you stand somewhere sets spawn to that spot, which gives you exact numbers. Until then, 0, 0 is a good guess.

---

## Privacy

Nothing you type is sent anywhere. The calculator runs entirely on your computer and works without an internet connection (internet is only needed once, while `build.bat` downloads its helper packages). Your entries are saved in `%APPDATA%\MinecraftDistanceCalculator` on your own computer.

---

*This is an unofficial fan-made tool. Minecraft is a trademark of Mojang AB and Microsoft. This project is not affiliated with or endorsed by Mojang or Microsoft.*
