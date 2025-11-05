# Banker's Algorithm Implementation
## CECS 326 - Operating Systems Project 3

### Team Members
- Ryan Tran
- Phu Quach

### Project Description
This project implements the Banker's Algorithm for deadlock avoidance in resource allocation. The program simulates a system with 5 processes and 3 types of resources, demonstrating safe state detection and resource request handling.

### How to Compile and Run

#### Option 1: Run directly with Python
```bash
python bankers_algorithm.py
```
or
```bash
python3 bankers_algorithm.py
```

#### Option 2: Make the file executable (Linux/Mac)
```bash
chmod +x bankers_algorithm.py
./bankers_algorithm.py
```

### Program Features

The program provides an interactive menu with the following options:

1. **Display current system state** - Shows the current Available, Maximum, Allocation, and Need matrices
2. **Find safe sequence** - Runs the safety algorithm to find a safe execution sequence
3. **Request resources** - Allows a process to request resources (with safety checking)
4. **Run test cases** - Automatically runs the three test cases from the project specification
5. **Reset system** - Resets all matrices to their initial values
6. **Exit** - Exits the program



