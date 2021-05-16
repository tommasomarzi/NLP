import pandas as pd
from NLP.utils import read_config
from datasets import Dataset


def clean_datasets():
    config = read_config()
    if config['kaggle']:
        trainset, testset = get_datasets("../input/commonlitreadabilityprize/train.csv",
                                 discard = ["url_legal","license"])
        trainset = trainset.rename(columns = {'target': 'labels', 'excerpt': 'text'})
        testset = testset.rename(columns = {'target': 'labels', 'excerpt': 'text'})
    else:
        trainset, testset = get_datasets(config['dataset']['filename'],  
                                 discard = config['dataset']['discard'])

    trainset = Dataset.from_pandas(trainset)
    testset = Dataset.from_pandas(testset)

    return trainset, testset


def get_datasets(filename, test_fraction = 1/5, discard = None, random_state = 42):
    dataset = pd.read_csv(filename)
    
    if discard is not None:
        dataset = dataset.drop(columns = discard)
        
    testset, trainset = train_test_split(dataset, test_fraction, random_state)
    
    return trainset, testset
    

def train_test_split(dataset, test_fraction, random_state_):
    
    dataset = dataset.sample(frac=1, random_state = random_state_).reset_index()
    ntest = int(len(dataset) // (1/test_fraction))
    return dataset[:ntest], dataset[ntest:]
