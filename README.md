# generate_json_translator_file
This is a simple python script to create json translation file. It uses microsoft translator

# INSTRUCTIONS:
# 1. Install python3 or above
# 2. Install packages translate, jproperties using - pip3 install translate, pip3 install jproperties
# 3. RUN command in terminal : python3 create_trans_file.py existing_file_path new_file_name from_lang to_lang
# 4. Example: python3 create_trans_file.py ./test.en.json test en es  -> It will generate test.es.json
# above command will generate tarns.es.json

# NOTE: This script uses microsoft translator. So user must have a secret access key to access Microsoft API.
# The secret access key in this script is fetched from trans.properties file.
