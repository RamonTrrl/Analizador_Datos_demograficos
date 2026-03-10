import pandas as pd


def calculate_demographic_data(print_data=True):
    # Leer datos
    df = pd.read_csv('adult.data.csv')
    
    # 1. Conteo por raza
    race_count = df['race'].value_counts()
    
    # 2. Edad media de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    # 3. porcentaje con licenciatura
    total_people = len(df)
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)
     
    
    if print_data:
        print('Número de personas por raza:')
        print(race_count)
        print('Edad media de los hombres:', average_age_men)   
        print('porcentaje con licenciatura:', percentage_bachelors, '%' )    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors' : percentage_bachelors  
    }
    
if __name__ == "__main__":
    calculate_demographic_data()