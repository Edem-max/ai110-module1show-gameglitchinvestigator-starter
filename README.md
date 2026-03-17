# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] The game, "Glitchy Guesser," is a number-guessing game where players attempt to guess a randomly generated secret number within a specific range. The range and the number of attempts allowed are determined by the selected difficulty level (Easy, Normal, Hard). The game provides hints ("Go higher!" or "Go lower!") to guide the player based on their guesses.
- [ ] Detail which bugs you found.
- [ ] Detail which bugs you found:

The hint logic in the check_guess function was incorrect. It always displayed "Go lower!" for numbers below 90 and "Go higher!" for numbers above 90, regardless of the actual secret number.
The get_range_for_difficulty function had swapped ranges for Normal and Hard difficulties. Normal was set to 1–100, and Hard was set to 1–50, which was incorrect.
On even attempts, the secret number was being cast to a string, causing lexicographic comparisons instead of numeric comparisons. This made the hints behave unpredictably.
- [ ] Explain what fixes you applied.
- [ ] Updated the check_guess function to correctly compare the guess with the secret number and provide appropriate hints ("Go higher!" or "Go lower!") based on the relationship between the two.
Corrected the ranges in the get_range_for_difficulty function to ensure Easy is 1–20, Normal is 1–50, and Hard is 1–100.
Removed the unnecessary casting of the secret number to a string, ensuring all comparisons are numeric and consistent throughout the game.

## 📸 Demo

- [ ] [<img width="757" height="437" alt="Screenshot 2026-03-09 at 01 15 37" src="https://github.com/user-attachments/assets/ce49261b-1265-46e4-95b7-e14d6d8756e6" />]

## 🚀 Stretch Features

- [ ] 
[If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
