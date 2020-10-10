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
            <p>Para construirmos a máscara que deixa (praticamente) apenas o paraquedas à mostra, é necessário criar um <i>range</i> entre dois vetores em HSV <i>(lower_red</i> e <i>upper_red)</i>. Após a criação da máscara, o algoritmo exibirá as duas janelas, o <i>frame</i> com o vídeo original, <b>em sua resolução nativa</b>, rodando junto com a janela para a máscara, com os filtros aplicados.</p>
            <br>
            <p>Para uma melhor execução, o sistema de varredura funciona apenas a cada quatro (04) <i>frames</i> e a partir do <i>frame</i> 20. A varredura percorre toda a imagem preta e branca da máscara em busca de valores diferentes de zero, sendo esses detectados como o paraquedas. Dentro dessa condicional, dois laços, um dentro do outro, são iniciados, um contendo o valor do tamanho da janela em Y e o outro contendo o valor do tamanho da janela em X, respectivamente.</p>
            <br>
            <p>A variável <i>valor</i> é equivalente ao valor do pixel atual da máscara, sendo assim, caso o valor atual da máscara e valor dos <i>frames</i> sejam iguais, o algoritmo entra na condicional da criação da base de dados para os vetores de posição <i>cX e cY</i>. Para esta primeira condicional, o único critério é o tamanho dos vetores de poisção. Caso eles sejam menores do que dez, então eles receberão os valores atuais de X e Y. A partir de dez índices para cada vetor, novos critérios de condicionais são atribuídos.</p>
            <br>
            <p>Assim, entramos no cálculo da diferença. Este cálculo  funciona para que as curvas do gráfico final não fiquem tão bruscas e tenham valores mais próximos com a real distância entre os pontos.</p>
            <br>
            <p>Para a próxima condicional, temos: caso o valor atual de X seja maior que o valor anterior de X e caso o valor atual de Y seja maior que o valor anterior de Y, a diferença é calculada pela subtração do valor atual menos o valor anterior para X e para Y. Após o cálculo, o valor anterior mais a diferença dividida por dois <i>((n-1) + ((n-(n-1)/2)))</i> é adicionado aos vetores de posição. Após o cálculo, o valor do frame, da posição em X e da posição em Y são adicionados ao arquivo <i>coords.txt</i>. Variável <i>K</i> e<i> frame_atual</i> tem seus valores aumentados em 1. <i>K</i> é o valor do índice atual da base de dados para as comparações dos vetores de X e Y.</p>
            <br>
            <p>A segunda condicional, na sequência é o contrário da condição anterior (caso o valor anterior seja maior que o valor atual, tanto para X quanto para Y). A diferença também é calculada de forma invertida, com o valor maior subtraindo o valor menor. Após o cálculo, o processo de finalização da condicional é o mesmo.</P>
            <br>
            <p>A função <i>numpy.savetxt</i> salva, a cada quatro quadros, a imagem com base na máscara. O arquivo salvo em questão é um <i>txt</i> com valores 0 e 255, onde 255 é a posição do paraquedas e 0 são os pontos nulos da imagem.</p>
            <br>
            <p>Ao final, temos o cálculo do delta para o tempo, resultando no tempo de execução total do algoritmo. Os índices 0 e 1 do vetor <i>cY</i> são zerados, pois não conseguimos remover os ruídos iniciais da imagem.</p>
            <br>
            <p>Após o cancelamento manual dos ruídos iniciais, o gráfico é construído e tem sua base nos vetores <i>cX</i> e<i> cY</i>, vale ressaltar que o tamanho dos vetores tem que ser igual para que o gráfico seja <i>plotado</i>.</p>
    </li>
  </ol>
  <br>
  <li>
    coords.py
    <br>
    <p>O arquivo de coordenadas é dividido em três colunas, sendo elas, respectivamente, F (<i>frames</i>), X e Y. Os dados são coletados pelo arquivo <i>main.py</i> e servem para uma futura planilha no Excel.</p>
  </li>
  <br>
  <li>
  ./src
  <br>
  <p>O diretório <i>src</i> conta com o vídeo utilizado para que o algoritmo funcione.</p>
  </li>
  <br>
  <li>
  ./data
    <br>
    <p>O diretório <i>data</i> armazena os arquvios de texto para as matrizes binárias a cada quatro frames da varredura. Para visualizar o paraquedas nesses arquivos, é recomendável utilizar o comando de busca <i>Ctrl + F</i> e digitar 255 para que os valores encontrados fiquem grifados, facilitando a visualização. Cada arquivo é nomeado com o número do quadro em que foi criado.</p>
  </li>
  <br>
  <li>
  Próximas atualizações
  <br>
  <p>Atualização na otimização do programa; Utilizar resolução dinâmica para que o mesmo código sirva para diferentes vídeos do mesmo tipo; Atomização das funções condicionais e melhoramento das funções; Automatização da passagem de dados de <i>txt</i> para <i>xls</i>; Diminuição do tempo de execução; Utilização de outras linguagens para a parte de laços (C, por exemplo) e aperfeiçoamento do tratamento da imagem (diminuição de ruídos, objeto melhor detectado, sem falhas).</p>
 </ol>

