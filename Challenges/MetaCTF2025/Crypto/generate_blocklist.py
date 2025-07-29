# Problem: Dynamically Generated Attacker
# Copyright: MetaCTF 2019

from datetime import datetime
import string
from hashlib import md5
    
def generate_next_domain():
    curr_datetime = datetime.strptime('07/11/2019 19:38', '%m/%d/%Y %H:%M')
    prev_dom = '6c8553-f-21b9cc.top'
    next_dom = ''
    part1 = ''
    part2 = ''
    part3 = ''
    tld = ''
    
    # Write your code here

    next_dom = str(part1) + '-' + str(part2) + '-' + str(part3) + tld

    return next_dom

print(generate_next_domain())
