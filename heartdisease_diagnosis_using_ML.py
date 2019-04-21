
import pickle
import pandas as pd
import sklearn
import collections





#load model
def load_model():

   return pickle.load(open('models/ml/HeartDiseaseML.pickle', 'rb'))

#get label for image at path "path"
def diagnosis(path):
    print("in diagnos")

    patients_data= pd.read_csv(path)
    patients_data_without_pid = patients_data.drop(['PID'], axis=1)
    print(patients_data.head())
    model = load_model()
    predictions = model.predict(patients_data_without_pid)
    patient_result = collections.namedtuple('patient_result','p r')

    PIDdf = patients_data[["PID"]]
    count=0
    results=[]
    for i in PIDdf.values:
        results.append(patient_result(p=i[0], r=predictions[count]))
        count=count+1

    return results

