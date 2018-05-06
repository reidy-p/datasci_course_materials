import json
import sys

def clean_tweet(tweet_text):
    tweet_text = tweet_text.replace(',', '')
    tweet_text = tweet_text.replace('"', '')
    tweet_text = tweet_text.replace('#', '')
    tweet_text = tweet_text.replace('\t', '')
    tweet_text = tweet_text.replace('\n', '')
    tweet_text = tweet_text.lower()
    
    return tweet_text

def main():
    all_words = [] 
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        d = json.loads(line)
        if 'text' in d.keys():
            all_words += clean_tweet(d['text']).split(' ')
    
    word_freq = {}
    for w in all_words:
        if w in word_freq.keys():
            word_freq[w] += 1
        else:
            word_freq[w] = 1
    
    for key, val in word_freq.items():
        print "{} {}".format(key.encode('utf-8'), 
                             str(float(val) / len(all_words)))

if __name__ == "__main__":
    main()
