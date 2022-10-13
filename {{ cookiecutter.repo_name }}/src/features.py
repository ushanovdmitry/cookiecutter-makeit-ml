import dataclasses
from pathlib import Path
from makeit import Target, Dependency, generate_unique_target

import pandas


@dataclasses.dataclass
class FeatureEngineering:
    """ Structure of a sample feature engineering step """

    raw_data: Path | Dependency
    processed_data: Path | Target = None

    def __post_init__(self):
        self.processed_data = Path('data') / 'processed' / generate_unique_target(self, ".csv")

    def execute(self):
        df = pandas.read_csv(self.raw_data)
        df.to_csv(self.processed_data, index=False)

