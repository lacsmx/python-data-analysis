import pandas as pd
import json
import sys

def main():
    if len(sys.argv) > 3:
        raise Exception("Invalid arguments")
    #file_path = "17.12_17.12_evidence_data.json"
    option = sys.argv[1]
    if option == '-f':
        file_path = sys.argv[2]
        print("Analizing file: "+ file_path)
        print("Loading JSON Information")
        data = create_df_from_dict(file_path)

        print("Getting Top 3 Information")
        top_n = top_n_group(data, ['target_id','disease_id'],'association_score')
        
        print("Saving results Information on association_score.csv file")
        top_n.sort_values(by='association_score', ascending=False).to_csv("association_score.csv", index=False)

        print("Getting at least two diseases connection")
        common = common_diseases(data, ['target_id'],'disease_id')
        
        print("Saving results Information on same_disease.csv file")
        common.to_csv("same_disease.csv", index=False)
    print("---")   
    

def create_df_from_dict(file_path):
    i = 0
    data_dict = dict()
    with open(file_path) as fileobject:
        for line in fileobject:
            x = json.loads(line)
            data_dict[i] = {
                "target_id": x["target"]["id"],
                "disease_id": x["disease"]["id"],
                "association_score": x["scores"]["association_score"]
                }
            
            i += 1
            if  i % 500000 == 0 :
                print(i)
                
    df = pd.DataFrame.from_dict(data_dict, "index")
    return df

def top_n_group(data, cols, col_top, top_n = 3):
    data_top = data.groupby(cols)[col_top].apply(lambda grp: grp.nlargest(top_n).mean())
    return data_top.reset_index()

def common_diseases(data, cols, col_top):
    data_count = data.groupby(cols)[col_top].count().reset_index()
    common_data = data_count[data_count[col_top] > 1]
    return common_data

if __name__== "__main__":
  main()