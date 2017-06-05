# -*- coding: utf-8 -*-

## Getting a list of urls from a dictionary of internet domains
"""
Created on Sat Jan 21 10:10:25 2017 

@author: Liyi Li

"""
import subprocess
import sys
import os

#SEED DOMAINS
gov_domains = [
    ".un.org",
    ".undp.org"
    ]

# Fetching functions

def countPages (domains):
    command= 'python cdx-index-client\cdx-index-client.py -c'
    index = 'CC-MAIN-2016-50'
    search_prefix = '*'
    options = '--show-num-pages'
    for domain in gov_domains:
        subprocess.call(str(command +' '+ index + ' ' + search_prefix + domain + ' ' + options), shell=True)

def getUrls (domains):
    command= 'python cdx-index-client\cdx-index-client.py -c CC-MAIN-2016-50 *'
    options = '-j -d'  #use -z for .gz compressed files
    outputFolder = "D:\result2"     #create this directory manually
    for domain in gov_domains:
        subprocess.call(str(command + domain + ' ' + options + ' ' + outputFolder), shell=True)
        
#countPages(gov_domains)
getUrls(gov_domains)
