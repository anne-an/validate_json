import json
import glob
import os
from jsonschema import Draft4Validator

schemas = {}

with open('task_folder/schema/cmarker_created.schema') as f:
    cmarker_created = json.load(f)
    schemas['cmarker_created'] = cmarker_created

with open('task_folder/schema/label_selected.schema') as f:
    label_selected = json.load(f)
    schemas['label_selected'] = label_selected

with open('task_folder/schema/sleep_created.schema') as f:
    sleep_created = json.load(f)
    schemas['sleep_created'] = sleep_created

with open('task_folder/schema/workout_created.schema') as f:
    workout_created = json.load(f)
    schemas['workout_created'] = workout_created


def validate_json(data, schema):
    validator = Draft4Validator(schema)
    errors = validator.iter_errors(data)
    return errors


res = open('errors.txt', 'w', encoding='utf-8')
path = 'task_folder/event'

for schema in schemas.keys():
    for filename in glob.glob(os.path.join(path, '*.json')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            current_json = json.load(f)
            res.write('Schema: ' + schema + '\nJSON file: ' + filename[18:] + '\nErrors:\n')
            for error in validate_json(current_json, schemas[schema]):
                error = str(error).split('\n')
                error_text = error[0]
                res.write(error_text + '\n')
            res.write('\n')

res.close()