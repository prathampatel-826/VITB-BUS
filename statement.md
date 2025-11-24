1. Problem Statement
In university environments like VIT, students frequently travel to nearby cities for weekends or holidays. Currently, tracking which bus is going where and finding out which seats are empty can be confusing and disorganized if done manually. There is a lack of a simple, centralized system where a student can easily see bus timings, check seat availability visually, and confirm a booking without physical hassle or confusion.

2. Scope of the Project
The VIT Bus Booking System is a Python-based console application designed to solve this management problem. The scope of this project includes:

Route Simulation: Managing transport logic for three specific destinations: Bhopal, Ashta, and Sehore.
Inventory Management: Tracking specific bus numbers and their respective departure times.
Seat Reservation Logic: Providing a real-time simulation of booking seats on a 28-seater bus.
Input Validation: Ensuring users cannot book tickets for past dates or invalid seat numbers.
Note: This project focuses on the backend logic and user interface simulation. It does not currently integrate with a live payment gateway or external cloud database.

3. Target Users
The primary audience for this software includes:

VIT Students: The main users who need to book travel to their hometowns or the city center.
University Transport Coordinators: Staff who need to visualize how full a bus is before it departs.
Faculty Members: Staff members who utilize the college shuttle services.
4. High-Level Features
Visual Seat Layout: Unlike standard lists, this system displays a 2D grid of the bus. It clearly marks available seats with numbers and booked seats with "XX", helping users make informed choices.
Date Verification System: The system uses the datetime module to ensure that bookings are only made for valid, future dates.
Menu-Driven Interface: A clean, looping menu allows users to navigate easily between checking routes, viewing buses, and making bookings without restarting the program.
Dynamic Booking System: The application updates the seat status instantly. Once a seat is chosen, it is locked (marked as XX) to prevent double-booking during the session.
Error Handling: The system protects against crashes by handling invalid inputs (like entering letters where numbers are needed) gracefully.