# VIT Bus Booking System

### 1. Project Overview
Welcome to the **VIT Bus Booking System**! This is a Python-based console application designed to solve a real-world problem for students: managing daily commutes.

Instead of guessing which bus goes where, this system allows users to view routes, check specific bus timings, and simulate booking a seat on a visual grid. It replaces manual confusion with a structured digital workflow.

### 2. Key Features
This project is built with modular functions to handle specific tasks:

* **Smart Date Validation:** You can't book a bus for yesterday! The system checks the date you enter against today's date to ensure it's valid.
* **Route & Bus Selection:** Choose from major routes (Bhopal, Ashta, Sehore) and see specific bus numbers and timings available for that route.
* **Visual Seat Booking:** A visual grid (Matrix) represents the bus. You can see which seats are empty (XX represents booked) and pick your favorite spot.
* **Error Handling:** If you type a letter instead of a number, or pick a seat that doesn't exist, the system catches the error and asks you to try again politely.
* **Seat Availability Check:** A "View Only" mode where you can check how full a bus is without making a booking.

### 3. Technologies Used
* **Language:** Python 3.x
* **Libraries:** datetime (Standard library for handling real-time dates).
* **Concepts:** Lists (2D Arrays/Matrices), Error Handling (try-except), and Modular Functions.

### 4. How to Install & Run
Follow these simple steps to get the project running on your local machine:

1.  **Prerequisites:** Make sure you have Python installed. You can check by typing `python --version` in your terminal.
2.  **Download:** Clone this repository or download the `main.py` file.
3.  **Run:** Open your terminal/command prompt, navigate to the folder, and type:
    ```bash
    python main.py
    ```
4.  **Interact:** Follow the on-screen menu instructions.

### 5. How to Test (Walkthrough)
To verify the system is working as expected, try these scenarios:

* **Test 1: Date Validation**
    * Start the program.
    * Enter a date from the *past* (e.g., last year).
    * *Result:* The system should show "Invalid Date!" and ask again.
* **Test 2: Successful Booking**
    * Select **Option 1 (Book Tickets)**.
    * Choose Route 1 (Bhopal) -> Bus 1.
    * Select Seat **5**.
    * *Result:* The system confirms the booking and marks Seat 5 as `XX` in the layout.
* **Test 3: Double Booking Prevention**
    * Try to book Seat **5** again on the same bus.
    * *Result:* The system should say "Seat already booked!" and ask you to pick another.
* **Test 4: Input Safety**
    * When asked for a menu option, type "hello" instead of a number.
    * *Result:* The program shouldn't crash; it will ask for a valid number.

### 6. Future Enhancements
Currently, this system runs in the console. In the future, this can be expanded by:
* Connecting to a database (SQL) to save bookings permanently.
* Adding a Login system for students.
* Creating a graphical user interface (GUI).
