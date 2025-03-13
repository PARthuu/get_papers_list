#!/bin/bash

# Exit on errors
set -e

echo "Building package..."
poetry build

echo "Publishing to TestPyPI..."
poetry publish -r testpypi

echo "Done!"
