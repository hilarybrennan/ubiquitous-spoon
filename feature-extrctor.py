# Establishes training and submission data classes and methods
# Owner: Hilary Brennan
# Last Update: 12/15/2019

import pandas as pd

#Create Corpus class to read poetry data from local csv file into pandas dataframe

class Corpus():
    def __init__(self, abspath):
        self.self = self
        self.abspath = abspath

        # Load data from csv to dataframe
        self.df = pd.read_csv(abspath, header='infer')
        self.fields = self.df.columns


#     This file is part of ubiquitous-spoon.
#
#     ubiquitous-spoon is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     ubiquitous-spoon is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with ubiquitous-spoon.  If not, see <https://www.gnu.org/licenses/>.
