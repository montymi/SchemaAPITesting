import requests
import json
import yaml

api='logistic_order_api.yaml'

# importing yaml files
with open(api, 'r') as file:
    try:
        lo_api=yaml.safe_load(file)
    except yaml.YAMLError:
        print("Error in configuration file: ", api)
        
paths=[path for path in lo_api.get("paths").items()]
for path in paths:
    print(f"({paths.index(path)}) {path[0]}")
chosen_path_index=input("\nPick path to be tested: ")
print("\nTesting ",end="")
print(f"\033[1;92m{paths[int(chosen_path_index)][0]}\033[00m ",end="")
print("for HTTP request types: ",end="")

# Input Spec Sheets
req_type=[req for k, req in paths[int(chosen_path_index)][1].items()]
example, schema=list(str([[[[f_path for key, f_path in spec.items()]
            for k, spec in ex.items()]
           for app, ex in v.items()]
          for content, v  in req_type[0].get('requestBody').items() if content == "content"]
                  ).replace("'","").replace("[","").replace("]","").split(", "))
# Testing
current_path=paths[int(chosen_path_index)][1]
http_request_type=[request for request in current_path.keys() if request in ['put', 'post', 'patch', 'get']]
print(f"\033[96m{http_request_type}\033[00m")
print("-----------------------------")
for req in http_request_type:
    print(f"\033[96m{req}\033[00m")
    codes_path=current_path.get(req).get('responses')
    codes=list(codes_path.keys())

    fpath=[]
    for i in range(len(codes)):
        content=codes_path.get(codes[i]).get("content")
        if content:
            e, s = [spec for key, spec in content.get("application/json").items()]
        fpath.append(e.get("$ref")) if content else fpath.append(None)

    tupled_list=list(zip(codes, fpath))
    file_path=dict(tupled_list)
    with open(s.get("$ref")) as jfile:
        try:
            sc=json.load(jfile)
            # Example file testing
            for k, v in file_path.items():
                if v:
                    with open(v, 'r') as f:
                        try:
                            ex=yaml.safe_load(f)
                        except yaml.YAMLError:
                            print("Error in configuration file: ", example)
                    print(f"PASSED: {v}") if sc.get("required") == list(ex.keys()) else print(f"Example file in path {v} missing required element")
                else: print(f"SKIPPED: No file to be tested for status code {k}")
            # HTTP Call Testing
            '''
            url=""
            match req:
                case "put":
                    response=requests.put(url)
                case "post":
                    response=requests.post(url)
                case "patch":
                    response=requests.patch(url)
                case "get":
                    response=requests.get(url)
            '''
        except ValueError:
              print("Error in configuration file: ", s.get("$ref"))
print("-----------------------------")
# Requests
print("\033[96msending\033[00m")
with open(schema, 'r') as json_file:
    try:
        sc=json.load(json_file)
        with open(example, 'r') as f:
            try:
                ex=yaml.safe_load(f)
            except yaml.YAMLError:
                print("Error in configuration file: ", example)
        print(f"PASSED: {v}") if sc.get("required") == list(ex.keys()) else print(f"Example file in path {v} missing required element")
    except ValueError:
        print("Error in configuration file: ", schema)
print("-----------------------------")

