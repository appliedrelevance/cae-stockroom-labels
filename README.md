# CAE Stockroom Locations Barcode location generator

This a small utility to generate a data table tht can be loaded into any barcode
generator software. In the case of this project, we are using the online utility
[Avery Design and Print](https://www.avery.com/software/design-and-print/).

_important_: The Avery print application can only support importing up to 3000 
rows per CSV file.  That's why the application generates multiple output files. 

## Running 

This is a very simple script and all of the parameters are hard-coded.  To
change change how the locations are generated requires updating the source code
of the script.  

> python3 cae-locations.py

the output files will be:

locations-a.csv  // The main stockroom locations
locations-b.csv  // Endcaps and and non-stockroom locations
locations-c.csv  // locations-a overflow. The stockroom had near 3000 records

## Printing the bar codes

This script *does not* actually generate bar codes. It generates comma separated
files that can be uploaded in the Avery Print online utility. 

