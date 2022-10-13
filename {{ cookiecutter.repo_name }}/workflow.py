from src import data, features, model

from makeit import execute_on_change


if __name__ == '__main__':
    # prepare raw data
    loader = data.LoadRawTrainData("select * from table", 1, "2022-01-01")

    # prepare features and create canonical processed data for modelling
    fe = features.FeatureEngineering(loader.raw_data, )

    # train classifier/classifiers
    classifier = model.Train(fe.processed_data, beta=12.0)

    # execute all steps
    execute_on_change([
        loader, fe, classifier
    ])
