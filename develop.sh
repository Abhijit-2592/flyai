#!/bin/bash
echo "Setting up Project 'FlyAI' in develop mode"
pip install -e .
pre-commit install
echo "Done!"
