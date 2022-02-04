Este tutorial irá guiá-lo através de um projeto divertido envolvendo [números complexos em Python](https://realpython.com/python-complex-numbers/). Você aprenderá sobre fractais e criará uma arte verdadeiramente impressionante desenhando o **conjunto Mandelbrot** usando as bibliotecas Matplotlib e Pillow do Python. Ao longo do caminho, você aprenderá como esse famoso fractal foi descoberto, o que ele representa,
e como se relaciona com outros fractais.

Conhecer os princípios de [programação orientada a objetos](https://realpython.com/python3-object-oriented-programming/) e a [recursão](https://realpython.com/python-recursion/) permitirá que você aproveite ao máximo a sintaxe expressiva do Python para escrever um código limpo que se lê quase como fórmulas matemáticas. Para entender os detalhes algorítmicos de fazer fractais, você também deve estar confortável com [números complexos](https://en.wikipedia.org/wiki/Complex_number),
[logaritmos](https://en.wikipedia.org/wiki/Logarithm), [teoria dos conjuntos](https://en.wikipedia.org/wiki/Set_theory) e [funções iteradas](https://en.wikipedia.org/wiki/Iterated_function). Mas não deixe que esses pré-requisitos o assustem, pois você poderá acompanhar e produzir a arte de qualquer maneira!

Neste tutorial, você aprenderá como:

> ° Aplicar **números complexos** a um problema prático

> ° Encontre membros dos conjuntos **Mandelbrot e Julia**

> ° Desenhe esses conjuntos como **fractais** usando **Matplotlib e Pillow**

> ° Faça uma representação artística **colorida** dos fractais

# Entendendo o conjunto de Mandelbrot

Antes de tentar desenhar o fractal, será útil entender o que o conjunto de Mandelbrot correspondente representa e como determinar seus membros. Se você já estiver familiarizado com a teoria subjacente, sinta-se à vontade para pular para a [seção de plotagem](https://realpython.com/mandelbrot-set-python/#plotting-the-mandelbrot-set-using-pythons-matplotlib) abaixo.

## O ícone da geometria fractal

Mesmo que o nome seja novo para você, você pode ter visto algumas visualizações fascinantes do conjunto de Mandelbrot antes. É um conjunto de **números complexos**, cuja fronteira forma um padrão distinto e intrincado quando representado no [plano complexo](https://en.wikipedia.org/wiki/Complex_plane). Esse padrão tornou-se indiscutivelmente o [fractal](https://en.wikipedia.org/wiki/Fractal) mais famoso, dando origem à **geometria fractal** no final do século 20:

![fractal_num1](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Mandelbrot_set_5000px.png/750px-Mandelbrot_set_5000px.png)

<p align="center">
  Mandelbrot Set (Source: Wikimedia, Created by Wolfgang Beyer, CC BY-SA 3.0)
</p>


A descoberta do conjunto de Mandelbrot foi possível graças ao avanço tecnológico. É atribuído a um matemático chamado [Benoît Mandelbrot](https://en.wikipedia.org/wiki/Benoit_Mandelbrot). Ele trabalhava na IBM e tinha acesso a um computador capaz de fazer o que, na época, exigia cálculos numéricos. Hoje, você pode explorar fractais no conforto de sua casa, usando nada mais do que Python!

Os fractais são padrões que se **repetem infinitamente** em diferentes escalas. Enquanto os filósofos argumentam há séculos sobre a existência do infinito, os fractais têm uma analogia no mundo real. É um fenômeno bastante comum que ocorre na natureza. Por exemplo, esta couve-flor Romanesco é finita, mas tem uma estrutura **semelhante** porque cada parte do vegetal se parece com o todo, só que menor:

![fractal_num2](https://files.realpython.com/media/cauliflower.422e79018866.jpg)

<p align="center">
  Fractal Structure of a Romanesco Cauliflower
</p>

## O limite da estabilidade iterativa

Formalmente, o conjunto de Mandelbrot é o conjunto de números complexos, _c_, para os quais uma sequência infinita de números, _z0, z1, …, zn, …,_ permanece [limitada](https://en.wikipedia.org/wiki/Bounded_function). Em outras palavras, existe um limite que a magnitude de cada número complexo nessa sequência nunca excede. A sequência de Mandelbrot é dada pela seguinte fórmula recursiva:

![linear_system_num1](https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/latex_mandelbrot.95af84d59784.png&w=825&sig=76fd043318d344bd0c1a04d1b4d08579192d8a8e)

Em linguagem simples, para decidir se algum número complexo, _c_, pertence ao conjunto de Mandelbrot, você deve inserir esse número na fórmula acima. De agora em diante, o número c permanecerá constante enquanto você itera a sequência. O primeiro elemento da sequência, _z0_, é sempre igual a zero. Para calcular o próximo elemento, _z(n+1)_,
você continuará **elevando** ao quadrado o último elemento, _z(n)_, e **adicionando** seu número inicial, _c_, em um loop de feedback.
