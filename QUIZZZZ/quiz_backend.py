import random

# Define quiz data
intensity_data = {
    "easy": [
        {
            "question": "What is the most basic data type in Python?",
            "choices": ["int", "str", "float", "list"],
            "answer": "int"
        },
        {
            "question": "What does 'print()' function do in Python?",
            "choices": ["takes a picture", "prints output to the console", "sends an email", "plays music"],
            "answer": "prints output to the console"
        },
        {
            "question": "What is the result of 2 + 2 in Python?",
            "choices": ["3", "5", "4", "6"],
            "answer": "4"
        },
        {
            "question": "How do you start a single-line comment in Python?",
            "choices": ["/*", "//", "#", "<!--"],
            "answer": "#"
        },
        {
            "question": "Which operator is used for exponentiation in Python?",
            "choices": ["^", "**", "//", "%"],
            "answer": "**"
        },
        {
            "question": "What is the purpose of 'len()' function in Python?",
            "choices": ["Measuring temperature", "Calculating the length of a string", "Counting words in a text", "Performing complex math operations"],
            "answer": "Calculating the length of a string"
        },
        {
            "question": "How do you concatenate two strings in Python?",
            "choices": ["merge()", "join()", "+", "concatenate()"],
            "answer": "+"
        },
        {
            "question": "What is the purpose of 'input()' function in Python?",
            "choices": ["Printing text", "Taking user input", "Drawing shapes", "Generating random numbers"],
            "answer": "Taking user input"
        },
        {
            "question": "Which data type is used for true or false values in Python?",
            "choices": ["int", "str", "bool", "list"],
            "answer": "bool"
        },
        {
            "question": "What is the primary use of a Python list?",
            "choices": ["Storing key-value pairs", "Performing mathematical operations", "Storing ordered elements", "Storing only integers"],
            "answer": "Storing ordered elements"
        },
    ],
    "moderate": [
        {
            "question": "What is the purpose of 'if' statements in Python?",
            "choices": ["Defining a function", "Performing conditional execution", "Declaring a variable", "Creating a list"],
            "answer": "Performing conditional execution"
        },
        {
            "question": "How do you write a 'for' loop in Python?",
            "choices": ["for (i = 0; i < 5; i++)", "for i in range(5)", "loop (i = 0; i < 5)", "iterate 5 times"],
            "answer": "for i in range(5)"
        },
        {
            "question": "What is the result of 4 / 2 in Python?",
            "choices": ["1.0", "2", "4", "0.5"],
            "answer": "2"
        },
        {
            "question": "How can you add a comment in Python?",
            "choices": ["// This is a comment", "/* This is a comment */", "# This is a comment", "<!-- This is a comment -->"],
            "answer": "# This is a comment"
        },
        {
            "question": "Which data type is used for a single character in Python?",
            "choices": ["char", "character", "str", "single"],
            "answer": "str"
        },
        {
            "question": "What is the 'elif' statement used for in Python?",
            "choices": ["Ending a loop", "Defining a function", "Checking another condition after 'if'", "Printing text"],
            "answer": "Checking another condition after 'if'"
        },
        {
            "question": "What is the 'else' statement used for in Python?",
            "choices": ["Starting a loop", "Declaring a variable", "Performing a specific action if 'if' is false", "Creating a list"],
            "answer": "Performing a specific action if 'if' is false"
        },
        {
            "question": "What is the result of '3' + '4' in Python?",
            "choices": ["7", "34", "12", "Error"],
            "answer": "34"
        },
        {
            "question": "What is the 'and' operator used for in Python?",
            "choices": ["String concatenation", "Logical AND operation", "Addition", "Multiplication"],
            "answer": "Logical AND operation"
        },
        {
            "question": "What is the purpose of 'break' in a loop in Python?",
            "choices": ["Exiting the loop prematurely", "Skipping a condition", "Adding an element to a list", "Starting a loop"],
            "answer": "Exiting the loop prematurely"
        },
    ],
    "hard": [
        {
            "question": "Explain the concept of 'recursion' in programming.",
            "choices": ["A function that calls itself", "A loop that repeats indefinitely", "A type of data structure", "A database management system"],
            "answer": "A function that calls itself"
        },
        {
            "question": "What is the purpose of 'try' and 'except' in exception handling?",
            "choices": ["Handling file operations", "Handling keyboard input", "Handling exceptions and errors", "Handling network connections"],
            "answer": "Handling exceptions and errors"
        },
        {
            "question": "What is object-oriented programming (OOP) and how does it relate to Python?",
            "choices": ["A programming language", "A coding style", "A programming paradigm that uses objects and classes; Python supports OOP", "A Python library"],
            "answer": "A programming paradigm that uses objects and classes; Python supports OOP"
        },
        {
            "question": "What are the principles of clean code and why are they important?",
            "choices": ["Optimization and speed", "Readability, maintainability, and collaboration; important for code quality", "Code length and complexity", "Use of the latest programming tools"],
            "answer": "Readability, maintainability, and collaboration; important for code quality"
        },
        {
            "question": "Describe the use of 'decorators' in Python.",
            "choices": ["Adding furniture to a room", "Adding comments to code", "Functions that modify other functions", "A Python design pattern"],
            "answer": "Functions that modify other functions"
        },
        {
            "question": "What is the purpose of 'list comprehension' in Python?",
            "choices": ["Creating a shopping list", "Building lists from existing ones using a concise syntax", "Defining a class in Python", "Generating random numbers"],
            "answer": "Building lists from existing ones using a concise syntax"
        },
        {
            "question": "What is 'inheritance' in object-oriented programming?",
            "choices": ["An error in Python code", "A mechanism for creating new classes from existing ones", "A Python keyword for defining functions", "A loop in Python"],
            "answer": "A mechanism for creating new classes from existing ones"
        },
        {
            "question": "How do you open and read a text file in Python?",
            "choices": ["Using 'print()' function", "Using 'open()' and 'read()' functions", "By declaring a variable", "By using 'for' loop"],
            "answer": "Using 'open()' and 'read()' functions"
        },
        {
            "question": "What is the primary purpose of 'import' statements in Python?",
            "choices": ["Sending an email", "Declaring variables", "Including external modules or libraries", "Creating loops"],
            "answer": "Including external modules or libraries"
        },
        {
            "question": "What is the role of 'self' in Python classes?",
            "choices": ["A keyword used to create a list", "A variable that stores the current date and time", "A reference to the instance of the class", "A built-in Python module"],
            "answer": "A reference to the instance of the class"
        },
    ],
    "extreme": [
        {
            "question": "What are lambda functions in Python and when are they used?",
            "choices": ["Long-term memory management", "Anonymous functions used for short, simple operations", "High-level programming languages", "Video game development"],
            "answer": "Anonymous functions used for short, simple operations"
        },
        {
            "question": "Explain the Global Interpreter Lock (GIL) in Python.",
            "choices": ["A way to lock your computer", "A global code repository", "A mutex that allows only one thread to execute in CPython", "A debugging tool"],
            "answer": "A mutex that allows only one thread to execute in CPython"
        },
        {
            "question": "What is the purpose of the 'yield' keyword in Python?",
            "choices": ["Yielding control to another process", "Yielding a crop in a farming simulation game", "Used in generators to yield a value and save state", "A Python keyword for exiting a program"],
            "answer": "Used in generators to yield a value and save state"
        },
        {
            "question": "Describe the concept of 'Big O notation' in algorithm analysis.",
            "choices": ["A music notation system", "A way to measure the physical size of data", "A notation for analyzing the efficiency of algorithms", "A method for printing large text"],
            "answer": "A notation for analyzing the efficiency of algorithms"
        },
        {
            "question": "How does Python manage memory and garbage collection?",
            "choices": ["Manually releasing memory", "Using a memory card", "Uses automatic memory management and a reference counting system", "Allocating memory using malloc"],
            "answer": "Uses automatic memory management and a reference counting system"
        },
        {
            "question": "What is a 'tuple' in Python?",
            "choices": ["A musical instrument", "An ordered and immutable collection of elements", "A type of loop", "A Python keyword"],
            "answer": "An ordered and immutable collection of elements"
        },
        {
            "question": "What is the purpose of the 'map' function in Python?",
            "choices": ["Creating maps for video games", "Mapping keys to values", "Applying a function to each item in an iterable", "Drawing maps"],
            "answer": "Applying a function to each item in an iterable"
        },
        {
            "question": "What is the role of '__init__' method in Python classes?",
            "choices": ["Initializing a class object", "Printing a message", "Defining a variable", "Performing a loop"],
            "answer": "Initializing a class object"
        },
        {
            "question": "What is the use of 'modules' in Python?",
            "choices": ["A way to create animations", "Storing variables", "Organizing code into reusable files", "Implementing conditional statements"],
            "answer": "Organizing code into reusable files"
        },
        {
            "question": "What does 'pip' stand for in Python?",
            "choices": ["A type of fruit", "Package Installer for Python", "A popular snake species", "A game in Python"],
            "answer": "Package Installer for Python"
        },
    ],
}

# List to keep track of finished intensities
finished_intensities = []


# Function to randomize the order of questions for a given intensity
def randomize_questions(intensity):
    random.shuffle(intensity_data[intensity])

# Function to check if the selected choice is correct
def check_answer(selected_choice, correct_answer):
    return selected_choice == correct_answer

# Function to start the quiz with the selected intensity
def start_quiz(selected_intensity):
    if selected_intensity != "new_intensity":
        if selected_intensity not in finished_intensities:
            # Randomize the questions for the selected intensity
            randomize_questions(selected_intensity)
            # Mark this intensity as finished
            finished_intensities.append(selected_intensity)
            return True
    return False