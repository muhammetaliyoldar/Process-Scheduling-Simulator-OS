# Scheduling algorithms implementation
# This file contains the core logic for 4 different CPU scheduling algorithms

# ASSUMPTIONS:
# 1. Context-switching overhead is zero.
# 2. Tie-breaking: FCFS (Arrival Time) is used when burst times or priorities are equal.

import copy


def run_fcfs(processes):
    """
    First Come First Served (FCFS) Scheduling Algorithm
    Non-preemptive: Once a process starts, it runs to completion
    
    Args:
        processes (list): List of Process objects
    
    Returns:
        tuple: (gantt_chart, processes) where gantt_chart shows execution timeline
    """
    # Make a copy to avoid modifying original list
    processes = copy.deepcopy(processes)
    
    # Sort processes by arrival time (first come first served)
    processes.sort(key=lambda p: p.arrival_time)
    
    # Initialize variables
    current_time = 0
    gantt_chart = []  # Will store (process_id, start_time, end_time)
    completed = []  # Track completed processes
    
    # Process each job in order
    for process in processes:
        # If CPU is idle (current time is before process arrival), add IDLE time
        if current_time < process.arrival_time:
            gantt_chart.append(('IDLE', current_time, process.arrival_time))
            current_time = process.arrival_time
        
        # Record start time (first time this process gets CPU)
        process.start_time = current_time
        
        # Process runs for its full burst time
        current_time += process.burst_time
        
        # Record finish time
        process.finish_time = current_time
        
        # Calculate turnaround time: finish_time - arrival_time
        process.turnaround_time = process.finish_time - process.arrival_time
        
        # Calculate waiting time: turnaround_time - burst_time
        process.waiting_time = process.turnaround_time - process.burst_time
        
        # Add to Gantt chart
        gantt_chart.append((process.process_id, process.start_time, process.finish_time))
        completed.append(process)
    
    return gantt_chart, completed


def run_sjf(processes):
    """
    Shortest Job First (SJF) Scheduling Algorithm
    Non-preemptive: Pick the process with shortest burst time among arrived processes
    
    Args:
        processes (list): List of Process objects
    
    Returns:
        tuple: (gantt_chart, processes) where gantt_chart shows execution timeline
    """
    # Make a copy to avoid modifying original list
    processes = copy.deepcopy(processes)
    
    # Sort by arrival time initially
    processes.sort(key=lambda p: p.arrival_time)
    
    # Initialize variables
    current_time = 0
    gantt_chart = []
    completed = []
    remaining = processes.copy()  # Processes not yet completed
    
    # Continue until all processes are completed
    while remaining:
        # Find all processes that have arrived by current_time
        ready_queue = [p for p in remaining if p.arrival_time <= current_time]
        
        # Check if ready queue is empty
        if not ready_queue:
            # CPU is idle, jump to next process arrival
            next_arrival = min(p.arrival_time for p in remaining)
            gantt_chart.append(('IDLE', current_time, next_arrival))
            current_time = next_arrival
            continue
        
        # Select process with shortest burst time (SJF logic)
        shortest_job = min(ready_queue, key=lambda p: p.burst_time)
        
        # Record start time
        shortest_job.start_time = current_time
        
        # Process runs to completion
        current_time += shortest_job.burst_time
        
        # Record finish time
        shortest_job.finish_time = current_time
        
        # Calculate turnaround time and waiting time
        shortest_job.turnaround_time = shortest_job.finish_time - shortest_job.arrival_time
        shortest_job.waiting_time = shortest_job.turnaround_time - shortest_job.burst_time
        
        # Add to Gantt chart
        gantt_chart.append((shortest_job.process_id, shortest_job.start_time, shortest_job.finish_time))
        
        # Move from remaining to completed
        completed.append(shortest_job)
        remaining.remove(shortest_job)
    
    return gantt_chart, completed


