"""
Download 2016 data from the FEC's FTP server 

Nathan @nate_somewhere
2017-03-12
"""
# http://www.fec.gov/finance/disclosure/ftpdet.shtml#a2015_2016

import os
from ftplib import FTP

if __name__ == '__main__':
    ftp = FTP('ftp.fec.gov', 'anonymous','anonymous')

    ftp.cwd("/FEC/2016/")
    file_list = []
    ftp.retrlines("NLST", file_list.append)

    for filename in file_list:
        if (filename == '.') or (filename == '..'):
            pass
        else:
            file_path = os.path.join('data', 'zipped', filename)
            ftp.retrbinary("RETR " + filename, open(file_path, "wb").write)
