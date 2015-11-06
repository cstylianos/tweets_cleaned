"""
The objective of this code is to read from a file that
contains twitter data in JSON format, extract the
hashtags, create an edge list and calculate the rolling average.
The average for each tweet is the written to an output file.

Twitter strings contain JSON data and the JSON
library will allow to use tweet strings as a
normal dictionary

Import JSON library
""" 
import json                               # load JSON module
"""
Import RE module. It will be used
to extract hashtags from a tweet
"""
import re                                 # load re module
"""
Datetime library is required to extract
time from tweet timestapm
"""
import datetime as dt                     #load datetime module
"""
Itertools library is needed to calculate
the number of hashtags connections
"""
from itertools import permutations        # load itertools module
"""
Initialize parameters
"""
total_nodes=0
j1=0
m=0
edgelist=[]
"""
Input filename with extension of input file that
contains raw twitter data
"""
input_file=raw_input("Insert input filename:")
output_file=raw_input("Insert output filename:")

"""
Open input and output files. Then read line by line
and extract timestamp and text fields. 
"""
with open(input_file,'r') as input_f:               # load input file as input_f and close it automatically as soon as loop ends
    with open(output_file,'w') as output_f:         # load output file as output_f and close it automatically as soon as loop ends
        """ Read lines from file. Note: Probably not an optimal way to read from a file """
        line=input_f.readlines()
        while m < len(line):
            """ Initialize time difference """
            time_diff=0
            """ Extract tweet from line m """
            raw_tweet=json.loads(line[m])
            """ Increment line number """
            m +=1
            """ Extract timestamp
                Note: It was noticed that some lines did not
                contain tweeter data. For example, some lines were as follows:
                {"limit":{"track":6,"timestamp_ms":"1446218985909"}

                Therefore a condition was needed to test whether
                a line is consistent with the expected tweeter format.
                If not, that line is ignored.
            """
            if 'text' in raw_tweet:
                """ Extract timestamp and hashtag Note: remove duplicates """
                timestamp=raw_tweet['created_at'].split()
                raw_text=raw_tweet['text']
                start_hash_tag=[re.sub(r"(\W+)$", "", j, flags=re.UNICODE) for j in set([i for i in raw_text.split() if i.startswith("#")])]
                """ Create an edgelist that will contain the edges of the initial tweets """  
                start_edgelist=[]
                """ Calculate number of connections between hashtags in initial tweet """
                for p in permutations(start_hash_tag,2):
                    """ Update edge list """
                    start_edgelist.append(p)
                """ Calculate time of initial tweet """
                start = dt.datetime.strptime(timestamp[3], '%H:%M:%S')
                """ The following loop includes only the tweets appeared within the 60 seconds window """
                while time_diff<60:
                    """ Extract tweet data """
                    raw_tweet=json.loads(line[j1])
                    j1 +=1
                    if 'text' in raw_tweet:
                        """ Extract timestamp """
                        timestamp=raw_tweet['created_at'].split()
                        " time of latest tweet """
                        end = dt.datetime.strptime(timestamp[3], '%H:%M:%S')
                        """ Time difference between first and current tweet in seconds """
                        time_diff=(end - start).seconds
                        """ Extract hashtags from tweet - Note: remove duplicates """
                        raw_text=raw_tweet['text']
                        hash_tag=[re.sub(r"(\W+)$", "", j, flags=re.UNICODE) for j in set([i for i in raw_text.split() if i.startswith("#")])]
                        """ if tweet contains more than two hashtags (reject tweets with less than one hashtag) then: """
                        if len(hash_tag)>1:
                            """ Number of hashtags, i.e.,nodes, in latest tweet """
                            nodes=len(hash_tag)
                            """ Calculate number of connections between hashtags in latest tweet """
                            for p in permutations(hash_tag,2):
                                """ Update edge list """
                                edgelist.append(p)
                            """ Calculate number of edges """
                            edges=len(edgelist)
                            """ Update number of nodes to provide the total number of nodes within the 60 seconds window  """
                            total_nodes=total_nodes+nodes
                            """ Calculate average of tweets within the 60 seconds window """
                            average=float(edges)/total_nodes
                            """ Print rolling average in output file """
                            output_f.write("%.2f\n" % average)
                            """ Read next tweet while time difference between initial and latest tweet is less than 60 seconds """
                """ Remove initial tweet which is not outside from the 60 seconds window and update the edgelist and number of nodes """
                total_nodes=total_nodes-len(start_hash_tag)
                edgelist=edgelist[len(start_edgelist):]
                """ Go back to start and read from next line and repeat """
