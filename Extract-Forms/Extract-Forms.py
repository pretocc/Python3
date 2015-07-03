# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:17:41 2015
Python 3.4
@author: Preto

"""

from bs4 import BeautifulSoup
import urllib


def GetForms(url):
    """Search all the forms in the web and return a GET request."""

    URLs = []
    contents = urllib.request.urlopen(url)
    bs = BeautifulSoup(contents, "lxml")
    forms = bs.find_all('form')

    for f in forms:
        ilist = []
        postURL = url + f.attrs["action"] + "?"
        inputs = f.find_all('input')
        for i in inputs:
            if "name" in i.attrs:
                ilist.append(i.attrs["name"]+"=a")

        URLs.append(postURL + "&".join(ilist))

    return URLs


def GetWebUrllib(url):
    """ Submit a form with GET using urllib."""

    contents = urllib.request.urlopen(url)
    bs = BeautifulSoup(contents, "lxml")
    print(bs)


if __name__ == '__main__':

    urls = GetForms('http://host113.kvchosting.com/~pirataga/')

    for u in urls:
        print(u)
        GetWebUrllib(u)
