import tkinter as tk
from tkinter import ttk
import random
import time


# Calculate runtime with sorting algorithm
# Bubble Sort
def bubble_sort(values, draw_bars, ascending):
    start_time = time.time()
    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            if (values[j] > values[j + 1]) if ascending else (values[j] < values[j + 1]):
                values[j], values[j + 1] = values[j + 1], values[j]
                draw_bars(values, [j, j + 1], swapped=True)
                time.sleep(0.15)
    draw_bars(values, [], sorted=True)
    update_runtime(time.time() - start_time)

# Selection Sort
def selection_sort(values, draw_bars, ascending):
    start_time = time.time()
    for i in range(len(values)):
        min_max_index = i
        for j in range(i + 1, len(values)):
            if (values[j] < values[min_max_index]) if ascending else (values[j] > values[min_max_index]):
                min_max_index = j
        values[i], values[min_max_index] = values[min_max_index], values[i]
        draw_bars(values, [i, min_max_index], swapped=True)
        time.sleep(0.15)
    draw_bars(values, [], sorted=True)
    update_runtime(time.time() - start_time)

# Insertion Sort
def insertion_sort(values, draw_bars, ascending):
    start_time = time.time()
    for i in range(1, len(values)):
        key_value = values[i]
        j = i - 1
        while j >= 0 and ((key_value < values[j]) if ascending else (key_value > values[j])):
            values[j + 1] = values[j]
            j -= 1
            draw_bars(values, [j + 1, i], swapped=True)
            time.sleep(0.15)
        values[j + 1] = key_value
        draw_bars(values, [j + 1, i])
    draw_bars(values, [], sorted=True)
    update_runtime(time.time() - start_time)

# Merge Sort
def merge_sort(values, draw_bars, ascending):
    start_time = time.time()
    merge_sort_recursive(values, 0, len(values) - 1, draw_bars, ascending)
    update_runtime(time.time() - start_time)

# Merge Sort Recursion
def merge_sort_recursive(values, left, right, draw_bars, ascending):
    if left < right:
        mid = (left + right) // 2
        merge_sort_recursive(values, left, mid, draw_bars, ascending)
        merge_sort_recursive(values, mid + 1, right, draw_bars, ascending)
        merge(values, left, mid, right, draw_bars, ascending)

def merge(values, left, mid, right, draw_bars, ascending):
    left_side = values[left:mid + 1]
    right_side = values[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_side) and j < len(right_side):
        if (left_side[i] <= right_side[j]) if ascending else (left_side[i] >= right_side[j]):
            values[k] = left_side[i]
            i += 1
        else:
            values[k] = right_side[j]
            j += 1
        k += 1
        draw_bars(values, [k])
        time.sleep(0.15)
    while i < len(left_side):
        values[k] = left_side[i]
        i += 1
        k += 1
        draw_bars(values, [k])
        time.sleep(0.15)
    while j < len(right_side):
        values[k] = right_side[j]
        j += 1
        k += 1
        draw_bars(values, [k])
        time.sleep(0.15)


# Quick Sort
def quick_sort(values, draw_bars, ascending):
    start_time = time.time()
    quick_sort_recursive(values, 0, len(values) - 1, draw_bars, ascending)
    update_runtime(time.time() - start_time)


def quick_sort_recursive(values, low, high, draw_bars, ascending):
    if low < high:
        pivot = partition(values, low, high, draw_bars, ascending)
        quick_sort_recursive(values, low, pivot - 1, draw_bars, ascending)
        quick_sort_recursive(values, pivot + 1, high, draw_bars, ascending)


def partition(values, low, high, draw_bars, ascending):
    pivot_value = values[high]
    i = low - 1
    for j in range(low, high):
        if (values[j] < pivot_value) if ascending else (values[j] > pivot_value):
            i += 1
            values[i], values[j] = values[j], values[i]
            draw_bars(values, [i, j], swapped=True)
            time.sleep(0.15)
    values[i + 1], values[high] = values[high], values[i + 1]
    draw_bars(values, [i + 1, high], swapped=True)
    time.sleep(0.15)
    return i + 1

# Quick Sort using 3 Median
def quick_sort_median_of_three(values, draw_bars, ascending):
    start_time = time.time()
    quick_sort_recursive_median_of_three(values, 0, len(values) - 1, draw_bars, ascending)
    update_runtime(time.time() - start_time)


def quick_sort_recursive_median_of_three(values, low, high, draw_bars, ascending):
    if low < high:
        pivot = partition_median_of_three(values, low, high, draw_bars, ascending)
        quick_sort_recursive_median_of_three(values, low, pivot - 1, draw_bars, ascending)
        quick_sort_recursive_median_of_three(values, pivot + 1, high, draw_bars, ascending)


