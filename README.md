# Number Guessing Game 🎮

A simple, interactive console game built with Python designed to practice core programming logic and input validation.

## 📝 Project Overview
This project was developed to transition from basic syntax to functional application. It challenges the player to find a secret number chosen by the computer within a specific range, providing real-time feedback on each attempt.

## 🧠 Core Logic & Structure
The project follows a **"Security Checkpoint"** architecture to ensure clean and stable execution:

1. **Setup (Preparation):**
   - Uses the `random` module to pick a secret number.
   - Initializes a `tries` counter to track player performance.

2. **The Game Loop:**
   - Employs a `while` loop that runs indefinitely until the user successfully guesses the number.

3. **The Bouncer (Validation):**
   - **Type Checking:** Ensures the user enters an integer, not text.
   - **Range Checking:** Validates that the guess is within the allowed bounds (e.g., 1-100).
   - *This prevents the program from crashing on "bad" input.*

4. **Comparison Logic:**
   - Evaluates if the guess is **Too High**, **Too Low**, or **Correct**.

## 🛠️ How to Run
1. Ensure you have Python installed.
2. Clone this repository.
3. Run the script using:
   ```bash
   python main.py
