import numpy as np


current_dir = "sort_csv/"
seeds_path = current_dir + "res/seeds/animate_nodupl.txt"


class Centroid:

    def __init__(self, model):
        self.model = model

        word_vectors = self.model.wv
        seeds = []
        with open(seeds_path, "r", encoding="utf-8") as seeds_file:
            for line in seeds_file:
                try:
                    seeds.append(word_vectors[line.strip("\n")])
                except:
                    print(line + "is not in model vectors")
                    continue

        self.vector = np.average(seeds, axis=0)
