from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from sys import argv
from selenium.webdriver.chrome.options import Options
import os
dict=[]
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1280,800')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
driver=webdriver.Chrome(os.getcwd()+r"\chromedriver.exe",options=chrome_options)
Key = {'astro-ph': "Astrophysics", 'hep-th': "High Energy Physics Theoretical", 'math-ph': "Mathematical Physics", 'quant-ph': "Quantum Physics",
       'gr-qc': "General Relativity and Quantum Cosmology", 'hep-ex': "High Energy Physics Experimental", 'hep-ph': "High Energy Physics Phenomenology",
       'physics': "Physics", 'nucl-th':'Nuclear Theory','hep-lat':'High energy Physics Lattice','nucl-ex':'Nuclear Experiment',
       'math-ph':'Mathematical Physics','cond-mat':'Condensed Matter','math':"Mathematics",'stat':"Statistics",'physics.acc-ph':"Accelerator Physics",
       'cs':'Computer Science','nlin':"Non Linear Sciences",'q-bio':"Quantitative Biology",'eess':"Electrical Engineering and Systems Science",
       'physics.ins-det': 'physics.in-det'}
for i in range(0,1): 
    driver.get('https://inspirehep.net/authors?sort=bestmatch&size='+str(argv[2])+'&page=1&q='+str(argv[1]))
    author_links=[]
    authors=[]
    WebDriverWait(driver,30).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.ant-card-body')))
    cards=driver.find_elements_by_class_name('ant-card-body')
    
    for card in cards:
        try:
            card.find_elements_by_class_name('ant-tag __UnclickableTag__')
            authors.append(card.find_element_by_class_name('result-item-title').text)
            author_links.append(card.find_element_by_class_name('result-item-title').get_attribute('href'))
        except:
            continue
    j=0
    for author,link in zip(authors,author_links):
        j=j+1
        print("Professor:"+str(j))
        areas=[]
        driver.get(link)
        sleep(2)
        try:
            areas_dom=driver.find_elements_by_class_name('__InlineList__')[1]
            elements=areas_dom.find_elements_by_tag_name('li')
        except:
            areas=['']
            elements=[]
        for element in elements:
            if element.text in Key:
                areas.append(Key[element.text])
        web=''    
        try:
            university=driver.find_element_by_tag_name('h2').find_element_by_tag_name('li').text
        except:
            university=''
        try:
            mail=driver.find_elements_by_class_name('__ListItemAction__')[0].find_element_by_tag_name('a').get_attribute('href')
            if mail[0:4]=='http':
                web=mail
                mail=''
            else:
                mail=mail[7:]
        except:
            mail=' '
        if web=='':
            try:
                web=driver.find_elements_by_class_name('__ListItemAction__')[1].find_element_by_tag_name('a').get_attribute('href')
            except:
                web=' '
        seperator = ', '
        areastr=seperator.join(areas)
        df1={
        'Name': author,
        'Fields of interest': areastr,
        'E-mail': mail,
        'Website': web,
        'University':university
        }
        dict.append(df1)
    
df=pd.DataFrame(dict)
df.to_csv('profname.csv', index = False)
driver.quit()
