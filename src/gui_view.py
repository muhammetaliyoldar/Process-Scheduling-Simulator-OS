# GUI View - Tkinter-based graphical interface for the scheduler

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from src.parser import parse_input
from src.scheduler import run_fcfs, run_sjf, run_priority, run_rr
from src.cli_view import calculate_cpu_utilization


class SchedulerApp:
    """
    Main GUI application for Process Scheduling Simulator.
    Uses tkinter for graphical interface.
    """
    
    def __init__(self, root):
        """
        Initialize the GUI application.
        
        Args:
            root: tkinter root window
        """
        self.root = root
        self.root.title("CS305 Process Scheduling Simulator")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Variables
        self.file_path = None
        self.processes = []
        self.time_quantum = tk.IntVar(value=3)  # Default time quantum
        
        # Colors for different processes in Gantt chart
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', 
                       '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E2']
        
        # Create GUI components
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout all GUI components."""
        
        # ===== TOP SECTION: File Selection and Time Quantum =====
        top_frame = tk.Frame(self.root, bg="#2C3E50", pady=15)
        top_frame.pack(fill=tk.X)
        
        # File selection button
        self.btn_select_file = tk.Button(
            top_frame, 
            text="Select Input File", 
            command=self.select_file,
            bg="#3498DB",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        self.btn_select_file.pack(side=tk.LEFT, padx=10)
        
        # File path label
        self.lbl_file_path = tk.Label(
            top_frame, 
            text="No file selected", 
            bg="#2C3E50",
            fg="white",
            font=("Arial", 9)
        )
        self.lbl_file_path.pack(side=tk.LEFT, padx=10)
        
        # Time Quantum input
        tk.Label(
            top_frame, 
            text="Time Quantum:", 
            bg="#2C3E50",
            fg="white",
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(40, 5))
        
        self.entry_quantum = tk.Entry(
            top_frame, 
            textvariable=self.time_quantum,
            width=5,
            font=("Arial", 10)
        )
        self.entry_quantum.pack(side=tk.LEFT)
        
        # ===== MIDDLE SECTION: Algorithm Buttons =====
        btn_frame = tk.Frame(self.root, bg="#ECF0F1", pady=15)
        btn_frame.pack(fill=tk.X)
        
        # Create 4 algorithm buttons
        algorithms = [
            ("FCFS", self.run_fcfs, "#27AE60"),
            ("SJF", self.run_sjf, "#E67E22"),
            ("Priority", self.run_priority, "#8E44AD"),
            ("Round Robin", self.run_rr, "#C0392B")
        ]
        
        for name, command, color in algorithms:
            btn = tk.Button(
                btn_frame,
                text=name,
                command=command,
                bg=color,
                fg="white",
                font=("Arial", 11, "bold"),
                width=12,
                height=2
            )
            btn.pack(side=tk.LEFT, padx=15, expand=True)
        
        # ===== BOTTOM SECTION: Results Display =====
        results_frame = tk.Frame(self.root, bg="white")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Gantt Chart Canvas
        tk.Label(
            results_frame, 
            text="Gantt Chart:", 
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(anchor=tk.W, pady=(5, 0))
        
        self.canvas = tk.Canvas(
            results_frame, 
            height=100, 
            bg="white",
            highlightthickness=1,
            highlightbackground="#BDC3C7"
        )
        self.canvas.pack(fill=tk.X, pady=5)
        
        # Process Details Table
        tk.Label(
            results_frame, 
            text="Process Details:", 
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(anchor=tk.W, pady=(10, 0))
        
        # Create Treeview for table
        columns = ("ID", "Arrival", "Burst", "Finish", "Turnaround", "Waiting")
        self.tree = ttk.Treeview(
            results_frame, 
            columns=columns, 
            show="headings",
            height=8
        )
        
        # Define column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130, anchor=tk.CENTER)
        
        self.tree.pack(fill=tk.BOTH, pady=5)
        
        # Statistics Labels
        stats_frame = tk.Frame(results_frame, bg="white")
        stats_frame.pack(fill=tk.X, pady=10)
        
        self.lbl_avg_turnaround = tk.Label(
            stats_frame,
            text="Average Turnaround Time: --",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#27AE60"
        )
        self.lbl_avg_turnaround.pack(side=tk.LEFT, padx=20)
        
        self.lbl_avg_waiting = tk.Label(
            stats_frame,
            text="Average Waiting Time: --",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#E67E22"
        )
        self.lbl_avg_waiting.pack(side=tk.LEFT, padx=20)
        
        self.lbl_cpu_util = tk.Label(
            stats_frame,
            text="CPU Utilization: --",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#3498DB"
        )
        self.lbl_cpu_util.pack(side=tk.LEFT, padx=20)
    
    def select_file(self):
        """Open file dialog to select input file."""
        file_path = filedialog.askopenfilename(
            title="Select Input File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if file_path:
            self.file_path = file_path
            # Show shortened path if too long
            display_path = file_path if len(file_path) < 50 else "..." + file_path[-47:]
            self.lbl_file_path.config(text=display_path)
            
            # Parse the file
            self.processes = parse_input(file_path)
            if self.processes:
                messagebox.showinfo("Success", f"Loaded {len(self.processes)} processes!")
            else:
                messagebox.showerror("Error", "Failed to load processes from file.")
    
    def check_file_loaded(self):
        """Check if a file has been loaded. Show error if not."""
        if not self.file_path or not self.processes:
            messagebox.showerror("Error", "Please select an input file first!")
            return False
        return True
    
    def run_fcfs(self):
        """Run FCFS algorithm and display results."""
        if not self.check_file_loaded():
            return
        
        gantt_chart, completed = run_fcfs(self.processes)
        self.display_results("FCFS", completed, gantt_chart)
    
    def run_sjf(self):
        """Run SJF algorithm and display results."""
        if not self.check_file_loaded():
            return
        
        gantt_chart, completed = run_sjf(self.processes)
        self.display_results("SJF", completed, gantt_chart)
    
    def run_priority(self):
        """Run Priority algorithm and display results."""
        if not self.check_file_loaded():
            return
        
        gantt_chart, completed = run_priority(self.processes)
        self.display_results("Priority", completed, gantt_chart)
    
    def run_rr(self):
        """Run Round Robin algorithm and display results."""
        if not self.check_file_loaded():
            return
        
        # Get time quantum value
        try:
            quantum = self.time_quantum.get()
            if quantum <= 0:
                messagebox.showerror("Error", "Time quantum must be greater than 0!")
                return
        except:
            messagebox.showerror("Error", "Invalid time quantum value!")
            return
        
        gantt_chart, completed = run_rr(self.processes, quantum)
        self.display_results(f"Round Robin (Q={quantum})", completed, gantt_chart)
    
    def display_results(self, algorithm_name, processes, gantt_chart):
        """
        Display scheduling results in the GUI.
        
        Args:
            algorithm_name (str): Name of the algorithm
            processes (list): List of completed processes
            gantt_chart (list): Gantt chart data
        """
        # Clear previous results
        self.canvas.delete("all")
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Draw Gantt Chart
        self.draw_gantt_chart(gantt_chart)
        
        # Populate table
        processes_sorted = sorted(processes, key=lambda p: p.process_id)
        for process in processes_sorted:
            self.tree.insert("", tk.END, values=(
                process.process_id,
                process.arrival_time,
                process.burst_time,
                process.finish_time,
                process.turnaround_time,
                process.waiting_time
            ))
        
        # Calculate and display statistics
        avg_turnaround = sum(p.turnaround_time for p in processes) / len(processes)
        avg_waiting = sum(p.waiting_time for p in processes) / len(processes)
        cpu_util = calculate_cpu_utilization(gantt_chart)
        
        self.lbl_avg_turnaround.config(text=f"Average Turnaround Time: {avg_turnaround:.2f}")
        self.lbl_avg_waiting.config(text=f"Average Waiting Time: {avg_waiting:.2f}")
        self.lbl_cpu_util.config(text=f"CPU Utilization: {cpu_util:.2f}%")
    
    def draw_gantt_chart(self, gantt_chart):
        """
        Draw Gantt chart on canvas with colored rectangles.
        
        Args:
            gantt_chart (list): List of (process_id, start_time, end_time)
        """
        if not gantt_chart:
            return
        
        # Calculate canvas width and scaling
        canvas_width = self.canvas.winfo_width()
        if canvas_width <= 1:  # Canvas not yet rendered
            canvas_width = 850
        
        total_time = gantt_chart[-1][2]
        scale = (canvas_width - 40) / total_time if total_time > 0 else 1
        
        # Starting position
        y_top = 20
        y_bottom = 70
        x_offset = 20
        
        # Process color mapping
        process_colors = {}
        color_index = 0
        
        # Draw each time slice
        for process_id, start_time, end_time in gantt_chart:
            # Get color for this process
            if process_id not in process_colors:
                if process_id == 'IDLE':
                    process_colors[process_id] = '#BDC3C7'  # Gray for IDLE
                else:
                    process_colors[process_id] = self.colors[color_index % len(self.colors)]
                    color_index += 1
            
            color = process_colors[process_id]
            
            # Calculate rectangle coordinates
            x1 = x_offset + (start_time * scale)
            x2 = x_offset + (end_time * scale)
            
            # Draw rectangle
            self.canvas.create_rectangle(
                x1, y_top, x2, y_bottom,
                fill=color,
                outline="black",
                width=2
            )
            
            # Draw process ID text
            text_x = (x1 + x2) / 2
            text_y = (y_top + y_bottom) / 2
            self.canvas.create_text(
                text_x, text_y,
                text=process_id,
                font=("Arial", 9, "bold"),
                fill="white" if process_id != 'IDLE' else "black"
            )
            
            # Draw time markers
            self.canvas.create_text(
                x1, y_bottom + 15,
                text=str(start_time),
                font=("Arial", 8)
            )
        
        # Draw final time marker
        final_x = x_offset + (total_time * scale)
        self.canvas.create_text(
            final_x, y_bottom + 15,
            text=str(total_time),
            font=("Arial", 8)
        )


def run_gui():
    """Launch the GUI application."""
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()


# For testing purposes
if __name__ == "__main__":
    run_gui()
