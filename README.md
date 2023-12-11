## FFT-seq
FFT-seq: Fast Fourier Transformation (FFT) to convert the sequences of standard hydrophobicity values into components of frequencies and then the inverse.

## Problem definition
Proteins are macromolecules in the form of long chains of single building blocks. The building blocks are so called amino acids of which there are 20 (or up to 22) different types. Consequently, any protein can be represented as a text written in an alphabet of twenty symbols. Typically these texts range from 50 up to several hundred letters, i.e. amino acids. Each type of amino acid has key chemical and physical properties, e.g. electronegativity, charge, volume, hydrophobicity, etc. Most of these are continuous and thus can be represented by numerical values. This implies that a protein can be understood as a chain or sequence of these numerical values, e.g. a sequence of amino acid hydrophobicity values at pH 7 (neutral pH). 
This implementation transforms a sequence of amino acid into sequences of standardized hydrophobicity values at pH 7, where each amino acid in the protein sequence is replaced by the standardized hydrophobicity value of that amino acid. Later, it uses the Fast Fourier Transform algorithm (FFT) to convert the sequences of standard hydrophobicity values into components of frequencies.  Then, the result of the FFT is inversed by the Fast Fourier Transform algorithm, thus the original sequence of standard hydrophobicity values from the transformed values is constructed. For each sequence, two plots are generated, one showing the original sequence of standard hydrophobicity values and one showing the reconstructed values after applying first the FFT and then the inverse.

## Hydrophobicity values
The amino acid hydrophobicity values are collected from: https://www.sigmaaldrich.com/FR/fr/technical-documents/technical-article/protein-biology/protein-structural-analysis/amino-acid-reference-chart

## Environment Settings
- Ubuntu 18.04
- Python version:  '3.9'
- You have to install the required libraries (numpy, scipy, matplotlib) 

## Tip:
There was a problem with the installation of the library matplotlib in ubuntu 18.04. I solved the problem with the commands below:

- apt-get install libjpeg-dev zlib1g-dev

- pip3 install Pillow

- pip3 install --upgrade setuptools

And finally, I installed the library 'matplotlib'

## To run the code 
- Change directory to the code path by command:

  cd /path/to

- Run the code by command:

  cat hemoglobin.fasta.txt | python3 FFT_sequence.py

![Figure_1](https://user-images.githubusercontent.com/72028345/197471753-4bb065cd-8035-45a1-8ab4-885e9dff14ae.png)

![Figure_2](https://user-images.githubusercontent.com/72028345/197471766-57d98a77-d7a6-4c97-b859-a44c46ac04fa.png)

![Figure_3](https://user-images.githubusercontent.com/72028345/197471793-412fbb6f-261d-4f32-b0a3-9249233a3430.png)


# Contact
If you have any questions, do not hesitate to contact me at `khojasteh.hb@gmail.com`, I will be happy to assist.

