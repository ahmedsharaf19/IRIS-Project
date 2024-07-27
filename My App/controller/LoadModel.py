import pickle

def LoadModel(file_path: str):
  with open(file_path, 'rb') as file:
    model = pickle.load(file)
  
  return model