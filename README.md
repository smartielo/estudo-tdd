# TDD Study Exercises

This repository contains small Python exercises for practicing Test-Driven Development (TDD) with Pytest.

## Exercises

- `exemplo-frete`: shipping cost calculation and input validation
- `exercicio1`: student grade calculation
- `exercicio2`: shopping cart and discount coupons
- `exercicio3-banco`: bank deposits, withdrawals, and interest
- `exercicio4-aluguel`: car rental calculation
- `exercicio5-cinema`: movie ticket and snack orders
- `pytest-cov`: calculator tests and code coverage practice

Each exercise has its implementation files and a `tests` folder.

## Requirements

- Python 3
- Pytest
- pytest-cov

Install the test tools with:

```bash
pip install pytest pytest-cov
```

## Run the tests

From the repository root:

```bash
pytest
```

To run a specific exercise:

```bash
pytest exercicio3-banco/tests
```

To check code coverage for the calculator:

```bash
pytest pytest-cov/tests --cov=pytest-cov --cov-report=term-missing
```

The purpose of this repository is to learn how to write tests, validate input, handle errors, use parametrized tests, and measure code coverage.
