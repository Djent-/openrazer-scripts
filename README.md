# openrazer-scripts

## reactive_click.py
Works with: Firefly, Deathadder (probably most mice)

Effect: On left and right click, the mousepad and mouse have a reactive light effect. On scroll, one half of each device will have a reactive light effect. The colors are random each time - ie. everything will be the same random color.

Why: Enabling reactive mode on Firefly is marked as wontfix in the openrazer issues.

Bugs: The script occassionally stops working, starts flashing rapidly, and then starts working normally again. This is due to lol python threading. Don't thread on me!

## razer_spectrum_sync.py
Works with: Firefly, Deathadder (probably all mice), probably other devices

Effect: Synchronizes the start of the spectrum glow.

## bind_switch_tab.py
Works with: Deathadder Elite

Effect: Rebinds the left side buttons to cycle through browser tabs. The front button does Ctrl + Tab, the back button does Ctrl + Shift + Tab. This does override the default forward/back behavior the buttons have.

Bugs: Keeps working even after you kill the script? Idk sometimes. If you start it up multiple times, it will cycle through tabs equal to the number of instances of the script running. Makes sense, right?

*This is actually permanent lol I don't know why*

## keyboard_rows.py
Works with: All keyboards

Effect: Loops through each led, incrementing the hue a bit each time

## matrix.py
Works with: All keyboards

Effect: Creates a matrix-style green columns scrolling down the keyboard. Unfortunately, the columns on keyboards aren't particularly straight because of the Tab, Caps Lock, and Shift keys, so it's kind of diagonal and bendy in some spots.
