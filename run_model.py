import json
import argparse
import os
from model_predict import Model
from standard_payload import StandardPayload

REFERENCE_JSON = 'dependencies/standard_payload.json'


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def dump_json(data, path):
    with open(path, 'w') as f:
        data_str = json.dumps(data, indent=4)
        f.write(data_str)

def print_json(data):
    print(json.dumps(data, indent=4))

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('src', help='Source File of JSON Payload.')
    parser.add_argument('dst', help='Destination File of JSON Payload.')

    args = parser.parse_args()

    return args

def main():
    args = get_args()
    print(f'Reading file from {args.src}')

    # around here get file S3 and download locally
    

    # Get RAW JSON File
    raw_payload = load_json(args.src)

    model = Model()

    print('Making Prediction: ')
    print_json(raw_payload)

    std_payload = StandardPayload(ref_json=REFERENCE_JSON)

    input_payload = std_payload.validate_data(raw_payload)

    if input_payload['has_error']:
        print('Error Encountered: ')
        print_json(input_payload['error_msg'])
        return input_payload['error_msg']

    prediction = model.predict(input_payload['data'])
    final_output = {**raw_payload, **prediction}

    print('Prediction Output: ')
    print_json(final_output)
    
    print(f'Saving file to {args.dst}')
    dump_json(final_output, args.dst)

    # you can now upload to another S3





if __name__ == '__main__':
    main()
