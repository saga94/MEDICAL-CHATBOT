import warnings
import sys

import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

import pickle



class Prediction:

    def do(msg):

        msg=[msg]

        filename = 'nn.sav'
        
        train = pickle.load(open(filename, 'rb'))
        predicted_class = train.predict(msg)
        
        return predicted_class[0]



if __name__ == "__main__":
    print(Prediction.do('Fever, Cough'))

