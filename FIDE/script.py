from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import re

# GET URL INFOS
url = "https://www.fide.com/directory/affiliated-organizations"
page_info = [] # Lista das infos

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

# browser open
driver = webdriver.Chrome(options=options)

# get url
driver.get(url)
# loading dealy
time.sleep(10)

#store all page infos in a page_info list
#this saves time if we need to change the code / find bugs later
for i in range(1,24):
        driver.find_element_by_xpath(f'/html/body/app-root/app-client/app-directory/section/div/app-client-directory-list/app-shared-client-template-directory/div/div[1]/div/ul/li[{i}]/div').click()
        time.sleep(20)
    
        page_source = driver.page_source
        parsed_content = BeautifulSoup(page_source, 'html.parser')
        
        page_info.append(parsed_content)

driver.quit()

# EXTRACT INFOS FROM PAGE SOURCES
url = "https://www.fide.com/directory/affiliated-organizations"

nomes = []
president = []
sites = []
emails = []
tels = []
enderecos = []
mobiles = []
fax = []
acronym = []
logos = []

caracteres_tel = ("(",")","+","-",";"," ","0","1","2","3","4","5","6","7","8","9")

for i in page_info:
        membros = i.find_all("div", class_="member-block__one ng-star-inserted")

        membro = membros[0].get_text().strip()
        membro = membro.replace("https://"," https://").replace("Email:"," Email:").replace("Tel.:"," Tel:").replace("Tel:"," Tel:").replace("Url:"," Url:").replace("Address:"," Address:").replace("Mobile:"," Mobile:").replace("Fax:"," Fax:")
        print("MEMBRO:", membro)
        print("==========================")

        # Name
        nome = re.split(r"Email:|Tel|Url:|Fax:|Mobile:|Address:", membro)[0].strip()
        nome = nome.split("/")[0]
        nomes.append(nome.strip())
        print("NOME: ", nome)
        print("==========================")
        
        # Acronym
        if "(" and ")" in nome:
            pos1 = nome.find("(")
            pos2 = nome.find(")")
            
            acronym.append(nome[pos1:pos2+1])
        else:
            words = nome.split("/")[0]
            acro = "("
            for word in words.split():
                acro += str(word[0])
            acro = acro.upper()+")"
            acronym.append(acro)
        
        # Logo
        try:
            logo = i.find("div",class_="member-block-image")
            link = str(logo).split('src="')[1][:-(len('"/></div>'))]
            logos.append(link)
        except:
            logos.append(np.nan)
        
        # President
        
        if "President" in i.get_text():
            nome = re.split(r"Email:|Tel|Url:|Fax:|Mobile:|Address:", membros[1].get_text())[0]
            president.append(nome.replace("President","").strip())
        else:
            president.append(np.nan)
            

        # Email
        if "Email" in membro:
            email = re.search("Email:."+r"[\S]+",membro).group()
            email = email.replace("Email:","")
            emails.append(email.strip())
            print("EMAIL:  ", email)
            print("==========================")
        else:
            emails.append(np.nan)
            print("+++++++++++ EMAIL == NAN ++++++++++")

        # Tel
        if "Tel" in membro:
            pos = membro.find("Tel:")+len("Tel:")
            tel_sujo = membro[pos:]
            tel = ""
            
            for i in tel_sujo:
                if i in caracteres_tel:
                    tel += "".join(i)
                else:
                    break
            
            tels.append(tel.strip())
            print("TELEFONE: ", tel)
            print("==========================")
        else:
            tels.append(np.nan)
            print("+++++++++++ TELEFONE == NAN ++++++++++")
                
        #Mobile
        if "Mobile" in membro:
            pos = membro.find("Mobile:")+len("Mobile:")
            tel_sujo = membro[pos:]
            mobile = ""
            
            for i in tel_sujo:
                if i in caracteres_tel:
                    mobile += "".join(i)
                else:
                    break
                    
            mobiles.append(mobile.strip())
        else:
            mobiles.append(np.nan)
            print("+++++++++++ MOBILE == NAN ++++++++++")
        
        # Fax
        if "Fax" in membro:
            pos = membro.find("Fax")+len("Fax:")
            tel_sujo = membro[pos:]
            fx = ""
            for i in tel_sujo:
                if i in caracteres_tel:
                    fx += "".join(i)
                else:
                    break
            fax.append(fx)
        else:
            fax.append(np.nan)

        # URL
        if "Url" in membro:
            url = re.split("Url:", membro)[1]
            sites.append(url.strip())
            print("o URL é: ", url)
            print("==========================")
        else:
            sites.append(np.nan)
            print("+++++++++++ SITE == NAN ++++++++++")

        # Adress
        end = ""
        if "Address" in membro:
            local = str(membros[0])[str(membros[0]).find("Address:"):]
            local = local[:local.find("</tr>")]
            local = local.replace("Address:","").replace("</td>","").replace("<td>","")
            print("o ENDEREÇO é: ", local)
            print("==========================")
            end+= local.strip()
        else:
            print("+++++++++++ ENDERECO == NAN ++++++++++")

        # Postal Code
        if "City/Postal:" in membro:
            po = str(membros[0])[str(membros[0]).find("City/Postal:"):]
            po = po[:po.find("</tr>")]
            po = po.replace("City/Postal:","").replace("</td>","").replace("<td>","")
            print("Postal Code é: ", po)
            print("==========================")
            end+= " " + po.strip()
        else:
            print("+++++++++++ Postal Code é == NAN ++++++++++")
        
        if end == "":
            enderecos.append(np.nan)
        else:
            enderecos.append(end.strip())


           
#create/save table
df = pd.DataFrame({"Name":nomes,"Acronym":acronym,"Logo":logos,"President":president,"Telephone":tels,"Mobile":mobiles,"Fax":fax,"Adress":enderecos,"Website":sites,"Email":emails})
df["Federation"] = "International Chess Federation FIDE"
df["Recorded By"] = "tnorio"
#SAVE
df.to_excel("affiliated_organizations.xlsx")
