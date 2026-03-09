# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. Expected: The hint should say “go higher” when the guess is too low and “go lower” when the guess is too high.
Actual: The hint seems fixed around 90. Numbers below 90 always show “go lower”, and numbers above 90 always show “go higher,” regardless of the secret number.
2. Expected: Hard difficulty should have a larger range than Normal.
Actual: Normal uses 1–100, while Hard uses 1–50, making Hard easier than Normal.
3. Expected: The guessing range should change based on the selected difficulty (Easy 1–20, Normal 1–100, Hard 1–50).
Actual: The guessing range stays the same regardless of the difficulty selected.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Copilot and claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- "The issue seems to be in the check_guess function. It likely doesn't handle the cases where the guess is too low or too high relative to the secret number. You need to add logic to compare the guess with the secret and return appropriate hints." ~ Copilot
"The messages in check_guess are swapped. When guess > secret (too high), you should go lower, not higher." ~ClaudeCode
- How I veried it: I looked at the "Check_guess" part of the script. Upon looking at the script the inequality signs seems to be reversed. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- It tried to make me change that entire portion of the script which would make the correction complicated.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I rerun and tested cases for instances picking numbers higher then the actual secret number to see if it's giving clues to choose numbers lower.
- Describe at least one test you ran (manual or using pytest) 
  and what it showed you about your code.
  I chnaged the inqiality signs to test whether the part of the script suggested was indeed what where the problem was
- Did AI help you design or understand any tests? How? Yes Ai helped in explaining what was heppening what areas that I did not understand

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I learned that Streamlit reruns the entire script every time a user interacts with the app, such as clicking a button or entering a value. Because of this, variables reset each time the app reruns. To keep information between interactions, Streamlit uses session state, which stores data so it persists across reruns.

I would explain that Streamlit works by re-running the whole program every time something changes on the page. This means the app starts from the top again whenever the user interacts with it. Session state is like a memory box that keeps important variables saved so the app remembers them even after the script rerun
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- Going into debugging with a hypothesis of what I expect to see and and using that to figuring what was going on. 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task? Try asking it to help me find a more effcient way to execute that part of a script
- In one or two sentences, describe how this project changed the way you think about AI generated code.
They're can multply efficiency but only if you know how to use them.
