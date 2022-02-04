Este tutorial irá guiá-lo através de um projeto divertido envolvendo [números complexos em Python](https://realpython.com/python-complex-numbers/). Você aprenderá sobre fractais e criará uma arte verdadeiramente impressionante desenhando o **conjunto Mandelbrot** usando as bibliotecas Matplotlib e Pillow do Python. Ao longo do caminho, você aprenderá como esse famoso fractal foi descoberto, o que ele representa,
e como se relaciona com outros fractais.

Conhecer os princípios de [programação orientada a objetos](https://realpython.com/python3-object-oriented-programming/) e a [recursão](https://realpython.com/python-recursion/) permitirá que você aproveite ao máximo a sintaxe expressiva do Python para escrever um código limpo que se lê quase como fórmulas matemáticas. Para entender os detalhes algorítmicos de fazer fractais, você também deve estar confortável com [números complexos](https://en.wikipedia.org/wiki/Complex_number),
[logaritmos](https://en.wikipedia.org/wiki/Logarithm), [teoria dos conjuntos](https://en.wikipedia.org/wiki/Set_theory) e [funções iteradas](https://en.wikipedia.org/wiki/Iterated_function). Mas não deixe que esses pré-requisitos o assustem, pois você poderá acompanhar e produzir a arte de qualquer maneira!

Neste tutorial, você aprenderá como:

> ° Aplicar **números complexos** a um problema prático
>
> ° Encontre membros dos conjuntos **Mandelbrot e Julia**
>
> ° Desenhe esses conjuntos como **fractais** usando **Matplotlib e Pillow**
>
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

![linear_system_num1](https://raw.githubusercontent.com/CarlosViniMSouza/MandrelbotSet/master/images/linear_system_num1.webp)

Em linguagem simples, para decidir se algum número complexo, _c_, pertence ao conjunto de Mandelbrot, você deve inserir esse número na fórmula acima. De agora em diante, o número c permanecerá constante enquanto você itera a sequência. O primeiro elemento da sequência, _z0_, é sempre igual a zero. Para calcular o próximo elemento, _z(n+1)_,
você continuará **elevando** ao quadrado o último elemento, _z(n)_, e **adicionando** seu número inicial, _c_, em um loop de feedback.

Em linguagem simples, para decidir se algum número complexo, _c_, pertence ao conjunto de Mandelbrot, você deve inserir esse número na fórmula acima. De agora em diante, o número _c_ permanecerá constante enquanto você itera a sequência. O primeiro elemento da sequência, _z0_, é sempre igual a zero. Para calcular o próximo elemento, _z(n+1)_,
você continuará **elevando** ao quadrado o último elemento, _z(n)_, e **adicionando** seu número inicial, _c_, em um loop de feedback.

Ao observar como a sequência de números resultante se comporta, você poderá classificar seu número complexo, _c_, como um membro do conjunto de Mandelbrot ou não. A sequência é infinita, mas você deve parar de calcular seus elementos em algum momento. Fazer essa escolha é um tanto arbitrário e depende do seu nível de confiança aceito, pois mais elementos fornecerão uma decisão mais precisa sobre _c_.

> ° **Nota:** Todo o conjunto de Mandelbrot se encaixa em um círculo com um raio de dois quando representado no plano complexo. Este é um fato útil que permitirá pular muitos cálculos desnecessários para pontos que certamente não pertencem ao conjunto.

Com números complexos, você pode imaginar esse processo iterativo visualmente em duas dimensões, mas pode ir em frente e considerar apenas números reais para simplificar agora. Se você implementasse a equação acima em Python, poderia ser algo assim:

```python
def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c
```

Sua função z() retorna o enésimo elemento da sequência, e é por isso que ela espera o índice de um elemento, _n_, como o primeiro argumento. O segundo argumento, _c_, é um número fixo que você está testando. Essa função continuaria chamando a si mesma infinitamente devido à recursão. No entanto, para quebrar essa cadeia de chamadas **recursivas**,
uma condição verifica o caso base com uma solução imediatamente conhecida — zero.

Tente usar sua nova função para encontrar os dez primeiros elementos da sequência para _c_ = 1 e veja o que acontece:

```python
for n in range(10):
    print(f"z({n}) = {z(n, c=1)}")

"""
Output:

z(0) = 0
z(1) = 1
z(2) = 2
z(3) = 5
z(4) = 26
z(5) = 677
z(6) = 458330
z(7) = 210066388901
z(8) = 44127887745906175987802
z(9) = 1947270476915296449559703445493848930452791205
"""
```