def partition_median_of_three(values, low, high, draw_bars, ascending):
    mid = (low + high) // 2
    pivot_index = median_of_three(values, low, mid, high)
    values[pivot_index], values[high] = values[high], values[pivot_index]

    pivot_value = values[high]
    i = low - 1
    for j in range(low, high):
        if (values[j] < pivot_value) if ascending else (values[j] > pivot_value):
            i += 1
            values[i], values[j] = values[j], values[i]
            draw_bars(values, [i, j], swapped=True)
            time.sleep(0.15)
    values[i + 1], values[high] = values[high], values[i + 1]
    draw_bars(values, [i + 1, high], swapped=True)
    time.sleep(0.15)
    return i + 1


def median_of_three(values, low, mid, high):
    if values[low] < values[mid]:
        if values[mid] < values[high]:
            return mid
        elif values[low] < values[high]:
            return high
        else:
            return low
    else:
        if values[low] < values[high]:
            return low
        elif values[mid] < values[high]:
            return high
        else:
            return mid

# Heap Sort
def heap_sort(values, draw_bars, ascending):
    start_time = time.time()
    n = len(values)
    for i in range(n // 2 - 1, -1, -1):
        heapify(values, n, i, draw_bars, ascending)
    for i in range(n - 1, 0, -1):
        values[i], values[0] = values[0], values[i]
        draw_bars(values, [i, 0], swapped=True)
        time.sleep(0.15)
        heapify(values, i, 0, draw_bars, ascending)
    update_runtime(time.time() - start_time)


def heapify(values, n, i, draw_bars, ascending):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and (
            (values[left_child] > values[largest]) if ascending else (values[left_child] < values[largest])):
        largest = left_child
    if right_child < n and (
            (values[right_child] > values[largest]) if ascending else (values[right_child] < values[largest])):
        largest = right_child
    if largest != i:
        values[i], values[largest] = values[largest], values[i]
        draw_bars(values, [i, largest], swapped=True)
        time.sleep(0.15)
        heapify(values, n, largest, draw_bars, ascending)

# Display Complexity
complexity_dict = {
    "Bubble Sort": ("O(n^2)", "O(1)"),
    "Selection Sort": ("O(n^2)", "O(1)"),
    "Insertion Sort": ("O(n^2)", "O(1)"),
    "Merge Sort": ("O(n log n)", "O(n)"),
    "Regular Quick Sort": ("O(n log n)", "O(log n)"),
    "Quick Sort Using 3 Medians": ("O(n log n)", "O(log n)"),
    "Heap Sort": ("O(n log n)", "O(1)")
}

# GUI Update elements
BUFFER = 20


def draw_bars(values, highlighted, sorted=False, swapped=False):
    canvas.delete("all")
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height() - BUFFER
    bar_width = canvas_width / len(values)
    max_value = max(values)

    for index, value in enumerate(values):
        x0 = index * bar_width
        y0 = canvas_height - (value / max_value) * canvas_height * 0.9
        x1 = (index + 1) * bar_width
        y1 = canvas_height + BUFFER
        if sorted:
            color = "#4CAF50"
        elif index in highlighted:
            color = "#FF5733" if not swapped else "#4CAF50"
        else:
            color = "#0084FF"

        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        canvas.create_text((x0 + x1) / 2, y0 - BUFFER / 2, text=str(value), anchor=tk.S, fill="white",
                           font=("Aptos", 8))
    root.update_idletasks()


def update_runtime(runtime):
    runtime_label.config(text=f"Runtime: {runtime:.2f} s")


def start_sorting():
    global values
    if not values:
        return
    selected_algorithm = algorithm_menu.get()
    ascending = sort_order.get() == "Ascending"
    if selected_algorithm == "Bubble Sort":
        bubble_sort(values, draw_bars, ascending)
    elif selected_algorithm == "Selection Sort":
        selection_sort(values, draw_bars, ascending)
    elif selected_algorithm == "Insertion Sort":
        insertion_sort(values, draw_bars, ascending)
    elif selected_algorithm == "Merge Sort":
        merge_sort(values, draw_bars, ascending)
    elif selected_algorithm == "Regular Quick Sort":
        quick_sort(values, draw_bars, ascending)
    elif selected_algorithm == "Quick Sort Using 3 Medians":
        quick_sort_median_of_three(values, draw_bars, ascending)
    elif selected_algorithm == "Heap Sort":
        heap_sort(values, draw_bars, ascending)


# Save the last generated array value
saved_values = None

# generate random array (size 5 to 50)
def generate_values():
    global values, saved_values
    array_size = size_scale.get()
    values = [random.randint(1, 100) for _ in range(array_size)]
    saved_values = values.copy()
    draw_bars(values, [])


def recall_values():
    global values, saved_values
    if saved_values:
        values = saved_values.copy()
        draw_bars(values, [])

# update complexity
def update_complexity():
    selected_algo = algorithm_menu.get()
    time_complexity, space_complexity = complexity_dict[selected_algo]
    time_complexity_label.config(text=f"Time Complexity: {time_complexity}")
    space_complexity_label.config(text=f"Space Complexity: {space_complexity}")


# GUI Starting
root = tk.Tk()
root.title("Sorting Algorithm Visualizer Created By Pinky")
root.geometry("1000x650")
root.config(bg="#F4F4F5")

# Variables
values = []
saved_values = None
sort_order = tk.StringVar(value="Ascending")

# UI Frame
ui_frame = tk.Frame(root, width=900, height=100, bg="#F4F4F5")
ui_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=(20, 10))

