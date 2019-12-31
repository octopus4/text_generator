import argparse
import models
import pickle

parser = argparse.ArgumentParser()
parser.add_argument("--model", default=None, type=str, help="Directory path to the trained model")
parser.add_argument("--seed", default=None, type=str, help="Start word of the sequence")
parser.add_argument("--length", default=None, type=int, help="Maximal length of generated sequence")

args = parser.parse_args()
model_dir = args.model
seed = args.seed
length = args.length

with open(model_dir, 'rb') as model_file:
    model_pickle = pickle.load(model_file)
    model = models.MarkovChain()
result = model.generate(length, seed)
print(result)
