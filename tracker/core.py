import sgp4
from sgp4 import omm
import requests
import xml.etree.ElementTree as ET
import datatime

# Using new OMM (Orbital Mean elements Message) format over TLE
# https://celestrak.com/NORAD/documentation/gp-data-formats.php
url = 'https://celestrak.com/NORAD/elements/gp.php?CATNR=25544&FORMAT=xml' # ISS (Zarya)

def OMM(OMM_url):

    # Get response from celestrak
    OMM_url = url
    r = requests.get(OMM_url)
    if r.status_code != 200:
        print("There was an error getting the XML response for the OMM. GET error: {}".format(r.status_code))
    print(r.status_code)

    # Different things you can do with the response object
    # https://docs.python-requests.org/en/latest/user/quickstart/
    # print(r.content) # This returns a binary reponse
    # print('\n')
    # print(r.text)
    # print('\n')
    # print(r.encoding)

    # Grab all meta data from xml api response and put in a dict
    root = ET.fromstring(r.text) # https://docs.python.org/3/library/xml.etree.elementtree.html
    rdata = {}
    for data in root[0][1][0][0]:
        rdata[data.tag] = data.text
    for data in root[0][1][0][1][0]:
        rdata[data.tag] = data.text
    for data in root[0][1][0][1][1]:
        rdata[data.tag] = data.text
    # print(rdata)

    # I really should just go and grab the TLE seperately from the API if I want to use that eventually. Not now though
    #build TLE
    s = '1 ' + rdata['NORAD_CAT_ID'] + rdata['CLASSIFICATION_TYPE'] + ' ' \
        + rdata['OBJECT_ID'][2:4] + rdata['OBJECT_ID'][5:] + ' ' \
        + rdata['EPOCH'][2:4]
    print(s)
    # tle = [s = '', t = '']

if __name__ == '__main__':
    OMM(url)
