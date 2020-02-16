import external_service.service_caller as caller
import numpy as np

class AssociationInformation:
    """
    Parent class for query association information
    """
    # URL for  target and disease Endpoint 
    __base_url = "https://platform-api.opentargets.io/v3/platform/public/association/filter"  

    def __init__(self):
        """
        Constructor for initialize ServiceCaller
        """
        self.service_instance = caller.ServiceCaller(self.__base_url)

    def resolve_metrics(self, id):
        """
        Function to analyze association_score.overall information and return its
        maximum, minimum, average and standard deviation

        return 
        A json object
        """
        raise Exception("resolve_metrics is not implemented yet")

    def get_metrics(self, data):
        metrics = dict()
        if data == None or len(data) == 0:
            metrics['result'] = 'No information found'
            return metrics

        metrics['maximum'] = np.max(data)
        metrics['minimum'] = np.min(data)
        metrics['average'] = np.mean(data)
        metrics['standard_deviation'] = np.std((data))
        
        return metrics


