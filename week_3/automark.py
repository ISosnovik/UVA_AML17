from __future__ import print_function
import os
import sys
import json
import requests
import shutil
import numpy as np
import hashlib
import pickle


class Config:
    host = 'http://ec2-18-194-63-174.eu-central-1.compute.amazonaws.com:8080/'
    test_folder = 'local_tests'
    test_name = 'tests.pickle'
    test_path = os.path.join(test_folder, test_name)

# Local tests
def __remove_local_tests():
    try:
        os.remove(Config.test_path)
        print('Current version of remote tests is deprecated. '
              'Tests are removed.')
        sys.stdout.flush()
    except FileNotFoundError:
        pass


def __load_local_tests():
    if not os.path.exists(Config.test_folder):
        os.mkdir(Config.test_folder)

    try:
        endpoint = Config.host + 'loadtests'
        stream = requests.get(endpoint, stream=True)
        with open(Config.test_path, 'wb') as f:
            stream.raw.decode_content = True
            shutil.copyfileobj(stream.raw, f)  
        print('Local tests are downloaded.')
        sys.stdout.flush()
    except:
        print('Error downloading local tests.')


def __local_tests_are_valid():
    try:
        hash_md5 = hashlib.md5()
        with open(Config.test_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        local_md5 =  hash_md5.hexdigest()
        endpoint = Config.host + 'checksum/{}'.format(local_md5)
        response = requests.get(endpoint).json()
        return response['success']
    except:
        return False


def __passed_local_tests(function, arg_keys):
    with open(Config.test_path, 'rb') as f:
        test_data = pickle.load(f, encoding='latin1') 
    data = test_data[function.__name__]
    inputs = data['inputs']
    outputs = data['outputs']

    for in_, out_ in zip(inputs, outputs):
        args_ = {k:in_[k] for k in arg_keys}
        answer = function(**args_)
        if not np.allclose(answer, out_, rtol=1e-5, atol=1e-5):
            return False
    return True


# Remote tests
def __run_remote_test(username, function, arg_keys):
    endpoint = Config.host + 'input/{}/{}'.format(username, function.__name__)
    response = requests.get(endpoint)
    try:
        data = response.json()
    except: 
        print('Error loading response. Check `username`, '
              '`function` and the list of arguements')
        return 

    arguements = []
    for key in arg_keys:
        arg_ = data['input'][key]
        arg_value = data['input'][key]['data']
        if arg_['type'] == 'ndarray':
            arg_value = np.array(arg_value)
        arguements.append(arg_value)

    test_result = function(*arguements)
    test_result = np.array(test_result).tolist()
    endpoint = Config.host
    endpoint += 'result/{}/{}/{}/{}'.format(username, function.__name__, data['ipd'], json.dumps(test_result))

    answer_response = requests.get(endpoint).json()

    if answer_response['correct']:
        print("Test was successful. Congratulations!")
    else:
        print("Test failed. Please review your code.")


def get_progress(username):
    endpoint = Config.host + 'submissions/{}'.format(username)
    print(endpoint)


def register_id(username, credentials):
    endpoint = Config.host 
    endpoint += 'register_user/{}/{}/{}'.format(username, credentials[0], credentials[1])
    response = requests.get(endpoint)
    try:
        print(response.text)
    except:
        print("Something went wrong.")


def test_student_function(username, function, arg_keys):
    if not __local_tests_are_valid():
        __remove_local_tests()
        __load_local_tests()

    print('Running local tests...')
    if __passed_local_tests(function, arg_keys):
        print('{} successfully passed local tests'.format(function.__name__))
        print('Running remote tests...')
        sys.stdout.flush()
        __run_remote_test(username, function, arg_keys)
    else:
        print('{} failed some local tests'.format(function.__name__))








