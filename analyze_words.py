import pickle

if __name__ == "__main__":
	resultspath = './results/'
	tot_pickle_path = resultspath + 'RG_tot.pickle'
	tot_topic_vectors_path = resultspath + 'RG_tot_topic_vectors.csv'

	K = 20

	par = pickle.load(open(tot_pickle_path))
	for topic in par['n']:
		top_words = sorted([(j, i) for i, j in enumerate(topic)], reverse = True)[:K]
		print "TOPIC>>>>>"
		for prob, word_id in top_words:
			print par['word_token'][word_id]
		print "\n\n"
