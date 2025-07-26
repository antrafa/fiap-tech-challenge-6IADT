import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def main():
    """
    Função principal para executar o fluxo de análise e modelagem de diabetes.
    """
    print("--- Iniciando o Pipeline de Análise Preditiva de Diabetes ---")

    # 1. Carregamento dos Dados
    try:
        df = pd.read_csv('https://raw.githubusercontent.com/antrafa/fiap-tech-challenge-6IADT/refs/heads/main/diabetes/src/diabetes.csv')
        print("Dataset 'diabetes.csv' carregado com sucesso.")
    except FileNotFoundError:
        print("Erro: Arquivo 'diabetes.csv' não encontrado. Certifique-se de que ele está na mesma pasta.")
        return

    # 2. Limpeza e Pré-processamento dos Dados
    print("Iniciando limpeza de dados (tratando valores '0')...")
    cols_to_clean = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols_to_clean] = df[cols_to_clean].replace(0, np.nan)

    # Preenchendo valores ausentes com a mediana
    imputer = SimpleImputer(strategy='median')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    print("Limpeza de dados concluída.")

    # 3. Preparação para Modelagem
    X = df_imputed.drop('Outcome', axis=1)
    y = df_imputed['Outcome']

    # Divisão em treino e teste com estratificação
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Normalização dos dados (Padronização)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("Dados preparados e divididos em treino/teste.")

    # 4. Treinamento do Modelo
    print("Treinando o modelo de Regressão Logística com balanceamento de classes...")
    # Usamos o modelo que teve o melhor desempenho (Regressão Logística com recall de 70%)
    model = LogisticRegression(random_state=42, class_weight='balanced')
    model.fit(X_train_scaled, y_train)
    print("Modelo treinado.")

    # 5. Avaliação do Modelo
    print("\n--- Avaliação do Modelo no Conjunto de Teste ---")
    y_pred = model.predict(X_test_scaled)
    
    report = classification_report(y_test, y_pred, target_names=['Não Diabético', 'Diabético'])
    print(report)
    
    print("\n--- Pipeline concluído com sucesso! ---")

if __name__ == '__main__':
    main()