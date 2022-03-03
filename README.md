This package is meant to pull sm4 file types into python. 

It is meant to integrate easily with stmpy: https://github.com/harrispirie/stmpy 

stmpy has its own function that uses this package to port all of the sm4 data into the same format stmpy uses

## To install

Clone or download this repository onto your folder

navigate to the directory in your terminal

run the command `pip install -e .` 'LineType': 5,

add `import rhk_sm4` to python files to access methods

## General Repo Structure
- **data** folder contains test data
- **notebooks** folder contains tutorial and test notebooks
- **rhk_sm4** contains the package code


## Basic Usage
`file = rhk_sm4.load_sm4('file')`

`file.print_info()` displays all the different channels exported in the .sm4

Each exported channel in the sm4 (topography, current, dF, etc) becomes a 'page' in the file, which can be accessed by `file[index]` where index is the index in the print_info data table corresponding to the channel of interest.

to get the data
`file[index].data`

to get x coordinates for the data
`file[index].coords`

to get a list of metadata
`file[index].attrs`

## Tested Cases
Different 'line types' (which are associated with different spectrum types i.e. oscope trace, noise spectrum etc) process and scale the raw data differently. Here are the tested spectrum + channel types that have been explicitely examined and we are confident import correctly with correct scaling etc.

- Noise spectrum + current channel
- Noise spectrum + ch3 input
