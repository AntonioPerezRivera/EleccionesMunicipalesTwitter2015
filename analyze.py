import json                                           # Importacion de modulos de python : json,pandas,plot.
import pandas as pd
import matplotlib.pyplot as plt
import re


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


def main():


	# Leyendo tweets...
	print 'Leyendo tweets..\n'
	tweets_data_path = 'tweet_data.txt'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_data.append(tweet)
	    except:
	        continue


	# Estructurando tweets...
	print 'Estructurando tweets...\n'
	tweets = pd.DataFrame()
	tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
	tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
	tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)


	print 'Procesando...'
	tweets['podemos'] = tweets['text'].apply(lambda tweet: word_in_text('podemos', tweet))
	tweets['psoe'] = tweets['text'].apply(lambda tweet: word_in_text('psoe', tweet))
	tweets['pp'] = tweets['text'].apply(lambda tweet: word_in_text('pp', tweet))


	# Analizando tweets segun mencion a partido politico
	print 'Analizando tweets segun mencion a partido politico...\n'
	prg_langs = ['podemos', 'psoe', 'pp']
	tweets_by_prg_lang = [tweets['podemos'].value_counts()[True], tweets['psoe'].value_counts()[True], tweets['pp'].value_counts()[True]]
	x_pos = list(range(len(prg_langs)))
	width = 1
	fig, ax = plt.subplots()
	plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='blue')
	ax.set_ylabel('Numero de tweets', fontsize=15)
	ax.set_title('Ranking: Podemos - PSOE - PP', fontsize=10, fontweight='bold')
	ax.set_xticks([p + 0.4 * width for p in x_pos])
	ax.set_xticklabels(prg_langs)
	plt.grid()
	plt.savefig('tweets_por_partido', format='png')


if __name__=='__main__':
	main()
