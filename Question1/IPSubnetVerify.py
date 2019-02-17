#!/usr/bin/python3
#Author - Ravi Ainampudi

from netaddr import IPNetwork
from sys import argv
from functools import lru_cache 
import os.path
from unittest import TestCase, main

system_arguments = argv[1:]
if len(system_arguments) == 2:
    system_arguments_check_file = [os.path.exists(system_arguments[0]), os.path.exists(system_arguments[1])]

def verify(pair):
    """This function is used to verify if pairs of 32 bit unsigned integer(hex) as an IP address is present in the given subnet or not."""
    try:
        pair = pair.split(" ")
        ip_int = int(pair[0], 16)
        subnet = pair[1]
        ip_address_func = lambda ip_int: map(str, [(ip_int >> j) % 256 for j in (24, 16, 8, 0)])
        ip_address = ".".join(list(ip_address_func(ip_int)))
        
        @lru_cache()
        def subnet_func(subnet):
            """Subnet function returns a list of available hosts in network with LRU cache for subnet(string)-hosts(list) data."""
            return [str(ip) for ip in IPNetwork(subnet)]

        if ip_address in subnet_func(subnet):
            return True
        else:
            return False

    except Exception as error:
        print(error)

if __name__ == "__main__":
    if len(system_arguments) == 0:
        #Test Cases executed when just the python file is an argumnet.
        class TestCases(TestCase):
            def test_check_True(self):
                self.assertTrue(verify("0x62D2EDEC 98.210.237.192/26"))
                self.assertTrue(verify("0x62D2EDD4 98.210.237.192/26"))
            def test_check_False(self):
                self.assertFalse(verify("0x62D2ED4B 98.210.237.192/26"))
                self.assertFalse(verify("0x62D2ED1C 98.210.237.192/26"))
        main()
        
    elif len(system_arguments) == 2:
        #If arguments are NOT files and only pair of 32 but unsigned integer and a subnet.
        if not system_arguments_check_file[0]:
            pair = " ".join([inp.strip() for inp in system_arguments])
            print(pair+ " = " + str(verify(pair)))
        
        #If files with input data and output filename passed as arguments. 
        else:
            #Read Input Data as pairs
            with open(system_arguments[0].strip(), "r") as file_read:
                file_read_input = [i.strip() for i in file_read.read().split("\n") if len(i) > 0]
        
            #write corresponding boolean result of those pairs. Ex: 0x62D2ED4B 98.210.237.192/26 = False
            with open(system_arguments[1].strip(),"w") as file_write:
                for pair in file_read_input:
                    file_write.write(pair +" = "+ str(verify(pair))+"\n")
                    
    else:
        print("Provide either Input and Output file names. Or, provide Unsigned 32 bit IP Address and subnet.")
