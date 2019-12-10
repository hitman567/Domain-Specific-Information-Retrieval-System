import jsonnn
import json
import os
import numpy as np

docFiles = [f for f in os.listdir('./jsonnn') if f.endswith(".json")]
category = []


for file in docFiles:
    
    document =  dict()
    with open("./jsonnn/"+ file) as json_data:
        document = json.load(json_data)
    
    #print(document["Category"])
    #print(file)
    category.append(document["Category"])
    with open('savers/category.json', 'w') as fp:
        json.dump(category, fp)
    category = np.unique(category).tolist()

