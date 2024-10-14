# Rankine

This is the github repository of the Rankine controls and simulations team '24-'25.

# Using the Repository

For exploratory code, design optimization, and writing controls algorithms, we will store all of our code in **Jupyter notebooks**. There are two top-level folders for these notebooks.

**controls_notebooks** is for analyses related to control systems, dynamic analyses, and similar content, following [Russ Tedrake's course on underactuated robotics.](https://underactuated.csail.mit.edu).

**flight_notebooks** is for analyses of the fluid and flight dynamics of our real and hypothetical airplane designs.

## Making a Virtual Environment

For better dependency management (always a pain in Python), **each top level folder is designed to be run with its own virtual environment.** 

Because the robotics library [PyDrake](https://drake.mit.edu/pydrake/index.html) used in the course only runs on *nix systems (Linux and MacOS), Windows users will need to make sure to use that folder inside WSL.

To create a virtual environment:

```bash
cd flight_notebooks # or controls_notebooks
python -m venv .venv 
source .venv/bin/activate # platform dependent - in Powershell, .venv/Scripts/activate.ps1
pip install -r requirements.txt
```

You will need to do this in each top-level notebook.
