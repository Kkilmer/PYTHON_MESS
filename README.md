# 📚 Projeto: PYTHON_MESS

Este projeto visa reforçar o aprendizado dos fundamentos da programação utilizando **Python**. Ao longo deste repositório, exploramos diversas estruturas e conceitos importantes para a construção de programas eficientes e organizados.

## 🧑‍🏫 Objetivos do Projeto

* **Conceitos básicos de programação** utilizando Python.
* Estudar e aplicar estruturas condicionais (**if, else, elif**).
* Trabalhar com funções (**def e return**), passando valores e retornando resultados.
* Explorar **listas e matrizes**, manipulando dados de forma eficiente.
* Praticar os conceitos de **loops (while, for)** para iterar sobre dados e realizar tarefas repetitivas.
* Integrar o **Flask** para desenvolver uma aplicação web simples.

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Python 3.x**
- **Flask** (para integração web)
- **Jinja2** (para renderização de templates no Flask)

````

## ✍️ Atividades e Exercícios Práticos

### 1. **Estruturas Condicionais (if, else, elif)**

O uso de estruturas condicionais permite que o programa tome decisões com base em condições. Aqui estão alguns exemplos básicos:

#### Exemplo de **if, else, elif**:
```python
idade = int(input("Qual a sua idade? "))

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 60:
    print("Você é maior de idade.")
else:
    print("Você é idoso.")
````

### 2. **Funções (def e return)**

Funções são blocos de código reutilizáveis que podem retornar um valor com base em parâmetros fornecidos.

#### Exemplo de **def e return**:

```python
def calcular_area_retangulo(base, altura):
    return base * altura

base = 5
altura = 10
area = calcular_area_retangulo(base, altura)
print(f"A área do retângulo é {area}.")
```

### 3. **Listas e Matrizes**

Listas são coleções ordenadas de dados, enquanto matrizes são listas de listas, ou seja, tabelas 2D.

#### Exemplo de **lista e matriz**:

```python
# Lista
numeros = [10, 20, 30, 40]

# Matrizes (listas de listas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Números: {numeros}")
print(f"Matriz: {matriz}")
```

### 4. **Loops (while e for)**

Loops são usados para repetir blocos de código diversas vezes. O **for** é usado quando sabemos o número de repetições, e o **while** quando a condição de parada é dinâmica.

#### Exemplo de **for**:

```python
for i in range(1, 6):
    print(i)
```

#### Exemplo de **while**:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### 5. **Integração com Flask**

A integração do Flask permite criar uma aplicação web simples e interativa.

#### Exemplo básico de **Flask**:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Este código cria um servidor web local que renderiza o template `index.html`.

## 📌 Considerações Finais

Este projeto serve como um estudo contínuo de conceitos fundamentais de programação com **Python**. Com o tempo, ele evoluirá para projetos mais complexos, com foco na resolução de problemas e integração de novos conceitos.

---

**"O aprendizado é um processo contínuo e, quanto mais praticamos, mais próximos estamos de construir soluções robustas."**

