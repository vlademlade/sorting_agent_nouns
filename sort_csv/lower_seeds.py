from gensim.models import Word2Vec


# model_path = "res/wiki/frwiki.model"
#
# model = Word2Vec.load(model_path)
#
# print(model.wv.most_similar("Mongol"))

with open("res/seeds/animate.txt", mode="r", encoding="utf-8") as seeds:
    with open("res/seeds/animate.txt", mode="w", encoding="utf-8") as new:
        for line in seeds:
            new.write(line.lower())

print("done")
