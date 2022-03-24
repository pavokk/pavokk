import pandas as pd

# Replaces a column with ID's in 1 file with a mapping from another file. The mapping-file can only have 2 columns.


def id_to_name(source, target, t_column):
    print('Start!')
    dfs = pd.read_csv(source)
    dft = pd.read_csv(target)

    brand_map = dict(dfs.values)
    increment = 0

    for value in dft[t_column]:
        dft[t_column][increment] = brand_map[value]
        increment += 1

    dft.to_csv('replaced-list.csv')
    print('Done.')


id_to_name('mock-brands.csv', 'mock-products.csv', 'Producer')