# Canvas for visualization
canvas = tk.Canvas(root, bg="#121212", highlightthickness=1)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.bind("<Configure>", lambda event: draw_bars(values, []) if values else None)

# List of Sorting Algorithms for drop down
sorting_algorithms = [
    "Choose Algorithm", "Merge Sort", "Heap Sort", "Regular Quick Sort",
    "Quick Sort Using 3 Medians", "Insertion Sort", "Selection Sort", "Bubble Sort"
]

# UI Elements
label_style = {"bg": "#F4F4F5", "fg": "#2D2D34", "font": ("Aptos", 10, "bold")}
tk.Label(ui_frame, text="Algorithm:", **label_style).grid(row=0, column=0, padx=5, pady=5)

algorithm_menu = ttk.Combobox(ui_frame, values=sorting_algorithms, font=("Aptos", 10))
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)
algorithm_menu.bind("<<ComboboxSelected>>", lambda e: update_complexity())

tk.Label(ui_frame, text="Size of Array:", **label_style).grid(row=0, column=2, padx=5, pady=5)
size_scale = tk.Scale(ui_frame, from_=5, to=50, resolution=1, orient=tk.HORIZONTAL, bg="#F4F4F5", fg="#2D2D34",
                      troughcolor="#D1D5DB")
size_scale.grid(row=0, column=3, padx=5, pady=5)
size_scale.set(20)

# Sorting Order Selection
order_label = tk.Label(ui_frame, text="Sorting Order:", **label_style)
order_label.grid(row=0, column=4, padx=5, pady=5)
order_frame = tk.Frame(ui_frame, bg="#F4F4F5")
order_frame.grid(row=0, column=5, padx=5, pady=5)
ascending_button = tk.Radiobutton(order_frame, text="Ascending", variable=sort_order, value="Ascending", bg="#D1D5DB",
                                  selectcolor="#0084FF", font=("Aptos", 10))
ascending_button.grid(row=0, column=0)
descending_button = tk.Radiobutton(order_frame, text="Descending", variable=sort_order, value="Descending",
                                   bg="#D1D5DB", selectcolor="#FF5733", font=("Aptos", 10))
descending_button.grid(row=0, column=1)

# Complexity and Runtime Display
time_complexity_label = tk.Label(ui_frame, text="Time Complexity: -", **label_style)
time_complexity_label.grid(row=1, column=0, padx=10, pady=5)
space_complexity_label = tk.Label(ui_frame, text="Space Complexity: -", **label_style)
space_complexity_label.grid(row=1, column=1, padx=10, pady=5)
runtime_label = tk.Label(ui_frame, text="Runtime: - s", **label_style)
runtime_label.grid(row=1, column=2, padx=10, pady=5)

# Buttons
button_style = {"font": ("Aptos", 10, "bold"), "bg": "#FF4D4F", "fg": "white", "relief": "flat"}
tk.Button(ui_frame, text="Generate", command=generate_values, **button_style).grid(row=1, column=3, padx=5, pady=5)
tk.Button(ui_frame, text="Recall", command=recall_values, **button_style).grid(row=1, column=4, padx=5, pady=5)
tk.Button(ui_frame, text="Sort", command=start_sorting, **button_style).grid(row=1, column=5, padx=5, pady=5)

# Footer
footer = tk.Label(root, text="Crafted by Pinky.", font=("Aptos", 12, "bold italic"), fg="#808080", bg="#F4F4F5")
footer.pack(side=tk.BOTTOM, anchor="se", padx=10, pady=10)

# Run the application
root.mainloop()