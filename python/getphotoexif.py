###
# File: getphotoexif.py
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

process = Popen([hunchly_api_path, 'photo', 'get', '-s', transform.values['hash']], stdout=PIPE, stderr=PIPE, errors="replace")

stdout, stderr = process.communicate()

try:

    result = json.loads(stdout)

    if result['number_of_results'] != 0:

        for result in result['photos']:

            if result['exif_data'] != None:

                for exif_key in result['exif_data']:
                    exif_phrase = "%s:%s" % (str(exif_key), str(result['exif_data'][exif_key]))

                    t = Phrase(exif_phrase)
                    t.entity_attributes['text'] = exif_phrase

                    convert_entity(transform, t)

except:
    transform.addUIMessage("Failed to retrieve results for %s" % transform.values['properties.hunchlycase'])

transform.returnOutput()
