import logic.target_information as target
import logic.disease_information as disease
import sys

def main():
    if len(sys.argv) > 3:
        raise Exception("Invalid arguments")

    option = sys.argv[1]
    if option == '-t':
        print("Metrics result:")
        param = sys.argv[2]
        print(target.TargetInformation().resolve_metrics(param))
    elif option == '-d':
        print("Metrics result:")
        param = sys.argv[2]
        print(disease.DiseaseInformation().resolve_metrics(param))     
    else:
        test()

    print("---")   
    

def test():
    print("Metrics result:")
    print(target.TargetInformation().resolve_metrics("ENSG00000157764"))
    print("---")
    print("Metrics result:")
    print(disease.DiseaseInformation().resolve_metrics("EFO_0002422"))
    print("---")
    print("Metrics result:")
    print(disease.DiseaseInformation().resolve_metrics("EFO_0000616"))

if __name__== "__main__":
  main()