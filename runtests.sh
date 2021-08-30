#!/bin/bash

coverage run -p --source='.' -m behave $@
if [ "$?" = "0" ]; then
    coverage combine
    echo -e "\n\n================================================"
    echo "Test Coverage"
    coverage report
    echo -e "\nrun \"coverage html\" for full report"
    echo -e "\n"
    echo -e "\n\n================================================"
    echo "Pyflakes"
    pyflakes marvin.py
    echo -e "\n"
fi
