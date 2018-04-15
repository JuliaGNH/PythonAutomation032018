import yaml
import json
from pprint import pprint as pp

with open("week1_ex6.yml") as f:
    yml_list = yaml.load(f)
with open("week1_ex6.json") as k:
    json_list = json.load(k)

print yml_list
pp(json_list)

