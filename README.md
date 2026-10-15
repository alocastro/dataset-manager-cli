# Dynamic Dataset Manager CLI

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A robust Command Line Interface (CLI) tool designed for creating, dynamically expanding, and manipulating structured key-value datasets in Python.

This project emphasizes **defensive programming principles**, ensuring complete immunity to runtime crashes caused by invalid user inputs.

## 🌟 Key Features

* **Interactive Dataset Builder**: Construct dynamic datasets with custom key-value data structures.
* **Defensive Input Validation**: Handled via a modular `utils` package ensuring type casting safety (`ValueError`), boundary enforcement, and text sanitization.
* **Dataset Mutation**: Add new key-value pairs or safely remove records by index with real-time feedback.
* **Modular Software Design**: Clean separation of validation logic (`utils/functions.py`) and application orchestration (`main.py`).

## 📁 Architecture

```text
dataset-manager-cli/
├── utils/
│   ├── __init__.py
│   └── functions.py     # Shared defensive input validation utilities
├── main.py              # Application main loop and dataset operations
├── .gitignore
└── README.md