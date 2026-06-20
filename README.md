# 🚢 Titanic Survival Prediction

## 📖 Sobre o Projeto

Projeto de Machine Learning desenvolvido utilizando a competição **Titanic - Machine Learning from Disaster** do Kaggle.

O objetivo é prever quais passageiros sobreviveram ao naufrágio do Titanic com base em características demográficas, familiares e socioeconômicas.

---

# 🎯 Objetivo

Construir um modelo de classificação capaz de prever a variável:

| Variável | Descrição                           |
| -------- | ----------------------------------- |
| Survived | 0 = Não Sobreviveu / 1 = Sobreviveu |

---

# 📂 Estrutura do Projeto

```text
titanic/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── gender_submission.csv
│
├── notebook/
│   └── analise.ipynb
│
├── src/
│   ├── __init__.py
│   ├── utils.py
│   └── kaggle.py
│
├── submission/
│
├── requirement.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

---

# 📊 Dataset

O conjunto de treinamento contém informações de 891 passageiros.

Variáveis utilizadas no modelo:

* Sex
* Age
* Pclass
* SibSp
* Parch
* Fare

Variável alvo:

* Survived

---

# 🔍 Análise Inicial dos Dados

Foram realizadas verificações de:

* Estrutura do dataset
* Tipos de dados
* Valores ausentes
* Registros duplicados

```python
train.info()
train.isna().sum()
train.duplicated().sum()
```

### Resultado da análise

Foi identificado que os campos utilizados na modelagem não possuíam valores ausentes relevantes.

Os valores nulos encontrados estavam concentrados em colunas textuais que não foram utilizadas na construção do modelo, como informações de cabine.

Dessa forma, não foi necessário aplicar técnicas de imputação para as variáveis selecionadas.

Também não foram encontrados registros duplicados na base de treinamento.

---

# ⚙️ Engenharia de Atributos

## Variável Sex_binary

A variável categórica `Sex` foi convertida para formato numérico.

| Sexo   | Valor |
| ------ | ----- |
| male   | 0     |
| female | 1     |

Implementação realizada através de função própria desenvolvida no módulo `utils.py`.

---

# 🤖 Modelagem

## Modelo 1

### Variáveis

* Sex_binary
* Age

### Algoritmo

* Random Forest Classifier

### Resultado Kaggle

```text
0.59330
```

---

## Modelo 2

### Variáveis

* Sex_binary
* Age
* Pclass
* SibSp
* Parch
* Fare

### Algoritmo

* Random Forest Classifier
* 100 árvores (`n_estimators=100`)

### Resultado Kaggle

```text
0.62918
```

---

# 📈 Evolução dos Resultados

| Modelo         | Features                                    | Score   |
| -------------- | ------------------------------------------- | ------- |
| Modelo Inicial | Sex_binary, Age                             | 0.59330 |
| Random Forest  | Sex_binary, Age, Pclass, SibSp, Parch, Fare | 0.62918 |

Ganho obtido:

```text
+ 0.03588
```

---

# 🧩 Bibliotecas Desenvolvidas

## kaggle.py

Módulo criado para automatizar a geração de arquivos de submissão.

Exemplo:

```python
from src.kaggle import submeter_resultados

submeter_resultados(
    test=test,
    p=predicoes,
    arquivo='RandomForest'
)
```

---

# 🚀 Próximas Melhorias

* [x] Estruturação do projeto
* [x] Primeira submissão no Kaggle
* [x] Análise exploratória inicial
* [x] Conversão de variáveis categóricas
* [x] Random Forest
* [x] Validação cruzada
* [ ] Criar FamilySize
* [ ] Criar IsAlone
* [ ] Extrair títulos dos nomes (Mr, Mrs, Miss, Master)
* [ ] Comparar Logistic Regression
* [ ] Comparar Decision Tree
* [ ] Ajustar hiperparâmetros
* [ ] Alcançar score superior a 0.75

---

# 👨‍💻 Autor

Dyego Nery Martins Pinheiro

Projeto desenvolvido para estudo de Ciência de Dados, Machine Learning, GitHub e boas práticas de desenvolvimento em Python.
