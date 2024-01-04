import json
import sys

json_file = open(sys.argv[1])

deserialized_data = json.load(json_file)
