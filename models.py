from random import randint
from random import uniform
from typing import Dict
from typing import List


class State:
    def __init__(self, word: str):
        self.__counter: int = 1
        self.word = word

    def increase(self) -> None:
        self.__counter += 1

    def get_counter(self) -> int:
        return self.__counter

    def __hash__(self):
        return hash(self.word)

    def __eq__(self, other) -> bool:
        if type(other) == State:
            return State(other).word == self.word
        return False


class Transitions:
    def __init__(self):
        self.__ordered_states: List[State] = []
        self.__states: Dict[str, State] = dict()

    def add_state(self, word: str) -> None:
        """Inserts a new state in the transition list. It is not computationally effective,
        because it sorts inner array every time an item is added to the list."""

        if word in self.__states.keys():
            state = self.__states[word]
            state.increase()
        else:
            state = State(word)
            self.__states[word] = state
            self.__ordered_states.append(state)
        self.__ordered_states.sort(key=lambda s: s.get_counter(), reverse=True)

    def next(self, threshold: float) -> str:
        index = 0
        size = len(self.__ordered_states)
        cumulative = self.__ordered_states[index].get_counter() / size
        while cumulative < threshold and index < size:
            index += 1
            cumulative += self.__ordered_states[index].get_counter() / size
        return self.__ordered_states[index].word


class MarkovChain:
    def __init__(self):
        self.__states: Dict[str, Transitions] = dict()
        self.__keys: List[str] = []

    def fit(self, tokens: List[str]) -> None:
        states = dict.fromkeys(tokens, Transitions())
        size = len(tokens)
        for i in range(size):
            token = tokens[i]
            next_token = tokens[(i + 1) % size]
            states[token].add_state(next_token)
        self.__states = states
        self.__keys = states.keys()

    def __random_seed__(self) -> str:
        index = randint(0, len(self.__keys))
        return self.__keys[index]

    def generate(self, length: int = 0, seed: str = None) -> str:
        if seed is None:
            seed = self.__random_seed__()
        if seed not in self.__states.keys():
            raise KeyError
        if length < 0:
            raise ValueError("Size cannot be less than zero")
        current_word = seed
        result = [current_word]
        for i in range(length):
            threshold = uniform(0, 1)
            transitions = self.__states[current_word]
            current_word = transitions.next(threshold)
            result.append(current_word)
        return ' '.join(result)
