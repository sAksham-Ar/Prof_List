from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from sys import argv
from selenium.webdriver.chrome.options import Options
dict=[]
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1280,800')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
driver=webdriver.Chrome(r"C:\Users\aryas\Documents\chromedriver.exe",options=chrome_options)
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
            if element.text=='astro-ph':
                areas.append("Astrophysics")
            elif element.text=='hep-th':
                areas.append("High Energy Physics Theoretical")
            elif element.text=='math-ph':
                areas.append("Mathematical Physics")
            elif element.text=='quant-ph':
                areas.append("Quantum Physics")
            elif element.text=='gr-qc':
                areas.append("General Relativity and Quantum Cosmology")
            elif element.text=='hep-ex':
                areas.append("High Energy Physics Experimental")
            elif element.text=='hep-ph':
                areas.append("High Energy Physics Phenomenology")
            elif element.text=='physics':
                areas.append(element.text)
            elif element.text=='nucl-th':
                areas.append('Nuclear Theory')
            elif element.text=='hep-lat':
                areas.append('High energy Physics Lattice')
            elif element.text=='nucl-ex':
                areas.append('Nuclear Experiment')
            elif element.text=='math-ph':
                areas.append('Mathematical Physics')
            elif element.text=='cond-mat':
                areas.append('Condensed Matter')
            elif element.text=='math':
                areas.append("Mathematics")
            elif element.text=='stat':
                areas.append("Statistics")
            elif element.text=='physics.acc-ph':
                areas.append("Accelerator Physics")
            elif element.text=='cs':
                areas.append('Computer Science')
            elif element.text=='nlin':
                areas.append("Non Linear Sciences")
            elif element.text=='q-bio':
                areas.append("Quantitative Biology")
            elif element.text=='eess':
                areas.append("Electrical Engineering and Systems Science")
            elif element.text=='physics.acc-ph':
                areas.append(element.text)
            

            
        try:
            university=driver.find_element_by_tag_name('h2').find_element_by_tag_name('li').text
        except:
            university=''
        try:
            mail=driver.find_elements_by_class_name('__ListItemAction__')[0].find_element_by_tag_name('a').get_attribute('href')[7:]
        except:
            mail=' '
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