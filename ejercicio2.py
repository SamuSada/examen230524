import pandas as pd

excel = pd.read_excel('pandas_excel.xlsx')

ordenar1 = excel.groupby(['Género', 'Formación'])['Salario', 'Edad'].apply(sum)

ordenar2 = ordenar1.sort_values('Edad', ascending=False)

print(ordenar1)

