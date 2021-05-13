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