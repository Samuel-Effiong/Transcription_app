
import re
import pickle
import string
import numpy as np
from typing import List

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

from gensim.models.keyedvectors import KeyedVectors

from nltk.tokenize import NLTKWordTokenizer
from nltk.stem import WordNetLemmatizer


class SemanticSearch:
    def __init__(self, file_control):
        self.__file_control = file_control
        # load up vectorizer
        
        vectorizer_path = "models\\vectorizer.pkl"
        topic_model_path = "models\\pca.pkl"
        
        self.__load_vectorizer(vectorizer_path)
        self.__load_topic_model(topic_model_path)
        self.__load_topic_vectors()
        # load pretrained topic vectors models

    def __load_vectorizer(self, path=None):
        if path:
            with open(path, 'rb') as obj:
                self.__vectorizer = pickle.load(obj)
        else:
            self.__vectorizer = None

    def __load_topic_model(self, path=None):
        if path:
            with open(path, 'rb') as obj:
                self.__topic_model = pickle.load(obj)
        else:
            self.__topic_model = None

    def __load_topic_vectors(self):
        query = """SELECT "Topic Vectors", "Id" FROM "Sermons" """
        response = self.__file_control.database.raw_query(query, 1)
        response = {item[1]: item[0] for item in response}

        self.keyed_vectors = KeyedVectors(80)
        keys, values = list(response.keys()), list(response.values())
        self.keyed_vectors.add_vectors(keys, values)

    def __preprocess_result(self, result) -> str:
        result = " OR ".join([""""Id" = '{}'""".format(word) for word in result])
        result = f"({result})"
        return result
    
    @property
    def get_similar_texts(self) -> List[str]:
        return self.__result
    
    def compute_topic_vectors(self, text) -> np.ndarray:
        # take the result string and convert it to it vectorized form
        query_vectorized = self.__vectorizer.transform([text]).toarray()
        # convert the vectorized result to its topic vectors
        query_topic_vector = self.__topic_model.transform(query_vectorized).ravel()
        
        return query_topic_vector

    def search(self, query, *, additional_param=None) -> str:
        
        # self.__vectorizer.input = 'content'
        query_topic_vector = self.compute_topic_vectors(query)

        # compare result topic vector to the other transcripts and find the most similar
        result = self.keyed_vectors.similar_by_vector(query_topic_vector)
        self.__result = [similarity[0] for similarity in result]

        # preprocess the result into valid SQL result
        formatted_result = self.__preprocess_result(self.__result)

        if additional_param:
            additional_query = []
            coordinator = additional_param['coordinator']
            teacher = additional_param['teacher']

            year = additional_param['year']
            month = additional_param['month']
            day = additional_param['day']

            if year and not year == 'None':
                additional_query.append(f"""EXTRACT(YEAR FROM "Dates") = {year} """)
            if month and not month == 'None':
                additional_query.append(f"""TO_CHAR("Dates", 'Month') LIKE '%{month}%' """)
            if day and not day == 'None':
                additional_query.append(f"""TO_CHAR("Dates", 'Day') LIKE '%{day}%' """)

            if coordinator and not coordinator == 'None':
                additional_query.append(f""""Coordinators" = '{coordinator}' """)
            if teacher and not teacher == 'None':
                additional_query.append(f""""Teachers" = '{teacher}' """)
            if additional_query:
                additional_query = " AND ".join(additional_query)
                if formatted_result:
                    additional_query = f" AND ({additional_query})"
                else:
                    additional_query = f"{additional_query}"
                formatted_result += additional_query
        return formatted_result
