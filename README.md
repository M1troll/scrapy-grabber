### scrapy-grabber
My first scrapy-grabber

### Install

1. Create separate python virtual environment:

  ```bash
  pyenv install 3.11 --skip-existing
  pyenv virtualenv `pyenv latest 3.11` scrapy-grabber
  pyenv local scrapy-grabber
  pyenv shell scrapy-grabber
  ```

2. Set up packages:

  ```bash
  python3.11 -m pip install --upgrade pip
  pip install -r requirements.in
  ```

# We use [invoke](https://pypi.org/project/invoke/)

It provide next shortcuts: 

 - inv parse --spider=authors
 - inv parse --spider=quotes
 
