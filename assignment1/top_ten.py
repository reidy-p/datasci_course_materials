import sys
import json

hashtag_count = {}
tweet_file = open(sys.argv[1])
for line in tweet_file:
    d = json.loads(line)
    if 'entities' in d.keys():
        if d['entities']['hashtags']:
            for i in d['entities']['hashtags']:
                hashtag = i['text'] 
                if hashtag in hashtag_count.keys():
                    hashtag_count[hashtag] += 1
                else:
                    hashtag_count[hashtag] = 1

for name, c in sorted(hashtag_count.iteritems(), key=lambda (k, v): (-v, k))[:10]:
    print("{} {}".format(name.encode('utf-8'), c))

