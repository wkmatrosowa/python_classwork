import os
import gensim

path = "/Users/vladislavasan/PycharmProjects/python_classwork_1/texts"

for root, dirs, files in os.walk(path):
    for fl in files:
        f = open("{}/{}".format(root, fl), encoding='utf8') #, encoding='latin1'
        for string in f:
            with open("training.txt", "a") as file:
                file.write(string)




# with open("training.txt", "w") as file:
#     file.write(f)
#
# train = "training.txt"
# data = gensim.models.word2vec.LineSentence(train) #делает отдельное предложение на отдельной строке
# model2 = gensim.models.Word2Vec(data, size=500, window=10, min_count=2, sg=0)
#
# model2.init_sims(replace=True)
#
# model2.init_sims(replace=True)
# model2.save("my_model2.model")
#
# word = "женщина"
# if word in model2:
#     for element in model2.wv.most_similar(positive=[word], topn=10):
#         print(element)