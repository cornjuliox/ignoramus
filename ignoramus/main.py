import click
import templates

@click.group()
def ignoramus():
    pass

@ignoramus.command()
@click.option('--output', default='.gitignore', help='specify output file name, default is .gitignore')
@click.argument('language', default='Python')
def generate(language, output):
    print('generating {} for {}'.format(output, language))

@ignoramus.command()
def available():
    filenames = templates.generate_files()
    available = templates.generate_lang_names(filenames)
    print(available)


if __name__ == '__main__':
    ignoramus()
