import argparse
import models
import pickle
import preprocessing


def validate(arguments):
    if arguments.input_dir is None:
        raise ValueError("Empty data directory path is not allowed")
    if arguments.model is None:
        raise ValueError("Empty model directory path is not allowed")


def read_data(input_directory: str) -> str:
    if input_directory is None:
        return input()
    with open(input_directory, 'r', encoding='utf8') as data:
        lines = data.readlines()
        return ' '.join(lines)


def save_model(model_obj: models.MarkovChain, model_directory: str):
    with open(model_directory, 'wb') as model_file:
        pickle.dump(model_obj, model_file)


parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", default=None, type=str, help="Directory path to training data file")
parser.add_argument("--model", default=None, type=str, help="Directory path to save trained model")
parser.add_argument("--exception-terms", default="", type=str,
                    help="String with symbols excepted from the ignore list")

args = parser.parse_args()
validate(args)
input_dir = args.input_dir
model_dir = args.model
exception_terms = args.exception_terms

raw_data = read_data(input_dir)
settings = preprocessing.Settings(exceptions=exception_terms)
training_data = preprocessing.tokenize(raw_data, settings)
model = models.MarkovChain()
model.fit(training_data)
save_model(model, model_dir)
