CS305 - Operating Systems
Assignment: Process Scheduling Simulator
Student: Muhammet Ali Yoldar
Student ID: 200444035
Date: December 2024
=========================================================================

1. PROJECT OVERVIEW
=========================================================================
This project implements a comprehensive CPU Process Scheduling Simulator
supporting four fundamental scheduling algorithms with advanced features
including intelligent performance analysis and automated reporting.

Supported Algorithms:
  - First-Come, First-Served (FCFS) - Non-preemptive
  - Shortest Job First (SJF) - Non-preemptive
  - Priority Scheduling - Non-preemptive
  - Round Robin (RR) - Preemptive

The simulator features a hybrid architecture combining both Command-Line 
Interface (CLI) for batch processing and automation, and a Graphical User
Interface (GUI) for interactive visualization with dynamic Gantt charts.

2. REQUIREMENTS
=========================================================================
- Python 3.10 or higher
- No external dependencies required
- Uses only Python Standard Library (tkinter, sys, copy, csv, logging)
- No 'pip install' needed
- Cross-platform compatible (Windows, macOS, Linux)

3. HOW TO RUN
=========================================================================
The main.py file serves as the entry point for both operational modes.

A) GUI Mode (Interactive - Recommended for Visualization):
   
   Command:
   $ python main.py

   Features:
   - File browser for input selection
   - Configurable Time Quantum for Round Robin
   - One-click algorithm execution with visual feedback
   - Color-coded Gantt chart visualization
   - Real-time performance metrics
   - Active button state tracking
   - Progress bar animations
   - CSV export functionality

B) CLI Mode (Batch Processing & Automation):
   
   Basic Usage:
   $ python main.py data/processes.txt
   
   Advanced Usage (Custom Time Quantum):
   $ python main.py data/processes.txt 5
   
   This will automatically:
   - Parse the input file
   - Execute all 4 algorithms sequentially
   - Display ASCII Gantt charts and process tables
   - Calculate average waiting time, turnaround time, and CPU utilization
   - Perform smart analysis to identify optimal algorithm
   - Export results to CSV with timestamp
   - Generate execution logs

4. UPDATED FEATURES (Enhancement Phase)
=========================================================================
The project has been enhanced with production-grade engineering features:

✓ System Logging (simulation.log)
  - Complete execution traceability
  - Timestamped event recording
  - Error tracking and debugging support
  - Industry-standard logging practices

✓ CSV Export (results.csv)
  - Automated result persistence
  - Append mode for historical tracking
  - Timestamp and priority metadata
  - Ready for external analysis tools

✓ Smart Analysis Engine
  - Automatic algorithm comparison
  - Winner detection based on Average Waiting Time
  - Visual highlighting with stars
  - Performance recommendation system

✓ CLI Enhancements
  - Configurable Time Quantum via command-line arguments
  - ASCII progress bar animations
  - Enhanced visual feedback

✓ GUI Enhancements
  - Active button state tracking
  - Progress bar with status messages
  - Highlighted key metrics
  - One-click CSV export

5. INPUT FILE FORMAT
=========================================================================
Input files should be plain text (CSV format) with the following structure:

Process_ID,Arrival_Time,Burst_Time,Priority

Example:
P1,0,8,3
P2,1,4,1
P3,2,9,4
P4,3,5,2

Lines starting with # are treated as comments and ignored.
Lower priority number indicates higher priority.

6. PROJECT STRUCTURE
=========================================================================
CS305_Scheduler/
│
├── main.py                # Entry point (mode selector)
├── requirements.txt       # Dependencies list
├── Makefile              # Quick run commands (Linux/Mac)
├── README.md             # GitHub documentation
├── README.txt            # This file
├── simulation.log        # Auto-generated execution log
├── results.csv           # Exported results (append mode)
│
├── data/                 # Test input files
│   ├── processes.txt     # Standard dataset
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
│   ├── cli_view.py       # Terminal output & CSV export
│   └── gui_view.py       # Tkinter GUI implementation
│
└── screenshots/          # Visual documentation
    ├── gui_final.png
    ├── cli_start.png
    ├── cli_output-FCFS.png
    ├── cli_output-SJF.png
    ├── cli_output-Priority.png
    ├── cli_output-RR(TQ=5).png
    ├── cli_final.png
    ├── log_preview.png
    └── csv_preview.png

