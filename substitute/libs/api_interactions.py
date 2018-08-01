import json

import requests

class DataApiClient:
    """
    Class to get data of products from the API OpenFoodFacts
    """

    def __init__(self, **kwargs):
        self.query = kwargs.get("query", "")
        self.category = kwargs.get("category", "")
        self.nutriscore = kwargs.get("nutriscore", "")

    def get_data_from_api(self):
        """
        This function search a product in Open Food Facts from the query of the
        user
        """

        payload = {
            "search_terms2": self.query,
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": self.category,
            "tagtype_1": "nutrition_grades",
            "tag_contains_1": "contains",
            "tag_1": self.nutriscore,
            "page_size": 50,
            "search_simple": 1,
            "json": 1
        }
        search = requests.get(
                        "https://fr.openfoodfacts.org/cgi/search.pl",
                        params=payload
                        )
        data = search.json()
        # return a list of dictionaries. Every product is a dictionary
        return data["products"]


class Substitutes:
    """ This class allows to find substitutes of food """

    def __init__(self, query):
        self.query = query

    def _get_category(self):
        """
        This method get the category of a product
        """

        data = DataApiClient(query=self.query)
        data_from_api = data.get_data_from_api()
        # I've made the choice to select the first product from the results of
        # the user request, to find the category.
        product = data_from_api[0]
        # I choose the last categery of the list 'categories_hieararchy'
        category = product["categories_hierarchy"]
        category = category[-1]
        # I just want to keep the string after the caracters of the country
        # ex: "fr:pâte-a-tartiner"
        category = category[3:].replace("-", " ") # => regex
        return category

    def get_substitutes(self):
        """
        This method get a list of substitues from the category of a sought
        product.
        """

        substitute_category = self._get_category()
        substitutes = []
        index = 0
        nutrition_grades = ["a", "b", "c","d","e"]
        # The goal of this loop is to have substitutes in the same category of
        # the sought product. If the search with nutrition grade 'A' don't have
        # results, I search substitutes in same category but with higher
        # nutrition grade
        while len(substitutes) == 0:
            try:
                data = DataApiClient(
                                    category=substitute_category,
                                    nutriscore=nutrition_grades[index]
                                    )
                substitutes = data.get_data_from_api()
                index += 1
            except IndexError:
                substitutes = []
                break
        return substitutes