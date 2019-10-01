
def msg_img_not_retrieved():
  print('Some image is not downloaded. Please manually edit the correct filename in file (not_retrieved)')

def invalid_command():
  print('invalid command')
  print('use: ')
  print ('[PYTHON_FILE] i     [SOURCE_FILE] [DIRECTORY_IMAGE]')
  print ('[PYTHON_FILE] image [SOURCE_FILE] [DIRECTORY_IMAGE]')
  print ('[PYTHON_FILE] s     [SOURCE_FILE] [DIRECTORY_IMAGE]')
  print ('[PYTHON_FILE] stats [SAVE_FILE] [IMAGE_LIST_FILE]')