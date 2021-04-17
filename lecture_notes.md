# IEEE@UCI Python Primer (For Engineers!)

## What is Python?
Python is an interpreted, high-level, dyanmically-typed programming language that is very quickly becoming popular for all kinds of applications. Although many engineering products do not necessarily contain code written in Python (being an interpreted language, it executes slower than C/C++ or Java, which are compiled languages), Python can be used to help developement because it is good for scripting and visualizing data.

## Hello World
Python is an interpreted language, meaning it is run line by line rather than being compiled into machine code before the program begins running. This makes running Python programs slightly easier than running programs written in compiled languages; all you need is the Python interpreter.
Another highlight of Python is its easy to read syntax. To print to the screen, all you need to do is:
```python
>> print( "Hello World" )
Hello World
```
In Python 3, print is a function with many arguments, many of them default parameters we won't get into here, but a string object or an object that has a string representation is passed in and the corresponding string is printed on the screen. Easy enough!

## Python Built-in Data Types
Python's built-in data Types are much like ones you find in other programming languages like C/C++ or Java. 
- int - integer values
- float - floating point values (decimal points/fractions); unlike other languages, Python does not differentiate between single and double precision floating point numbers
- string - character strings; unlike in C/C++, Python does not differentiate between single and double quotes (which can be used interchangably) and does not have a concept of a char data type
- bool - Boolean values True and False (note capitalized first letters)
  
Python is dynamically typed; you do not need to specify types for variables and a variable that before held one type can hold another in a different statement
```Python
a = 3 # a is a variable of type int and holds values 3
a = "Hello World" # a is now a variable of type string and holds values "Hello World"
```

## Python Built-in Data Structures
Python has many built-in data structures that make working with Python very easy
### List
Python's concept of a list is much like the an array in C/Java; it is an ordered collection of objections that can be indexed with brackets. Unlike more strongly typed languages, lists can hold objects of different types.
```python
list1 = [ 1, "two", 3.4, True ]
```
Unlike arrays in strongly typed languages, a list's length is not fixed at its instantiation; elements can be continuously added to the end of the list. In this way, Python's lists resemble linked lists.
Lists are initialized by putting a comma separated list of values between square brackets.
```python
list1 = [1, 2, 3]
list1.append( 4 ) # value 4 is appended to the end of the list
list1. += [5] # value 5 is appended to the end of the list
```
### Tuple
Tuples are essentially immutable lists; they will always be the same size and contain the same contents as when they are initialized. They can be indexed like lists, but their contents cannot be changed nor can values be append to the end of them.
Tuples are initialized by putting a comma separated list of values between parantheses.
```python
tuple1 = ( 1, "two", 3.4 )
a = tuple1[1] # a tuple can index and the value can be used
tuple[1] = 5 # illegal
```
### Dictionary
Dictionaries are analogous to what are called hash maps in many different languages: a collection of key-value pairs, where the keys are unique. Like with lists and tuples, the types of the keys do not need to be the same, nor do the types of the values need to match the keys. Dictionaries can be indexed by key
Dictionaries are initialized with a comma separated list of key-value pairs in curly braces.
```python
dict1 = { 1:"one", 2:2.222, "true":True}
dict1[1] # returns one"
```

## Flow Control
Like many other programming languages, Python has flow control statements, many of which will be familiar if you've programmed in another language

### If-Elif-Else Statement
In python, much like many other language, has an if statement. If the conditional expression is true, a block of statements indented one tab over from where the if statement starts are executed.
```python
if conditional:
    # statements indented one tab over
elif (conditional):
    # statements indented one tab over
else:
    # statements indented one tab over
```
### For Loop
For loops can be used on any iterable - examples include lists, tuples, dictionaries, and files.
```python
for i in iterable:
    # do something with variable i
```
To loop by indices, use the range(n) iterable, which returns a iterable with values 0 to n-1.
```python
for index in range(len(iterable)):
    # do something with iterable element i
```

## Functions
To declare a function in python, use the keyword *def*, followed by the function name and a list of parameters enclosed in parenthesis.
```python
def func1( arg1, arg2, arg3 ):
    pass
```
Unlike in more stronly typed languages, you do not need to specify a return type or the type of the arguments. Any value can be passed in to the function; however, the code in the function will restrict the types of values that will make the function run to completion.

### Type Annotations
You can optionally specify parameter and return types. This does not affect the types of values that can be passed into and returned from the function but it is helpful for the readability of the code.
```python
def func1( arg1:int, arg2:float, arg3:str, arg4:[int]) -> dict, {int:float}:
    pass
```
## Argparse
Python has a library to create Command Line Interfaces called Argparse

## The Program
We have a Spice output for a power system.
```
###################### operating point information begin #######################
format: all
   time         = 20.0000u       temp         = 27.0000        tnom         = 27.0000     

0 :g_sub        = 10.8449f    3 :net16        = 1.1645      3 :en1          = 3.3000      
1 :net19        = 1.0017      0 :g            = 152.4094n   0 :net11        = 1.0017      
2 :net4         = 1.8062      3 :n3           = 3.3000      2 :ncas         = 1.5494      
2 :nb1          = 1.1497      2 :nd           = 2.3450      3 :n3           = 99.9950m    
2 :nb2          = 1.1870      2 :net6         = 2.9055      2 :x1           = 2.9060      
2 :pbias        = 2.2234      2 :n1           = 575.4628m   3 :n3           = 2.0361      
2 :pd           = 972.2594m   0 :on           = 3.3000      2 :en1          = 3.3000      
2 :net8         = 199.9832m   3 :n3           = 100.5529m   2 :nn1          = 199.9889m   
2 :pcas         = 1.8489      0 :net4         = 1.8314      3 :n3           = 902.8242m   
2 :xen          = 167.4890n   2 :net5         = 902.8242m   2 :net2         = 201.0989m   
3 :n3           = 99.9978m    3 :n3           = 902.8242m   3 :n3           = 40.4653n    
1 :net1         = 163.9592n   2 :xo1          = 902.8242m   2 :pp1          = 199.9950m
...
```
It's more than 2000 lines long. 

