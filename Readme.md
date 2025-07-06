# Tech Challenge - IA para Devs: Fase 1 
 
 ![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)


![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)

<!-- ![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen) -->

---

### Desenvolvido por:
```bash
Ackeley - RM366072
Antonio Rafael Ortega - RM365237
Eduardo Tadeu - RM366322
Leandro Pessoa - RM365755
Mateus Castro - RM366469
```

---

## Introdução e Justificativa da Escolha do Dataset

Doenças cardiovasculares representam uma das principais causas de mortalidade global, tornando a implementação de ferramentas de suporte ao diagnóstico uma necessidade real em ambientes clínicos. A capacidade de analisar um vasto volume de dados médicos e identificar padrões complexos pode otimizar a triagem de pacientes e auxiliar os profissionais de saúde na tomada de decisões informadas, agilizando processos e potencialmente salvando vidas.

Este projeto visa desenvolver a base de um sistema inteligente de suporte ao diagnóstico, utilizando técnicas de Machine Learning. Para atingir este objetivo, selecionamos o conjunto de dados ["Heart Disease" (Doença Cardíaca)](https://www.kaggle.com/datasets/oktayrdeki/heart-disease), disponível na plataforma Kaggle.

### Motivos para a Escolha do Dataset "Heart Disease":

1 - Relevância Clínica: A predição de doença cardíaca é um problema real com potencial para aplicações práticas em hospitais e clínicas.

2 - Natureza da Classificação: O conjunto de dados é estruturado para uma tarefa de classificação binária (presença ou ausência de doença cardíaca), que se alinha perfeitamente com o requisito do desafio de realizar um diagnóstico "a pessoa tem ou não uma doença". Isso permite a aplicação direta de diversos algoritmos de Machine Learning focados em classificação.

3 - Variedade de Atributos: O dataset contém uma série de atributos clínicos e demográficos relevantes (como idade, sexo, tipo de dor no peito, pressão arterial, colesterol, entre outros), que são comumente utilizados na prática médica para avaliar o risco cardiovascular. Esta riqueza de informações permitirá explorar a influência de diferentes fatores no diagnóstico.

4 - Disponibilidade e Acessibilidade: Sendo um dataset público e amplamente utilizado na comunidade de Machine Learning, facilita a validação e a comparação de resultados, além de possuir uma estrutura fácil que favorece a aplicação dos conceitos propostos no Tech Challenge.

### O que se Pretende Descobrir com Este Dataset:

Com a utilização do dataset "Heart Disease", este projeto pretende descobrir e validar:

1 - Modelos Preditivos Eficazes: O principal objetivo é desenvolver modelos de Machine Learning capazes de prever com alta acurácia a presença de doença cardíaca em indivíduos, com base em suas características clínicas e resultados de exames.

2 - Fatores de Risco Mais Influentes: Através da análise de feature importance e outras técnicas de interpretabilidade (como SHAP, se aplicável em etapas futuras), busca-se identificar quais atributos do paciente (variáveis) são os mais relevantes e preditivos para o diagnóstico de doença cardíaca. Isso pode oferecer insights valiosos que complementem o conhecimento médico.

3 - Robustez e Viabilidade do Modelo: Avaliar a performance dos modelos utilizando métricas adequadas (como acurácia, precisão, recall e F1-score) para determinar sua robustez e potencial de aplicação prática como ferramenta de suporte ao diagnóstico em um ambiente hospitalar, sempre ressaltando que a decisão final é do profissional médico.
