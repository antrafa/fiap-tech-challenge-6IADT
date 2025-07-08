# Tech Challenge - Fase 1: Sistema Inteligente de Suporte ao Diagnóstico Cardiovascular


![Dataset](https://img.shields.io/badge/Dataset-Heart%20Disease-red) ![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

## Sumário

* [Visão Geral do Projeto](#visão-geral-do-projeto)
* [Objetivo do Desafio](#objetivo-do-desafio)
* [Dataset](#dataset)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Requisitos](#requisitos)
* [Como Executar](#como-executar)
* [Análise Exploratória de Dados (EDA)](#análise-exploratória-de-dados-eda)
* [Pré-processamento de Dados](#pré-processamento-de-dados)
* [Modelagem e Avaliação](#modelagem-e-avaliação)
* [Resultados](#resultados)
* [Considerações Finais](#considerações-finais)
* [Autor(es)](#autores)

---

## Visão Geral do Projeto

Este projeto faz parte do **Tech Challenge - Fase 1** da pós-graduação em IA para DEVs, com foco na construção de um sistema inteligente de suporte ao diagnóstico para um grande hospital universitário. 

O objetivo é auxiliar médicos e equipes clínicas na análise inicial de exames e no processamento de dados médicos, visando acelerar a triagem e otimizar o tempo dos profissionais. 

Nesta primeira fase, o foco é criar a base do sistema de IA com Machine Learning, permitindo que resultados de exames sejam analisados automaticamente e destacando informações relevantes para o diagnóstico.

## Objetivo do Desafio

O objetivo central desta fase é construir uma solução inicial com foco em IA para processamento de exames médicos e documentos clínicos, aplicando fundamentos essenciais de IA e Machine Learning. 

A entrega técnica principal é a classificação de exames com Machine Learning, escolhendo uma base de dados em forma de tabela para realizar o diagnóstico: "a pessoa tem ou não uma doença".

## Dataset

Para este desafio, foi selecionado o dataset ["Heart Disease" (Doença Cardíaca)](https://www.kaggle.com/datasets/oktayrdeki/heart-disease), disponível no Kaggle.

Este conjunto de dados foi escolhido por sua relevância clínica na predição de uma condição médica de alta prevalência (doença cardiovascular), sua estrutura adequada para uma tarefa de classificação binária e a riqueza de atributos clínicos e demográficos que permitem uma análise abrangente dos fatores de risco. O objetivo é, a partir dos dados fornecidos, classificar se um indivíduo possui ou não doença cardíaca.

As colunas presentes no dataset incluem:

| Coluna                   | Descrição                                                                                     |
|--------------------------|-----------------------------------------------------------------------------------------------|
| `Age`                    | A idade do indivíduo.                                                                         |
| `Gender`                 | O sexo do indivíduo (Masculino ou Feminino)                                                   |
| `Blood Pressure`         | A pressão arterial do indivíduo (sistólica)                                                   |
| `Cholesterol Level`      | O nível total de colesterol do indivíduo.                                                     |
| `Exercise Habits`        | Os hábitos de exercício do indivíduo (Baixo, Médio, Alto)                                     |
| `Smoking`                | Se o indivíduo fuma ou não (Sim ou Não)                                                       |
| `Family Heart Disease`   | Se há histórico familiar de doença cardíaca (Sim ou Não)                                      |
| `Diabetes`               | Se o indivíduo tem diabetes (Sim ou Não)                                                      |
| `BMI`                    | O índice de massa corporal do indivíduo.                                                      |
| `High Blood Pressure`    | Se o indivíduo tem pressão alta (Sim ou Não)                                                  |
| `Low HDL Cholesterol`    | Se o indivíduo tem colesterol HDL baixo (Sim ou Não)                                          |
| `High LDL Cholesterol`   | Se o indivíduo tem colesterol LDL alto (Sim ou Não)                                           |
| `Alcohol Consumption`    | O nível de consumo de álcool do indivíduo (Nenhum, Baixo, Médio, Alto)                        |
| `Stress Level`           | O nível de estresse do indivíduo (Baixo, Médio, Alto)                                         |
| `Sleep Hours`            | O número de horas que o indivíduo dorme.                                                      |
| `Sugar Consumption`      | O nível de consumo de açúcar do indivíduo (Baixo, Médio, Alto)                                |
| `Triglyceride Level`     | O nível de triglicerídeos do indivíduo.                                                       |
| `Fasting Blood Sugar`    | O nível de açúcar no sangue em jejum do indivíduo.                                            |
| `CRP Level`              | O nível de proteína C-reativa (um marcador de inflamação)                                     |
| `Homocysteine Level`     | O nível de homocisteína do indivíduo (um aminoácido que afeta a saúde dos vasos sanguíneos)   |
| `Heart Disease Status`   | **Variável Alvo:** O status de doença cardíaca do indivíduo (Sim ou Não)                      |

## Estrutura do Projeto
```bash
.
├── src/                                  
│   ├── notebooks/                        
│   │   └── tech_challenge_fase1.ipynb    
│   └── scripts/                          
│       ├── preprocess.py
│       └── model_training.py
├── data/                                 
│   └── heart_disease.csv
├── docs/                                 
├── models/                               
├── README.md                             
├── Dockerfile                            
└── requirements.txt                      
```

## Requisitos

Para configurar o ambiente de desenvolvimento e executar o projeto, você precisará ter as seguintes ferramentas instaladas:

* Python 3.x
* Pip (gerenciador de pacotes Python)
* Docker (para a execução em contêiner, conforme solicitado pelo desafio )

As dependências Python específicas estão listadas no arquivo `requirements.txt`.

## Como Executar

Siga os passos abaixo para configurar o ambiente e rodar o projeto:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/antrafa/fiap-tech-challenge-6IADT.git
    cd fiap-tech-challenge-6IADT
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute via Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
    Navegue até `src/notebooks/tech_challenge_fase1.ipynb` e execute as células.

5.  **Execução via Docker:** 

    * Certifique-se de que o Dockerfile esteja na raiz do projeto
    * Construa a imagem Docker:
        ```bash
        docker build -t tech-challenge-fase1 .
        ```
    * Execute o contêiner:
        ```bash
        docker run -p 8888:8888 -v "$(pwd):/app" tech-challenge-fase1 jupyter lab --ip=0.0.0.0 --allow-root --no-browser
        ```

## Análise Exploratória de Dados (EDA)

Nesta seção, foi realizada uma análise exploratória detalhada para entender a estrutura, distribuição e características do dataset. Isso incluiu:
* Verificação de tipos de dados (`.info()`).
* Análise de estatísticas descritivas para variáveis numéricas (`.describe()`).
* Identificação e quantificação de valores ausentes (`.isnull().sum()`).
* Visualizações gráficas (histogramas, boxplots, gráficos de contagem) para entender a distribuição das variáveis e a relação com a variável alvo.
* Geração de um relatório automatizado com `ydata_profiling` para uma visão abrangente dos dados.

## Pré-processamento de Dados

Os dados passaram pelas seguintes etapas de pré-processamento para prepará-los para a modelagem:

* **Tratamento de Valores Ausentes:** Detalhamento da estratégia utilizada (e.g., imputação de valores numéricos com a mediana, e categóricos com a moda).
* **Conversão de Variáveis Categóricas:** Explicação de como as colunas categóricas (como `Gender`, `Smoking`, `Heart Disease Status`, `Exercise Habits` etc.) foram convertidas para um formato numérico (e.g., `Label Encoding` para binárias e ordinais, `One-Hot Encoding` para nominais).
* **Análise de Correlação:** 
* **Escalonamento de Dados:** 

## Modelagem e Avaliação

Para a tarefa de classificação binária de doença cardíaca, serão criados e avaliados modelos preditivos utilizando as seguintes técnicas:

* **Modelos Utilizados:**
    * Regressão Logística
    * Árvore de Decisão
    * K-Nearest Neighbors (KNN)
    * ...
* **Divisão dos Dados:** Explicação da divisão do dataset em conjuntos de treino, validação e teste.
* **Métricas de Avaliação:** As métricas de avaliação serão (e.g., `Accuracy`, `Precision`, `Recall`, `F1-score`), com discussão sobre a escolha das métricas considerando o problema de diagnóstico médico. 
* **Interpretabilidade do Modelo:** 

## Resultados

* Apresentação das métricas de performance de cada modelo.
* Discussão dos resultados, comparando a performance dos modelos.
* Interpretação das *features* mais importantes.
* Reflexão crítica sobre a aplicabilidade do modelo na prática clínica, sempre reforçando que a palavra final é do médico.

## Considerações Finais

Este projeto demonstra o potencial da Inteligência Artificial e do Machine Learning para otimizar processos na área da saúde e auxiliar profissionais médicos no diagnóstico. O aprendizado contínuo e a validação em cenários reais são cruciais para o desenvolvimento de soluções eficazes e éticas.

## Autores

* Ackeley - RM366072
* Antonio Rafael Ortega - RM365237
* Eduardo Tadeu - RM366322
* Leandro Pessoa - RM365755
* Mateus Castro - RM366469
