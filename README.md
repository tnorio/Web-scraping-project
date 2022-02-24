# Web-scraping-project
Projeto para extrair dados de um site e agrupá-los em um dataset

Precisava juntar dados sobre perfis automatizados no twitter para um outro projeto(talvez eu poste ele aqui depois), então encontrei o site: https://botwiki.org.
Este site, que eu gostei muito por sinal, possui uma relação de diversos perfis automatizados no twitter, e também em outras plataformas. Ao filtrar os bots referentes ao twitter percebi que para obter as informações necessárias seria preciso:
1. existiam, na época, 64 páginas disponiveis e cada página continha cerca de 24 perfis por página.
2. Para obter o link para o twitter de um determinado perfil era necessário acessar a página daquele perfil, clicando em seu box container, e depois clicar no link para o twitter daquele perfil.
<p> Para obter de forma automatizada uma relação com o nome do perfil e o link do mesmo no twitter resolvi fazer um web scraping no site e após isso juntar os dados em um dataset. Estarei compartilhando o código criado e o  dataset gerado. </p>