def run_priority(processes):
    """
    Priority Scheduling Algorithm
    Non-preemptive: Pick the process with highest priority (lowest priority number)
    
    Args:
        processes (list): List of Process objects
    
    Returns:
        tuple: (gantt_chart, processes) where gantt_chart shows execution timeline
    """
    # Make a copy to avoid modifying original list
    processes = copy.deepcopy(processes)
    
    # Sort by arrival time initially
    processes.sort(key=lambda p: p.arrival_time)
    
    # Initialize variables
    current_time = 0
    gantt_chart = []
    completed = []
    remaining = processes.copy()
    
    # Continue until all processes are completed
    while remaining:
        # Find all processes that have arrived by current_time
        ready_queue = [p for p in remaining if p.arrival_time <= current_time]
        
        # Check if ready queue is empty
        if not ready_queue:
            # CPU is idle, jump to next process arrival
            next_arrival = min(p.arrival_time for p in remaining)
            gantt_chart.append(('IDLE', current_time, next_arrival))
            current_time = next_arrival
            continue
        
        # Select process with highest priority (lowest priority number)
        highest_priority = min(ready_queue, key=lambda p: p.priority)
        
        # Record start time
        highest_priority.start_time = current_time
        
        # Process runs to completion
        current_time += highest_priority.burst_time
        
        # Record finish time
        highest_priority.finish_time = current_time
        
        # Calculate turnaround time and waiting time
        highest_priority.turnaround_time = highest_priority.finish_time - highest_priority.arrival_time
        highest_priority.waiting_time = highest_priority.turnaround_time - highest_priority.burst_time
        
        # Add to Gantt chart
        gantt_chart.append((highest_priority.process_id, highest_priority.start_time, highest_priority.finish_time))
        
        # Move from remaining to completed
        completed.append(highest_priority)
        remaining.remove(highest_priority)
    
    return gantt_chart, completed


def run_rr(processes, time_quantum):
    """
    Round Robin (RR) Scheduling Algorithm
    Preemptive: Each process gets a time slice (quantum), then goes to back of queue
    
    Args:
        processes (list): List of Process objects
        time_quantum (int): Time slice for each process
    
    Returns:
        tuple: (gantt_chart, processes) where gantt_chart shows execution timeline
    """
    # Make a copy to avoid modifying original list
    processes = copy.deepcopy(processes)
    
    # Sort by arrival time
    processes.sort(key=lambda p: p.arrival_time)
    
    # Initialize variables
    current_time = 0
    gantt_chart = []
    ready_queue = []  # Queue of processes ready to execute
    completed = []
    remaining = processes.copy()
    
    # Continue until all processes are completed
    while remaining or ready_queue:
        # Add all processes that have arrived by current_time to ready queue
        arrived = [p for p in remaining if p.arrival_time <= current_time]
        for process in arrived:
            ready_queue.append(process)
            remaining.remove(process)
        
        # Check if ready queue is empty
        if not ready_queue:
            # CPU is idle, jump to next process arrival
            if remaining:
                next_arrival = min(p.arrival_time for p in remaining)
                gantt_chart.append(('IDLE', current_time, next_arrival))
                current_time = next_arrival
            continue
        
        # Get the first process from ready queue
        current_process = ready_queue.pop(0)
        
        # Record start time (only first time it gets CPU)
        if current_process.start_time is None:
            current_process.start_time = current_time
        
        # Calculate how long this process will run
        execution_time = min(time_quantum, current_process.remaining_time)
        
        # Execute the process for execution_time
        start = current_time
        current_time += execution_time
        current_process.remaining_time -= execution_time
        
        # Add to Gantt chart
        gantt_chart.append((current_process.process_id, start, current_time))
        
        # Check if new processes arrived during execution
        arrived = [p for p in remaining if p.arrival_time <= current_time]
        for process in arrived:
            ready_queue.append(process)
            remaining.remove(process)
        
        # Check if process is complete
        if current_process.remaining_time == 0:
            # Process finished
            current_process.finish_time = current_time
            current_process.turnaround_time = current_process.finish_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed.append(current_process)
        else:
            # Process not finished, add back to end of ready queue
            ready_queue.append(current_process)
    
    return gantt_chart, completed
