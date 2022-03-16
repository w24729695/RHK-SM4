This package is meant to pull sm4 file types into python. 

It is meant to integrate easily with stmpy: https://github.com/harrispirie/stmpy 

stmpy has its own function that uses this package to port all of the sm4 data into the same format stmpy uses

It is highly recommended to use nbstripout https://github.com/kynan/nbstripout if contributing to this repo. Install as described and then run `nbstripout --install` in terminal in the repository directory

## To install

Clone or download this repository onto your folder

navigate to the directory in your terminal

run the command `pip install -e .` 

add `import rhk_sm4.rhk_sm4 as sm4` to python files to access methods via `sm4.method()`

## General Repo Structure
- **data** folder contains test data
- **notebooks** folder contains tutorial and test notebooks
- **rhk_sm4** contains the package code


## Basic Usage
`file = rhk_sm4.load_sm4('file')`

`file.print_info()` displays all the different channels exported in the .sm4

Each exported channel in the sm4 (topography, current, dF, etc) becomes a 'page' in the file, which can be accessed by `file[index]` where index is the index in the print_info data table corresponding to the channel of interest.

`file[index].data` - independent variable of spectrum/topo     

`file[index].coords` - dependent variable of spectrum/topo (if 1D it's stored in 'x')

`file[index].attrs`- list of metadata

## Tested Cases
Different 'line types' (which are associated with different spectrum types i.e. oscope trace, noise spectrum etc) process and scale the raw data differently. Here are the tested spectrum + channel types that have been explicitely examined and we are confident import correctly with correct scaling etc.

- Noise spectrum + current channel
- Noise spectrum + ch3 input
- IZ current and coodinates
- Oscope current and topography
