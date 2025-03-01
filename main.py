import random
import streamlit as st

# Function to initialize or reset the game
def initialize_game():
    st.session_state.attempt_number = 0
    st.session_state.computer_number = random.randint(50, 100)
    st.session_state.game_over = False
    st.session_state.message = ""

# Initialize game state if not already present
if 'attempt_number' not in st.session_state:
    initialize_game()

# Streamlit app title
st.title("🎉 Number Guessing Game 🎉")
st.write("Welcome to the Number Guessing Game!")
st.write(f"You have 5 chances to guess the correct number between 50 and 100.")

# Display the current attempt number
st.write(f"Attempt {st.session_state.attempt_number + 1} of 5")

# Function to create a new input field for the next guess
def create_input_field():
    return st.number_input(
        "Enter your guess:",
        min_value=50,
        max_value=100,
        step=1,
        key=f"user_guess_{st.session_state.attempt_number}"
    )

# Display the current input field
user_guess = create_input_field()

# Button to submit the guess
if st.button("Submit Guess"):
    if user_guess:
        st.session_state.attempt_number += 1
        if user_guess == st.session_state.computer_number:
            st.session_state.game_over = True
            st.session_state.message = "🎉 Congratulations! You guessed the right number! 🎉"
        elif user_guess < st.session_state.computer_number:
            st.session_state.message = "Your guess is too low. Try again!"
        else:
            st.session_state.message = "Your guess is too high. Try again!"
    else:
        st.session_state.message = "Please enter a valid number."

# Display the message
st.write(st.session_state.message)

# Button to restart the game
if st.session_state.game_over or st.session_state.attempt_number >= 5:
    if st.button("Play Again"):
        initialize_game()
        st.rerun()
