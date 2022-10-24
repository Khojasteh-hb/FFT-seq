# The reconstructed values after applying first the fast fourier transformation and then the inverse.

# import required libraries
import sys

import numpy as np

import scipy.stats as stats

from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

def hydro_transform(file_pointer):

    # Collected from https://www.sigmaaldrich.com/FR/fr/technical-documents/technical-article/protein-biology/
	# protein-structural-analysis/amino-acid-reference-chart
    hydro_dict = {'A': 41, 'R': -14, 'N': -28, 'D': -55, 'C': 49,
                  'Q': -10, 'E': -31, 'G': 0, 'H': 8, 'I': 99,
                  'L': 97, 'K': -23, 'M': 74, 'F': 100, 'P': -46,
                  'S': -5, 'T': 13, 'W': 97, 'Y': 63, 'V': 76}

    keys, vals = zip(*hydro_dict.items())
    z = stats.zscore(vals)
    standarad_hydro_dict = dict(zip(keys, z))

    first_line = file_pointer.readline()
    name = first_line.split('>')[1:]
    name = ''.join(name)
    seq_name = name.split(' OS')[0]

    sequence = file_pointer.readline().split()
    sequence = ''.join(sequence)

    num_residues = len(sequence)

    encoding = []
    for residue in sequence:
        encoding.append(standarad_hydro_dict[residue])

    #print(encoding)

    y = fft(np.array(encoding))

    y_inv = ifft(y)
    #print(y_inv)
    num_y_inv = len(y_inv)

    fig, axs = plt.subplots(1, 2)

    x_data = range(1, num_residues + 1)
    axs[0].plot(x_data, encoding, linewidth=1.0)
    axs[0].set_title("Standardized " + seq_name)

    x_data = range(1, num_y_inv + 1)
    axs[1].plot(x_data, y_inv, linewidth=1.0)
    axs[1].set_title("FFT and inverse of FFT")

    for ax in axs.flat:
        ax.set(xlabel='Residue Number', ylabel='Hydrophobicity')

    plt.show()

    return encoding

def main():

    file = sys.stdin

    results = hydro_transform(file)


if __name__ == "__main__":
    main()











