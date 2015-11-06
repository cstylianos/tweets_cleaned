#!/usr/bin/env python2.7
"""
The objective of this code is to read from a file that
contains tweeter data in JSON format and extract the
timestamp and clean text in an output file. The text
has to be clean from escape and unicode characters.
The output must also provide the number of tweets that
contain unicode.

Tweet strings contain JSON data and the JSON
library will allow to use tweet strings as a
normal dictionary

Import JSON library
""" 
import json     # load JSON module

"""
Initialize count; unicode_count = tweets that contain unicode
"""

unicode_count=0

"""
Input filename with extension of file that
contains raw tweeter data
"""

input_file=raw_input("Insert input filename:")
output_file=raw_input("Insert output filename:")

"""
Open input and output files. Then read line by line
and extract timestamp and text fields which are 
"""
with open(input_file,'r') as input_f:                    # load file as input_f and close it automatically as soon as loop ends
    with open(output_file,'w') as output_f:
        for line in input_f:                                  # read line by line
            raw_tweet=json.loads(line)
            """ Extract timestamp and text
                Note: It was noticed that some lines did not
                contain tweeter data. For example, some lines were as follows:
                {"limit":{"track":6,"timestamp_ms":"1446218985909"}

                Therefore a condition was needed to test whether
                a line is consistent with the expected tweeter format.
                If not, that line is ignored.
            """
            if 'text' in raw_tweet:
                timestamp=raw_tweet['created_at']                    # extract timestamp
                raw_text=raw_tweet['text']                           # extract tweeter text
                """
                To check whether text has unicode characters
                a try/except method was selected. If a unicode characters
                is detected then the count is increased by one and the
                error is ignored.
                """
                try:                                                                 # try/except to check for unicode characters
                    """ Decode string to check for unicode error """
                    raw_text.decode('ascii')
                except UnicodeEncodeError:
                    """ If Unicode error then string contains unicode and count is increased by 1 """
                    unicode_count += 1                                               # count tweets with unicode
                """ Define escape characters """
                escapes = ''.join([chr(char) for char in range(1, 32)])
                """ Convert to ASCII, strip whitespaces and remove escape characters """
                clean_text=raw_text.encode('ascii',errors='ignore').strip().translate(None, escapes)  # convert to ASCII and ignore all symbols that are not supported
                """ Print timestamp and clean text in output file """
                output_f.write("%s (timestamp: %s)\n" % (clean_text, timestamp))              # print clean text and timestamp
        """ Print empty line and then the number of tweets that contain unicode """        
        output_f.write("\n%s tweets contained unicode" % unicode_count)                       #print total number of tweets with unicode


    

