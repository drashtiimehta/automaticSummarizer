from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import  TextRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
#nltk.download()

LANGUAGE = "english"
SENTENCES_COUNT = 1


if __name__ == "__main__":
    url = "http://www.businessinsider.in/Heres-a-super-quick-guide-to-what-traders-are-talking-about-right-now/articleshow/59387381.cms"
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    print (parser.document)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print (sentence)
	
