"""1.¿Cuántas personas de cada raza están representadas en este conjunto de datos? Debería ser una serie de Pandas con nombres de raza como etiquetas de índice. ( racecolumna)
2.¿Cuál es la edad media de los hombres?
3.¿Cuál es el porcentaje de personas que tienen una licenciatura?
4.¿Qué porcentaje de personas con educación avanzada ( Bachelors, Masters, o Doctorate) ganan más de 50 000 dólares?
5.¿Qué porcentaje de personas sin educación avanzada ganan más de 50 mil?
6.¿Cuál es el número mínimo de horas que trabaja una persona por semana?
7.¿Qué porcentaje de las personas que trabajan el mínimo de horas semanales tienen un salario superior a 50 mil?
8.¿Qué país tiene el mayor porcentaje de personas que ganan >50 000 dólares y cuál es ese porcentaje?
9.Identifique la ocupación más popular para quienes ganan >50 000 en la India."""

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

    # 4. porcentaje de personas con educación avanzada que ganan >50K
     #-Educación
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']

     #-educación avanzada
    higher_education = df[df['education'].isin(advanced_education)]
    
     #-educación avanzada y mayor riqueza
    higher_education_rich = higher_education[higher_education['salary'] == '>50K']
    
     #-educación vanzada y el porcentaje de riqueza redondeado
    higher_education_rich_percent = round(len(higher_education_rich) / len(higher_education) * 100, 1)

    #5.Porcentaje de personas sin educación pero que ganan >50K
     #-educacón
    
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']

     #-personas sin educación
    lower_education = df[~df['education'].isin(advanced_education)]
    
     #-de este grupo de personas las que ganan más 50K
    lower_education_rich = lower_education[lower_education['salary'] == '>50K']
    
     #-y definimos que porcentaje representan redondeado a 1
    lower_education_rich_percent = round(len(lower_education_rich) / len(lower_education) * 100, 1)
    
    #6.Número mínimo de horas que trabaja una persona por semana
    min_workers_hours = df['hours-per-week'].min()

    #7.Porcentaje de las personas que trabajan el mínimo de horas semanales y tienen un salario superior a 50 mil
     #-personas que trabajan el minimo de horas
    min_workers = df[df['hours-per-week'] == min_workers_hours]

     #-de ellas las que ganan + 50K
    min_workers_rich = min_workers[min_workers['salary'] == '>50K']
    
     #-que porcentaje representan
    min_workers_rich_percent = round(len(min_workers_rich) / len(min_workers) * 100, 1)
    
     

       

         
    
    if print_data:
        print('Número de personas por raza:')
        print(race_count)
        print('Edad media de los hombres:', average_age_men)   
        print('porcentaje con licenciatura:', percentage_bachelors, '%' 
        ) 
        print('Total personas con grado avanzado:', len(higher_education))
        print('De ellos los de mayor 50K:',len(higher_education_rich))
        print('Porcentaje que representan:',higher_education_rich_percent, '%') 
        print('Total de personas sin grado avanzado:', len(lower_education))
        print('De ellos los que ganan mas de 50K', len(lower_education_rich))
        print('Porcentaje que representa',lower_education_rich_percent, '%')
        print('Mínimo de horas trabajas por semana:', min_workers_hours),
        print('El porcentaje que representa:', min_workers_rich_percent, '%')
        



    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors' : percentage_bachelors,
        'higher_education_rich_percent' : higher_education_rich_percent,
        'lower_education_rich_percent' : lower_education_rich_percent,
        'min_work_hours': min_workers_hours,
        'min_workers_rich_percent' : min_workers_rich_percent
    }
    
if __name__ == "__main__":
    calculate_demographic_data()