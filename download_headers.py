"""
Download the csv header files for each of the 2016 data files

Nathan @nate_somewhere
2017-03-12
"""

import os
import requests

headers = ["http://www.fec.gov/finance/disclosure/metadata/indiv_header_file.csv",
    "http://www.fec.gov/finance/disclosure/metadata/cm_header_file.csv",
    "http://www.fec.gov/finance/disclosure/metadata/cn_header_file.csv",
    "http://www.fec.gov/finance/disclosure/metadata/ccl_header_file.csv",
    "http://www.fec.gov/finance/disclosure/metadata/oth_header_file.csv",
    "http://www.fec.gov/finance/disclosure/metadata/pas2_header_file.csv",
    "http://www.fec.gov/finance/disclosure/metadata/oppexp_header_file.csv"]

if __name__ == '__main__':
    for fileurl in headers:
        filename = fileurl.split('/')[-1]
        r = requests.get(fileurl)
        file_path = os.path.join('data', 'headers', filename)
        with open(file_path, 'wb') as f:
            f.write(r.content)
