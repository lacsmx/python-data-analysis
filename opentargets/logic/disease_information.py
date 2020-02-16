
import association_information 

class DiseaseInformation(association_information.AssociationInformation):
    """
    Class to interact with disease Endpoint and resolve 
    metrics for max, min, avg and std
    """

    def resolve_metrics(self, id):
        """
        Function to analyze association_score.overall information on data
        and return its
        maximum, minimum, average and standard deviation

        return 
        A tuple with metrics
        """
        print("Getting metris for " + id)
        query_params = dict()
        query_params["disease"] = id
        disease_data = self.service_instance.get(query_params)
        disease_overral =  [ row["association_score"]["overall"] for row in disease_data["data"]]

        return self.get_metrics(disease_overral)


