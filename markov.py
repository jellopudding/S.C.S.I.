import random
import io
import json

class Markov:
	# words = []
	# vocab = {}
	# wordsFile = open("words.json", "+w")
	# vocabFile = open("vocab.json", "+w")
	# def __init__(self):
	# 	self.words = json.load(Markov.wordsFile)
	# 	self.vocab = json.load(Markov.vocabFile)
	#
	# def readText(self, txt):
	# 	txt = txt.split()
	# 	try:
	# 		for i in range(len(txt) - 1):
	# 			try:
	# 				self.vocab[txt[i]].append(txt[i + 1])
	# 			except:
	# 				self.vocab[txt[i]] = [txt[i + 1]]
	# 			self.words.append(txt[i])
	# 	except:
	# 		pass
	#
	# def writeText(self, n = 100):
	# 	text = [random.choice(self.words)]
	# 	n -= 1
	# 	try:
	# 		for i in range(n):
	# 			tmp = self.vocab[text[i]]
	# 			text.append(random.choice(tmp))
	# 	except KeyError:
	# 		return " ".join(text)
	# 	except IndexError as e:
	# 		return e
	# 	return " ".join(text)
	#
	# def save(self):
	# 	Markov.wordsFile.flush();
	# 	json.dump(self.words, Markov.wordsFile)
	# 	Markov.vocabFile.flush();
	# 	json.dump(self.vocab, Markov.vocabFile)
	#
	# def stop(self):
	# 	self.save(self)
	# 	self.vocabFile.close()
	# 	self.wordsFile.close()
	# 	print("Stopping Markov!")
	vocab = {}
	words = []

	def readText(txt):
		txt = txt.split()
		for i in range(len(txt) - 1):
			try:
				Markov.vocab[txt[i]].append(txt[i + 1])
			except:
				Markov.vocab[txt[i]] = [txt[i + 1]]
			Markov.words.append(txt[i])


	def writeText(n = 100):
		text = [random.choice(Markov.words)]
		n -= 1
		try:
			for i in range(n):
				tmp = Markov.vocab[text[i]]
				text.append(random.choice(tmp))
		except KeyError:
			print("Just a key error, nothing to see here!")
			return " ".join(text)
		finally:
			return " ".join(text)

if __name__ == "__main__":
	text = """test"""
	Markov.readText(text)
	print(Markov.writeText())
#test
