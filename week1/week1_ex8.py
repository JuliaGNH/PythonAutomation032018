
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("config_file.txt")

crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO ")

for i in crypto_map:
    num=0
    print i
    for child in crypto_map[num].children:
        print child.text
    num = num + 1
    print '\n'

