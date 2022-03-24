import pandas as pd

# Replaces a column with ID's in 1 file with a mapping from another file. The mapping-file can only have 2 columns.


def id_to_name(source, target, t_column):
    print('Start!')
    df_brands = pd.read_csv(source)
    df_products = pd.read_csv(target)

    brand_map = dict(df_brands.values)
    increment = 0

    for value in df_products[t_column]:
        df_products[t_column][increment] = brand_map[value]
        increment += 1

    df_products.to_csv('replaced-list.csv')
    print('Done.')


id_to_name('mock-brands.csv', 'mock-products.csv', 'Producer')
