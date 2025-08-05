This project is a flexible and simple game engine that could be used to make 2D games.

It is currently still heavily under development, but it is still functional as a pip library.


To create a window to place all the objects on, you can write:

```python
import PotatoEngine as pe

windowVar = pe.Window(title, width, height)
```

There are currently only three types of objects to render to the window at the moment and they are as follows:
A Sprite
```python
sprite = pe.Sprite(window, imagePath, pos, size)
# A 32x32 pixel sized image of an elf being rendered on the window at x=100 and y=150.
elf = pe.Sprite(windowVar, './Elf.png', (100, 150), (32, 32))
```

A Button
```python
btn = pe.Button(window, text, pos, size, color)
# A red button with the size of 100x50 pixels at x=50 y=300 being rendered on the window t=with the text "Play" on it.
playBtn = pe.Button(windowVar, "Play", (50, 300), (100, 50), (255, 0, 0))
```

And Some Text
```python
txt = pe.Text(window, text, rect, font, fontSize, color)
#  Render green text saying "Hello" to the window at x=250 y=200 with the size of 100x150
# With the font as Comic Sans MS with the font size 32.
helloTxt = pe.Text(windowVar, "Hello", (250, 200, 100, 150), 'Comic Sans MS', 32, (0, 255, 0))
```

You can check what key was pressed with `pe.keypress(key)` like 'w' for an example.

```python
if pe.keypress('w'):
    # Do stuff...
```

And you can check what mouse key was pressed with ```pe.mouse_press(button)``` like the left mouse button.
```python
if pe.mouse_press('left'):
    # Process click...
```

And the position of the mouse can be gotten ```pe.mouse_pos()```