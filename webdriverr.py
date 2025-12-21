from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle

options=Options()
driver=webdriver.Chrome(options=options)
<<<<<<< HEAD
driver.get("https://github.com/Programmer-s-Picnic/Web-Data-Analyzer/blob/main/maggie.txt")
data=driver.page_source
datafile=open("kriti.txt","wb+")
=======
driver.get("https://github.com/Programmer-s-Picnic/Web-Data-Analyzer/blob/main/ashu.html")
data=driver.page_source
datafile=open("Ashu.txt","wb+")
>>>>>>> 8a497689d23a189f989113f77a09a8b641132e12
pickle.dump(data,datafile)
datafile.flush()
datafile.close()
print(data)
driver.quit()
