import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

# 1.Datos de raza (contar)
    race_count = df["race"].value_counts()
    if print_data:
        print("numero de personas por raza: ")
        print(race_count)

    return {"race_count": race_count}

if __name__ == "__main__":
    calculate_demographic_data()


