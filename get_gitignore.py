#!/usr/bin/env python
import requests
import sys

SITE = 'https://gitignore.io'

if __name__ == '__main__':
    try:
        language = sys.argv[1:]
    except IndexError:
        print('usage: python get_gitignore.py <PROGRAMMING_LANGUAGE>')
        sys.exit()

    url = SITE + '/dropdown/templates.json'
    print('getting templates from {}'.format(url))
    templates = requests.get(url).json()
    print('languages requested: {}'.format(language))
    print('attempting to match')
    matches = [match for lang in language for match in templates if match['id'] == lang.lower()]
    print('matches: {}'.format(matches))

    if matches:
        api_url = SITE + '/api/{}'.format(','.join([x['id'] for x in matches]))
        print('sending request to: {}'.format(api_url))
        gitignore = requests.get(api_url).text
        with open('new_gitignore', 'w') as F:
            F.write(gitignore)
            print('created new_gitignore, please rename file to gitignore')
    else:
        print('no matches found, try another programming language or combination thereof.')
        sys.exit()
    

