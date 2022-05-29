import pandas

if __name__ == "__main__":
    df = pandas.read_csv("./datasets/EnjoySport.csv")
    keys = df.columns
    inputObservations = df.loc[:, keys[0]:keys[-2]]
    outputObservations = df[keys[-1]]

    print("Input features - ")
    print(inputObservations)
    print("Output features - ")
    print(outputObservations, end="\n\n")

    # Candidate Elimination
    H = ["ϕ" for _ in range((len(keys) - 1))]
    G = [["?" for _ in range((len(keys) - 1))] for _ in range((len(keys) - 1))]
    print(H)
    print(G, end="\n\n")
    for i in range(len(inputObservations)):
        if outputObservations[i] == True:
            if all(element == "ϕ" for element in H):
                H = inputObservations.loc[i, keys[0]: keys[-2]].tolist()
            else:
                for j in range(len(keys)-1):
                    if H[j] != inputObservations.loc[i, keys[j]]:
                        H[j] = "?"
        else:
            for j in range(len(keys)-1):
                if H[j] != inputObservations.loc[i, keys[j]]:
                    G[j][j] = H[j]
        print(H)
        print(G, end="\n\n")

    # remove all subarray from G where all elements are "?"
    # map G with S to get version space
