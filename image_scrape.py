#!/uar/bin/python

import re, subprocess
# import os
# import sys
import utils

# Check if pokedex file is exists
utils.check_if_file_exists('pokedex')
# if not os.path.isfile('.pokedex'):
# 	sys.exit('pokedex file is not exists. please run stats_scrape first to create it')

# create directory
utils.check_if_directory_exists('image_scrape_result')
# path = 'image_scrape_result'
# access_rights = 0o755
# if not os.path.exists(path):
#   os.mkdir(path, access_rights)

# get list of pokemon from pokedex file
a_file = open('pokedex')
data = a_file.read()
a_file.close()
pokemons = re.findall(r'(.*?)\s(.*?)\n',data)

# container for failed images
not_retrieved = []

# loop through list
for pokemon in pokemons:
	try:
		subprocess.check_output(['wget http://img.pokemondb.net/artwork/large/'+pokemon[1]+'.jpg -q --show-progress'],shell=True)
		subprocess.check_output(['mv '+pokemon[1]+'.jpg image_scrape_result/'+pokemon[0]+'_'+pokemon[1]+'.jpg'],shell=True)
	except Exception:
		not_retrieved.append(pokemon)

# print message if there is one or more file that is failed to downloaded
if len(not_retrieved) > 0:
	print('Some image is not downloaded. Please manually edit the correct filename in file (not_retrieved)')

# save the list of failed image
i = 1
with open("not_retrieved", "w") as txt_file:
  for line in not_retrieved:
    txt_file.write(line[0] + ' ' + line[1].encode('utf-8').strip().lower() + "\n")
    i += 1
