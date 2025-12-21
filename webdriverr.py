from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle

options=Options()
driver=webdriver.Chrome(options=options)
driver.get("https://github.com/Programmer-s-Picnic/Web-Data-Analyzer/blob/main/ashu.html")
data=driver.page_source
datafile=open("Ashu.txt","wb+")
pickle.dump(data,datafile)
datafile.flush()
datafile.close()
print(data)
driver.quit()
