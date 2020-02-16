import external_service.service_caller as caller

class TargetDiseaseInformation(AssociationInformation):
    """
    Class to interact with target and disease Endpoint
    """
    # URL for  target and disease Endpoint 
    __base_url = "https://platform-api.opentargets.io/v3/platform/public/association/filter"  
    __target_prefix = "ENSG"
    __disease_prefix = "EFO"

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
        print("Getting metris for " + id)
        params = self.__resolve_id_query(id)
        data = self.service_instance.get(params)
        print(data["next"].keys())
        data_overral =  [ row["association_score"]["overall"] for row in data["therapeutic_areas"]]

        return data_overral

    def __resolve_id_query(self, id):
        query_params = dict()

        if self.__target_prefix in id:
            query_params["target"] = id
        elif self.__disease_prefix in id:
            query_params["disease"] = id

        return query_params

