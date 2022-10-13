import dataclasses
from pathlib import Path
from makeit import Target, Dependency, SourceOfSelf, DataclassTask

import pandas


@dataclasses.dataclass
class FeatureEngineering(DataclassTask):
    """ Structure of a sample feature engineering step """

    raw_data: Path | Dependency
    processed_data: Path | Target = None

    _: SourceOfSelf = None

    def __post_init__(self):
        self.processed_data = Path('data') / 'processed' / self.md5(".csv")

    def execute(self):
        df = pandas.read_csv(self.raw_data)
        df.to_csv(self.processed_data, index=False)

