import gensim
from nltk.tokenize import word_tokenize

f = open("spoilers.txt","r")
x = f.readlines()

print dir(gensim)

raw_documents = x

gen_docs = [[w.lower() for w in word_tokenize(text)] for text in raw_documents]
gen_docs = [x for x in gen_docs if len(x) != 0 ]
print gen_docs

dictionary = gensim.corpora.Dictionary(gen_docs)
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
tf_idf = gensim.models.TfidfModel(corpus)
sims = gensim.similarities.Similarity('',tf_idf[corpus],num_features=len(dictionary))
print(sims)
print(type(sims))

query_doc = [w.lower() for w in word_tokenize("Jon Snow dies")]
print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
print(query_doc_bow)
query_doc_tf_idf = tf_idf[query_doc_bow]
print(query_doc_tf_idf)

print sims[query_doc_tf_idf]