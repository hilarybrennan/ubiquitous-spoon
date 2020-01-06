# Getting Started with ubiquitous-spoon

## Installation Instructions

**1. Import Training Data:** ubiquitous-spoon pulls its training set from a directory in root called `data` containing `csv` files.

Training data CSVs should include the following fields:
0. ID - unique identified for the individual poem
1. Title - the poem's title
2. Content - the text of the content itself
3. Author - the name of the author
4. Tags - metadata used for tagging and categorization - this column can be empty.


**2. Install Packages:**
```buildoutcfg
$pip install pandas
```