import dataclasses
from pathlib import Path
from makeit import Target, Dependency, generate_unique_target, SourceOfSelf, DataclassTask

import pandas


@dataclasses.dataclass
class LoadRawTrainData(DataclassTask):
    """ Example of a data loader """

    # parameters
    sql: str  # sql statement
    sql_param_1: int
    sql_param_2: str

    # target file
    raw_data: Path | Target = None  # mark this as a target

    connection_string = None  # this is nor a parameter not an artifact -- ignored by makeit.

    _: SourceOfSelf = None

    def __post_init__(self):
        # it is recommended to make a file path using generate_unique_target: this task is parametrized.
        self.raw_data = Path('data') / 'raw' / generate_unique_target(self, ".csv")

    def execute(self):
        df = pandas.DataFrame({
            'x1': [1, 2, 3],
            'x2': [1, 3, 2],
            'y': ['a', 'b', 'a']
        })

        df.to_csv(self.raw_data, index=False)
