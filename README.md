# KWIC sentences sorter by noun agentivity

This project implements a method for sorting Key Word In Context (KWIC) sentences in French by the semantics of a target word in the sentence.


Using the Gensim library with Word2Vec modelling, the method first consists in training a distributional model based on a Wikipedia dump corpus. This model then serves to identify a semantic representation of a prototypical human agent by calculating the centroid of a set of vectors identified as human agents in the model (seeds).

The centroid can then be utilized as a benchmark for rating the agentiveness of a given word against it by measuring their cosine similarity. Given a set of French KWIC sentences containing a target word in a defined position, we can then sort these sentences in decreasing order of the agentivity of their target word.
