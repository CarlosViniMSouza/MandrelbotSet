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

Observe a rápida taxa de crescimento desses elementos de sequência. Ela diz algo sobre a pertinência de _c_ = 1. Especificamente, ela não pertence ao conjunto de Mandelbrot, porque a sequência correspondente cresce sem limites.

Às vezes, uma abordagem **iterativa** pode ser mais eficiente do que uma recursiva. Aqui está uma função equivalente que cria uma sequência infinita para o valor de entrada especificado, _c_:

```python
def sequence(c):
    z = 0
    while True:
        yield z
        z = z ** 2 + c
```

A função `sequence()` retorna um [objeto gerador](https://realpython.com/introduction-to-python-generators/) gerando elementos consecutivos da sequência infinitamente em um loop. Como ele não retorna os índices dos elementos correspondentes, você pode [enumerá-los](https://realpython.com/python-enumerate/) e parar o loop após um determinado número de iterações:

```python
for n, z in enumerate(sequence(c=1)):
    print(f"z({n}) = {z}")
    if n >= 9:
        break

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

O resultado é o mesmo de antes, mas a função do gerador permite calcular os elementos de sequência de forma mais eficiente usando a [avaliação lenta](https://en.wikipedia.org/wiki/Lazy_evaluation). Além disso, a iteração elimina chamadas de função redundantes para os elementos de sequência já calculados. Como consequência, você não corre mais o risco de atingir o [limite máximo de recursão](https://realpython.com/python-recursion/#recursion-in-python).

A maioria dos números fará essa sequência divergir ao infinito. No entanto, alguns a manterão **estável** convergindo a sequência para um único valor ou permanecendo dentro de um intervalo limitado. Outros tornarão a sequência **periodicamente estável**, alternando entre os mesmos poucos valores. Valores estáveis ​​e periodicamente estáveis ​​compõem o conjunto de Mandelbrot.

Por exemplo, conectar _c_ = 1 faz a sequência crescer sem limites como você acabou de aprender, mas _c_ = -1 faz com que ela salte entre 0 e -1 repetidamente, enquanto _c_ = 0 fornece uma sequência composta por um único valor:

| Element	| c = -1 | c = 0	|               c = 1 |
|---------|--------|--------|---------------------|
|   z0	  |   0	   |   0	  |                 0   |
|   z1	  |   -1   |   0	  |                 1   |
|   z2	  |   0	   |   0	  |                 2   |
|   z3	  |   -1	 |   0	  |                 5   |
|   z4	  |   0	   |   0	  |                26   |
|   z5	  |   0	   |   0	  |               677   |
|   z6	  |   -1   |   0	  |           458,330   |
|   z7	  |   0	   |   0	  |   210,066,388,901   |

Não é óbvio quais números são estáveis ​​e quais não são, porque a fórmula é sensível até mesmo à menor mudança do valor testado, _c_. Se você marcar os números estáveis ​​no plano complexo, verá o seguinte padrão surgir:

![fractal_num3](https://files.realpython.com/media/plot_mandelbrot_with_circle.ad8b99d3ee01.png)

<p align="center">
  Depiction of the Mandelbrot Set on the Complex Plane
</p>

Esta imagem foi gerada executando a fórmula recursiva até vinte vezes por pixel, com cada pixel representando algum valor c. Quando a [magnitude](https://en.wikipedia.org/wiki/Magnitude_(mathematics)) do número complexo resultante ainda era razoavelmente pequena após todas as iterações, o pixel correspondente era colorido em preto. No entanto, assim que a magnitude excedeu o raio de dois,
então a iteração parou e pulou o pixel atual.

> **Curiosidade**: O fractal correspondente ao conjunto de Mandelbrot tem uma **área** finita estimada em 1,506484 unidades quadradas. Os matemáticos ainda não identificaram o número exato e não sabem se é racional ou não. Por outro lado, o **perímetro** do conjunto de Mandelbrot é infinito. Confira o **paradoxo do litoral** para aprender sobre um paralelo interessante desse fato estranho na vida real.

Você pode achar surpreendente que uma fórmula relativamente simples que envolve apenas adição e multiplicação possa produzir uma estrutura tão elaborada. Mas isso não é tudo. Acontece que você pode pegar a mesma fórmula e usá-la para gerar infinitos fractais únicos! Você quer ver como?
