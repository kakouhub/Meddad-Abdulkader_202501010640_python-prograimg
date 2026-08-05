# Week 11 - Tutorial 11: Computer Lab Access System

## Overview
This is a Python-based Computer Lab Access System that automates student entry into computer laboratories at City University.

## Features
- Collects student information including name, ID, registration status
- Verifies three conditions before granting access:
  1. Student is registered for today's lab session
  2. Computer laboratory is open
  3. Computers are available
- Provides clear feedback on access status with specific reasons

## Modules
- **main.py**: Main application entry point that integrates all modules
- **student.py**: Handles user input collection
- **access.py**: Contains access verification logic
- **display.py**: Manages output formatting and display

## How to Run
1. Navigate to the week_11 directory
2. Run the following command:
   ```bash
   python main.py