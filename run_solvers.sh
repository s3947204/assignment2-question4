#!/bin/bash

methods=("greedy" "nearest" "brute")

for method in "${methods[@]}"; do
  for i in {2..10}; do
    python main.py "$method" "$i"
  done
done
