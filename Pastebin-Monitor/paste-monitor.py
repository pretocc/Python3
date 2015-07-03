# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:41:18 2015
Python 3.4
@author: Preto
"""

from bs4 import BeautifulSoup
import urllib
import os.path


def pastebin():
    """Search the archive of pastebin.com and get all the download links"""

    fdirpb = "C:\pastebins\\"  # Directorio donde se guardaran los pastes
    urlpbd = "http://pastebin.com/download.php?i="  # URL de descarga
    contents = urllib.request.urlopen("http://pastebin.com/archive")
    bs = BeautifulSoup(contents, "lxml")
    link = bs.find_all('table', {'class': 'maintable'})

    for l in link:
        href = l.find_all('a')
        for h in href:
            if 'href' in h.attrs:
                if 'archive' not in h['href']:
                    filepb = h['href'][1:]  # URL de cada enlace encontrado que contiene pastes
                    if filterurl(urlpbd+filepb) is True:
                        download(urlpbd+filepb, filepb, fdirpb)


def download(url, fname, fdir):
    """"Write the file to a folder only if don't exist.
         url - URL of the file to download.
         fname - Name for the downloaded file.
         fdir - Name of folder where the file will be downloaded."""
    if os.path.isfile(fdir+fname) is not True:
        
        try:
            fa = open(fdir+fname, "a")
            fileurl = urllib.request.urlopen(url)
            for f in fileurl:
                fa.write(f.decode('utf8'))
            fa.close()

        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            pass
        except:
            pass


def filterurl(urlf):
    """Check if a word is in the file.
        urlf - URL of the file to download and filter. """

    words = ["password", "passwd", "root", "@gmail.com", "DATABASE:", "login", "DB DUMP"]
    filt = urllib.request.urlopen(urlf)
    for f in filt:
        for w in words:
            if w.encode('utf8') in f:
                #print(w)
                return True


if __name__ == '__main__':
    
    pastebin()
