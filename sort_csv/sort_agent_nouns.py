from gensim.models import Word2Vec
import csv
import centroid as cd
import sentence as se

current_dir = "sort_csv/"
model_path = current_dir + "res/wiki/frwiki.model"
csv_path = current_dir + "res/frwac/concordance_preloaded_frtenten17_655.csv"
out_csv_path = current_dir + "res/frwac/out/out.csv"


def main():
    model = Word2Vec.load(model_path)

    sentences = dict()
    centroid = cd.Centroid(model)

    with open(csv_path) as csv_file:

        reader = csv.reader(csv_file)

        for row in reader:
            sentence = se.Sentence(row)
            key = sentence.get_similarity_with_centroid(model, centroid)

            if key not in sentences:
                sentences[key] = list()
                sentences[key].append(sentence)

            else:
                sentences[key].append(sentence)

    with open(out_csv_path, "wt") as outfile:

        writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)

        for key in sorted(sentences.keys(), reverse=True):
            writer.writerows([[
                sentence.source,
                sentence.left,
                sentence.kwic,
                sentence.right,
            ]
                for sentence in sentences[key]
            ])

    print("Process finished")


if __name__ == '__main__':
    main()
