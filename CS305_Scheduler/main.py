"""
CS305 Operating Systems - Process Scheduling Simulator
Student: Muhammet Ali Yoldar
Course: CS305 - Operating Systems

Main entry point for the scheduling simulator.
Supports both CLI and GUI modes.
"""

import sys
from src.parser import parse_input
from src.scheduler import run_fcfs, run_sjf, run_priority, run_rr
from src.cli_view import print_results, calculate_cpu_utilization
from src.gui_view import run_gui


def run_cli_mode(file_path):
    """
    Run the simulator in CLI (Command Line Interface) mode.
    Executes all 4 scheduling algorithms and displays results.
    
    Args:
        file_path (str): Path to the input file
    """
    print("\n" + "="*70)
    print("  CS305 PROCESS SCHEDULING SIMULATOR - CLI MODE")
    print("="*70)
    
    # Parse input file
    print(f"\nReading processes from: {file_path}")
    processes = parse_input(file_path)
    
    if not processes:
        print("Error: No processes loaded. Exiting.")
        return
    
    print(f"Successfully loaded {len(processes)} processes.\n")
    
    # Default time quantum for Round Robin
    TIME_QUANTUM = 3
    
    # Run all 4 scheduling algorithms
    
    # 1. First Come First Served (FCFS)
    gantt_chart, completed = run_fcfs(processes)
    cpu_util = calculate_cpu_utilization(gantt_chart)
    print_results("FCFS (First Come First Served)", completed, gantt_chart, cpu_util)
    
    # 2. Shortest Job First (SJF)
    gantt_chart, completed = run_sjf(processes)
    cpu_util = calculate_cpu_utilization(gantt_chart)
    print_results("SJF (Shortest Job First)", completed, gantt_chart, cpu_util)
    
    # 3. Priority Scheduling
    gantt_chart, completed = run_priority(processes)
    cpu_util = calculate_cpu_utilization(gantt_chart)
    print_results("Priority Scheduling", completed, gantt_chart, cpu_util)
    
    # 4. Round Robin (RR)
    gantt_chart, completed = run_rr(processes, TIME_QUANTUM)
    cpu_util = calculate_cpu_utilization(gantt_chart)
    print_results(f"Round Robin (Time Quantum = {TIME_QUANTUM})", completed, gantt_chart, cpu_util)
    
    print("\n" + "="*70)
    print("  All algorithms completed successfully!")
    print("="*70 + "\n")


def main():
    """
    Main function - Entry point of the application.
    Determines whether to run in CLI or GUI mode based on command-line arguments.
    """
    # Check if user provided command-line arguments
    if len(sys.argv) > 1:
        # CLI Mode: User provided input file path as argument
        # Usage: python main.py data/input.txt
        file_path = sys.argv[1]
        run_cli_mode(file_path)
    else:
        # GUI Mode: No arguments provided
        # Usage: python main.py
        print("No command-line arguments detected.")
        print("Launching GUI mode...\n")
        run_gui()


if __name__ == "__main__":
    main()
