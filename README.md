<h1>RocketIC - Documentação</h1>

<strong> O algoritmo consiste em detectar um paraquedas em queda e mostrar sua posição durante um intervalo de quadros.</strong>

<ol><h2>Funcionamento</h2>
  <p>Para a execução deste algoritmo, são necessários os seguintes componentes:</p>
    <ol>
    <br>
        <ul><a href="https://www.python.org/downloads/">Python 3</a></ul>
        <ul><a href="https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html">Opencv</a></ul>
        <ul><a href="https://matplotlib.org/3.1.1/users/installing.html">Matplotlib</a></ul>
        <ul><a href="https://numpy.org/install/">NumPy</a></ul>
    </ol>
  </li>
 </ol>
 <br><br>
 <ol><h2>Arquivos e diretórios</h2>
    <li>main.py
        <ol>
        <br>
            <p>Neste arquivo, encontramos o coração do nosso projeto, onde obtemos a criação de uma máscara a partir do vídeo da pasta <i>src</i>. O arquivo <i>main</i> continua em funcionamento até que o vídeo acabe, ou até que a tecla '<i>q</i>' seja pressionada.</p>
            <br>
            <p>Para construirmos a máscara que deixa (praticamente) apenas o paraquedas à mostra, é necessário criar um <i>range</i> de cores que serão detectadas no vídeo. Para isso, criamos as <i>trackbars</i>, onde cada uma representa um valor para <i>low</i> e <i>high</i> de cada valor do HSV (<i>hue, sturation, value</i>). Vale ressaltar que, na última atualização, esses valores podem ser trocados durante a execução do algoritmo, fazendo com que as mudanças sejam vistas em tempo real e o valor atual das barras é o recomendado para o vídeo de testes que utilizamos. Após a criação da máscara, o algoritmo exibirá as duas janelas, o <i>frame</i> com os filtros aplicados e as barras para alterações do <i>range</i> de cores e a máscara, ambos <b>em sua resolução nativa</b>.</p>
            <br>
            <p>Para que obtenhamos uma execução não tão longa, o sistema de varredura funciona apenas a cada quatro quadros do vídeo e a partir do vigésimo <i>frame</i>. A varredura percorre toda a imagem preta e branca da <b>máscara</b> em busca de valores diferentes de zero, sendo esses detectados como o paraquedas, ou ruídos, dependendo da maneira como o filtro foi inserido. Dentro dessa condicional, dois laços, um dentro do outro, são iniciados, o primeiro contendo o valor da resolução do vídeo em Y e o segundo contendo o valor da resolução do vídeo em X, respectivamente.</p>
            <br>
            <p>A variável <i>pxValue</i> é equivalente ao valor do pixel atual da máscara, sendo assim, caso <i>pxValue</i> seja diferente de zero e as variáveis de <i>frames</i> sejam iguais, o algoritmo entra na condicional da criação da base de dados para os vetores de posição <i>posX e posY</i>. Para esta primeira condicional, o único critério é o tamanho dos vetores de poisção. Caso eles tenham menos de dez índices, eles receberão os valores atuais de X e Y. A partir de dez índices para cada vetor, novos critérios de condicionais são atribuídos.</p>
            <br>
            <p>Assim, entramos no cálculo da diferença. Este cálculo  serve para que as curvas do gráfico final não destoem tanto do valor anterior e tenham valores mais próximos com a real distância entre os pontos.</p>
            <br>
            <p>Para a próxima condicional, temos: caso os valores atuais de X e Y sejam maiores que os valores anteriores de X e Y , a diferença é calculada pela subtração do valor atual menos o valor anterior. Após o cálculo, o valor da conta <b><i>(n-1) + (n-(n-1)/2)</i></b> é adicionado aos vetores de posição. Após o cálculo, o valor do quadro do vídeo, da posição em X e da posição em Y são adicionados ao arquivo <i>coords.txt</i>. Variáveis <i>K</i> e<i> frame_atual</i> têm seus valores aumentados em 1. <i>K</i> é o valor do índice atual da base de dados para as comparações dos vetores de X e Y.</p>
            <br>
            <p>A segunda condicional, na sequência é o contrário da condição anterior (caso o valor anterior seja maior que o valor atual, tanto para X quanto para Y). A diferença também é calculada de forma invertida, com o valor maior subtraindo o valor menor. Após o cálculo, o processo de finalização da condicional é o mesmo.</p>
            <br>
            <p>A função <i>numpy.savetxt</i> salva, a cada quatro quadros, a imagem em texto com base na máscara. O arquivo salvo em questão é um <i>txt</i> com valores 0 e 255, onde 255 é a posição do paraquedas e 0 são os pontos nulos da imagem.</p>
            <br>
            <p>Ao final, temos o cálculo do delta para o tempo, resultando no tempo de execução total do algoritmo. Os índices 0 e 1 do vetor <i>posY</i> são zerados, pois não conseguimos remover os ruídos iniciais da imagem devido a cor do chão ser parecida com a cor do paraquedas.</p>
            <br>
            <p>Após o cancelamento manual dos ruídos iniciais, o gráfico é construído e tem sua base nos vetores <i>posX</i> e <i>posY</i>, vale ressaltar que o tamanho dos vetores tem que ser igual para que o gráfico seja mostrado.</p>
    </li>
  </ol>
  <br>
  <li>
    coords.txt
    <br>
    <p>O arquivo de coordenadas é dividido em três colunas, sendo elas, respectivamente, F (<i>frames</i>), X e Y. Ao final do arquivo, consta o tempo total da execução do programa. Os dados são coletados pelo arquivo <i>main.py</i>.
  </li>
  <br>
  <li>
  ./src
  <br>
  <p>O diretório <i>src</i> conta com os vídeos utilizados para os testes do algoritmo, sendo essa a pasta onde os vídeos que serão usados devem ser alocados.</p>
  </li>
  <br>
  <li>
  ./data
    <br>
    <p>O diretório <i>data</i> armazena os arquvios de texto para as matrizes binárias a cada quatro quadros da varredura. Para visualizar o paraquedas nesses arquivos, é recomendável utilizar o comando de busca em texto e digitar 255 para que os valores encontrados sejam grifados, facilitando a visualização. Cada arquivo é nomeado com o número do quadro em que foi criado. O diretório é apagado e recriado sempre que o algoritmo é executado. Caso o diretório não exista, ele será criado automaticamente pelo algoritmo.</p>
  </li>
  <br>
  <li>
  Possíveis próximas atualizações
  <br>
  <p>Diminuição do tempo de execução; Utilização de outras linguagens para a parte de laços.</p>
 </ol>

