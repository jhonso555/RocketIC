<h1>RocketIC - Documentação</h1>

<strong> O algoritmo consiste em detectar um paraquedas em queda e mostrar sua posição durante um intervalo de frames. </strong>

<ol><h2>Funcionamento</h2>
  <p>Para a execução deste algoritmo, são necessários os seguintes componentes:</p>
    <ol>
    <br>
        <ul>Python 3</ul>
        <ul>Opencv</ul>
        <ul>Matplotlib</ul>
        <ul>Numpy</ul>
    </ol>
  </li>
 </ol>
 <br><br>
 <ol><h2>Arquivos e diretórios</h2>
    <li>main.py
        <ol>
        <br>
            <p>Neste arquivo encontramos o coração do nosso algoritmo. Onde obtemos a criação de uma máscar a partir do nosso vídeo da pasta <i>src</i>, o arquivo main continua em funcionamento durante toda a execução do vídeo, ou até que a tecla 'q' seja pressionada.</p>
            <br>
            <p>Para que seja construída a máscara que deixa (praticamente) apenas o paraquedas a mostra, é necessário criar um range entre dois vetores HSV <i>(lower_red e upper_red)</i>. Após a criação da máscara, o algoritmo exibirá as duas janelas, o <i>frame</i> com o vídeo original, <b>em sua resolução nativa</b> rodando junto com outra janela para a máscara, com os efeitos aplicados.</p>
            <br>
            <p>Para uma melhor execução, o sistema de varredura funciona apenas a cada quatro <i>frames</i> e a partir do <i>frame</i> 19. Dentro dessa condicional, dois laços, um dentro do outro, são iniciados, um contendo o valor do tamanho da janela em Y e o outro contendo o valor do tamanho da janela em X, respectivamente.</p>
            <br>
            <p>A variável <i>valor</i> é equivalente ao valor do pixel atual da máscara, sendo assim, caso o valor atual da máscara e valor dos <i>frames</i> seja igual, ele entra na condicional da criação da base de dados para os vetores de posição <i>cX e cY</i>. Para esta condicional, o único critério é o tamanho dos vetores de poisção. Caso eles sejam menores do que dez, então eles receberão os valores atuais de X e Y. A partir de dez índices para cada vetor, novos critérios de condicionais são atribuídos.</p>
            <br>
            <p>Assim entramos no cálculo de diferença. O cálculo de diferença entre os pontos serve para que as curvas no gráfico não fiquem tão bruscas e tenham valores mais próximos com a real distância entre os pontos.</p>
            <br>
            <p>Para a próxima condicional, temos: caso o valor atual de X seja maior que o valor anterior de X e caso o valor atual de Y seja maior que o valor anterior de Y, a diferença é calculada pela subtração do valor atual menos o valor anterior para X e para Y. Após o cálculo, o valor anterior mais a diferença dividida por dois <i>((n-1) + ((n-(n-1)/2)))</i> é adicionado aos vetores de posição. 
    </li>
 </ol>
