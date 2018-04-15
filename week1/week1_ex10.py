
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("config_file.txt")

crypto_map_no_aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO ", childspec=r"set transform-set AES-")

for i in crypto_map_no_aes:
    num=0
    print i
    for child in crypto_map_no_aes[num].children:
        print child.text
    num = num + 1
    print '\n'

