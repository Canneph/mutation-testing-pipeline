#!/usr/bin/env bash
set -e

echo "Cloning TheAlgorithms/Python..."
git clone https://github.com/TheAlgorithms/Python.git
cd Python

echo "Setting up environment..."
python3 -m venv venv
source venv/bin/activate

pip install -r ../config/requirements.txt

echo "Running baseline tests..."
pytest

echo "Running mutation testing..."
mutmut run

echo "Done."