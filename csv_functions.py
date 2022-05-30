import pandas as pd
pd.options.mode.chained_assignment = None


def replace_allcells_with_content(sourcefile, search, replace, encoding='utf-8'):
    """
    Search for specific phrase in csv-file and replace it.
    :param sourcefile: File to search
    :param search: Phrase to find
    :param replace: Phrase to replace with
    :param encoding: Encoding of the file, default is utf-8
    """

    print(f'Replacing cells that contains "{search}" with "{replace}" in {sourcefile}')
    df = pd.read_csv(sourcefile, encoding=encoding)

    for col in df.columns:
        increment = 0
        for cell in df[col]:
            if df[col][increment] == search:
                df[col][increment] = replace
            increment += 1
        print(f'Column {col} is done.')

    return df


def id_to_name(mapfile, sourcefile, columns):
    """
    Replaces numbers in specific columns with text from a mapping file.

    :param mapfile: csv-file with 2 columns. A: number, B: text
    :param sourcefile: csv-file to iterate through
    :param columns: array with header of columns in sourcefile to be changed
    """

    df_map = pd.read_csv(mapfile)
    df_source = pd.read_csv(sourcefile)
    item_map = dict(df_map.values)
    print(item_map)

    for col in columns:
        increment = 0
        changed = 0
        print(col)

        for value in df_source[col]:
            if value in item_map.keys():
                df_source[col][increment] = item_map[value]
                changed += 1
            increment += 1
        print(f'{col} processed. {changed} cells changed')

    df_source.to_csv('data/output/skvis-new-cats.csv')
    print('done.')
