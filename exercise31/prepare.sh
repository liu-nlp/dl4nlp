#!/bin/bash

set -e

nb_teacher="Transition-Based-Parser-WithSolutions.ipynb"
nb_student="Transition-Based-Parser.ipynb"

if [ "${nb_teacher}" -nt "${nb_student}" ]; then
    nb-filter-cells -t solution -i "${nb_teacher}" -o "${nb_student}"
fi
