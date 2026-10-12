
# Word Frequency Counter GUI

A small desktop app built with Python that counts repeated words in text you enter. It uses Tkinter and CustomTkinter to create a graphical interface.

## Features

- Enter words separated by spaces.
- Counts words without distinguishing uppercase and lowercase (for example, `Hello` and `hello` count as the same word).
- Displays only words that appear more than once.
- Simple desktop interface.

## Requirements

- Python 3
- Tk support for Python
- CustomTkinter

Tkinter is included with many Python installations, but some Linux distributions package it separately. On Arch Linux, install it with:

```bash
sudo pacman -S tk
```

## Setup

It’s recommended to use a virtual environment so the project’s Python packages stay separate from your system Python.

From the project folder, create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate
```

Install the project’s Python dependencies:

```bash
python -m pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file yet, create one containing:

```text
customtkinter
```

You can install the dependency directly instead with:

```bash
python -m pip install customtkinter
```

## Run the app

With the virtual environment activated, run:

```bash
python main.py
```

Replace `main.py` with the name of your Python file if needed.

## How to use

1. Launch the app.
2. Type words separated by spaces into the input field.
3. Click **Count repeated words**.
4. The result displays each repeated word and its count.

For example, this input:

```text
pp hard hi subscribe pp hard subscribe pp
```

produces:

```text
{'pp': 3, 'hard': 2, 'subscribe': 2}
```
