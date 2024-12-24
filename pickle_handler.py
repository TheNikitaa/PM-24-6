import pickle

def load_table(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

def save_table(table, path):
    with open(path, 'wb') as file:
        pickle.dump(table, file)
