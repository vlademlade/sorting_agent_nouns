import logging
from gensim.models import Word2Vec
from gensim.corpora.wikicorpus import WikiCorpus


current_dir = "sort_csv/"
wiki_dir = current_dir + "/res/wiki/"
zipped_dump_path = current_dir + wiki_dir + "frwiki-20220301-pages-articles-multistream.xml.bz2"


class WikiSentences:

    def __init__(self, wiki_zipped_dump):
        logging.info('Parsing wiki corpus')
        self.wiki = WikiCorpus(wiki_zipped_dump, processes=7)

    def __iter__(self):
        for sentence in self.wiki.get_texts():
            yield list(sentence)


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = WikiSentences(zipped_dump_path)
    model = Word2Vec(sentences, vector_size=300, workers=7)
    model.save(wiki_dir + "frwiki.model")


if __name__ == '__main__':
    main()
