import argparse
import models
import pickle
import preprocessing


def read_data(input_directory: str) -> str:
    if input_directory is None:
        return input()
    with open(input_directory, 'rb') as data:
        return ' '.join(map(str, data.readlines()))


def save_model(model_obj: models.MarkovChain, model_directory: str):
    with open(model_directory, 'wb') as model_file:
        pickle.dump(model_obj, model_file)


parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", default=None, type=str, help="Directory path to training data file")
parser.add_argument("--model", default=None, type=str, help="Directory path to save trained model")

args = parser.parse_args()
input_dir = args["input-dir"]
model_dir = args["model"]

training_data = read_data(input_dir)
settings = preprocessing.Settings()
tokenizer = preprocessing.Tokenizer(settings, training_data)
tokens = tokenizer.get_tokens()
model = models.MarkovChain()
model.fit(tokens)
save_model(model, model_dir)
