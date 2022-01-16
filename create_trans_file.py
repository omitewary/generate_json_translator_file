# INSTRUCTIONS:
# 1. Install python3 or above
# 2. Install packages translate, jproperties using - pip3 install translate, pip3 install jproperties
# 3. RUN command in terminal : python3 create_trans_file.py existing_file_path new_file_name from_lang to_lang
# 4. Example: python3 create_trans_file.py ./test.en.json test en es  -> It will generate test.es.json
# above command will generate tarns.es.json

# NOTE: This script uses microsoft translator. So user must have a secret access key to access Microsoft API.
# The secret access key in this script is fetched from trans.properties file.

import json
import sys
from json import JSONDecodeError
from translate import Translator
from jproperties import Properties

read_file_path = sys.argv[1]
file_name = sys.argv[2]
from_lang = sys.argv[3]
to_lang = sys.argv[4]

configs = Properties()

try:
    with open('trans.properties', 'rb') as read_prop:
        configs.load(read_prop)
        # Add your subscription key
        secret_key = configs.get("SECRET_KEY").data

        translator = Translator(provider='microsoft', from_lang=from_lang, to_lang=to_lang,
                                secret_access_key=secret_key)

        # Opening JSON file
        f = open(read_file_path)

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        print('data', data)

        for key, value in data.items():
            data[key] = translator.translate(value)
        print('test', data)

        filename = f'{file_name}.{to_lang}.json'
        json_object = json.dumps(data, indent=4, ensure_ascii=False)

        # Writing json to a file
        with open(filename, "w") as outfile:
            outfile.write(json_object)

        f.close()

except FileNotFoundError:
    print("Please enter correct file path!")

except JSONDecodeError:
    print("Json format is not correct")

except AttributeError as err:
    print(f'json attribute is not correct{err}')