# Pomodoro Timer

A simple Pomodoro timer built using Python's Tkinter library. The Pomodoro Technique is a time management method where you break work into intervals, traditionally 25 minutes in length, separated by short breaks. This app helps track your work and break sessions, providing a visual cue for your progress.

## Features

- **Work and Break Timers**: Work for 25 minutes, take a 5-minute break, and after four work sessions, enjoy a longer 20-minute break.
- **Progress Tracker**: This code shows the number of completed work sessions with check marks.
- **Reset Functionality**: You can reset the timer at any time.
- **Visual Representation**: A tomato icon with the timer displayed in the center.

## How It Works

1. **Work Session**: Work for 25 minutes (indicated by a green "Work" label).
2. **Short Break**: After a work session, take a 5-minute break (indicated by a pink "Break" label).
3. **Long Break**: After completing four work sessions, take a 20-minute break (indicated by a red "Break" label).
4. **Progress**: A check mark counter tracks how many work sessions you've completed.

## Code Walkthrough

- **Constants**: Set up the colors, font, and time intervals for work, short breaks, and long breaks.
- **Timer Mechanism**: The `start_timer()` function handles the switching between work sessions and breaks. The `count_down()` function updates the timer every second.
- **UI Elements**: The UI is set up with Tkinter, including a canvas that shows a tomato image, and a timer text that updates each second.
- **Progress Tracker**: After each work session, a check mark is added to track progress.
