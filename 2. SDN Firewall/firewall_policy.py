#!/usr/bin/python
															
"Project 2 - This creates the firewall policy. "

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import packets
from pyretic.core import packet

def make_firewall_policy(config):
    # TODO - This is where you need to write the functionality to create the
    # firewall. What is passed in is a list of rules that you must implement.
    
    # feel free to remove the following "print config" line once you no longer need it
    print config # for demonstration purposes only, so you can see the format of the config

    rules = []
    for entry in config:
        rule = match(ethtype=packet.IPV4, protocol=packet.TCP_PROTO)
        if entry['srcmac'] != '*':
            rule =  rule >> match(srcmac=MAC(entry['srcmac']))
        
        if entry['dstmac'] != '*':
            rule = rule >> match(srcmac=MAC(entry['dstmac']))
        
        if entry['srcip'] != '*':
            rule = rule >> match(srcip=entry['srcip'])
        
        if entry['dstip'] != '*':
            rule = rule >> match(dstip=entry['dstip'])
        
        if entry['srcport'] != '*':
            rule = rule >> match(srcport=int(entry['srcport']))
        
        if entry['dstport'] != '*':
            rule =  rule >> match(dstport=int(entry['dstport']))
        
        rules.append(rule)
       
        
        
    
    allowed = ~(union(rules))

    return allowed
