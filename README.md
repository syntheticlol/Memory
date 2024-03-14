# Python Memory Management Tool using Cython (ctypes)

This Python script provides a simple tool for managing memory using Cython (ctypes), a foreign function library for Python. It includes functionality for both memory allocation and deallocation, leveraging the Python C API.

## Features

- **Cross-platform Compatibility:** The script dynamically selects the appropriate Python DLL based on the system's platform, ensuring compatibility across different operating systems.
- **Flexible Memory Allocation:** Users can allocate memory of varying sizes using the `allocatemem` method, providing flexibility in memory management.
- **Efficient Memory Deallocation:** The `thisisfax` method frees allocated memory and triggers garbage collection to ensure efficient memory usage and prevent memory leaks.

## Usage

### 1. Clone the Repository:
```bash
git clone https://github.com/syntheticlol/memory
```
### 2. Navigate to the Directory:
```bash
cd memory
```
### 3. Run the Script:
```bash
py main.py
```
### 4. Interact with the Tool:

- Upon running the script, memory allocation and deallocation will be performed automatically.
- The script will print "Done.." once the process is complete.

## Note

It's important to exercise caution when manually managing memory, as improper usage can lead to memory leaks and other issues. Ensure that memory is allocated and deallocated appropriately to maintain the stability and efficiency of your Python applications.
