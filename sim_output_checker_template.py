#!/usr/bin/python3
from collections import defaultdict
import sys
import math
import argparse

def convert_to_numbers( l: [str] ) -> [float]:
    return [ convert_to_number( s ) for s in l ]

def convert_to_number( s: str ) -> float:
    engineering = { "m" : 10**-3,
                    "u" : 10**-6,
                    "n" : 10**-9,
                    "p" : 10**-12,
                    "f" : 10**-15,
                    "a" : 10**-18,
                    "z" : 10**-21
                   }

    # convert strings to numbers


def read_file( f: "open file", field: str ) -> ( {str: {str:float} }, [] ):
    fields = []
    names_dict = defaultdict( dict )

    for line in f:
        line_split = line.split()

        if( len( line_split ) <= 1 ):
            continue

        if line_split[0] == "hierarchy":
            # code here


    if fields:
        return names_dict, fields
    else:
        sys.stderr.write( "field name did not match any values, Aborting program immediately.\n" )
        exit()

def print_result( cutpoint: float, names: dict, field_names: str, print_all: bool ) -> None:
    s = "hierarchy, device"
    for field_name in field_names:
        s += "," + field_name
    print( s )

    if print_all == True:
        for name, field_dict in names.items():
            s = f"{name},"
            for field_name in field_names:
                if field_name in field_dict:
                    s += f"{field_dict[field_name]}"
            print( s )
    else:
        for name, field_dict in names.items():
            marked = False
            s = f"{name},"
            for field_name in field_names:
                # create string to print

if __name__ == "__main__":
    # write main here

