import wikipedia
from BeautifulSoup import BeautifulSoup

import pandas as pd
import numpy as np

from time import sleep

array = []
elementsArray = np.array(pd.read_csv('elements.csv')['name'])

for element in elementsArray:
	dummy = {}
	page = wikipedia.page(element)
	html = BeautifulSoup(page.html())
	info = html.findAll('table',{'class':'infobox'})[0]
	tr = info.findAll('tr')      
	for var in tr:
		
		if var.th and var.td:
			
			if var.th.a:
				dummy[str(var.th.a.text.encode('utf-8'))] = str(var.td.text.encode('utf-8'))
				
				if str(var.th.a.text.decode('utf-8'))== 'CAS Number':
					break

	array.append(dummy)
	print element
	sleep(10)				