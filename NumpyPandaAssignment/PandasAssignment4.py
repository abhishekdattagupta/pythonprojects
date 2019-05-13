'''
How to calculate the number of characters in each word in a series?
series = pd.Series(['how', 'to', 'kick', 'ass?'])
'''

import pandas as pd

series = pd.Series(['how', 'to', 'kick', 'ass?'])

print(series.map(lambda x: len(x)))