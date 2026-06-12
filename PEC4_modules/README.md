# PEC4_Sebastian_Moncada_Velasquez

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Entrega de la PEC4

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── docs               <- mkdocs project; see www.mkdocs.org for details
│   ├── docs/
│   ├── .gitkeep
│   ├── mkdocs.yml
│   └── README.md
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         pec4_sebastian_moncada_velasquez and configuration for tools like black
│
├── screenshots        <- Screenshots that demonstrate authorship
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
├── .env               <- Environment variables
├── config.py          <- Store useful variables and configuration
├── __init__.py        <- Makes PEC4 a Python module
│
└── src                <- Source code
    ├── data/          <- Downloaded datasets
    ├── img/           <- Generated plots and figures
    ├── exercises/     <- Exercise modules
    │   ├── __init__.py
    │   ├── ejercicio_1.py
    │   ├── ejercicio_2.py
    │   ├── ejercicio_3.py
    │   ├── ejercicio_4.py
    │   ├── ejercicio_5.py
    │   ├── ejercicio_6.py
    │   └── ejercicio_7.py
    └── main.py        <- Entry point; orchestrates all exercises
```

--------

# To install the project: 

## Installation

### Prerequisites
- Python 3.13
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Steps

1. Clone the repository and navigate to the project folder:
```bash
   git clone https://github.com/smoncadav/PEC4
   cd PEC4_modules
```

2. Create and activate the virtual environment:
```bash
   uv venv .venv
   source .venv/bin/activate  # Mac/Linux
   .venv\Scripts\activate     # Windows
```

3. Install the package and its dependencies:
```bash
   cd PEC4_modules
   uv pip install -r requirements.txt
   uv pip install -e .
```


4. Run the project:
```bash
   python src/main.py
```

--------

## Generating Documentation

Documentation is generated with `pydoc` from the docstrings in each exercise module.

### Steps

1. Set the Python path so modules can be found:
```bash
export PYTHONPATH=/path/to/PEC4/PEC4_modules/src
```

2. Navigate to the `src` folder:
```bash
cd PEC4_modules/src/exercises
```

3. Generate HTML documentation for all exercises:
```bash
python -m pydoc -w ejercicio_1.py
```

This creates `.html` files in the current directory, one per module.

4. To browse documentation interactively in the browser:
```bash
python -m pydoc -b
```

--------

* This documentation has been co-created with Claude: 
Reference: Anthropic. (2026). Claude (versión del 11 de junio de 2026) [Modelo de lenguaje grande]. https://claude.ai
