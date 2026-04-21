# EmojiLand's EmojiGame

Fully coded and produced by Fredrick Farouk.

---

## Context

This was created over the summer of 2025, alongside the more important part of this project: "EmojiLand".

During the process of creating my AI model that is under the "EmojiLand" repository, I needed some training data. Although I ended up using an alternative approach for the emoji model (directly hardcoded classifier), this allowed me to test the alternative and see which was better.

Although I personally labelled roughly 3,000 pieces of information, I never got enough data for it to be useful.

Since training data is very boring to label, I created a game (with some inside jokes) in roughly a week to make it more enjoyable, then sent it out to my friends, got their files, and used them.

This is that game.

---

## Implementation Notes

The code, although simpler, is vaguely similar to the "Heckathon" project. I did use a clever little trick by defining a "constrained input" function to avoid try except loops, which I was quite happy with.

---

## Setup Instructions

Below are some instructions for running (this was sent to non-technical friends, so it is intentionally written so that they could understand).

---

### FIRST TIME ONLY

Unzip the folder.

Put the EmojiGame folder inside your Downloads.

Press Windows Key + R → type powershell → press Enter.

Type this:
`python --version`

If you get red error text, then do this:
`cd Downloads/EmojiGame`
`python`

A Microsoft Store window will pop up → press Get.  
After it installs, go back to powershell and type:
`pip install pandas`

Wait for that to finish, then type:
`pip install pywin32`

If you don’t get red text, just type:
`cd Downloads/EmojiGame`
`pip install pandas`
`pip install pywin32`


Finally, run the game by typing:
`python users.py`

---

### EVERY TIME AFTER

Windows Key + R → type powershell → Enter.

Copy-paste this:
`cd Downloads/EmojiGame`
`python users.py`


When you’re done, type exit.

---

If you shut down your computer, or press the X in the top-right, or whatever, there's a non-zero chance you lose progress, so don't. Just type exit. Then do whatever you want.
