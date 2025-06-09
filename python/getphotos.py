###
# File: getphotos.py
# Authors: Divya Bhagavathiappan (divya@hunch.ly) and Justin Seitz (justin@hunch.ly)
# Last modified: 2025-06-09
###

import json
import sys
from pathlib import Path
from entities import *
from MaltegoTransform import *
from config import *
from subprocess import Popen, PIPE

# initialize the transform object
transform = MaltegoTransform()
transform.parseArguments(sys.argv)

# if passed a HunchlyPage we have a page_id
if transform.values.get("page_id"):
    process = Popen([hunchly_api_path, 'photo', 'get', '-p', transform.values['page_id']], stdout=PIPE, stderr=PIPE, errors="ignore")
else:
    process = Popen([hunchly_api_path, 'photo', 'get', '-n', transform.values['properties.hunchlycase']], stdout=PIPE,
                    stderr=PIPE, errors="replace")

stdout, stderr = process.communicate()

try:

    result = json.loads(stdout)

    if result['number_of_results'] != 0:

        for photo_result in result['photos']:
            try:
                # Get the raw file path from the Hunchly API result
                raw_path = photo_result.get('photo_local_file_path')

                # Skip if the path is missing
                if not raw_path:
                    continue

                # Use Python's pathlib to create a proper, cross-platform file URI
                local_file_uri = Path(raw_path).as_uri()

                # Create the HunchlyPhoto entity object
                t = HunchlyPhoto(photo_result['photo_hash'])
                t.entity_attributes['url'] = photo_result['photo_url']
                t.entity_attributes['hash'] = photo_result['photo_hash']
                
                # Store the clickable URI as a property in the entity's details
                t.entity_attributes['local_file'] = local_file_uri

                # Add the entity to the transform and get the Maltego object back
                maltego_entity = convert_entity(transform, t)
                
                # SET THE ICON: Tell Maltego to use the local file URI for the entity's graphic
                maltego_entity.setIconURL(local_file_uri)

            except Exception as e:
                # If there's an error processing a single photo, log it and continue
                transform.addUIMessage(f"Could not process photo {photo_result.get('photo_hash')}: {e}")

except Exception as e:
    transform.addUIMessage(f"Failed to retrieve results for {transform.values.get('properties.hunchlycase', 'Unknown Case')}: {e}")

transform.returnOutput()
