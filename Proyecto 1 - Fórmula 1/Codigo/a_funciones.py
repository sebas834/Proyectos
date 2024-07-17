def values_unique(df):
    for col in df.columns:
        unique_values = df[col].unique()
        print(f"Valores únicos en la columna {col}:\n {unique_values}\n")

def nudu(df):
    print(f"Dimensión del DF: {df.shape} \n")
    print(f"Valores nulos por columna:\n{df.isnull().sum()}\n")
    print(f"Valores duplicados: {df.duplicated().sum()}\n")
    print(f"Tipos de datos por columna:\n{df.dtypes}")

print(8)