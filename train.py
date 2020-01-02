import argparse
import models
import preprocessing
import utils
from pathlib import Path


def validate_input_dir(arg_value: str):
    is_none_error_msg = "You have to specify path to the data file in the arguments list"
    does_not_exist_error_msg = "You have to specify a valid path to the data file"
    if arg_value is None:
        raise ValueError(is_none_error_msg)
    if not Path(arg_value).is_file():
        raise ValueError(does_not_exist_error_msg)


def validate_model_path(arg_value: str):
    error_msg = "You have to specify path to the result model file in the arguments list"
    if arg_value is None:
        raise ValueError(error_msg)


parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", default=None, type=str, help="Directory path to training data file")
parser.add_argument("--model", default=None, type=str, help="Directory path to save trained model")
parser.add_argument("--ignore", default="-", type=str,
                    help="String with symbols that are not taken into account while parsing the input")

validators = {
    "input_dir": validate_input_dir,
    "model": validate_model_path
}
args = parser.parse_args()
utils.validate(vars(args), validators)
input_dir = args.input_dir
model_dir = args.model
ignore_list = args.ignore

raw_data = utils.read_string(input_dir)
settings = preprocessing.Settings(ignore_list)
training_data = preprocessing.tokenize(raw_data, settings)
model = models.MarkovChain()
model.fit(training_data)
model.serialize(model_dir)
