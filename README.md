# Task
Get a list of pairs from a configuration file (sample configuration file is provided below), and replace value1 by value2 for all matches in a given text file (sample text file is provided below). All values in configuration file are unique; no need to take care of preventing change of already changed value. Names of both files are passed as command line arguments. Sort changed lines by the total number of symbols replaced, starting from the most changed line. Output resulting text to console.
Sample configuration file:
```
a=z
b=y
c=x
```
Sample text file:
```
jgrebk6hnae
cnhjrfyjvth3nxr
b#sjcf_ansvo!
djf#aemfaaofna%
```

## Usage

To use the script, you need to provide two command-line arguments:
- The path to the configuration file.
- The path to the text file.

Here's an example of how to run the script:
```
python main.py config.txt input.txt
```
This will replace the values in the input.txt file based on the config.txt file, and save the modified file in a sorted order.
The output will look something like this:
```
djf#zemfzzofnz%
y#sjxf_znsvo!
jgreyk6hnze
xnhjrfyjvth3nxr
```
