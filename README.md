# Day 16 — Daily Habit Tracker

## About the Project
This is Day 16 of my Project 20 Python challenge. The Daily Habit Tracker helps users manage daily habits, track completion, and calculate their progress.

## Features
- Add new habits.
- View all habits and their statuses.
- Mark habits as completed.
- Calculate daily progress as a percentage.
- Handle invalid menu choices and numeric input.
- Run an interactive menu until the user exits.

## Python Concepts Learned
- Functions and function calls
- Lists and dictionaries
- `enumerate()` and `sum()`
- `while` loops and `break`
- Conditional statements
- Ternary conditional expressions
- Exception handling with `try` and `except`
- String formatting and percentage calculations

## How It Works
1. The user selects an option from the menu.
2. Habits are stored as dictionaries inside a list.
3. Each habit has a name and a completion status.
4. The program updates the selected habit when marked completed.
5. Progress is calculated using completed habits divided by total habits.
6. The menu continues until the user chooses Exit.

## How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Run `habit_tracker.py`.
4. Follow the menu instructions in the terminal.

## What I Learned
- How to store related information using dictionaries.
- How to manage a collection of items with lists.
- How to use `enumerate()` to display numbered items.
- How to calculate progress using Boolean values.
- How to handle invalid input without stopping the program.

## Limitations
Habits are stored in memory and are lost when the program closes. File handling could be added to save them permanently.

## Project 20
Part of my 20-day Python project challenge to strengthen my coding logic and become more independent at programming.