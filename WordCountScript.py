import os
import requests
import re
URL_SRC='https://www.gutenberg.org/files/1256/1256-0.txt'
WORKDIR='/tmp/scripts/'
def get_script(url):
  filename = url.split('/')[-1]

  r = requests.get(url, allow_redirects=True)

  text = clean_script(r.text)

  os.makedirs(WORKDIR, exist_ok = True)
  open(WORKDIR+filename, 'w').write(text)

def clean_script(text):
  text = re.sub(r'^.*\*\*\* START OF THIS PROJECT GUTENBERG EBOOK [A-Z ]* \*\*\*', '',text, flags=re.S)
  text = re.sub(r'\*\*\* END OF THIS PROJECT GUTENBERG EBOOK.*$','', text, flags=re.S)
  return text
if __name__ == "__main__":
  get_script(URL_SRC)

