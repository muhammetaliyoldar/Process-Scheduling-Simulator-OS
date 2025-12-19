CS305 - Operating Systems
Assignment: Process Scheduling Simulator
Student: Muhammet Ali Yoldar
ID: 200444035
Date: December 2024
=========================================================================

1. PROJECT OVERVIEW
=========================================================================
This project implements a CPU Process Scheduling Simulator that supports
four fundamental scheduling algorithms:

  - First-Come, First-Served (FCFS) - Non-preemptive
  - Shortest Job First (SJF) - Non-preemptive
  - Priority Scheduling - Non-preemptive
  - Round Robin (RR) - Preemptive

The simulator features a hybrid architecture with both Command-Line 
Interface (CLI) for batch processing and a Graphical User Interface (GUI)
for interactive visualization with Gantt charts.

2. REQUIREMENTS
=========================================================================
- Python 3.10 or higher
- No external dependencies required
- Uses only Python Standard Library (tkinter, sys, copy)
- No 'pip install' needed

3. HOW TO RUN
=========================================================================
The main.py file serves as the entry point for both modes.

A) GUI Mode (Interactive - Recommended for Visualization):
   
   Command:
   $ python main.py

   Features:
   - Browse and select input files using file dialog
   - Configure Time Quantum for Round Robin
   - Run any algorithm with a single button click
   - View color-coded Gantt charts
   - Analyze detailed metrics in table format

B) CLI Mode (Batch Processing):
   
   Command:
   $ python main.py data/input.txt

   This will automatically:
   - Parse the input file
   - Execute all 4 algorithms sequentially
   - Display Gantt charts, process tables, and statistics
   - Calculate average waiting time, turnaround time, and CPU utilization

4. INPUT FILE FORMAT
=========================================================================
Input files should be plain text (CSV format) with the following structure:

Process_ID,Arrival_Time,Burst_Time,Priority

Example:
P1,0,8,3
P2,1,4,1
P3,2,9,4
P4,3,5,2

Lines starting with # are treated as comments and ignored.

5. PROJECT STRUCTURE
=========================================================================
CS305_Scheduler/
│
├── main.py                # Entry point (mode selector)
├── requirements.txt       # Dependencies list
├── Makefile              # Quick run commands (Linux/Mac)
├── README.md             # GitHub documentation
├── README.txt            # This file
│
├── data/                 # Test input files
│   ├── input.txt         # Instructor's example dataset
│   ├── starvation.txt    # Priority starvation demonstration
│   ├── idle_test.txt     # CPU idle time testing
│   ├── ties.txt          # Tie-breaking scenarios
│   └── rr_heavy.txt      # Round Robin stress test
│
├── src/                  # Source code modules
│   ├── __init__.py       # Package initializer
│   ├── model.py          # Process class and data structures
│   ├── parser.py         # File I/O operations
│   ├── scheduler.py      # Core algorithm implementations
│   ├── cli_view.py       # Terminal output formatting
│   └── gui_view.py       # Tkinter GUI implementation
│
└── screenshots/          # Visual documentation
    ├── gui_main.png
    ├── gui_results.png
    ├── cli_output-FCFS.png
    ├── cli_output-SJF.png
    ├── cli_output-Priority.png
    └── cli_output-RR.png

6. FEATURES IMPLEMENTED
=========================================================================
✓ Four scheduling algorithms (FCFS, SJF, Priority, Round Robin)
✓ Gantt chart visualization (GUI: color-coded, CLI: text-based)
✓ Automatic calculation of:
  - Waiting Time
  - Turnaround Time
  - CPU Utilization
✓ Idle time handling
✓ Starvation demonstration (starvation.txt)
✓ Clean, modular, and well-documented code

7. ALGORITHM-SPECIFIC NOTES
=========================================================================
- FCFS: Simple queue-based scheduling, prone to convoy effect
- SJF: Minimizes average waiting time but can cause starvation
- Priority: Lower number = higher priority; can lead to starvation
- Round Robin: Default Time Quantum = 3 (configurable in GUI)

8. TEST FILES DESCRIPTION
=========================================================================
1. input.txt      - Standard test case from assignment specifications
2. starvation.txt - Demonstrates priority scheduling starvation problem
3. idle_test.txt  - Tests CPU idle period handling with arrival gaps
4. ties.txt       - Tests tie-breaking rules when processes arrive together
5. rr_heavy.txt   - Stress tests Round Robin with various burst times

9. KNOWN LIMITATIONS
=========================================================================
- All algorithms assume CPU-bound processes
- No I/O burst modeling
- Priority aging mechanism not implemented
- Context switch overhead not considered in Round Robin

10. CONTACT INFORMATION
=========================================================================
Student: Muhammet Ali Yoldar
Student ID: 200444035
Course: CS305 - Operating Systems
Institution: Türk Hava Kurumu University

=========================================================================
Thank you for reviewing this project!
=========================================================================