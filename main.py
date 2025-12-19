"""
CS305 Operating Systems - Process Scheduling Simulator
Student: Muhammet Ali Yoldar
Course: CS305 - Operating Systems

Main entry point for the scheduling simulator.
Supports both CLI and GUI modes.
"""

import sys
import logging
from src.parser import parse_input
from src.scheduler import run_fcfs, run_sjf, run_priority, run_rr
from src.cli_view import print_results, calculate_cpu_utilization, get_average_waiting_time, export_to_csv
from src.gui_view import run_gui

# Configure logging
logging.basicConfig(
    filename='simulation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def run_cli_mode(file_path, time_quantum=3):
    """
    Run the simulator in CLI (Command Line Interface) mode.
    Executes all 4 scheduling algorithms and displays results.
    
    Args:
        file_path (str): Path to the input file
        time_quantum (int): Time Quantum for Round Robin (default: 3)
    """
    logging.info("CLI mode started")
    print("\n" + "="*70)
    print("  CS305 PROCESS SCHEDULING SIMULATOR - CLI MODE")
    print("="*70)
    
    # Parse input file
    print(f"\nReading processes from: {file_path}")
    logging.info(f"Reading input file: {file_path}")
    processes = parse_input(file_path)
    
    if not processes:
        logging.error("No processes loaded from input file")
        print("Error: No processes loaded. Exiting.")
        return
    
    logging.info(f"Input file parsed: {len(processes)} processes loaded")
    print(f"Successfully loaded {len(processes)} processes.\n")
    
    # Dictionary to store results for comparison and CSV export
    results = {}
    
    # Run all 4 scheduling algorithms
    
    # 1. First Come First Served (FCFS)
    logging.info("Algorithm FCFS execution started")
    gantt_chart, completed = run_fcfs(processes)
    cpu_util = calculate_cpu_utilization(gantt_chart)
    avg_wt = get_average_waiting_time(completed)
    results['FCFS'] = (completed, avg_wt)
    print_results("FCFS (First Come First Served)", completed, gantt_chart, cpu_util)
    logging.info(f"Algorithm FCFS execution completed - Avg WT: {avg_wt:.2f}")
    
    # 2. Shortest Job First (SJF)
    logging.info("Algorithm SJF execution started")
    gantt_chart, completed = run_sjf(processes)
    cpu_util = calculate_cpu_utilization(gantt_chart)
    avg_wt = get_average_waiting_time(completed)
    results['SJF'] = (completed, avg_wt)
    print_results("SJF (Shortest Job First)", completed, gantt_chart, cpu_util)
    logging.info(f"Algorithm SJF execution completed - Avg WT: {avg_wt:.2f}")
    
    # 3. Priority Scheduling
    logging.info("Algorithm Priority execution started")
    gantt_chart, completed = run_priority(processes)
    cpu_util = calculate_cpu_utilization(gantt_chart)
    avg_wt = get_average_waiting_time(completed)
    results['Priority'] = (completed, avg_wt)
    print_results("Priority Scheduling", completed, gantt_chart, cpu_util)
    logging.info(f"Algorithm Priority execution completed - Avg WT: {avg_wt:.2f}")
    
    # 4. Round Robin (RR)
    logging.info(f"Algorithm Round Robin execution started (TQ={time_quantum})")
    gantt_chart, completed = run_rr(processes, time_quantum)
    cpu_util = calculate_cpu_utilization(gantt_chart)
    avg_wt = get_average_waiting_time(completed)
    results['Round Robin'] = (completed, avg_wt)
    print_results(f"Round Robin (Time Quantum = {time_quantum})", completed, gantt_chart, cpu_util)
    logging.info(f"Algorithm Round Robin execution completed - Avg WT: {avg_wt:.2f}")
    
    print("\n" + "="*70)
    print("  All algorithms completed successfully!")
    print("="*70)
    
    # Smart Recommendation: Find the best algorithm
    print_smart_recommendation(results)
    
    # Export results to CSV
    logging.info("Exporting results to CSV")
    export_to_csv(results, filename="results.csv")
    logging.info("Results exported successfully")
    
    print()




def print_smart_recommendation(results):
    """
    Analyze and recommend the best algorithm based on average waiting time.
    
    Args:
        results (dict): Dictionary mapping algorithm names to (processes, avg_waiting_time)
    """
    if not results:
        return
    
    print("\n" + "="*70)
    print("  SMART RECOMMENDATION - ALGORITHM COMPARISON")
    print("="*70)
    
    # Display all algorithms with their average waiting times
    print("\nAverage Waiting Times:")
    for algo_name, (_, avg_wt) in results.items():
        print(f"  • {algo_name:<20} : {avg_wt:.2f} time units")
    
    # Find the best algorithm (lowest average waiting time)
    best_algorithm = min(results.items(), key=lambda x: x[1][1])
    best_name = best_algorithm[0]
    best_avg_wt = best_algorithm[1][1]
    
    print("\n" + "-"*70)
    print("  " + "⭐" * 30)
    print(f"  *** WINNER ALGORITHM: {best_name} ***")
    print(f"      Most efficient for this workload!")
    print(f"      Lowest Average Waiting Time: {best_avg_wt:.2f} time units")
    print("  " + "⭐" * 30)
    print("-"*70)
    
    logging.info(f"Best algorithm: {best_name} with avg WT: {best_avg_wt:.2f}")


def main():
    """
    Main function - Entry point of the application.
    Determines whether to run in CLI or GUI mode based on command-line arguments.
    """
    logging.info("Application started")
    # Check if user provided command-line arguments
    if len(sys.argv) > 1:
        # CLI Mode: User provided input file path and optional time quantum
        # Usage: python main.py data/processes.txt [time_quantum]
        # Example: python main.py data/processes.txt 4
        file_path = sys.argv[1]
        
        # Check if time quantum is provided as second argument
        if len(sys.argv) > 2:
            try:
                time_quantum = int(sys.argv[2])
            except ValueError:
                print("Error: Time Quantum must be an integer. Using default value 3.")
                time_quantum = 3
        else:
            time_quantum = 3  # Default value
        
        run_cli_mode(file_path, time_quantum)
    else:
        # GUI Mode: No arguments provided
        # Usage: python main.py
        print("No command-line arguments detected.")
        print("Launching GUI mode...\n")
        run_gui()


if __name__ == "__main__":
    main()
