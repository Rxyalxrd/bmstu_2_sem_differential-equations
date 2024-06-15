# bmstu_2_sem_differential-equations


## Overview

This repository contains several Python scripts and Jupyter notebooks for numerical analysis and solving differential equations. The tools included are focused on Fourier series, solving second-order ordinary differential equations (ODEs), and using the Euler method for ODEs. Additionally, there is a script for modeling uranium decay.

## Files

### 1. Fourier Series (5.ipynb)

- **Description**: This Jupyter notebook is designed to generate and plot Fourier series.
- **Contents**:
  - Import statements for necessary libraries (`numpy`, `matplotlib.pyplot`).
  - A class `FourierSeries` that includes methods for initializing parameters and generating the series.
- **Usage**: Open the notebook in Jupyter and run the cells to see the implementation and plots.

### 2. Second-Order ODE Solver (13.ipynb)

- **Description**: This notebook provides a numerical solution for second-order ODEs.
- **Contents**:
  - Import statements for `numpy` and `matplotlib.pyplot`.
  - A class `SecondOrderODESolver` that includes methods to set up and solve the differential equations.
- **Usage**: Open the notebook in Jupyter and follow the provided steps to solve second-order ODEs.

### 3.Second-Order ODE Solver (12.ipynb)
- **Description**: This notebook provides a numerical solution for second-order ordinary differential equations (ODEs) using the Runge-Kutta 4th order (RK4) method.
- **Contents**:
    - Import statements for numpy and matplotlib.pyplot.
    - A class SecondOrderODESolver that includes methods to set up and solve the differential equations.
- **Usage**: Open the notebook in Jupyter and follow the provided steps to solve second-order ODEs.

### 4. Euler Method (Euler method.ipynb)

- **Description**: This notebook explains and implements the Euler method for solving ODEs.
- **Contents**:
  - Markdown cells with explanations of the Euler method.
  - A class `Euler` with methods to implement the Euler method.
- **Usage**: Open the notebook in Jupyter to read the explanations and run the code cells to see the Euler method in action.

### 5. Uranium Decay Solver (mathmodel.py)

- **Description**: This Python script models the decay of uranium using a numerical approach.
- **Contents**:
  - Import statements for `numpy` and `matplotlib.pyplot`.
  - A class `UraniumDecaySolver` with methods to simulate uranium decay over time.
- **Usage**: Run the script in a Python environment to simulate uranium decay and generate plots.

## Getting Started

To use the notebooks and scripts in this repository, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   ```

2. **Install the necessary packages**:
   Ensure you have `numpy` and `matplotlib` installed. You can install them using pip:
   ```sh
   pip install numpy
   pip install matplotlib
   ```

3. **Run the notebooks**:
   - Open Jupyter Notebook or JupyterLab.
   - Navigate to the directory containing the cloned repository.
   - Open the desired `.ipynb` file and run the cells sequentially.

4. **Run the Python script**:
   - Execute the `mathmodel.py` script in a Python environment:
     ```sh
     python mathmodel.py
     ```
