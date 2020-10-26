import pandas as pd
from Corpus.TurkishSplitter import TurkishSplitter as splitter
from NGram import NGram
from NGram import LaplaceSmoothing
from Corpus.Sentence import Sentence
class ARTICLE_Ngram():
    def __init__(self, raw_file):
        self.raw_text = self.get_raw_text(raw_file)
        self.sentences = self.get_sentence()
        self.corpus = self.get_corpus()

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
                sentence_text += [word.getName()]
            corpus += [sentence_text]
        return corpus

    def save_corpus(self):
        with open('corpus.txt', 'w') as f:
            for item in self.corpus:
                f.write("{}\n".format(item))



n_gram = ARTICLE_Ngram('raw_articles.csv')

# n_gram.save_corpus()

gram_2 = NGram.NGram(2, n_gram.corpus)
gram_2_smooth = NGram.NGram(2, n_gram.corpus)
gram_2_smooth.calculateNGramProbabilitiesSimple(LaplaceSmoothing.LaplaceSmoothing())