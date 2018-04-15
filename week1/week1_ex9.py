
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("config_file.txt")

crypto_map_pfs_group2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO ", childspec=r"set pfs group2")

for i in crypto_map_pfs_group2:
    num=0
    print i
    for child in crypto_map_pfs_group2[num].children:
        print child.text
    num = num + 1
    print '\n'

