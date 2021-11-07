#!/usr/bin/python

import argparse
import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt

# Reads an excel formatted file, assuming data are in columns and of type float.
# Columns are in varying size, the longest sequence is used as resample length.
# All columns are resampled using SciPy's signal.resample method.
# Results is saved into new excel file with prefix 'new_' to the original file name.
# Plotting of signals is available
# No exception handling.
# Invocation: $ python -f <filename> -o <filename> -p [True/False]
# Arguments:
#   f: Input filename
#   o: Output filename
#   p: Plot, default False
#
# Mats Melander 2021-11-06
#


class Msr:
    def __init__(self, fname):
        self.name = fname
        self.max_samples = 0
        self.df = pd.read_excel(self.name)

        self.samples = {col: np.array(self.df[col]) for col in self.df.columns}
        for key, val in self.samples.items():
            self.samples[key] = val[~np.isnan(val)]  # Avoid NaN samples
            if self.max_samples < self.samples[key].size:
                self.max_samples = self.samples[key].size

        self.x = np.arange(0, self.max_samples)

    def resample(self):
        new_samples = dict(self.samples)
        for key, val in self.samples.items():
            new_samples[key] = signal.resample(val, self.max_samples)
        self.samples = new_samples

    def plot(self):
        for key, val in self.samples.items():
            plt.plot(np.arange(val.size), val)
        plt.show()

    def save(self, fname):
        df = pd.DataFrame.from_dict(self.samples)
        df.to_excel(fname, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Resampling of data')
    parser.add_argument('-f', '--file', help='Input filename', required=True)
    parser.add_argument('-o', '--outfile', help='Output filename', default="outfile.xlsx", required=False)
    parser.add_argument('-p', '--plot', help='Plot data', action="store_true", required=False)
    args = parser.parse_args()

    m = Msr(fname=args.file)
    m.resample()
    if args.plot:
        m.plot()
    m.save(fname=args.outfile)
