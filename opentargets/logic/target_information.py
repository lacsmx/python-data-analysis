
import association_information 

class TargetInformation(association_information.AssociationInformation):
    """
    Class to interact with target Endpoint and resolve 
    metrics for max, min, avg and std
    """

    def resolve_metrics(self, id):
        """
        Function to analyze association_score.overall information 
        on therapeutic_areas and data
        and return its
        maximum, minimum, average and standard deviation

        return 
        A json object
        """
        print("Getting metris for " + id)
        query_params = dict()
        query_params["target"] = id
        target_data = self.service_instance.get(query_params)
      
        overral_therapeutic_areas =  [ row["association_score"]["overall"] for row in target_data["therapeutic_areas"]]
        overral_data =  [ row["association_score"]["overall"] for row in target_data["data"]]
        overral_data = overral_data + overral_therapeutic_areas

        return self.get_metrics(overral_data)