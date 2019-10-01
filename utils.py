from collections import OrderedDict
import requests
import lxml.html as lh
import re

# Add bracket if pokemon name has sub-name
def str_bracket(word):
    list = [x for x in word]
    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' ' + list[char_ind]

    fin_list = ''.join(list).split(' ')
    fin_list = filter(None, fin_list)

    length = len(fin_list)

    if length > 1:
        fin_list.insert(1, '(')
        fin_list.append(')')
    
    return ' '.join(fin_list)

# Break name at upper case
def str_break(word):
    list = [x for x in word]
    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' ' + list[char_ind]
    fin_list = ''.join(list).split(' ')
    
    return fin_list

# Generate filename
def generate_img_file_name(word):
    word = re.sub(r'\W+', '', word)
    list = [x for x in word]

    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' ' + list[char_ind]

    fin_list = ''.join(list).split(' ')

    # remove empty string in array
    fin_list = filter(None, fin_list)

    # remove duplicates
    fin_list = remove_duplicate(fin_list)
    return '-'.join(fin_list).lower()

# Remove duplicates
def remove_duplicate(x):
    return list(OrderedDict.fromkeys(x))

# Get table data from webpage
def getData(url, xpath):
  url = url
  page = requests.get(url)
  doc = lh.fromstring(page.content)
  tr_elements = doc.xpath(xpath)
  return tr_elements

# Clean string
def clean_string(word):
  return word.lower().replace(' ', '').replace('.', '-')

# iterate through all pokemon list and save img_filename
def save_df_to_text(data_frame, filename, row_data):
  with open(filename, "w") as txt_file:
    for index, row in data_frame.iterrows():
      txt_file.write(str(index + 1).zfill(3) + ' ' + row[row_data].encode('utf-8').strip().lower() + "\n")
