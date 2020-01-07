# Establishes training and submission data classes and methods
# Owner: Hilary Brennan
# Last Update: 12/15/2019

import pandas as pd

#Create Corpus class to read poetry data from local csv file into pandas dataframe
#Training and submission corpi have the following format:
# id, title, text, author, tags

# TODO: create resiliency around incorrect formatting of data.

class Corpus():
    def __init__(self, abspath):
        self.self = self
        self.abspath = abspath

        # Load data from csv to dataframe
        self.df = pd.read_csv(abspath, header='infer')

        self.lexicon = self.lexicon(self.df_clean())

    def df_clean(self):
        df = self.df
        df_clean = df
        df_clean['Poem'] = df['Poem'].str.replace('[!,.?/><:;"@%&\'\(\)*^]', ' ', regex=True)

        return df_clean

    # Construct the lexicon from the corpus
    def lexicon(df):
        text_column = df['Poem']
        corpus_string = " ".join(text_column)
        lex_list = []
        lex_count = []

        for w in corpus_string:
            if w in lex_list:
                index = lex_list.index(w)
                lex_count[index] = lex_count[index]+1
            if w not in lex_list:
                lex_list.append(w)
                lex_count.append(1)
            else: continue

        lexicon = pd.DataFrame(data = [lex_list, lex_count])
        return lexicon

    def smooth_lexicon(self):
        lexicon = self.lexicon


# Data loads from local data directory **DO NOT CHECK IN DATA ITSELF**

training = Corpus('./data/training.csv')
training_lexicon = training.lexicon
print(training_lexicon.head())

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
