# -*-coding:Utf-8 -*

import re
import discogs_client

#récupère les chiffres du code-barre
barcode = input('')

#crée le fichier csv et renseigne les en-têtes
output_file = open('/home/jericho/Bureau/nbeniesDB_cd.csv','a')
print('UPC;titre;genre;syle;année;labels;crédits;notes;pistes',file=output_file)

#interroge discogs
d = discogs_client.Client('nbeniesDB/0.1', user_token='wajqAKExyzgibnQMPYciXWvynuBcumRgIZbgllWe')
results = d.search(barcode)
release_query = str(results.page(1))

try:
	release_code = re.findall(r'Release (\d*) \'',release_query)[0]
	release = d.release(release_code)
	print('UPC:'+barcode)
	print('title:'+str(release.title))
	print('genres:'+str(release.genres))
	print('styles:'+str(release.styles))
	print('year:'+str(release.year))
	print('labels:'+str(release.labels))
	print('credits:'+str(release.credits))
	print('tracklist:'+str(release.tracklist))

	#met à jour le fichier csv
	print(barcode+';'+str(release.title)+';'+str(release.genres)+';'+str(release.styles)+';'+str(release.year)+';'+str(release.labels)+';'+str(release.credits)+';'+str(release.tracklist),file=output_file)

except IndexError:
	print('no match for UPC:'+barcode)
	print(barcode+';none;none;none;none;none;none;none;none',file=output_file)
