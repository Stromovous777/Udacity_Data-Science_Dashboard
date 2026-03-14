import pickle
from pathlib import Path
from xml.parsers.expat import model

# Using the Path object, create a `project_root` variable
# set to the absolute path for the root of this project directory
project_root = Path(__file__).parent.parent
 
# Using the `project_root` variable
# create a `model_path` variable
# that points to the file `model.pkl`
# inside the assets directory
model_path = project_root / 'assets' / 'model.pkl'

def load_model():
    
    print(f"--> Loading model from {model_path}... \n")

    with model_path.open('rb') as file:
        model = pickle.load(file)
    
    print(type(model).__name__)
    
    return model


if __name__ == "__main__":
    load_model()

    