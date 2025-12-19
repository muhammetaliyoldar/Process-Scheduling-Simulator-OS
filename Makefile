# Makefile for CS305 Process Scheduling Simulator
# Quick commands for running the simulator

.PHONY: run gui clean

# Run CLI mode with default input file
run:
	python main.py data/processes.txt

# Run CLI mode with custom Time Quantum (example: TQ=4)
run-tq:
	python main.py data/processes.txt 4

# Run GUI mode
gui:
	python main.py

# Clean Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
