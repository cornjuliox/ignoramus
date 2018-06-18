#!/usr/bin/env python
# Copyright (C) 2018, Enrico Tuvera Jr
import click
import ignoramus.templates as templates

@click.group()
def supermain():
    pass

@supermain.command()
@click.option('--output', default='.gitignore', help='specify output file name, default is .gitignore')
@click.argument('language')
def generate(language, output):
    templates.generate_gitignore(language.lower(), output)

@supermain.command()
def available():
    filenames = templates.generate_files()
    available = templates.generate_lang_names(filenames)
    # TODO: find a way to pretty print this shit
    if available:
        for x in sorted(available):
            print(x)
    else:
        print('len(available) = {}'.format(len(available)))
        print('No templates found - installation is borked.')

if __name__ == '__main__':
    supermain()
