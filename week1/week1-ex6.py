import yaml
import json

week1_dict = {
    'ip_addr': '10.10.10.1',
    'mac_addr': '0a:fc:b4:7k:2d:1c'
}   

week1_list = [
    'exercise_6',
    'list_example',
    week1_dict
]


with open("week1_ex6.yml", "w") as f:
    f.write(yaml.dump(week1_list, default_flow_style=False))
with open("week1_ex6.json", "w") as k:
    json.dump(week1_list, k)


