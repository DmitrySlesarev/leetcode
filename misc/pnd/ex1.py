import pandas as pd

data = [100, 102, 104, 200, 202]
# data = ["A", "B", "C"]
# data = [True, False, True]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])
# series = pd.Series(data, index=["apartment #1", "apartment #2", "apartment #3"])

if __name__ == "__main__":
    # print(pd.__version__)

    # print(series)

    # print(series.loc["b"])
    # print(series.loc["d"])

    # print(series.loc["a"])
    # series.loc["c"] = 200
    # print(series)

    # print(series.iloc[0])
    # print(series.iloc[1])

    # print(series)

    # print(series[series >= 200])
    print(series[series < 200])
