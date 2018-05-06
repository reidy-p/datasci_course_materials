import sys
import json

def clean_tweet(tweet_text):
    tweet_text = tweet_text.replace(',', '')
    tweet_text = tweet_text.replace('"', '')
    tweet_text = tweet_text.replace('#', '')
    tweet_text = tweet_text.lower()
    
    return tweet_text

def main():
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet_score = 0
        d = json.loads(line)
        if 'text' in d.keys():
            tweet_text = clean_tweet(d['text'])
            all_words = tweet_text.split(' ')
            for w in all_words:
                if w.encode('utf-8') in scores.keys():
                    tweet_score += scores[w]
            
        print tweet_score

if __name__ == '__main__':
    main()

