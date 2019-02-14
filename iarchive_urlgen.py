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
import requests
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
    jsonurl = {"&fl[]": field for field in args["f"]}
    urlArgs = ["&"+urlencode({"fl[]": field}) for field in args["f"]]
    requestURL = baseurl + \
        urlencode({"q": "title:({}) AND mediatype:(audio)".format(args["title"]), "output": "json"}) + \
        "".join(urlArgs)
    print("URL: {}".format(requestURL))
    r = requests.get(requestURL)
    r.connection.close()
    print("Status code: {}\nOutput: {}".format(r.status_code, r.text))
    print(jsonurl)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Internet Archive query url generator")
    parser.add_argument("title", help="Title contains")
    parser.add_argument("-f", action="append", required=True, choices=choiceList, help="Fields to be returned")
    arguments = vars(parser.parse_args())
    sys.exit(main(arguments))
