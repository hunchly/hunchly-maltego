###
# File: getpages.py
# Authors: Divya Bhagavathiappan (divya@hunch.ly) and Justin Seitz (justin@hunch.ly)
# Last modified: 2021-02-19
###

import json
import sys
from entities import *
from MaltegoTransform import *
from config import *
from subprocess import Popen, PIPE
from html import escape

# initialize the transform object
transform = MaltegoTransform()
transform.parseArguments(sys.argv)

process = Popen([hunchly_api_path, "page", "list", "-n", transform.values['properties.hunchlycase']], stdout=PIPE,
                stderr=PIPE, errors="ignore")
stdout, stderr = process.communicate()

try:

    result = json.loads(stdout)

    for result in result['pages']:
        t = HunchlyPage(result['url'])
        t.entity_attributes['url'] = result['url']
        t.entity_attributes['page_id'] = str(result['id'])
        t.entity_attributes['title'] = escape(result['title'])
        t.entity_attributes['short-title'] = escape(result['title'])

        convert_entity(transform, t)

except:
    transform.addUIMessage("Failed to retrieve results for %s" % transform.values['properties.hunchlycase'])

transform.returnOutput()
