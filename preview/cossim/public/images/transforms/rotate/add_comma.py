import os

import numpy as np


def main():
    res_dir = '/Users/ruthfong/papers/post--interactive_similarity/static/images/transforms/rotate/lines'    
    paths = [os.path.join(res_dir, f) for f in os.listdir(res_dir) if '.csv' in f]
    for path in paths:
        try:
            add_commas(path)
        except:
            print(f'Skipping {path}')


def add_commas(path):
    x = np.loadtxt(path)
    np.savetxt(path, x, fmt='%.2f', delimiter=',')


if __name__ == '__main__':
    main()