import os
import glob
import zipfile


if __name__ == '__main__':
    all_files = glob.glob('data/zipped/**')

    zip_files = [fn for fn in all_files if fn.endswith('.zip')]

    for zfile in zip_files:
        zip_ref = zipfile.ZipFile(zfile, 'r')
        file_path = os.path.join('data')
        zip_ref.extractall(file_path)
