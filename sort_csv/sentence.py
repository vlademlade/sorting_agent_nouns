class Sentence:

    def __init__(self, row):
        self.source = row.pop(0)
        self.left = row.pop(0)
        self.kwic = row.pop(0)
        self.right = row.pop(0)

    def get_noun(self):
        return self.kwic.split()[-1].lower()

    def get_similarity_with_centroid(self, model, centroid):
        try:
            return model.wv.cosine_similarities(centroid.vector, [model.wv.get_vector(self.get_noun())])[0]
        except:
            return 0.0
