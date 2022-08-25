#!/bin/bash

set -e

nb_teacher="Assignment2-WithSolutions.ipynb"
nb_student="Assignment2.ipynb"

if [ "${nb_teacher}" -nt "${nb_student}" ]; then
    nb-filter-cells -t solution -i "${nb_teacher}" -o "${nb_student}"
fi
