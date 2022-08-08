
import re
import string
from typing import List

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.corpus import stopwords

stop_word = set(stopwords.words('english') + list(ENGLISH_STOP_WORDS))


class KeywordSearch:
    def __init__(self, file_control):
        self.__file_control = file_control

    def preprocess_query(self, query) -> List[str]:
        query = [f'{re.sub(f"[{string.punctuation}]+", "", word)}' for word in query.split()]
        # remove stopwords from result
        query = [word for word in query if word not in stop_word]
        return query

    def search(self, query, *, additional_param: dict = None) -> str:
        if query:
            query = self.preprocess_query(query)
            if query:  # in case if the search result contains only stopwords
                formatted_query = " OR ".join([""""Messages" LIKE '%{}%'""".format(word) for word in query])
                formatted_query = f"({formatted_query})"
            else:
                formatted_query = ""
        else:
            formatted_query = ""

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
                if formatted_query:
                    additional_query = f" AND ({additional_query})"
                else:
                    additional_query = f"{additional_query}"
                formatted_query += additional_query
        return formatted_query
