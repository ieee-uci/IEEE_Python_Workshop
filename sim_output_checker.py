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

    if "e" in s: # scientific notation
        base, exponent = s.split( "e" )
        return float(base) * (10**float(exponent))
    elif s[-1] in engineering:
        return float(s[:-1]) * engineering[ s[-1] ]
    else:
        return float( s )

def read_file( f: "open file", field: str ) -> ( {str: {str:float} }, [] ):
    fields = []
    names_dict = defaultdict( dict )

    for line in f:
        line_split = line.split()

        if( len( line_split ) <= 1 ):
            continue

        if line_split[0] == "hierarchy":
            names = line_split[1:]
            device = next( f ).split()[1:]
            for l in f:
                l_split = l.split()
                if len( l_split ) <= 1:
                    break

                if l_split[0].lower().startswith( field ):
                    if l_split[0] not in fields:
                        fields.append( l_split[0] )
                    values = convert_to_numbers( l_split[1:] )
                    for i in range( len( names ) ):
                        names_dict[ names[i]+","+device[i] ][ l_split[0] ] = values[i]
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
                if field_name in field_dict and math.fabs( field_dict[ field_name ] ) >= cutpoint:
                    s += f"{field_dict[field_name]}"
                    marked = True
                s += ","
            if marked:
                print( s ) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser( description='parses spice output' )
    parser.add_argument( 'filename', type=str, help='filename of spice output' )
    parser.add_argument( 'field', type=str, help='start of field to parse for (v, i, vgs)' )
    parser.add_argument( 'cutpoint', type=float, help='cutpoint for field' )
    parser.add_argument( '--all', action='store_true', help='print all devices' )
    args = parser.parse_args()
    with open( args.filename, 'r' ) as f:
        names, field_names = read_file( f, args.field )
    print_result( args.cutpoint, names, field_names, args.all )

