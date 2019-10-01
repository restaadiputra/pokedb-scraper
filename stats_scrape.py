import pandas as pd
import utils

tr_elements = utils.getData('http://pokemondb.net/pokedex/all', '//tr')
col = []

# For each row, store each first element (header) and an empty list
i = 0
for t in tr_elements[0]:
  name = t.text_content()
  if name == '#':
    name = 'no'

  col.append((utils.clean_string(name), []))
  i += 1

# Since out first row is the header, data is stored on the second row onwards
for j in range(1, len(tr_elements)):
  T = tr_elements[j]

  if len(T) != 10:
    break

  i = 0
  for t in T.iterchildren():
    data = t.text_content()

    if i > 0:
      try:
        data = int(data)
      except:
        pass
    
    col[i][1].append(data)
    i += 1

# Construct Data Frame using Pandas.
Dict = {title: column for (title, column) in col}
df = pd.DataFrame(Dict)

# Apply clean up 
df['name'] = df['name'].apply(utils.str_bracket)
df['type'] = df['type'].apply(utils.str_break)
df['img_filename'] = df['name']
df['img_filename'] = df['img_filename'].apply(utils.generate_img_file_name)

# Save to json
df.to_json('PokemonData.json', orient='records')

# Save image_filename list
utils.save_df_to_text(df, 'pokedex', 'img_filename')