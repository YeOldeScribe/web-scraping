import requests
import csv
from BeautifulSoup import BeautifulSoup

## Part One ##

url = "http://www.showmeboone.com/sheriff/jailresidents/jailresidents.asp"

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

results_table = soup.find('table', attrs={'class': 'resultsTable'})

## Part Two ##

output = []

for row in results_table.findAll('tr'):
	# print '---ROW STARTS HERE---'

	output_row = []

	for cell in row.findAll('td'):
		clean_data = cell.text.replace('&nbsp;', '')
		output_row.append(clean_data)

	output.append(output_row)

csv_file = open('inmates.csv', 'w')
writer = csv.writer(csv_file)
writer.writerows(output)