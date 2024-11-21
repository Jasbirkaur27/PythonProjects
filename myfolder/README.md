# Quiz Application

This project implements a basic quiz application in Python that allows the user to answer questions from a set of predefined questions. The questions are sourced from an external data structure (`question_data`), and the quiz is managed by the `QuizBrain` class.

## Project Structure

- **question_model.py**: Defines the `Question` class, which represents a single quiz question with its text and answer.
- **data.py**: Contains the `question_data` structure, which holds the data for all quiz questions (text and answers).
- **quiz_brain.py**: Implements the `QuizBrain` class that handles the logic for running the quiz, including keeping track of the user's score and moving through the questions.

## How It Works

1. **Question Data**: The quiz fetches questions from the `question_data` array.
2. **Question Model**: Each question is turned into a `Question` object, which stores both the question's text and answer.
3. **QuizBrain**: The `QuizBrain` class is responsible for managing the quiz, such as keeping track of the score and handling the flow of questions.
4. **Running the Quiz**: The `while` loop continues to ask questions until there are no more remaining. The final score is printed once the user finishes.

