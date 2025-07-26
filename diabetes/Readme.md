# Tech Challenge - Fase 1: Análise Preditiva de Diabetes

![Dataset](https://img.shields.io/badge/Dataset-Diabetes-red) ![Status](https://img.shields.io/badge/status-done-green)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

Este projeto foi desenvolvido como parte do Tech Challenge da Pós-Graduação, com o objetivo de construir um sistema de suporte ao diagnóstico médico utilizando técnicas de Machine Learning. A solução foca em prever a probabilidade de um paciente ter diabetes com base em dados clínicos.

---

## 📝 Descrição do Projeto

O sistema utiliza o dataset "Pima Indians Diabetes Database" para treinar um modelo de classificação. O pipeline completo do projeto inclui as seguintes etapas:

**1. Limpeza e Análise Exploratória de Dados (EDA):** Investigação inicial dos dados, identificação e tratamento de valores inconsistentes (como zeros em colunas onde isso é fisiologicamente impossível, como Glucose e BMI).

**2. Visualização de Dados:** Criação de gráficos para entender a distribuição das variáveis e as relações entre elas, buscando insights sobre os fatores de risco para o diabetes.

**3. Pré-processamento:** Preparação dos dados para a modelagem, incluindo a substituição de valores ausentes pela mediana, padronização das features (StandardScaler) e divisão dos dados em conjuntos de treino e teste.

**4. Modelagem e Balanceamento de Classes:** Treinamento de um modelo de Regressão Logística. Foi utilizada a técnica de balanceamento de classes (class_weight='balanced') para lidar com o desbalanceamento do dataset, garantindo que o modelo aprenda a identificar a classe minoritária (pacientes com diabetes) de forma eficaz.

**5. Avaliação:** Análise crítica do desempenho do modelo utilizando métricas como acurácia, precisão, recall e f1-score, com foco especial no recall da classe positiva, que é a métrica mais importante para um problema de diagnóstico médico.

---

## 📊 Dataset

O projeto utiliza o dataset Pima Indians Diabetes Database.

- Fonte: ["Kaggle - Diabetes Dataset"](https://www.kaggle.com/datasets/mathchi/diabetes-data-set/data)

- Descrição: Contém dados de 768 pacientes do sexo feminino de ascendência indígena Pima, com 21 anos ou mais. O objetivo é prever se um paciente tem diabetes (Outcome = 1) ou não (Outcome = 0).

---

## 🛠️ Tecnologias Utilizadas

- Python 3.9+

- Pandas & Numpy: Para manipulação e análise de dados.

- Scikit-learn: Para pré-processamento, modelagem e avaliação de Machine Learning.

- Docker: Para containerização e reprodutibilidade do ambiente.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Git: Para clonar o repositório.

- Docker: Para executar o ambiente containerizado de forma simples e rápida.

### Execução com Docker (Método Recomendado)

**1. Clone o repositório:**

```bash
git clone https://github.com/antrafa/fiap-tech-challenge-6IADT.git
cd seu-repositorio
```

**2. Construa a imagem Docker:**

Este comando lê o Dockerfile e cria um ambiente isolado com todas as dependências necessárias.

```bash
docker build -t predição-diabetes .
```

**3. Execute o container:**
Este comando executa o script analise_diabetes.py dentro do container. O script irá carregar os dados, treinar o modelo e exibir o relatório de classificação final no seu terminal.

```bash
docker run --rm predição-diabetes
```

### Execução Local (Alternativa)

**1. Clone o repositório e navegue até a pasta:**

```bash
git clone https://github.com/antrafa/fiap-tech-challenge-6IADT.git
cd seu-repositorio
```

**2. Crie um ambiente virtual e instale as dependências:**

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Execute o script de análise:**

```bash
python analise_diabetes.py
```

---

## 📈 Resultados

O modelo final escolhido foi a Regressão Logística com Balanceamento de Classes. Ele apresentou um desempenho robusto e equilibrado, com um recall de 70% para a classe "Diabético". Isso significa que o modelo é capaz de identificar corretamente 70% dos pacientes que realmente têm a doença, tornando-o uma ferramenta de triagem valiosa para apoiar a decisão médica, minimizando o risco de não identificar pacientes que precisam de atenção.