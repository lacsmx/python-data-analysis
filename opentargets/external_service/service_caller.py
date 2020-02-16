import requests

class ServiceCaller:
    """
    Class for generic API operations:
    - get http operation
    """
    
    def __init__(self, base_url):
        """
        Constructor for any Service Endpoint
        """
        self.base_url = base_url

    def get(self, query_map):
        """
        Query over current instance's base URL using a dictionary stored in query_map
        param:value

        return 
        A json object
        """
        print("GET on REST API " + self.base_url)
        print(query_map)
        response = requests.get(self.base_url, params=query_map)
        return response.json()
