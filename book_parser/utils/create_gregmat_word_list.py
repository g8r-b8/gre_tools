'''Create gregmat word list.'''

import pandas as pd
import numpy as np
from itertools import chain

def parse_csv():
    ''' Parse csv in resc'''
    fp = '~/Projects/gre_tools/book_parser/resc/gregmat_vocab.csv'
    df = pd.read_csv(fp, header=None)
    values = df.values
    values = list(chain(*values))
    values = [e for e in values if e != np.nan if e != 'nan' if e if isinstance(e, str)]
    print(values[:10])
    print('Word Count: ', len(values))


if __name__ == "__main__":
    parse_csv()
