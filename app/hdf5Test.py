### Using pandas

import pandas as pd

#persist dataframe
with pd.HDFStore('../h5data/pytablesTest.h5') as store:
    store['key'] = pd.DataFrame()

#load dataframe
with pd.HDFStore('../h5data/pytablesTest.h5') as store:
    df = store['key']
    store = store

print(df)
print(store)

### Using numpy

import numpy as np
import h5py

a = np.random.random(size=(100,20))
h5f = h5py.File('../h5data/h5pyTest.h5', 'w')
h5f.create_dataset('dataset_1', data=a)
h5f.close()

h5f = h5py.File('../h5data/h5pyTest.h5','r')
b = h5f['dataset_1'][:]
h5f.close()

print(b)

np.allclose(a,b)
