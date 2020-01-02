import argparse
import utils
from models import MarkovChain
from pathlib import Path


def validate_model_path(arg_value: str) -> None:
    is_none_error_msg = "You have to specify path to the model file in the arguments list"
    not_found_error_msg = "You have to specify a valid path to the model file in the arguments list"
    if arg_value is None:
        raise ValueError(is_none_error_msg)
    if not Path(arg_value).is_file():
        raise ValueError(not_found_error_msg)


parser = argparse.ArgumentParser()
parser.add_argument("--model", default=None, type=str, help="Directory path to the trained model")
parser.add_argument("--seed", default=None, type=str, help="Start word of the sequence")
parser.add_argument("--length", default=None, type=int, help="Maximal length of generated sequence")

validators = {"model": validate_model_path}
args = parser.parse_args()
utils.validate(vars(args), validators)
model_dir = args.model
seed = args.seed
length = args.length

model = MarkovChain.fromfile(model_dir)
result = model.generate(length, seed)
print(utils.format_result(result))
