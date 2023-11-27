import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import quiz_backend
import sys

# Initialize progress for each intensity level
progress = {intensity: {"score": 0, "completed": False} for intensity in quiz_backend.intensity_data.keys()}

# Dictionary to store user scores for each intensity
user_scores = {intensity: 0 for intensity in quiz_backend.intensity_data.keys()}

# Initialize the selected intensity variable
selected_intensity = None

# Variable to track whether the quiz has started
quiz_started = False

# Function to hide the Finish button
def hide_finish_button():
    finish_button.pack_forget()

# Function to show the Finish button
def show_finish_button():
    finish_button.pack(side="bottom", pady=50)

# Function to show the intensity selection frame
def show_intensity_selection():
    # This function is called when the user clicks the "Start Quiz" button after entering their name.
    name = name_entry.get()
    if name:
        # If the user has entered a name, hide the name frame and show the intensity selection frame.
        name_frame.pack_forget()
        intensity_frame.pack()
        show_finish_button()  # Show the Finish button when selecting intensity
    else:
        # If no name is entered, display a warning message.
        messagebox.showwarning("Name Required", "Please enter your name.")

# Function to start the quiz
def start_quiz():
    global selected_intensity, quiz_started
    # This function is called when the user clicks the "Start Quiz" button after selecting an intensity.
    selected_intensity = intensity_var.get()

    if progress[selected_intensity]["completed"]:
        # If the selected intensity is already completed, show a message and reset the intensity selection.
        intensity_var.set("new_intensity")
        return

    if quiz_backend.start_quiz(selected_intensity):
        # If the quiz for the selected intensity can be started, initiate the questionnaire.
        start_questionnaire(selected_intensity)
        quiz_started = True  # Set quiz_started to True when the quiz starts
        hide_finish_button()  # Hide the Finish button when the quiz starts
    else:
        # If the quiz for the selected intensity is already finished, display a warning message.
        messagebox.showwarning("Intensity is already finished", "Please select another intensity.")
        show_finish_button()  # Show the Finish button when the warning is displayed

# Function to start the questionnaire
def start_questionnaire(intensity):
    # This function initiates the quiz questionnaire for the selected intensity.
    global current_question, score, current_questions, selected_intensity  # Declare selected_intensity as global
    current_question = 0
    score = 0
    current_questions = quiz_backend.intensity_data[intensity]

    # Hide the intensity selection frame.
    intensity_frame.pack_forget()

    # Show the quiz interface elements.
    qs_label.pack(pady=10)
    for button in choice_btns:
        button.pack(pady=5)
    feedback_label.pack(pady=10)
    next_btn.pack(pady=10)

    # Set the selected intensity variable
    selected_intensity = intensity
    show_question()

# Function to show the next question
def show_question():
    global current_question, selected_intensity

    if current_question < len(current_questions):
        question = current_questions[current_question]

        question_text = question["question"]
        qs_label.config(text=question_text)

        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal", command=lambda i=i: check_answer(i))

        feedback_label.config(text="")
        next_btn.config(state="disabled")

    else:
        # If all questions are answered, display the final score and update progress.
        # Reset the quiz or perform any other actions as needed
        reset_quiz()
        
        # Update the user's score for the completed intensity
        user_scores[selected_intensity] += score

        return  # Stop execution here to avoid calling show_question() again

    # Increment the question counter only when the user clicks the "Next" button
    current_question += 1

# Function to check the answer
def check_answer(choice):
    # This function checks if the selected choice matches the correct answer.
    selected_choice = choice_btns[choice]["text"]
    correct_answer = current_questions[current_question - 1]["answer"]

    if quiz_backend.check_answer(selected_choice, correct_answer):
        global score
        score += 1
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

    if current_question == len(current_questions):
        reset_quiz()

