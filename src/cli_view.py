# CLI View - Terminal output formatting for scheduling results


def print_results(algorithm_name, processes, gantt_chart, cpu_utilization):
    """
    Print scheduling results in a nicely formatted way to the terminal.
    
    Args:
        algorithm_name (str): Name of the scheduling algorithm
        processes (list): List of completed Process objects
        gantt_chart (list): List of tuples (process_id, start_time, end_time)
        cpu_utilization (float): CPU utilization percentage
    """
    # Print header with algorithm name
    print("\n" + "="*70)
    print(f"  {algorithm_name} SCHEDULING RESULTS")
    print("="*70)
    
    # Print Gantt Chart
    print("\nGantt Chart:")
    print_gantt_chart(gantt_chart)
    
    # Print process details table
    print("\nProcess Details:")
    print_process_table(processes)
    
    # Calculate and print average times
    print_average_times(processes)
    
    # Print CPU utilization
    print(f"\nCPU Utilization: {cpu_utilization:.2f}%")
    print("="*70 + "\n")


def print_gantt_chart(gantt_chart):
    """
    Print Gantt chart in format: [0]--P1--[5]--P2--[10]
    
    Args:
        gantt_chart (list): List of tuples (process_id, start_time, end_time)
    """
    if not gantt_chart:
        print("  (Empty)")
        return
    
    # Build the Gantt chart string
    gantt_str = ""
    
    for process_id, start_time, end_time in gantt_chart:
        # Add start time bracket
        gantt_str += f"[{start_time}]"
        
        # Add process ID with dashes
        gantt_str += f"--{process_id}--"
    
    # Add final end time bracket
    if gantt_chart:
        last_end_time = gantt_chart[-1][2]
        gantt_str += f"[{last_end_time}]"
    
    print(f"  {gantt_str}")


def print_process_table(processes):
    """
    Print a formatted table showing process scheduling metrics.
    
    Args:
        processes (list): List of Process objects with calculated times
    """
    # Table header
    print("  " + "-"*60)
    print(f"  | {'ID':<6} | {'Arrival':<8} | {'Burst':<6} | {'Finish':<7} | {'TAT':<6} | {'WT':<6} |")
    print("  " + "-"*60)
    
    # Sort processes by process ID for consistent display
    processes_sorted = sorted(processes, key=lambda p: p.process_id)
    
    # Print each process row
    for process in processes_sorted:
        print(f"  | {process.process_id:<6} | "
              f"{process.arrival_time:<8} | "
              f"{process.burst_time:<6} | "
              f"{process.finish_time:<7} | "
              f"{process.turnaround_time:<6} | "
              f"{process.waiting_time:<6} |")
    
    # Table footer
    print("  " + "-"*60)
    print("  Note: TAT = Turnaround Time, WT = Waiting Time")


def print_average_times(processes):
    """
    Calculate and print average turnaround time and waiting time.
    
    Args:
        processes (list): List of Process objects
    """
    if not processes:
        print("\n  No processes to calculate averages.")
        return
    
    # Calculate total turnaround time and waiting time
    total_turnaround = sum(p.turnaround_time for p in processes)
    total_waiting = sum(p.waiting_time for p in processes)
    
    # Calculate averages
    num_processes = len(processes)
    avg_turnaround = total_turnaround / num_processes
    avg_waiting = total_waiting / num_processes
    
    # Print averages
    print(f"\n  Average Turnaround Time: {avg_turnaround:.2f}")
    print(f"  Average Waiting Time: {avg_waiting:.2f}")


def calculate_cpu_utilization(gantt_chart):
    """
    Calculate CPU utilization percentage from Gantt chart.
    CPU Utilization = (Total CPU busy time / Total time) * 100
    
    Args:
        gantt_chart (list): List of tuples (process_id, start_time, end_time)
    
    Returns:
        float: CPU utilization percentage
    """
    if not gantt_chart:
        return 0.0
    
    # Calculate total time (from start to end)
    total_time = gantt_chart[-1][2] - gantt_chart[0][1]
    
    if total_time == 0:
        return 0.0
    
    # Calculate busy time (exclude IDLE periods)
    busy_time = 0
    for process_id, start_time, end_time in gantt_chart:
        if process_id != 'IDLE':
            busy_time += (end_time - start_time)
    
    # Calculate utilization percentage
    cpu_utilization = (busy_time / total_time) * 100
    
    return cpu_utilization


def get_average_waiting_time(processes):
    """
    Calculate average waiting time for a list of processes.
    
    Args:
        processes (list): List of Process objects
    
    Returns:
        float: Average waiting time
    """
    if not processes:
        return 0.0
    
    total_waiting = sum(p.waiting_time for p in processes)
    return total_waiting / len(processes)


def export_to_csv(results_dict, filename="results.csv"):
    """
    Export scheduling results to a CSV file with append mode.
    
    Args:
        results_dict (dict): Dictionary mapping algorithm names to (processes, avg_waiting_time)
        filename (str): Output CSV filename (default: "results.csv")
    """
    import csv
    import os
    from datetime import datetime
    
    try:
        # Check if file exists to determine if we need to write headers
        file_exists = os.path.exists(filename)
        
        # Show ASCII progress bar
        show_ascii_progress("Saving results")
        
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write header only if file doesn't exist
            if not file_exists:
                writer.writerow(['Timestamp', 'Algorithm', 'Process_ID', 'Arrival', 
                               'Burst', 'Priority', 'Finish', 'Turnaround', 'Waiting'])
            
            # Get current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Write data for each algorithm
            for algorithm_name, (processes, _) in results_dict.items():
                for process in sorted(processes, key=lambda p: p.process_id):
                    writer.writerow([
                        timestamp,
                        algorithm_name,
                        process.process_id,
                        process.arrival_time,
                        process.burst_time,
                        process.priority if hasattr(process, 'priority') else 'N/A',
                        process.finish_time,
                        process.turnaround_time,
                        process.waiting_time
                    ])
        
        print(f"\n✓ Results exported to {filename}")
        return True
    
    except Exception as e:
        print(f"\n✗ Error exporting to CSV: {e}")
        return False


def show_ascii_progress(message="Processing", duration=0.8):
    """
    Display an ASCII progress bar in the terminal.
    
    Args:
        message (str): Message to display
        duration (float): Animation duration in seconds
    """
    import sys
    import time
    
    total_bars = 10
    delay = duration / total_bars
    
    for i in range(total_bars + 1):
        filled = '█' * i
        empty = '░' * (total_bars - i)
        percent = (i / total_bars) * 100
        
        # Print progress bar on same line
        sys.stdout.write(f'\r{message}... [{filled}{empty}] {percent:.0f}%')
        sys.stdout.flush()
        
        time.sleep(delay)
    
    # Move to next line after completion
    sys.stdout.write('\n')
    sys.stdout.flush()

