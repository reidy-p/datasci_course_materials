import sys
import json

def clean_tweet(tweet_text):
    tweet_text = tweet_text.replace(',', '')
    tweet_text = tweet_text.replace('"', '')
    tweet_text = tweet_text.replace('#', '')
    tweet_text = tweet_text.lower()
    
    return tweet_text

def tweet_sentiment(tweet_text, scores):

    tweet_score = 0

    tweet_text = clean_tweet(tweet_text)
    all_words = tweet_text.split(' ')
    for w in all_words:
        if w.encode('utf-8') in scores.keys():
            tweet_score += scores[w]

    return tweet_score

if __name__ == '__main__':

    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)

    state_score = {}
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        d = json.loads(line)
        if 'text' in d.keys():
            location_dict = d['place']
            if location_dict is not None and location_dict['country'] == 'United States':
                state = location_dict['full_name'].split(',')[1]
                state = state.replace(' ', '')
                if state not in ['USA', 'US']:
                    if state in state_score.keys():
                        state_score[state] += [tweet_sentiment(d['text'], scores)]
                    else:
                        state_score[state] = [tweet_sentiment(d['text'], scores)]

    for state, score in state_score.items():
        state_score[state] = sum(score) / float(len(score))

    print(max(state_score, key=state_score.get))