7. FEATURES IMPLEMENTED
=========================================================================
✓ Four scheduling algorithms (FCFS, SJF, Priority, Round Robin)
✓ Dual interface: CLI + GUI
✓ Gantt chart visualization (GUI: color-coded, CLI: ASCII-based)
✓ Automatic calculation of:
  - Waiting Time
  - Turnaround Time
  - CPU Utilization
✓ Idle time handling
✓ Starvation demonstration (starvation.txt)
✓ Configurable Time Quantum (CLI argument or GUI input)
✓ Smart recommendation engine
✓ Production-grade logging system
✓ Automated CSV export with append mode
✓ Active UI state tracking
✓ Progress animations and visual feedback
✓ Clean, modular, and well-documented code

8. ALGORITHM-SPECIFIC NOTES
=========================================================================
- FCFS: Simple queue-based scheduling, prone to convoy effect
- SJF: Minimizes average waiting time but can cause starvation
- Priority: Lower number = higher priority; demonstrates starvation
- Round Robin: Default Time Quantum = 3 (configurable via CLI/GUI)

ASSUMPTIONS:
1. Context-switching overhead is zero.
2. Tie-breaking: FCFS (Arrival Time) is used when burst times or 
   priorities are equal.

9. TEST FILES DESCRIPTION
=========================================================================
1. processes.txt  - Standard test case from assignment specifications
2. starvation.txt - Demonstrates priority scheduling starvation problem
3. idle_test.txt  - Tests CPU idle period handling with arrival gaps
4. ties.txt       - Tests tie-breaking rules when processes arrive together
5. rr_heavy.txt   - Stress tests Round Robin with various burst times

10. HOW TO VERIFY STARVATION
=========================================================================
To demonstrate the starvation problem in Priority Scheduling:

Command:
$ python main.py data/starvation.txt

The starvation.txt file contains low-priority processes that arrive early
but get delayed indefinitely by continuously arriving high-priority processes.
Observe how low-priority processes have very high waiting times.

11. GENERATED ARTIFACTS
=========================================================================
Running the simulator generates the following files:

- simulation.log     : Timestamped execution log for debugging
- results.csv        : Exported results with historical tracking
- gui_results.csv    : GUI-specific export (when using export button)

All artifacts use UTF-8 encoding for universal compatibility.

12. ENGINEERING BEST PRACTICES
=========================================================================
This project demonstrates industry-standard software engineering practices:

✓ Modular Architecture - Clean separation of concerns
✓ MVC Pattern - Model, View, Controller design
✓ Production Logging - Comprehensive event tracking
✓ Data Persistence - Historical result tracking
✓ Error Handling - Robust exception management
✓ Code Documentation - Detailed docstrings
✓ User Experience - Progress feedback and visual states
✓ Zero Dependencies - Maximum portability

13. TESTING & VALIDATION
=========================================================================
The project has been extensively tested with:
- Multiple input datasets (5 test files)
- Various Time Quantum values (1-10)
- Edge cases (idle periods, ties, starvation)
- Both operational modes (CLI and GUI)
- Cross-algorithm comparison
- Export functionality validation

14. KNOWN LIMITATIONS
=========================================================================
- All algorithms assume CPU-bound processes
- No I/O burst modeling
- Priority aging mechanism not implemented
- Context switch overhead not considered

15. CONTACT INFORMATION
=========================================================================
Student: Muhammet Ali Yoldar
Student ID: 200444035
Course: CS305 - Operating Systems
Institution: Türk Hava Kurumu University

=========================================================================
Thank you for reviewing this project!
=========================================================================