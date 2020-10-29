import pandas as pd
import random
from Corpus.TurkishSplitter import TurkishSplitter as splitter
from NGram import NGram
from NGram import LaplaceSmoothing, GoodTuringSmoothing


class ARTICLE_Ngram():
    def __init__(self, raw_file):
        self.raw_text = self.get_raw_text(raw_file)
        self.sentences = self.get_sentence()
        self.corpus = self.get_corpus()
        self.words = self.get_words()

    # Reformating articles in one text
    def get_raw_text(self, raw_file):
        raw_text = ""
        for row in pd.read_csv(raw_file)['Text']:
            # Removing Nan and empty lines
            if len(str(row)) > 3:
                raw_text += str(row)
        print("Number of words in the corpus: {}".format(len(raw_text.split(" "))))
        return raw_text

    # Splitting the corpus into sentences
    def get_sentence(self):
        sentences = splitter().split(self.raw_text)
        print("Number of generated sentences: {}".format(len(sentences)))
        return sentences

    # Creating Corpus
    def get_corpus(self):
        corpus = []
        for sentence in self.sentences:
            sentence_text = []
            for word in sentence.getWords():
                # eliminate links from the corpus
                if 'http' in word.getName():
                    pass
                else:
                    sentence_text += [word.getName()]
            corpus += [sentence_text]
        return corpus

    # Create a list of corpus vocabulary
    def get_words(self):
        print("\nCreating vocabulary list...")
        words = []
        for sentence in self.corpus:
            for word in sentence:
                if word not in words:
                    words.append(word)
        print("\nNumber of Vocabularies: {}".format(len(words)))
        return words

    # Generate sentence based on Unigram model with Laplace smoothing:
    def generate_1gramlaplace_sentence(self, min, max):
        print('\nGenerating sample sentences using Unigram with Laplace...\n')
        sentences = []
        n = 0
        # Unigram model with Laplace smoothing
        gram_1_laplace = NGram.NGram(1, self.corpus)
        gram_1_laplace.calculateNGramProbabilitiesSimple(LaplaceSmoothing.LaplaceSmoothing())
        while n < 6:
            sentence = []
            first_word = random.choice(self.words)
            sentence.append(first_word)
            for x in range(max - 1):
                next_word = random.choice(self.words)
                sentence.append(next_word)
                # End the sentence if we hit . and met the min number of words
                if len(sentence) >= min and next_word == '.':
                    break
            sentence = ' '.join([str(item) for item in sentence]) + '.'
            sentences.append(sentence)
            n += 1
        for i in sentences:
            print(i)

    # Generate sentence based on Unigram model with Good-Turing:
    def generate_1gramGood_sentence(self, min, max):
        print('\nGenerating sample sentences using Unigram with Good-Turing...\n')
        sentences = []
        n = 0
        # Unigram model with Good-Turing smoothing
        gram_1_good = NGram.NGram(1, self.corpus)
        gram_1_good.calculateNGramProbabilitiesSimple(GoodTuringSmoothing.GoodTuringSmoothing())
        while n < 6:
            sentence = []
            first_word = random.choice(self.words)
            sentence.append(first_word)
            for x in range(max - 1):
                next_word = random.choice(self.words)
                sentence.append(next_word)
                # End the sentence if we hit . and met the min number of words
                if len(sentence) >= min and next_word == '.':
                    break
            sentence = ' '.join([str(item) for item in sentence]) + '.'
            sentences.append(sentence)
            n += 1
        for i in sentences:
            print(i)


    # Generate sentence based on Bigram model with Laplace smoothing:
    def generate_2gramlaplace_sentence(self, min, max):
        print('\nGenerating sample sentences using bigram with Laplace...\n')
        corpus_2 = self.corpus
        for i in corpus_2:
            i.insert(0, '<s>')
            i.insert(len(i), '</s>')
        sentences = []
        n = 0
        # Bigram model with Laplace smoothing
        gram_2_laplace = NGram.NGram(2, corpus_2)
        gram_2_laplace.calculateNGramProbabilitiesSimple(LaplaceSmoothing.LaplaceSmoothing())
        while n < 6:
            sentence = []
            # generate the first word
            start1 = '<s>'
            first_word = ''
            while True:
                possible_first = random.choice(self.words)
                if gram_2_laplace._NGram__getBiGramProbability(start1, possible_first) > 0.001:
                    first_word = possible_first
                    break
            sentence.append(start1)
            sentence.append(first_word)
            for x in range(max - 1):
                next_word = self.words[0]
                for word in self.words:
                    if gram_2_laplace._NGram__getBiGramProbability(first_word, word) \
                            > gram_2_laplace._NGram__getBiGramProbability(first_word, next_word) \
                            and word not in sentence:
                        next_word = word
                first_word = next_word
                sentence.append(next_word)
                # End the sentence if we hit . and met the min number of words
                if len(sentence) >= min and first_word == '.':
                    break
            sentence = ' '.join([str(item) for item in sentence]) + '.'
            sentences.append(sentence)
            n += 1
        for i in sentences:
            print(i)

    # Generate sentence based on Bigram model with Good-Turing smoothing:
    def generate_2gramGoodTuring_sentence(self, min, max):
        print('\nGenerating sample sentences using bigram with Good-Turing...\n')
        corpus_2 = self.corpus
        for i in corpus_2:
            i.insert(0, '<s>')
            i.insert(len(i), '</s>')
        sentences = []
        n = 0
        # Bigram model with GoodTurning smoothing
        gram_2_Good = NGram.NGram(2, corpus_2)
        gram_2_Good.calculateNGramProbabilitiesSimple(GoodTuringSmoothing.GoodTuringSmoothing())
        # If not given randomly choose a word
        while n < 6:
            sentence = []
            # generate the first word
            start1 = '<s>'
            first_word = ''
            while True:
                possible_first = random.choice(self.words)
                if gram_2_Good._NGram__getBiGramProbability(start1, possible_first) > 0.001:
                    first_word = possible_first
                    break
            sentence.append(start1)
            sentence.append(first_word)
            for x in range(max - 1):
                next_word = self.words[0]
                for word in self.words:
                    if gram_2_Good._NGram__getBiGramProbability(sentence[-1], word) \
                            > gram_2_Good._NGram__getBiGramProbability(sentence[-1], next_word) \
                            and word not in sentence:
                        next_word = word
                sentence.append(next_word)
                # End the sentence if we hit . and met the min number of words
                if len(sentence) >= min and first_word == '.':
                    break
            sentence = ' '.join([str(item) for item in sentence]) + '.'
            sentences.append(sentence)
            n += 1
        for i in sentences:
            print(i)


    # Generate sentence based on Trigram model with Laplace smoothing:
    def generate_3gramlaplace_sentence(self, min, max):
        print('\nGenerating sample sentences using Tigram with Laplace...\n')
        # Adding start and end charecters
        corpus_3 = self.corpus
        for i in corpus_3:
            i.insert(0, '<s>')
            i.insert(0, '<s>')
            i.insert(len(i), '</s>')
            i.insert(len(i), '</s>')
        sentences = []
        n = 0
        # Trigram model with Laplace smoothing
        gram_3_laplace = NGram.NGram(3, corpus_3)
        gram_3_laplace.calculateNGramProbabilitiesSimple(LaplaceSmoothing.LaplaceSmoothing())
        while n < 6:
            sentence = []
            # generate the first two words
            start1 = '<s>'
            start2 = '<s>'
            first_word = ''
            while True:
                possible_first = random.choice(self.words)
                if gram_3_laplace._NGram__getTriGramProbability(start1, start2, possible_first) > 0.001:
                    first_word = possible_first
                    break
            sentence.append(start1)
            sentence.append(start2)
            sentence.append(first_word)
            words = self.words
            for x in range(max - 1):
                third_word = words[0]
                for word in words:
                    if gram_3_laplace._NGram__getTriGramProbability(sentence[-2], sentence[-1], word) \
                            > gram_3_laplace._NGram__getTriGramProbability(sentence[-2], sentence[-1], third_word) \
                            and word not in sentence:
                        third_word = word
                        sentence.append(third_word)
                        words.remove(word)
                # End the sentence if we hit . and met the min number of words
                if len(sentence) >= min and third_word == '</s>':
                    break
            sentence = ' '.join([str(item) for item in sentence]) + '.'
            sentences.append(sentence)
            n += 1
        for i in sentences:
            print(i)

    # Generate sentence based on Trigram model with Good_turing smoothing:
    def generate_3gramGood_sentence(self, min, max):
        print('\nGenerating sample sentences using Trigram with Good-Turing...\n')
        # Adding start and end charecters
        corpus_3 = self.corpus
        for i in corpus_3:
            i.insert(0, '<s>')
            i.insert(0, '<s>')
            i.insert(len(i), '</s>')
            i.insert(len(i), '</s>')
        sentences = []
        n = 0
        # Trigram model with Good-Turing smoothing
        gram_3_Good = NGram.NGram(3, corpus_3)
        gram_3_Good.calculateNGramProbabilitiesSimple(GoodTuringSmoothing.GoodTuringSmoothing())
        while n < 6:
            sentence = []
            # generate the first two words
            start1 = '<s>'
            start2 = '<s>'
            first_word = ''
            while True:
                possible_first = random.choice(self.words)
                if gram_3_Good._NGram__getTriGramProbability(start1, start2, possible_first) > 0.001:
                    first_word = possible_first
                    break
            sentence.append(start1)
            sentence.append(start2)
            sentence.append(first_word)
            words =self.words
            for x in range(max-1):
                third_word = words[0]
                for word in words:
                    if gram_3_Good._NGram__getTriGramProbability(sentence[-2], sentence[-1], word) \
                            > gram_3_Good._NGram__getTriGramProbability(sentence[-2], sentence[-1], third_word) \
                            and word not in sentence:
                        third_word = word
                        sentence.append(third_word)
                        words.remove(word)
                # End the sentence if we hit . and met the min number of words
                if len(sentence) >= min and third_word == '</s>':
                    break
            sentence = ' '.join([str(item) for item in sentence]) + '.'
            sentences.append(sentence)
            n += 1
        for i in sentences:
            print(i)


    def save_corpus(self):
        with open('corpus.txt', 'w') as f:
            for item in self.corpus:
                f.write("{}\n".format(item))



n_gram = ARTICLE_Ngram('raw_articles.csv')
n_gram.generate_1gramlaplace_sentence(5,10)
n_gram.generate_1gramGood_sentence(5,10)
n_gram.generate_2gramlaplace_sentence(10,20)
n_gram.generate_2gramGoodTuring_sentence(10,20)
n_gram.generate_3gramlaplace_sentence(10,20)
n_gram.generate_3gramGood_sentence(10,20)

# n_gram.save_corpus()