# File parser to read process data from input files

from src.model import Process


def parse_input(file_path):
    """
    Read and parse process data from a text file.
    
    Expected file format (CSV):
    process_id,arrival_time,burst_time,priority
    P1,0,5,2
    P2,1,3,1
    
    Args:
        file_path (str): Path to the input file
    
    Returns:
        list: List of Process objects created from the file data
    """
    processes = []  # Initialize empty list to store processes
    
    try:
        # Try to open and read the file
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            
            # Process each line
            for line in lines:
                # Remove whitespace and skip empty lines or comments
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                # Split the line by comma to get individual values
                parts = line.split(',')
                
                # Make sure we have exactly 4 values
                if len(parts) != 4:
                    print(f"Warning: Skipping invalid line: {line}")
                    continue
                
                # Extract values from the split parts
                process_id = parts[0].strip()
                arrival_time = int(parts[1].strip())
                burst_time = int(parts[2].strip())
                priority = int(parts[3].strip())
                
                # Create a new Process object and add to list
                process = Process(process_id, arrival_time, burst_time, priority)
                processes.append(process)
    
    except FileNotFoundError:
        # Handle case when file doesn't exist
        print(f"Error: File '{file_path}' not found!")
        return []
    
    except ValueError as e:
        # Handle case when conversion to int fails
        print(f"Error: Invalid data format in file. {e}")
        return []
    
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error reading file: {e}")
        return []
    
    # Return the list of processes
    return processes
