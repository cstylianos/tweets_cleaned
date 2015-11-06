# tweets_cleaned

This repository contains python files in response to the Insight Data Engineering Coding Challenge.

The python files extract information (clean text and timestamp) and perform rolling average calculations on twitter raw data.

The python files are located in /src. 

A file (tweets.txt) that contains 10,000 tweets was used to test the python files. 

The first python file "tweets_cleaned.py" reads from file "tweets.txt" (located in /tweet_input) that
contains twitter data in JSON format. It then extracts the timestamp and clean text and writes in an output file, "ft1.txt", located in /tweet_output. 

Note: The file provides twitter text clean from escape and unicode characters. Each line in "ft1.txt" contains a cleaned tweet text followed by its timestamp. At the end of the file, the number of tweets that contain unicode is provided.

The second python file "average_degree.py" also reads from "tweets.txt" and provides the average vertex of a hashtag graph. The output is in "ft2.txt", located in /tweet.output. Each line in "ft2.txt" represents the rolling average.

Note: For the calculation of the rolling average, tweets with no hashtags or no hashtags were ignored. Only tweets that were within a 60 second window were taken into account.

The run the pyhon file, execute ./run.sh. Then provide the location of tweets.txt (./tweet_input/tweets.txt for example) and location of output file (./tweet_output.ft1.txt for example).
