import pandas as pd
import glob

def get_raw_data():
    data = []
    for f in sorted(glob.glob('./data/*.json')):
        temp = pd.read_json(f)
        data.append(temp)
    return pd.concat(data)

def get_clean_data():
    train = pd.read_csv('./CleanData/train_svm.csv')
    validation = pd.read_csv('./CleanData/valid_svm.csv')
    test = pd.read_csv('./CleanData/test_svm.csv')
    return train, validation, test


if __name__ == '__main__':
    print(get_data().head())