Somewhere in here, there are some mistakes. A few components are high (3.6V) when they shouldn't be. We will be writting a program to parse this output file to find the offending components. In the end, we want to have all offending components to be printed out in a table-like format so that it can be loaded as an Excel spreadsheet.

##### But aren't there programs already to do this?
Yes, but you are adding a check every cycle of your simulation for every single component of your circuit and when there are a lot of components, this scales extremely poorly. Running this program takes less than a second (saves a bunch of time).

### Converting strings to numbers
Starting with a small problem, we will figure out how to convert the strings containing numbers to floating point numbers. This is slightly complicated by how this output file has a mixture of scientific and engineering notation.
If you just have a number with no qualifiers, you can just stick the value in the ```float()``` function.
```python
num_float = float( num_string )
```
For the numbers with engineering notation, we first need to separate the suffix from the numerical part, which we can do with indexing:
```python
num, suffix = num_string[:-1], num_string[-1]
```
To turn the suffix into a number, we'll use a dictionary to store the values and use the suffix as the key.
```python
engineering = { "m" : 10**-3,
                "u" : 10**-6,
                "n" : 10**-9,
                "p" : 10**-12,
                "f" : 10**-15,
                 "a" : 10**-18,
                "z" : 10**-21
            }
suffix_num = engineering[suffix]
number = num * suffix_num
```
For the numbers in scientific notation, we need to check the number string to see if it contains an e, which can be done easily with the *in* operator and then split the string into two parts: the base and the exponent.
```python
base, exponent = num_string.split( "e" )
float(base) * (10**float(exponent))
```
Putting these all together we can get a function to convert any string representation of a number to a float
```python
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
```

### Reading the file
In python, file objects can be iterated over just like lists.
```python
# f is an open file object
for line in f:
    #do something with the line
    ...
```
(There are other ways to iterate over files in Python but this is most efficient way to do it)

Looking back to what we are parsing we can see a pattern in the output.
```
#### vccsBehavior:
hierarchy        xu1.x_c0         xu1.xi1.x_mp13   xu1.x_c1         xu1.x_c4         xu1.xi1.x_c8     
device           2:g1             3:g1             2:g1             2:g1             3:g1             
v                4.9983           0.0000           3.3000           5.1409           3.3000           
i                -399.3476a       0.0000           -2.0000f         5.7314p          -4.0000f         

hierarchy        xu1.xi_16.x_mp1  xu1.xi_17.x_mp1  xu1.xi3.x_c7     xu1.x_c2         xu1.xi1.x_mp10<1> 
device           3:g1             3:g1             3:g1             2:g1             3:g1             
v                3.3000           14.9558n         11.6536n         4.9983           0.0000           
i                0.0000           0.0000           -1.0000f         -10.0000f        0.0000           
```
Each line has a hierarchy and a device followed by a list of measurements taken. Taking the hierarchy and the device gives us a unique identifier for each component.

We read in the hierarchy line, then the device line, and then continue reading lines until a blank line or the next hierarchy line.

For the field, we are matching all fields that start with what the user inputted. For example, if a user inputed "v," then it would match "v", "vgs", and all other fields that start with v. Luckily there is a function that checks if a string starts with another string, aptly named ```startswith()```.

```python
if l_split[0].lower().startswith( field ):
    pass
```
All these fields will be added to a list that contains all the fields we mark down in order to create the top line of the table.

The full function is below:
```python
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
```

### Parsing Command Line Arguments and Main
Unlike in Java and C/C++, there is not a designated "main" function in Python; instead whatever file is run is considered the "main." Because of this, we use the line ```if __name__ == "__main__":``` to figure out whether this the file the program was launched from.
```python
if __name__ == "__main__":
    pass
```

In this main, we will parse the command line arguments using argparse. First we will define an instance of argparse:
```python
parser = argparse.ArgumentParser( description='parses spice output' )
```
Then we can add to the parser object all the arguments we want: the filename of the spice output, the field name we are parsing for, and the cutpoint for which we are looking for values. Additionally, we add the option to print all devices values as an optional argument.
```python
parser.add_argument( 'filename', type=str, help='filename of spice output' )
parser.add_argument( 'field', type=str, help='start of field to parse for (v, i, vgs)' )
parser.add_argument( 'cutpoint', type=float, help='cutpoint for field' )
parser.add_argument( '--all', action='store_true', help='print all devices' )
```
After configuring argparse to know what we are looking for, we simply call ```parse_args()``` to collect values.
```python
args = parser.parse_args()
```
After this, *args* holds all the parsed command line arguments, which we can access by their names (*args.filename*)

From here we just call the functions with the command line arguments to finish out our main.
```python
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
```