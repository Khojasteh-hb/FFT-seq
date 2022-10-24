## FFT-seq
FFT-seq: Fast Fourier Transformation (FFT) to convert the sequences of standard hydrophobicity values into components of frequencies and then the inverse.

## Problem definition
Proteins are macromolecules in the form of long chains of single building blocks. The building blocks are so called amino acids of which there are 20 (or up to 22) different types. Consequently, any protein can be represented as a text written in an alphabet of twenty symbols. Typically these texts range from 50 up to several hundred letters, i.e. amino acids. Each type of amino acid has key chemical and physical properties, e.g. electronegativity, charge, volume, hydrophobicity, etc. Most of these are continuous and thus can be represented by numerical values. This implies that a protein can be understood as a chain or sequence of these numerical values, e.g. a sequence of amino acid hydrophobicity values at pH 7 (neutral pH). 
This implementation transforms a sequence of amino acid into sequences of standardized hydrophobicity values at pH 7, where each amino acid in the protein sequence is replaced by the standardized hydrophobicity value of that amino acid. Later, it uses the Fast Fourier Transform algorithm (FFT) to convert the sequences of standard hydrophobicity values into components of frequencies.  Then, the result of the FFT is inversed by the Fast Fourier Transform algorithm, thus the original sequence of standard hydrophobicity values from the transformed values is constructed. For each sequence, two plots are generated, one showing the original sequence of standard hydrophobicity values and one showing the reconstructed values after applying first the FFT and then the inverse.

## Environment Settings
- Python version:  '3.9'

- You have to install the required libraries (numpy, scipy, matplotlib) 

## To run the code 
- Change directory to the code path by command:
  cd /path/to

- Run the code by command:

  cat hemoglobin.fasta.txt | python3 FFT_sequence.py

![Figure_3](https://user-images.githubusercontent.com/72028345/197471630-135128a8-74bc-4087-87dd-21a8760ca317.png)


# Contact
If you have any questions, do not hesitate to contact me by `khojasteh@znu.ac.ir` or `khojasteh.hb@gmail.com`, I will be happy to assist.

