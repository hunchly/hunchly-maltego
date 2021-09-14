###
# File: getselectors.py
# Authors: Divya Bhagavathiappan (divya@hunch.ly) and Justin Seitz (justin@hunch.ly)
# Last modified: 2021-02-19
###


import json
from entities import *
from MaltegoTransform import *
from config import *
from subprocess import Popen, PIPE

# initialize the transform object
transform = MaltegoTransform()
transform.parseArguments(sys.argv)

# if passed a HunchlyPage we have a page_id
if transform.values.get("page_id"):
    process = Popen([hunchly_api_path, 'selector', 'get', '-p', transform.values['page_id']], stdout=PIPE, stderr=PIPE, errors="replace")
else:
    process = Popen([hunchly_api_path, 'selector', 'get', '-n', transform.values['properties.hunchlycase']],
                    stdout=PIPE, stderr=PIPE, errors="replace")

stdout, stderr = process.communicate()

try:

    result = json.loads(stdout)

    if result['number_of_results'] != 0:

        for result in result['selectors']:
            t = HunchlySelector(result['selector'])

            convert_entity(transform, t)

except:
    transform.addUIMessage("Failed to retrieve results for %s" % transform.values['properties.hunchlycase'])

transform.returnOutput()