# Function to reset the quiz
def reset_quiz():
    # This function resets the quiz state, hides the quiz interface, and shows the intensity selection frame.
    global user_scores, quiz_started
    # Update the user's score for the completed intensity
    user_scores[selected_intensity] += score

    for button in choice_btns:
        button.config(state="disabled")
        button.pack_forget()
    feedback_label.pack_forget()
    next_btn.pack_forget()
    qs_label.pack_forget()
    intensity_frame.pack()

    # Check if the intensity is completed after packing the intensity_frame
    if progress[selected_intensity]["completed"]:
        show_finish_button()  # Show the Finish button when the intensity is completed
    elif quiz_started:
        show_finish_button()  # Show the Finish button when the quiz has started

# Add this line at the beginning to initialize user_scores
user_scores = {intensity: 0 for intensity in quiz_backend.intensity_data.keys()}

# Function to check the user's score
def check_score():
    # This function displays the user's scores for each intensity.
    score_message = "\n".join([f"{intensity}: {user_scores.get(intensity)}/{len(quiz_backend.intensity_data[intensity])}" for intensity in quiz_backend.intensity_data.keys()])
    messagebox.showinfo("Your Score", score_message)

# Function to finish the quiz
def finish_quiz():
    # This function is called when the user clicks the "Finish" button.
    messagebox.showinfo("Thank you!", "Thank you for playing the quiz.")
    sys.exit()

# Create the main Tkinter window
root = tk.Tk()
root.title("ProgQuiz")
root.geometry("1000x550")  # Set the initial size of the window
style = Style(theme="darkly")  # Set the ttkbootstrap theme for styling

# Create a frame for entering the name
name_frame = ttk.Frame(root)
name_frame.pack()

name_label = ttk.Label(name_frame, text="Enter Your Name:")
name_label.pack(pady=10)

name_entry = ttk.Entry(name_frame)
name_entry.pack(pady=10)

name_button = ttk.Button(name_frame, text="Start Quiz", command=show_intensity_selection)
name_button.pack(pady=20, padx=20)

# Create a frame for selecting quiz intensity
intensity_frame = ttk.Frame(root)
intensity_frame.pack_forget()

intensity_label = ttk.Label(intensity_frame, text="Select Quiz Intensity:")
intensity_label.pack()

intensity_var = tk.StringVar()
intensity_var.set("new_intensity")

# Create intensity selection radio buttons
for option in quiz_backend.intensity_data.keys():
    intensity_button = ttk.Radiobutton(intensity_frame, text=option, variable=intensity_var, value=option)
    intensity_button.pack(pady=5)

start_button = ttk.Button(intensity_frame, text="Start Quiz", command=start_quiz)
start_button.pack(pady=10)

# Button to check user's scores
check_score_button = ttk.Button(intensity_frame, text="Check Score", command=check_score)
check_score_button.pack(pady=10)

# Initialize variables
current_question = 0
score = 0
current_questions = []
intensity_options = list(quiz_backend.intensity_data.keys())

# Create labels, buttons, and other UI elements for the quiz interface
qs_label = ttk.Label(root, anchor="center", wraplength=500, padding=10)
qs_label.pack(pady=10)
qs_label.pack_forget()

choice_btns = []
for i in range(4):
    button = ttk.Button(root, command=lambda i=i: check_answer(i))
    choice_btns.append(button)
    button.pack_forget()

feedback_label = ttk.Label(root, anchor="center", padding=10)
feedback_label.pack()
feedback_label.pack_forget()

next_btn = ttk.Button(root, text="Next", command=show_question, state="disabled")
next_btn.pack(padx=10)
next_btn.pack_forget()

# Configure styles for the UI elements
style.configure("TLabel", font=("Helvetica", 23, ))
style.configure("TButton", font=("Helvetica", 16))
style.configure("TRadiobutton", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 20))

# Create a "Finish" button
finish_button = ttk.Button(root, text="Finish", command=finish_quiz)
finish_button.pack(side="bottom", pady=50)  # Use the pack geometry manager with the side option

# Start the main application loop
root.mainloop()
