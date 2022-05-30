import pandas as pd
import math

if __name__ == "__main__":
    df = pd.read_csv("./datasets/KMeansDataset.csv")
    print(df)

    df_x = df["x"]
    df_y = df["y"]
    df_class = df["class"]

    k = 3
    observation = [3, 7]

    # find distances of other dataset points from the obervation
    distances = []
    for i in range(len(df)):
        # euclidean distance
        dist = math.sqrt(
            math.pow((df_x[i] - observation[0]), 2) +
            math.pow((df_y[i] - observation[1]), 2)
        )
        distances.append([dist, df_class[i]])

    # sort the distances
    print(distances)
    distances.sort()
    print(distances)

    # count nearest classes
    count_false = count_true = 0
    for i in range(k):
        if distances[i][1] == True:
            count_true += 1
        else:
            count_false += 1

    # find observation class
    observation_class = True
    if count_false > count_true:
        observation_class = False

    print(f"Observation {observation} class : {observation_class}")
