from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as soup 

urls = ['https://www.ycombinator.com/companies?batch=W23']

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

Uclient = urlopen(req)

hot_soup = soup(Uclient.read(),'html.parser')

Uclient.close()

print(hot_soup)

# def pull_surf_condidtions():
# 	waves = []
# 	for url in urls: 
# 		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# 		Uclient = urlopen(req)
# 		soups = soup(Uclient.read(),'html.parser')
# 		Uclient.close()

# 		beach_name = soups.find_all('h1','sl-forecast-header__main__title')[0].text.replace('Surf Report & Forecast','')
# 		wave_size = soups.find_all("div", "quiver-spot-forecast-summary__stat-container quiver-spot-forecast-summary__stat-container--surf-height")[0].find_all('span','quiver-surf-height')[0].text
# 		conditions = soups.find_all('div','quiver-spot-report')[0].contents[0].text
# 		waves.append(beach_name + ': ' + wave_size + ' ' + conditions +'\n' )
# 	str1 = ' '
# 	wave_report = (str1.join(waves))
# 	return wave_report


#waves = send_email(pull_surf_condidtions())
