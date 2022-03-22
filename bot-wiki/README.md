# Bot-Wiki
Projeto para extrair dados de um site e agrupá-los em um dataset

Precisava juntar dados sobre perfis automatizados no twitter para um outro projeto(talvez eu poste ele aqui depois), então encontrei o site da [botwiki](https://botwiki.org) .
Este site, que eu gostei muito por sinal, possui uma relação de diversos perfis automatizados no twitter, e também em outras plataformas. <p> Ao filtrar os bots referentes ao twitter percebi que para obter as informações necessárias seria preciso: </p>
  
1. Acessar todas as páginas de interesse do site. Existiam, na época, 64 páginas disponiveis e cada página continha cerca de 24 perfis por página.
2. Para obter o link para o twitter de um determinado bot era necessário acessar a página daquele bot na botwiki, clicando em seu box container, e depois clicar no link para o twitter daquele bot.
  
<p> Para obter de forma automatizada uma relação com o nome do perfil e o link do mesmo no twitter resolvi fazer um web scraping no site e após isso juntar os dados em um dataset.</p>
<mark> Básicamente o código criado ele: </mark>

1. Acessa a primeira página do [site](https://botwiki.org/bot/?networks=twitter-bots)
2. Coleta os links dos perfis, do próprio site, de cada bot na página.
3. Para cada um dos link obtidos no passo 2, acessa e coleta o link do twitter do respectivo bot.
4. Avança para a próxima página e repete os passos 2 e 3. Até finalizar todas as páginas.
  
 Estarei compartilhando o código criado e o  dataset gerado.
