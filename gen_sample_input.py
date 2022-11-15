import json

def dump_json(data, path):
    with open(path, 'w') as f:
        data_str = json.dumps(data, indent=4)
        f.write(data_str)


data = {'age': 82,
 'workclass': 'Private',
 'fnlwgt': 132870,
 'education': 'HS-grad',
 'marital.status': 'Widowed',
 'occupation': 'Exec-managerial',
 'relationship': 'Not-in-family',
 'race': 'White',
 'sex': 'Female',
 'capital.gain': 0,
 'capital.loss': 4356,
 'hours.per.week': 18,
 'native.country': 'United-States'}


dump_json(data, 'sample_input/sample_input.json')