The code comprises of following Python scripts:

	1. tot.py:
		This is the file which implements a Gibbs sampler
		for Events over Time.
		The parameters are defined in the method called' InitializeParameters'

	2. main.py:
		This code calls for the Gibbs Sampler for training dataset.
		It can be run as follows:
			python main.py <train_file>
			e.g: python main.py train.tsv

		REMINDER: Please create a folder called 'results' in the
				  directory where you run the code.

	3. visualize.py:
		It reads result files dumped in the 'results' folder.
		It gives visualization of the results.
			python visualize.py

	4. analyze_words.py:
		It gives top 20 word for each topics.
			python analyze_words.py

	5. evaluation.py:
		It implements time prediction to check the accuracy
		of the implemented method.
			python evaluation.py <test_file> <first_tp> <last_tp>
			python evaluation.py test.tsv 20131229160416 20140602223903

Both test and train files have following tab separated format:
	<tweet_id> <cleaned_text> <timestamp>
