#!/usr/bin/env python
# Copyright (C) 2018, Enrico Tuvera Jr
# 38480876

import click
import ignoramus.templates as templates
import more_itertools as mit

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
    table = templates.generate_table()

    if available:
        formatted = mit.chunked(sorted(table.keys()), 5)
        for x in formatted:
            print(', '.join(x))
    else:
        click.echo('len(available) = {}'.format(len(available)))
        click.echo('No templates found - installation is borked.')

@supermain.command()
@click.argument('languages', nargs=-1)
def combine(languages)


if __name__ == '__main__':
    supermain()
