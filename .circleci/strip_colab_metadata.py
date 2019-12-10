"""
Remove 'colab' item from 'metadata' and enforce JupyterLab's indentation style.

Usage:
    python strip_colab_metadata.py filename.ipynb
"""
import json
import sys

filename = sys.argv[1]

with open(filename, 'r') as infile:
    notebook = json.load(infile)
if 'colab' in notebook['metadata']:
    notebook['metadata'].pop('colab')
    with open(filename, 'w') as outfile:
        json.dump(notebook, outfile, indent=1)