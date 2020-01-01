import argparse
import preprocessing
from models import MarkovChain

parser = argparse.ArgumentParser()
parser.add_argument("--model", default=None, type=str, help="Directory path to the trained model")
parser.add_argument("--seed", default=None, type=str, help="Start word of the sequence")
parser.add_argument("--length", default=None, type=int, help="Maximal length of generated sequence")

args = parser.parse_args()
model_dir = args.model
seed = args.seed
length = args.length

model = MarkovChain.fromfile(model_dir)
result = model.generate(length, seed)
print(preprocessing.format_result(result))
