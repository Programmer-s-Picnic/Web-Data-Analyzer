import pickle
from bs4 import BeautifulSoup

<<<<<<< HEAD
datafile = open("kriti.txt", "rb+")
data = pickle.load(datafile)
datafile.close()
soup = BeautifulSoup(data, "html.parser")
divs = soup.find_all("textarea")
=======
datafile = open("Ashu.txt", "rb+")
data = pickle.load(datafile)
datafile.close()
soup = BeautifulSoup(data, "html.parser")
divs = soup.find_all("tr")
>>>>>>> 8a497689d23a189f989113f77a09a8b641132e12
for d in divs:
    print(d.text)