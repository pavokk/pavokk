import pandas as pd
pd.options.mode.chained_assignment = None # Ignoring a pandas error

# Replaces a column with ID's in 1 file with a mapping from another file. The mapping-file can only have 2 columns.


def id_to_name(source, target, t_column_id, t_column_model):
    print('Start!')
    dfs = pd.read_csv(source)
    dft = pd.read_csv(target)
    brand_map = dict(dfs.values)
    increment = 0

    for value in dft[t_column_id]:
        if value in brand_map.keys():
            dft[t_column_model][increment] = brand_map[value]
        else:
            pass
        
        increment += 1

    dft.to_csv('replaced-list.csv')
    print('Done.')


id_to_name('mock-brands.csv', 'mock-products.csv', 'Producer')
