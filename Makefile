# Makefile for CS305 Process Scheduling Simulator
# Quick commands for running the simulator

.PHONY: run gui clean

# Run CLI mode with default input file
run:
	python main.py data/input.txt

# Run GUI mode
gui:
	python main.py

# Clean Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
