from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation
import heapq
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

def summarizer(extracted_text):
    
    extracted_text = re.sub(r'\[[0-9]*\]', ' ', extracted_text)
    extracted_text = re.sub(r'\s+', ' ', extracted_text)
    formatted_extracted_text = re.sub('[^a-zA-Z]', ' ', extracted_text)
    formatted_extracted_text = re.sub(r'\s+', ' ', formatted_extracted_text)

    sentence_list = nltk.sent_tokenize(extracted_text)
    stop_words = stopwords.words('english')
    word_freq = {}
    for word in nltk.word_tokenize(formatted_extracted_text):
        if word not in stop_words:
            if word not in word_freq.keys():
                word_freq[word] = 1
            else:
                word_freq[word] += 1

    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = (word_freq[word]/max_freq)

    sent_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_freq.keys():
                if len(sent.split(' ')) < 20:
                    if sent not in sent_scores.keys():
                        sent_scores[sent] = word_freq[word]
                    else:
                        sent_scores[sent] += word_freq[word]

    summarized_sentences = heapq.nlargest(5, sent_scores, key=sent_scores.get)
    summary = ' '.join(summarized_sentences)
    return summary
