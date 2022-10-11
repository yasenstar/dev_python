# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'], index=['a', 'b', 'c', 'd'])

print(df)

df['floats'] = (1.5, 2.5, 3.5, 4.5)

print(df)

df['names'] = pd.DataFrame(['Yves', 'Guido', 'Felix', 'Francesc'], index = ['d', 'a', 'b', 'c'])

print(df)

df = df.append(pd.DataFrame({'numbers': 100, 'floats': 5.75, 'names': 'Henry'}, index=['z']))

print(df)

df=df.join(pd.DataFrame([1, 4, 9, 16, 25], index=['a', 'b', 'c', 'd', 'y'], columns=['squares',]), how='outer')

print(df)

print(df[['numbers', 'squares']].mean())