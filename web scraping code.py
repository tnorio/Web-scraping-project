url = "https://botwiki.org/bot/page/{N_PAG}/?networks=twitter-bots"
paginas = 64 # são 64 paginas nesse site
nomes = [] # nome + descrição dos perfis
links_site = [] # link bot no site da botwiki
links_twt = [] # link do bot no twt

for pagina in range(1,paginas + 1 ):
  print("Estou aqui "+url.format(N_PAG=pagina))
  print("=================================================")
  request = get(url.format(N_PAG=pagina))
  soup = BeautifulSoup(request.text,"html.parser")
  links_perfis_botwiki = soup.findAll("h5",class_="card-title")   # todos os links dos perfis daquela pagina
  perfis_containers = soup.findAll("div", class_="col-sm-12 col-md-6 col-lg-4 list-item") # informações do box/container de cada perfil

# pegar os nomes dos perfis
  for perfil in perfis_containers:
    nomes.append(perfil.text.strip().replace("\n"," "))
    
# pegar o link pro twitter

  # Pega o link dos perfis na botwiki e insere na lista links_site
  for link in links_perfis_botwiki:
    links_site.append(str(link).partition('href="')[2].rsplit('"')[0]) 
 # Acessa os links dos perfis e coleta o link pro twitter
for linktwt in links_site:
  print("estou vendo " + linktwt)
  url_twt = linktwt
  requisicao = get(url_twt)
  sopa = BeautifulSoup(requisicao.text,"html.parser")
  links_twt.append(sopa.find("a",class_="btn").get("href"))

  time.sleep(random.randrange(0,5)) # vamos dar um delay para não sobre carregar os servidor do site.
  
  # criando o dataset
  
  bots_twt_botwiki = pd.DataFrame({"nomes":nomes,"links_twt":links_twt})
