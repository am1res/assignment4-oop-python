# Assignment 4 — Python OOP

## Structure
```
assignment4/
├── main.py
├── students.csv     
├── analytics/
│   ├── __init__.py
│   ├── file_manager.py
│   ├── data_loader.py
│   ├── analyser.py
│   ├── result_saver.py
│   └── report.py
└── tests/
    ├── __init__.py
    └── test_analyser.py
```

## Run the program
```
python main.py
```

## Run tests
```
python -m unittest tests/test_analyser.py -v
```

## Covered concepts
- **Inheritance** — GpaAnalyser, CountryAnalyser extend DataAnalyser
- **Association** — Report uses DataAnalyser and ResultSaver
- **Polymorphism** — loop calls analyse() and print_results() on different objects
- **Modules & Package** — analytics/ package with relative imports
- **Unit Tests** — 4 tests in tests/test_analyser.py
