import random
import io
import json
import time


class Markov:
    try:
        wordsFile = open("words.json", "+r")
        vocabFile = open("vocab.json", "+r")
        words = json.load(wordsFile)
        vocab = json.load(vocabFile)
    except:
        wordsFile = open("words.json", "+w")
        vocabFile = open("vocab.json", "+w")
        words = []
        vocab = {}

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

    def readText(txt):
        txt = txt.split()
        for i in range(len(txt) - 1):
            try:
                Markov.vocab[txt[i]].append(txt[i + 1])
            except:
                Markov.vocab[txt[i]] = [txt[i + 1]]
            Markov.words.append(txt[i])

    def save():
        Markov.wordsFile.flush()
        Markov.vocabFile.flush()
        json.dump(Markov.words, Markov.wordsFile, sort_keys=True)
        json.dump(Markov.vocab, Markov.vocabFile, sort_keys=True)

    def writeText(n=10):
        print("writing")
        text = [random.choice(Markov.words)]
        n -= 1
        for i in range(n):
            try:
                tmp = Markov.vocab[text[i]]
            except KeyError:
                print("Just a key error, nothing to see here!")
                time.sleep(0.05)
                tmp = Markov.vocab[random.choice(Markov.words)]
            text.append(random.choice(tmp))
        return " ".join(text)

    def stop():
        Markov.save()
        Markov.vocabFile.close()
        Markov.wordsFile.close()


if __name__ == "__main__":
    Markov.readText("this is a test")
    Markov.readText("a mighty fine test indeed")
    print(Markov.writeText())
    Markov.stop()
# test
