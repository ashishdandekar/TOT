import sys
import math
import pickle
import random
import matplotlib.pyplot as plt

def predict_topic(phi, words):
	temp = []
	for i in range(len(phi)):
		likelihood = 0
		for j in words:
			likelihood += (math.log(phi[i][j]) if phi[i][j] != 0 else math.log(0.0001))
		temp.append((likelihood, i))

	return max(temp)[1]
	#return max([(sum([math.log(phi[i][j]) for j in words]), i) for i in range(len(phi))])[1]

def evaluate(par, fname, first, norm):
	with open(fname) as test_file:
		differences = []
		count = 0
		for line in test_file:
			_, tweet, true_tp = line.strip().split('\t')
			tp = predict_topic(par['n'], [par['word_id'][i] for i in tweet.strip().split(' ') if i in par['word_id']])
			predicted_tp = random.betavariate(par['psi'][tp][0], par['psi'][tp][1])

			true_tp = (float(true_tp) - first) / norm
			differences.append(abs(float(true_tp) - predicted_tp))

			if count % 1000 == 0:
				print "Tested %d documents." % count
			count += 1
	plt.hist(differences, bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
	plt.xlabel('Differences')
	plt.ylabel('Number of Tweets')
	plt.show()

if __name__ == "__main__":
	resultspath = './results/'
	tot_pickle_path = resultspath + 'RG_tot.pickle'

	if len(sys.argv) != 4:
		print 'Usage: python %s <test_file> <first_timestamp> <last_timestamp>' % sys.argv[0]

	par = pickle.load(open(tot_pickle_path))
	first = float(sys.argv[2])
	last = float(sys.argv[3])
	evaluate(par, sys.argv[1], first, last - first)
