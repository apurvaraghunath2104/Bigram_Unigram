
import re

# Function to split a piece of text into sentences
# Arguments:
# text: A string containing input text
# Returns: sents (list)
# Where, sents (list) is a list of sentences that the text is split into
def get_sents(text):
	sents = re.split("[\n\.!?]", text)
	sents = list(filter(len, [s.strip() for s in sents]))
	return sents


# Function to split a sentence into a list of words
# Arguments:
# sent: A string containing input sentence
# Returns: words (list)
# Where, words (list) is a list of words that the sentence is split into
def get_words(sent):
	words = re.split(r"[^A-Za-z0-9-]", sent)
	words = list(filter(len, words))
	return words


# Function to get unigram counts
# Arguments:
# text: A string containing input text (may have multiple sentences)
# Returns: unigrams (dict)
# Where, unigrams (dict) is a python dictionary countaining lower case unigrams (words) as keys and counts as values
def get_unigram_counts(text):
	sents = get_sents(text)
	res_dict = {}
	for each_sent in sents:
		words = get_words(each_sent)
		for word in words:
			word = word.lower()
			if word in res_dict:
				res_dict[word] += 1
			else:
				res_dict[word] = 1
	return res_dict



# Function to get bigram counts
# Arguments:
# text: A string containing input text (may have multiple sentences)
# Returns: bigrams (dict)
# Where, unigrams (dict) is a python dictionary countaining lower case bigrams as keys and counts as values.
# Bigram keys must be formatted as two words separated by an underscore character
def get_bigram_counts(text):
	sents = get_sents(text)
	res_dict = {}
	res_list = []
	for each_sent in sents:
		words = get_words(each_sent)
		for i in range(0,len(words)):
			for j in range(i+1, len(words)):
				x = words[i:j+1]
				if len(x)==2:
					res_list.append(x)
	result = [[j.lower() for j in i] for i in res_list]
	result = ["_".join(i) for i in result]
	for i in result:
		if i in res_dict:
			res_dict[i]+=1
		else:
			res_dict[i]=1
	return res_dict


#
def main():

	with open('Book2.txt','r',encoding="utf8") as book2:
		text = book2.read()
	sents = get_sents(text)
	print("First sentence: {0}".format(sents[0]))
	print("Second sentence: {0}".format(sents[1]))

	# # Any sentence can then be converted into a list of wrods using get_words function
	words = get_words(sents[0])
	print("Words in first sentence: {0}".format(words))

	# Get unigram counts as
	counts = get_unigram_counts(text)
	print("Unigram counts: {0}".format(counts))

	with open('book2_unigram_output.csv', 'w') as book2_unigram_output:
		for key in counts.keys():
			book2_unigram_output.write("%s,%s\n"%(key,counts[key]))

	counts = get_bigram_counts(text)
	print("Bigram counts: {0}".format(counts))

	with open('book2_bigram_output.csv', 'w') as book2_bigram_output:
		for key in counts.keys():
			book2_bigram_output.write("%s,%s\n"%(key,counts[key]))
	return 0


################ Do not make any changes below this line ################
if __name__ == '__main__':
	exit(main())
