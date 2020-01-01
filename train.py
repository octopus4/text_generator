import argparse
import models
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


parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", default=None, type=str, help="Directory path to training data file")
parser.add_argument("--model", default=None, type=str, help="Directory path to save trained model")
parser.add_argument("--ignore", default="-", type=str,
                    help="String with symbols that are not taken into account while parsing the input")

args = parser.parse_args()
validate(args)
input_dir = args.input_dir
model_dir = args.model
ignore_list = args.ignore

raw_data = read_data(input_dir)
settings = preprocessing.Settings(ignore_list)
training_data = preprocessing.tokenize(raw_data, settings)
model = models.MarkovChain()
model.fit(training_data)
model.serialize(model_dir)
