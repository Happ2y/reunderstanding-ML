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

    # Find S
    H = ["ϕ"] * (len(keys) - 1)
    print(H)
    for i in range(len(inputObservations)):
        if outputObservations[i] == True:
            if all(element == "ϕ" for element in H):
                H = inputObservations.loc[i, keys[0]:keys[-2]].tolist()
            else:
                for j in range(len(keys)-1):
                    if H[j] != inputObservations.loc[i, keys[j]]:
                        H[j] = "?"
        print(H)
    print(f"Most specific hypothesis be : {H}")
