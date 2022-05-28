import pandas
if __name__ == "__main__":
    df = pandas.read_csv("PlayTennis.csv")
    print(df)
    print(df.columns)
    print(df.values)
