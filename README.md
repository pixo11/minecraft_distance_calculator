[README.md](https://github.com/user-attachments/files/33229048/README.md)
# Minecraft Distance Calculator

A free, offline desktop app that tells you **how far away** your bases, portals and landmarks are in Minecraft, **which way to go**, and **how long it will take**. It works in the **Overworld**, the **Nether** and **The End**, and converts between them using the 8:1 Nether scale.

No account, no internet connection, no tracking. Everything you type stays on your computer.

---

## Table of contents

1. [Download (easiest)](#-download-easiest)
2. [How to use the app](#-how-to-use-the-app)
3. [What every number means](#-what-every-number-means)
4. [Travel methods and speeds](#-travel-methods-and-speeds)
5. [Dimensions and the Nether scale](#-dimensions-and-the-nether-scale)
6. [Accuracy and limits](#-accuracy-and-limits)
7. [Build the .exe yourself](#-build-the-exe-yourself)
8. [Run it without the .exe](#-run-it-without-the-exe)
9. [Troubleshooting](#-troubleshooting)
10. [Project files](#-project-files)

---

## Download (easiest)

**Go to the [Releases](../../releases) section on the right side of this GitHub page** (or click the "Releases" link above) and download the latest `MinecraftDistanceCalculator.exe`.

Then just double-click it. There is nothing to install.

> **Windows shows a blue "Windows protected your PC" popup?**
> This happens because the app is new and not digitally signed (signing costs money). Click **More info**, then click **Run anyway**. It is safe, and the full source code is in this repository so you can check it yourself. If you would rather not trust a downloaded file, you can [build the .exe yourself](#-build-the-exe-yourself).

**Requirements:** Windows 10 or 11. The app uses Microsoft Edge WebView2, which is already built into Windows 11 and most up-to-date Windows 10 PCs. If the window opens blank, install the free [WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/).

---

## How to use the app

The app has two pages, switched with the tabs at the top: **Calculator** and **How to use**. The three colored dots in the top corner switch the theme (Overworld green, Nether red, The End purple). That is only cosmetic.

### Step 1: Find your coordinates in Minecraft

- **Java Edition:** press **F3** and read the line that starts with **XYZ**.
- **Bedrock Edition** (Windows, console, phone): turn on **Show Coordinates** in the world settings, then read the top-left corner of the screen.

You get three numbers: **X, Y, Z**. You only need **X** (the first) and **Z** (the third). **Y is height and is ignored.** Decimals are fine, and negative numbers are fine.

### Step 2: Say where you are

On the **Calculator** page, under **Your position**:

1. Press the dimension you are standing in: **Overworld**, **Nether** or **The End**.
2. Type **Your X** and **Your Z**.

The app remembers a separate position for each dimension, so you can flip between them as you travel. Underneath, a line shows your **converted spot** in the other dimension (for example "Your Nether spot").

### Step 3: Add your waypoints

**Spawn** is already in the list at 0, 0. Your world's spawn is usually near there but not always, so change it if yours is different.

Press **+ Add waypoint** and fill in:

- **Name** (for example "My House" or "Nether Hub")
- **Dimension** where that place is (Overworld, Nether or The End)
- **X** and **Z**, typed exactly as Minecraft shows them *in that dimension*

Press the **×** button on a waypoint to remove it. You can add as many as you like.

### Step 4: Read the results

Every waypoint card updates the instant you type. Each card shows:

- A **compass needle** pointing the way
- A big **distance** number
- A set of boxes with the details (explained [below](#-what-every-number-means))

The waypoint nearest to you gets a colored outline and a **Closest** badge. The **Closest in ...** panel at the top right also shows its name and distance.

### Step 5: Pick a different travel method (optional)

Use **Also show travel by** to add one extra travel time to every card (boat, elytra, horse and more). You can edit its speed in the **Its speed (blocks/s)** box. Open **Speeds (blocks per second)** to change the walking and sprinting speeds too.

### Other features

| Feature | What it does |
|---|---|
| **World seed (optional)** | Type a seed or any text. It is saved on your computer for future features. It is **not used in any calculation yet**, so leaving it empty changes nothing. |
| **Reset everything** | Clears all your positions, waypoints, speeds and seed. |
| **How to use tab** | A full interactive guide with live demos, a step-by-step math lab, a travel-time race, a portal-link converter, a FAQ, a five-question quiz and a cheat sheet. |
| **Load a ready-made example** | On the How to use tab, fills the calculator with sample data so you can see how it works. |
| **Auto-save** | Everything you type is saved automatically and is still there next time you open the app. |

---

## What every number means

Each waypoint card shows these. In the examples, you are at X 312, Z -148 and a house is at X -85, Z 240, both in the Overworld.

| Box | Meaning |
|---|---|
| **Distance (big number)** | Straight-line distance along the ground, in blocks. |
| **Chunks** | The distance expressed in chunks (1 chunk = 16 blocks). |
| **Head toward** | The direction to go, one of 8 names: North, North-East, East, South-East, South, South-West, West, North-West. |
| **Bearing** | The direction in degrees, measured clockwise from North (0° = North, 90° = East, 180° = South, 270° = West). |
| **Walking** | Travel time at walking speed (default 4.317 blocks/s). |
| **Sprinting** | Travel time at sprinting speed (default 5.612 blocks/s). |
| **Extra method** | Travel time for the method you picked under "Also show travel by" (the default is a boat on water). |
| **Nether (X, Z)** | The matching coordinates in the other dimension, so you know where to build or find a portal. |
| **In the Nether / Nether walking** | Distance and walking time if you take the Nether shortcut. |

### The formulas

```
dx = waypoint X - your X
dz = waypoint Z - your Z

distance = sqrt(dx^2 + dz^2)            (Pythagorean theorem)
bearing  = atan2(dx, -dz) in degrees    (add 360 if negative)
time     = distance / speed             (shown as minutes and seconds)
```

North is **smaller** Z, not bigger. That is the opposite of a school graph. South has the bigger Z.

---

## Travel methods and speeds

All speeds are in blocks per second, taken from the Minecraft Wiki, for flat ground with no Speed or Slowness effects. You can edit any of them.

| Method | Speed (blocks/s) | Note |
|---|---|---|
| Walking | 4.317 | Default |
| Sprinting | 5.612 | Default |
| Boat on water | 8 | Flat water |
| Boat on ice | 40 | Ice or packed ice |
| Boat on blue ice | 72.73 | Blue ice |
| Minecart | 8 | Powered rails |
| Horse (average) | 9.49 | Varies, up to about 14.57 |
| Elytra (level glide) | 30 | Varies with pitch |
| Elytra + rockets | 33.5 | Continuous firework boost |
| Swimming | 2.2 | Still water surface |
| Sprint-swimming | 3.918 | Still water |
| Creative flying | 11 | Adjustable in game |
| Creative sprint-flying | 22 | Adjustable in game |

---

## Dimensions and the Nether scale

The Nether is scaled **1 to 8**: one block walked in the Nether equals **eight blocks** in the Overworld. That is why the Nether is a shortcut.

```
Overworld -> Nether:   X / 8 and Z / 8   (rounded down, like the game)
Nether -> Overworld:   X * 8 and Z * 8
```

Only X and Z are scaled. Height (Y) is not.

### When you and a waypoint are in different dimensions

| You are in | Waypoint is in | What the app does |
|---|---|---|
| Same dimension | Same dimension | Measures the distance directly. |
| Overworld | Nether (or the reverse) | Converts the coordinates first, then measures. |
| Anywhere | The End | No distance is calculated, because The End does not link to the other dimensions by coordinates. |

### Portal linking

When you step through a portal, the game converts your coordinates and searches for an existing portal nearby. If it finds one, it links to it. If not, it builds a new one. According to the Minecraft Wiki the search radius is:

- **Overworld to Nether:** 16 blocks in Java Edition (128 in Bedrock)
- **Nether to Overworld:** 128 blocks in both editions

So build your portal close to the "Nether (X, Z)" spot shown on the card and it will link where you expect.

---

## Accuracy and limits

| Number | How it is rounded |
|---|---|
| Distance, chunks, Nether blocks | 1 decimal place (the math inside is not rounded) |
| Bearing | Nearest whole degree |
| Travel time | Nearest whole second |
| Overworld to Nether coordinates | Divided by 8 and rounded down |
| Nether to Overworld coordinates | Multiplied by 8 (always exact) |

Good to know:

- **Straight line, not a path.** Lakes, mountains and ravines make the real trip longer, and times assume flat ground with nothing in the way.
- **Height is ignored.** The full 3D distance would be `sqrt(dx^2 + dy^2 + dz^2)`. The app leaves out `dy` on purpose because ground travel is usually what you care about.
- **Speeds are approximations.** Soul sand, ice, water, boats, horses, elytra and potions all change them. Pick a travel method or edit the speed boxes to match how you move.
- **Portals can drift.** The game links to the nearest portal in range, so you may arrive a few blocks from the matching spot. Use the numbers as a target, not a pin.
- **Real Nether trips cost extra time.** Building a portal and standing in it (about 4 seconds in Survival) isn't included, so the Nether only wins on longer trips.

---

## Build the .exe yourself

You do **not** need to do this if you downloaded the app from [Releases](../../releases). This is for people who want to build it from source.

### What you need

- A Windows PC
- [Python 3](https://www.python.org/downloads/) installed. **Important:** on the first installer screen, tick **"Add python.exe to PATH"** before clicking Install.

### Steps

1. **Download this repository.** Click the green **Code** button, then **Download ZIP**.
2. **Unzip it** (right-click the ZIP, then **Extract All**).
3. Open the unzipped folder. You should see `app.py`, `build.bat` and `minecraft_distance_calculator.html` together.
4. **Double-click `build.bat`.**
5. If Windows shows a blue **"Windows protected your PC"** popup, click **More info**, then **Run anyway**. (It appears because `build.bat` is a script downloaded from the internet.)
6. A black window opens and starts installing and building. **Wait until it says "Done"** and shows "Press any key to continue". This takes roughly 1 to 3 minutes the first time. Do not close the window while it works. Lots of scrolling text is normal.
7. Press any key to close the window.
8. Open the new **`dist`** folder. Your app is in there: **`MinecraftDistanceCalculator.exe`**.

You can move that single `.exe` anywhere, put it on your desktop, or share it. It does not need the other files.

`build.bat` builds inside a clean temporary environment (a `venv` folder) so that unrelated Python packages on your computer do not get bundled in. This keeps the exe small. After building, you can delete the `build`, `venv` and `dist`-related leftovers (`build` folder and the `.spec` file) if you want to tidy up. Only the `.exe` in `dist` matters.

---

## Run it without the .exe

Don't want an exe at all? The calculator is just one HTML file. Double-click **`minecraft_distance_calculator.html`** and it opens in your web browser. It works fully offline.

To run it as a desktop window using Python instead of building an exe:

```bash
pip install pywebview
python app.py
```

---

## Troubleshooting

**Windows says "Windows protected your PC".**
Click **More info**, then **Run anyway**. This happens with any unsigned app.

**My antivirus flags the exe.**
Apps made with PyInstaller are sometimes flagged by mistake (a false positive), because the tool is also used by other software. The code in this repository is the only thing inside. You can read it, or build the exe yourself to be sure.

**The app opens but the window is blank.**
Install the [WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/) from Microsoft, then try again.

**`build.bat` says "python is not recognized".**
Python isn't installed or wasn't added to PATH. Reinstall Python and tick **"Add python.exe to PATH"** on the first screen.

**The build is very slow or the exe is huge.**
Make sure you are using the latest `build.bat` from this repository. It builds in a clean environment. Delete any old `build`, `dist` and `venv` folders and run it again.

**My saved data disappeared.**
Data is saved on your computer in `%APPDATA%\MinecraftDistanceCalculator`. Using **Reset everything**, or deleting that folder, clears it.

**A distance shows "–".**
Either your position or the waypoint's X and Z are empty, or the waypoint is in The End (no distance is calculated for The End).

---

## Project files

| File | Purpose |
|---|---|
| `minecraft_distance_calculator.html` | The whole calculator (HTML, CSS and JavaScript in one file). |
| `app.py` | A tiny launcher that shows the HTML in a native Windows window. |
| `build.bat` | One-click script that builds `MinecraftDistanceCalculator.exe`. |

---

## Disclaimer

This is an unofficial fan project. It is not affiliated with, endorsed by, or connected to Mojang Studios or Microsoft. "Minecraft" is a trademark of Mojang Studios.
