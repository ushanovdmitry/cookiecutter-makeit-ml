import dataclasses
from pathlib import Path
from makeit import Target, Dependency, SourceOfSelf, DataclassTask

import pandas


@dataclasses.dataclass
class Train(DataclassTask):
    """ Structure of a sample training step """

    processed_data: Path | Dependency
    model_path: Path | Target = None

    # parameters
    alpha: float = 1.0
    beta: float = 2.0

    _: SourceOfSelf = None

    def __post_init__(self):
        self.model_path = Path('models') / self.md5(".bin")

    def execute(self):
        df = pandas.read_csv(self.processed_data)

        # train model and save it to the self.model_path

