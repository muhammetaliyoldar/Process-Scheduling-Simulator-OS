# Process class to represent a process in the scheduling simulator

class Process:
    """
    Represents a single process with all necessary scheduling attributes.
    """
    
    def __init__(self, process_id, arrival_time, burst_time, priority):
        """
        Initialize a new process with basic attributes.
        
        Args:
            process_id (str): Unique identifier for the process (e.g., "P1", "P2")
            arrival_time (int): Time when the process arrives in the ready queue
            burst_time (int): Total CPU time required by the process
            priority (int): Priority level of the process (lower number = higher priority)
        """
        # Basic process attributes from input
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        
        # Scheduling calculation attributes (initialized to default values)
        self.remaining_time = burst_time  # Initialize remaining time to full burst time
        self.start_time = None  # Time when process first gets CPU (None until scheduled)
        self.finish_time = None  # Time when process completes execution
        self.turnaround_time = 0  # Total time from arrival to completion
        self.waiting_time = 0  # Total time spent waiting in ready queue
    
    def __repr__(self):
        """
        String representation of the process for debugging purposes.
        
        Returns:
            str: Formatted string showing process details
        """
        return f"Process({self.process_id}, AT={self.arrival_time}, BT={self.burst_time}, P={self.priority})"
