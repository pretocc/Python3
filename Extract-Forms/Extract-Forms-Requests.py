# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:14:47 2015
Python 3.4
@author: preto
"""

from bs4 import BeautifulSoup
import urllib
import requests


def GetForms(url):
    """Search all the forms in the web and return the values.\n
           actionURLS is a list with the action values.\n
           dlist is a list of dictionaries with the input name values.\n
           methods is a list with the method values (POST or GET)"""

    dlist = []
    actionURLS = []
    methods = []
    contents = urllib.request.urlopen(url)
    bs = BeautifulSoup(contents, "lxml")
    forms = bs.find_all("form")

    for f in forms:
        actionURL = url + f.attrs["action"]
        idic = {}
        inputs = f.find_all("input")

        if "method" in f.attrs:
            method = f.attrs["method"]
        else:
            method = "get"

        for i in inputs:
            if "name" in i.attrs:
                idic[i.attrs["name"]] = "'"

        dlist.append(idic)
        actionURLS.append(actionURL)
        methods.append(method)

    return actionURLS, dlist, methods


def GetWeb(url, data, method):
    """ Submit a form with POST or GET using Requests.\n
            url = URL of the form action.\n
            data = Dictionary with the input values.\n
            method = The method to use in the connection (POST or GET).\n """

    print("\n" + url)
    if method == "post":
        r = requests.post(url, data=data)
    elif method == "get":
        r = requests.get(url, params=data)
    print(r.content)

if __name__ == '__main__':

    url = 'http://host113.kvchosting.com/~pirataga/'
    content = GetForms(url)

    i = 0
    for c in content[0]:
        GetWeb(c, content[1][i], content[2][i])
