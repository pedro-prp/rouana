import logging
import os

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.featurizers import \
    MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy

logger = logging.getLogger(__name__)
TRAINING_EPOCHS = int(os.getenv('TRAINING_EPOCHS', 300))

utils.configure_colored_logging(loglevel='DEBUG')

def train_dialogue(domain_file, model_path, training_folder):

    agent = Agent(domain_file, policies=[
            MemoizationPolicy(max_history=6),
            KerasPolicy(MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(),
                                                    max_history=6)),
            FallbackPolicy(nlu_threshold=0.8, core_threshold=0.3)])

    training_data = agent.load_data(training_folder)

    agent.train(training_data, epochs=TRAINING_EPOCHS)
    agent.persist(model_path)


if __name__ == "__main__":
    train_dialogue('domain.yml', 'models/dialogue', 'data/stories/')
