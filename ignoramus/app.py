#!/usr/bin/env python
# Copyright (C) 2018, Enrico Tuvera Jr
import click
import templates

@click.group()
def supermain():
    pass

@supermain.command()
@click.option('--output', default='.gitignore', help='specify output file name, default is .gitignore')
@click.argument('language', default='Python')
def generate(language, output):
    templates.generate_gitignore(language.lower(), output)

@supermain.command()
def available():
    filenames = templates.generate_files()
    available = templates.generate_lang_names(filenames)
    # TODO: find a way to pretty print this shit
    for x in sorted(available):
        print(x)

if __name__ == '__main__':
    supermain()
