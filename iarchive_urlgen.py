#! bin/env python3
# -*- coding: utf-8 -*-
#
#  iarchive_urlgen.py
#  
#  Copyright 2019 Francesco Antoniazzi <francesco.antoniazzi1991@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import argparse
from urllib.parse import urlencode
#import requests
import json

baseurl = "https://archive.org/advancedsearch.php?"
choiceList = [
    "backup_location",
    "btih",
    "avg_rating",
    "call_number",
    "collection",
    "contributor",
    "coverage",
    "creator",
    "date",
    "description",
    "downloads",
    "external-identifier",
    "foldoutcount",
    "format",
    "genre",
    "headerImage",
    "identifier",
    "imagecount",
    "indexflag",
    "item_size",
    "language",
    "licenseurl",
    "mediatype",
    "members",
    "month",
    "name",
    "noindex",
    "num_reviews",
    "oai_updatedate",
    "publicdate",
    "publisher",
    "related-external-id",
    "reviewdate",
    "rights",
    "scanningcentre",
    "source",
    "stripped_tags",
    "subject",
    "title",
    "type",
    "volume",
    "week",
    "year"]

def main(args):
    if args["f"] is None:
	    urlArgs = []
    else:
        jsonurl = {"&fl[]": field for field in args["f"]}
        urlArgs = ["&"+urlencode({"fl[]": field}) for field in args["f"]]
    requestURL = baseurl + \
        urlencode({"q": "title:({}) AND mediatype:(audio)".format(args["pattern"]), 
		           "rows": args["r"], "page": args["p"], "output": "json", "save": "yes"}) + \
        "".join(urlArgs)
    print("URL: {}".format(requestURL))
    #r = requests.get(requestURL)
    #r.connection.close()
    #print("Status code: {}\nOutput: {}".format(r.status_code, r.text))
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Internet Archive query url generator")
    parser.add_argument("pattern", help="Pattern to be researched")
    parser.add_argument("-f", action="append", choices=choiceList, help="Fields to be returned")
    parser.add_argument("-r", action="store", default=50, help="Number of results")
    parser.add_argument("-p", action="store", default=1, help="Page number")
    arguments = vars(parser.parse_args())
    sys.exit(main(arguments))
