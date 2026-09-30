## Problem Statement
Users frequently require a lightweight, immediate tool for basic arithmetic operations without the overhead of heavy graphical applications. A terminal-based calculator provides a fast, resource-efficient solution, but it must be resilient against common user input errors, such as typing non-numeric characters or attempting invalid mathematical operations.

## Scope of the Project
The project encompasses a command-line interface that executes standard arithmetic calculations (addition, subtraction, multiplication, division, modulus, power, and square root)[cite: 2]. The scope includes strict input validation to handle edge cases like zero-division and non-real number processing. The system will not include advanced scientific functions (e.g., trigonometry) or graphical user interfaces.

## Target Users
* Students and beginners learning basic mathematics.
* Developers or terminal users needing quick arithmetic results without switching contexts.
* Educators looking for a clear, modular example of Python application structure.

## High-Level Features
* **Interactive Menu:** A clear, text-based navigation system for selecting operations[cite: 2].
* **Modular Arithmetic Engine:** Discrete functions for distinct mathematical operations.
* **Input Sanitization:** A dedicated validation layer intercepting invalid keystrokes and illogical mathematical requests before processing.