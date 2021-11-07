# MR
Simple script for resampling.

The script reads from an excel formatted file, where data is assumed to be stored in columns with header cells.
Data i assumed to be of type float and length of columns might vary, ie the number of data points in each column can
be different. The output is a new excel file, with columns equal in size.

The script will read each column, find out the max length of the columns and use this length as the resampling factor,
meaning that all columns will be equal in size to the max length after they are resampled.
Resampling (actually upsampling) is done through SciPy signal.resample method, see 
[https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.resample.html]. Columns will max length will be 
identical with the resampled columns. Columns that are shorter in length will be equal to max length after resampling, 
the average value will be equal to the average value before resampling.

Installation (using python virtualenv)

    $ python3 -m venv venv
    $ pip install -r requirements.txt

Remember to activate the virtualenv: `$ source venv/bin/activate`

Arguments to script is:
* -f: input filename
* -o: output filename, optional argument, if not provided default is 'outfile.xlsx'
* -p: plot resampled columns using matplot. Optional, default False, use True to get a plot.

Example

    $ python mr.py -f Example.xlsx -o New_Example.xlsx -p True

