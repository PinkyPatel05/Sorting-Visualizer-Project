# Sorting-Visualizer-Project

A Python project that provides a graphical interface to demonstrate popular sorting algorithms step-by-step. The visualizer allows users to observe how different sorting algorithms operate on an array in real-time, making it easier to understand each algorithm's process.

Project Overview
This project visualizes the following sorting algorithms:
* Merge Sort
* Heap Sort
* Quick Sort (Regular)
* Quick Sort (3-Median)
* Insertion Sort
* Selection Sort
* Bubble Sort
The Sorting Algorithm Visualizer is built using Python and Tkinter, displaying the sorting process as bars that change positions step-by-step according to the algorithm selected.

Key Features
1. Graphical Interface: The GUI, created with Tkinter, uses bars to represent array elements. The array values are displayed on top of the bars.
2. Array Generation: Users can generate a random array of integers to serve as input data.
3. Algorithm Visualization: The sorting process is displayed visually, updating the bar positions after each comparison and swap.
4. Step-by-Step Execution: The visualizer executes each algorithm incrementally to show the sorting process in detail.
5. Sorting Algorithm Options: Users can choose between different sorting algorithms to visualize.
6. Time Delay: Each step of the sorting process has a fixed delay (0.15 seconds) for better observation.
7. Color Indications: Bars change colors to represent different statuses (unsorted, being compared, or swapped).
8. Complexity Display: Shows time and space complexity for the selected sorting algorithm.
9. Recall Functionality: A recall button allows users to save the last generated array.

Implementation Steps
1. GUI Setup: Initialize the Tkinter GUI with Canvas for displaying array bars.
2. Array Generation: Implement functions to create and display random arrays.
3. Algorithm Integration: Add the six sorting algorithms with step-by-step GUI updates.
4. User Interaction: Create buttons or a dropdown to select and run sorting algorithms.
5. Time Delay & Color Coding: Set a fixed delay and color changes for better visualization.
6. Testing: Run tests with different array sizes to observe the algorithms in action.

File Directory:
README: Shows project descriptions, implementation step of GUI and File directory
Sorting_gui.py file shows all sorting algoritham with GUI implementation code
Programming Project_DAA_2024.pdf files shows documentation of shorting algorithm projects
Sorting Algo(ExcelFile): Experimental data for Graph creation


