# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  - Hints were backwards.
  - New game is not initialized after correct guess.
  - Previous guesses are not actually stored in History right away.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used GitHub Copilot (including Agent mode) as a teammate to refactor functions, add tests, and review game state logic while I validated each change myself. One correct suggestion was to move reusable logic (`get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score`) into `logic_utils.py` so behavior could be tested independently from the Streamlit UI. That suggestion was correct because after refactoring, I ran `pytest` and also manually played the app to confirm guesses, hints, and scoring still behaved as expected. One incorrect/misleading suggestion appeared in the hint logic direction, where the outcome label and hint text did not always align with gameplay expectations (for example, high guesses previously showed the wrong directional guidance). I verified the mismatch by manually guessing above and below a known secret in the app and then fixed it so `Too High` consistently says to go lower and `Too Low` says to go higher.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I treated each bug as fixed only after it passed both manual gameplay checks and automated tests. For manual checks, I started a new game, entered guesses above and below the secret, and confirmed the hint directions matched the outcome labels every time. I also ran `pytest` and verified that the tests for win, too high, and too low all passed, which confirmed that `check_guess` returned both the correct outcome and message text. AI helped me improve the tests by suggesting that I assert on both the game outcome and the hint message, not just one value. That made the tests better at catching regressions in player-facing behavior.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
