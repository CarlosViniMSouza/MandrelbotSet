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

<p align="center">
  <table>
    <tr>
      <td>Element</td>
      <td>c = -1</td>
      <td>c = 0</td>
      <td>c = 1</td>
    </tr>
    <tr>
      <td>z0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>z2</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <td>z3</td>
      <td> -1 </td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <td>z4</td>
      <td>0</td>
      <td>0</td>
      <td>26</td>
    </tr>
    <tr>
      <td>z5</td>
      <td> -1 </td>
      <td>0</td>
      <td>677</td>
    </tr>
    <tr>
      <td>z6</td>
      <td> -1 </td>
      <td>0</td>
      <td>458,330</td>
    </tr>
    <tr>
      <td>z7</td>
      <td>0</td>
      <td>0</td>
      <td>210,066,388,901</td>
    </tr>
  </table>
</p>

Não é óbvio quais números são estáveis ​​e quais não são, porque a fórmula é sensível até mesmo à menor mudança do valor testado, _c_. Se você marcar os números estáveis ​​no plano complexo, verá o seguinte padrão surgir:

![fractal_num3](https://files.realpython.com/media/plot_mandelbrot_with_circle.ad8b99d3ee01.png)

<p align="center">
  Depiction of the Mandelbrot Set on the Complex Plane
</p>

Esta imagem foi gerada executando a fórmula recursiva até vinte vezes por pixel, com cada pixel representando algum valor c. Quando a [magnitude](https://en.wikipedia.org/wiki/Magnitude_(mathematics)) do número complexo resultante ainda era razoavelmente pequena após todas as iterações, o pixel correspondente era colorido em preto. No entanto, assim que a magnitude excedeu o raio de dois,
então a iteração parou e pulou o pixel atual.

> **Curiosidade**: O fractal correspondente ao conjunto de Mandelbrot tem uma **área** finita estimada em 1,506484 unidades quadradas. Os matemáticos ainda não identificaram o número exato e não sabem se é racional ou não. Por outro lado, o **perímetro** do conjunto de Mandelbrot é infinito. Confira o **paradoxo do litoral** para aprender sobre um paralelo interessante desse fato estranho na vida real.

Você pode achar surpreendente que uma fórmula relativamente simples que envolve apenas adição e multiplicação possa produzir uma estrutura tão elaborada. Mas isso não é tudo. Acontece que você pode pegar a mesma fórmula e usá-la para gerar infinitos fractais únicos! Você quer ver como?

# O Mapa dos Conjuntos de Julia

É difícil falar sobre o conjunto de Mandelbrot sem mencionar os conjuntos de Julia, que foram descobertos pelo matemático francês [Gaston Julia](https://en.wikipedia.org/wiki/Gaston_Julia) várias décadas antes sem a ajuda de computadores. Os conjuntos de Julia e o conjunto de Mandelbrot estão intimamente relacionados porque você pode obtê-los através da mesma fórmula recursiva, apenas com diferentes conjuntos de condições de partida.

Embora haja apenas um conjunto de Mandelbrot, existem infinitos conjuntos de Julia. Até agora, você sempre iniciou a sequência em _z0_ = 0 e testou sistematicamente algum número complexo arbitrário, _c_, quanto à sua pertinência. Por outro lado, para descobrir se um número pertence a um conjunto de Julia, você deve usar esse número como ponto de partida para a sequência e escolher outro valor para o parâmetro c.

Aqui está uma comparação rápida dos termos da fórmula, dependendo de qual conjunto você está investigando:

<p align="center">
  <table>
    <tr>
      <td>Termo</td>
      <td>Conjunto Mandrelbot</td>
      <td>Conjunto Julia</td>
    </tr>
    <tr>
      <td>z0</td>
      <td>0</td>
      <td>Valor do Candidato</td>
    </tr>
    <tr>
      <td>c</td>
      <td>Valor do Candidato</td>
      <td>Constante Fixa</td>
    </tr>
  </table>
</p>

No primeiro caso, c representa um membro potencial do conjunto de Mandelbrot e é o único valor de entrada necessário porque _z0_ permanece fixo em zero. No entanto, cada termo muda seu significado quando você usa a fórmula no modo Julia. Agora, _c_ funciona como um parâmetro que determina a forma e a forma de um conjunto de Julia inteiro, enquanto _z0_ se torna seu ponto de interesse. Ao contrário de antes, a fórmula para um conjunto de Julia espera não um, mas dois valores de entrada.

Você pode modificar uma de suas funções definidas antes para torná-la mais genérica. Dessa forma, você pode criar sequências infinitas começando em qualquer ponto em vez de sempre zero:

```python
def sequence(c, z=0):
    while True:
        yield z
        z = z ** 2 + c
        return z


print(sequence(c=4, z=0))
# Output: <generator object sequence at 0x000001F498FE5FC0>
```

Graças ao [valor do argumento padrão](https://realpython.com/python-optional-arguments/) na linha destacada, você ainda pode usar esta função como antes porque _z_ é opcional. Ao mesmo tempo, você pode alterar o ponto inicial da sequência. Talvez você tenha uma ideia melhor depois de definir as funções de wrapper para os conjuntos Mandelbrot e Julia:

```python
def mandelbrot(candidate):
    return sequence(z=0, c=candidate)

def julia(candidate, parameter):
    return sequence(z=candidate, c=parameter)
```

Cada função retorna um objeto gerador ajustado para sua condição inicial desejada. Os princípios para determinar se um valor candidato pertence a um conjunto de Julia são semelhantes ao conjunto de Mandelbrot que você viu anteriormente. Em poucas palavras, você deve iterar a sequência e observar seu comportamento ao longo do tempo.

Benoît Mandelbrot foi, de fato, estudar Julia define em sua pesquisa científica. Ele estava particularmente interessado em encontrar os valores de c que produzem os chamados conjuntos de Julia [conectados](https://en.wikipedia.org/wiki/Connected_space) em oposição aos seus homólogos desconectados. Estes últimos são conhecidos como [conjuntos de Fatou](https://en.wikipedia.org/wiki/Fatou_set) e aparecem como poeira composta por um número infinito de peças quando visualizadas no plano complexo:

![fractal_num4](https://files.realpython.com/media/plot_julia_fatou.e0eee824ae2d.png)

<p align="center">
  Connected Julia Set vs Fatou Dust
</p>

A imagem no canto superior esquerdo representa um conjunto de Julia conectado derivado de _c_ = 0,25, que pertence ao conjunto de Mandelbrot. Você sabe que inserir um membro do conjunto de Mandelbrot na fórmula recursiva produzirá uma sequência de números complexos que convergem. Os números convergem para 0,5 neste caso. Contudo, uma pequena mudança em c pode de repente transformar seu conjunto de Julia em poeira desconectada e fazer a sequência correspondente divergir para o infinito.

Coincidentemente, os conjuntos de Julia conectados correspondem a valores de c que geram sequências estáveis ​​da fórmula recursiva acima. Assim, pode-se dizer que Benoît Mandelbrot estava procurando o **limite da estabilidade iterativa**, ou um mapa de todos os conjuntos de Julia que mostrasse onde esses conjuntos estão conectados e onde são poeira.

Veja como a escolha de diferentes pontos para o parâmetro c no plano complexo afeta o conjunto de Julia resultante:

![fractal_num5](https://github.com/CarlosViniMSouza/MandrelbotSet/blob/master/images/fractal_num5.jpg)

<p align="center">
  It's a GIF; but i can't insert here!
</p>

O pequeno círculo vermelho em movimento indica o valor de _c_. Enquanto permanecer dentro do conjunto de Mandelbrot mostrado à esquerda, o conjunto de Julia correspondente representado à direita permanece conectado. Caso contrário, o conjunto de Julia estoura como uma bolha se espalhando em infinitas peças empoeiradas.

Você notou como os conjuntos de Julia estão mudando de forma? Acontece que um determinado conjunto de Julia compartilha características visuais comuns com a área específica do conjunto de Mandelbrot usado para semear o valor de _c_. Quando você olha através de uma lupa, ambos os fractais parecerão um pouco semelhantes.

Ok, chega de teoria. Hora de traçar seu primeiro conjunto de Mandelbrot!

# Traçando o conjunto de Mandelbrot usando o Matplotlib do Python

Há muitas maneiras de visualizar o conjunto de Mandelbrot em Python. Se você estiver confortável com [NumPy](https://realpython.com/numpy-tutorial/) e [Matplotlib](https://realpython.com/python-matplotlib-guide/), essas duas bibliotecas juntas fornecerão uma das maneiras mais diretas de plotar o fractal. Eles convenientemente poupam você de ter que converter entre o mundo e as coordenadas de pixel.

> **Nota**: As coordenadas mundiais correspondem ao espectro contínuo de números no plano complexo, estendendo-se até o infinito. Por outro lado, as coordenadas de pixel são discretas e limitadas pelo tamanho finito da tela. 

Para gerar o conjunto inicial de **valores candidatos**, você pode aproveitar [np.linspace()](https://realpython.com/np-linspace-numpy/), que cria números uniformemente espaçados em um determinado intervalo:

```python
import numpy as np

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j
```

A função acima retornará um array bidimensional de números complexos dentro de uma área retangular dada por quatro parâmetros. Os parâmetros xmin e xmax especificam os limites na direção horizontal, enquanto `ymin` e `ymax` o fazem na direção vertical. O quinto parâmetro, `pixel_density`, determina o número desejado de pixels por unidade.

Agora, você pode pegar essa [matriz](https://en.wikipedia.org/wiki/Matrix_(mathematics)) de números complexos e executá-la pela conhecida fórmula recursiva para ver quais números permanecem estáveis ​​e quais não. Graças à [vetorização](https://realpython.com/numpy-array-programming/#what-is-vectorization) do NumPy, você pode passar a matriz como um único parâmetro, _c_, e realizar os cálculos em cada elemento sem precisar escrever loops explícitos:

```python
def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2
```

O código na linha destacada é executado para _todos_ os elementos da matriz _c_ em cada iteração. Como _z_ e _c_ começam com dimensões diferentes inicialmente, o NumPy usa a [transmissão](https://realpython.com/numpy-array-programming/#broadcasting) para estender habilmente a primeira, de modo que ambos acabem tendo formas compatíveis. Finalmente, a função cria uma [máscara](https://realpython.com/numpy-tutorial/#masking-and-filtering) bidimensional de valores booleanos sobre a matriz resultante, _z_. Cada valor corresponde à estabilidade da sequência naquele ponto.

> **Nota**: Para aproveitar a computação vetorizada, o loop no exemplo de código continua elevando ao quadrado e adicionando números incondicionalmente, independentemente de quão grandes eles já fossem. Isso não é ideal porque, em muitos casos, os números divergem para o infinito logo no início, tornando a maioria dos cálculos um desperdício.
>
> Além disso, os números que crescem rapidamente geralmente levam a um erro de estouro. O NumPy detecta esses estouros e emite um aviso no fluxo de erro padrão (stderr). Se você deseja suprimir esses avisos, pode definir um filtro relevante antes de chamar sua função:
>
> ```python
> import numpy as np
>
> np.warnings.filterwarnings("ignore")
> ```
>
> Ignorar esses estouros é inofensivo porque você não está interessado em magnitudes específicas, mas sim se elas se encaixam no limite determinado.

Após um número escolhido de iterações, a magnitude de cada número complexo na matriz permanecerá dentro ou excederá o limite de dois. Aqueles que são pequenos o suficiente são provavelmente membros do conjunto de Mandelbrot. Agora você pode visualizá-los usando o Matplotlib.

# Gráfico de dispersão de baixa resolução

Uma maneira rápida e suja de visualizar o conjunto de Mandelbrot é através de um [gráfico de dispersão](https://realpython.com/visualizing-python-plt-scatter/), que ilustra as relações entre variáveis ​​emparelhadas. Como os números complexos são pares de componentes **reais** e **imaginários**, você pode desembaraçá-los em matrizes separadas que funcionarão bem com o gráfico de dispersão.

Mas primeiro, você precisa transformar sua máscara booleana de estabilidade nos números complexos iniciais que semearam a sequência. Você pode fazer isso com a ajuda da **filtragem mascarada** do NumPy:

```python
def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]
```

Essa função retornará uma matriz unidimensional composta apenas pelos números complexos que são estáveis ​​e, portanto, pertencem ao conjunto de Mandelbrot. Ao combinar as funções definidas até agora, você poderá mostrar um gráfico de dispersão usando o Matplotlib. Não se esqueça de adicionar a instrução de importação necessária no início do seu arquivo:

```python
import matplotlib.pyplot as plt
import numpy as np

np.warnings.filterwarnings("ignore")
```

Isso traz a interface de plotagem para seu namespace atual. Agora você pode calcular seus dados e plotá-los:

```python
c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)
members = get_members(c, num_iterations=20)

plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
```

A chamada para `complex_matrix()` prepara uma matriz retangular de números complexos no intervalo de -2 a 0,5 na direção x e entre -1,5 e 1,5 na direção y. A chamada subsequente para `get_members()` passa apenas pelos números que são membros do conjunto Mandelbrot. Finalmente, `plt.scatter()` plota o conjunto e `plt.show()` revela esta imagem:

![fractal_img_py_num1](../images/fractal_img_py_num1.jpeg)

<p align="center">
  Visualization of the Mandelbrot Set in a Scatter Plot
</p>

Ele contém 749 pontos e se assemelha à impressão ASCII original feita em uma impressora matricial pelo próprio Benoît Mandelbrot algumas décadas atrás. Você está revivendo a história matemática! Brinque ajustando a densidade de pixels e o número de iterações para ver como elas afetam o resultado.
