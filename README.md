# Hoohacks 2025 - Paint by Goals (Pygame Project)

## Authors
1) Grace Zhang, aad8rp@virginia.edu, [gracezh5]
2) Cathy Joseph, hjj2rw@virginia.edu, [crjoseph01]

## Project Structure
* `main.py`: The main script that runs the main application and manages changes between scenes.
* `goal.py`: Contains functions for loading and interacting with the goals page, including adding and checking off daily goals which gives you a token.
* `paintings.py`: Contains the script for allowing the user to unlock a painting after reciving a token.
* `draw.py`: The drawing scene allows user to interact with digital image and the palatte to color "pixel by pixel."
* `see_goals.png`, `see_paintings.png`, `hoohacks_background.png`, `locked_drawing.png`, `puzzle_frog.png`, `return_menu.png`, `title_main.png`, `unlocked.png`, `cursor.png`: Images used for buttons and the custom cursor.

## Dependencies

* Python 3.x
* Pygame (`pip install pygame`)

## How to Run
1.  **Install Pygame:**
    ```bash
    pip install pygame
    ```
2.  **Clone or download the project files.**
3.  **Run `main.py`:**
    ```bash
    python main.py
    ```

## Issues and Future Improvements

* Achieve for smoother functioning of the drawing page
    * Implement a color picker option that allows the user to download any pixel color by number and complete it.
* Improve UI design and user experience by adding interactive elements, background music, confetti, etc.
* Adding persistence to save and load goals even after the application may be closed. However, the application should also reset daily.