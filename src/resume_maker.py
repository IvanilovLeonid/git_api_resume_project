from datetime import datetime
from jinja2 import Template

import requests
from dotenv import load_dotenv
import os

load_dotenv()


url = 'https://api.github.com/user'

TEMPL_NAME = "./Templates/index.html"

IND_NAME = "./public/index.html"

def generate_():
    def read_token():
        try:
            return os.getenv('GITHUB_TOKEN')
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            exit(1)

    token = read_token()


    headers = {'Authorization': f'token {token}'}

    try:
        resp = requests.get(url, headers=headers)

        if resp.status_code == 200:
            user_info = resp.json()

            with open(TEMPL_NAME, "r", encoding="utf-8") as template_file:
                templ_text = template_file.read()
                jinja_template = Template(templ_text)
                rendered_resume = jinja_template.render(
                login = user_info['login'],
                id = user_info['id'],
                name = user_info['name'],
                email = user_info['email'],
                company = user_info['company'],
                bio = user_info['bio'],
                pub_repos = user_info['public_repos'],
                url_git = user_info['url'],
                datetime = datetime.now().time()
                )
            with open(IND_NAME, "w", encoding="utf-8") as resume_file:
                resume_file.write(rendered_resume)

            return rendered_resume
        else:
            print(f"Ошибка: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

