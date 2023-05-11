import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
directory = os.path.dirname(file_path)

transpositions = {
    'c' : 'a',
    'c#' : 'a#',
    'd' : 'b',
    'd#' : 'c',
    'e' : 'c#',
    'f' : 'd',
    'f#' : 'd#',
    'g' : 'e',
    'g#' : 'f',
    'a' : 'f#',
    'a#' : 'g',
    'b' : 'g#'
}

def transpose_symbol(symbol):
    if len(symbol) >= 2:
        transposed_symbol = transpositions.get(symbol[:2], None)
        if transposed_symbol is not None:
            return transposed_symbol + symbol[2:]
    transposed_symbol = transpositions.get(symbol[0], None)
    return transposed_symbol + symbol[1:]

def transpose_symbols(symbols):
    transposed_symbols = []
    for symbol in symbols:
        if '\n' in symbol:
            symbol_pair = symbol.split('\n')
            transposed_symbols.append(transpose_symbol(symbol_pair[0]) + '\n' + transpose_symbol(symbol_pair[1]))
        else:
            transposed_symbols.append(transpose_symbol(symbol))
    return transposed_symbols

if file_path.endswith('.txt'):
    try:
        with open(file_path, 'r') as input_file:
            file_contents = input_file.read()
            input_file.close()
            symbols = file_contents.lower().split(' ')
            if ' ' in symbols:
                symbols = symbols.remove(' ')

            with open(file_path[:-4] + '_transposed.txt', 'w') as output_file:
                output_file.write(' '.join(transpose_symbols(symbols)))
                output_file.close()
    except FileNotFoundError:
        print('Error opening file.')
else:
    print('File must be a .txt file.')