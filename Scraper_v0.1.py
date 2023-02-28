from bs4 import BeautifulSoup as soup 
import io

#f = io.open("output.html", mode="r", encoding="utf-8")

f = open("output.html","r", encoding="utf-8")

index = f.read().encode('utf8').decode('ascii', 'ignore')

new_soup = soup(index, 'html.parser')

this = new_soup.find_all("a")[0]

name = this.find('span').text

print(this)

#print(new_soup)

# import codecs
#f = codecs.open("output.html", "r", "utf-8")
# f.read()

#print(f)





#print(index)


# Uclient = urlopen(url)

# hot_soup = soup(Uclient.read(),'html.parser').prettify().encode("utf-8")

# Uclient.close()

#conditions = hot_soup.find_all('div','q1vdpoLtJkwUT8jN22K2 dsStC1AzZueqISZqfHLZ')

#print(r.text)


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
