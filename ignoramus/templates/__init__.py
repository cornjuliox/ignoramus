import os
import os.path

def generate_files():
    # NOTE: this is probably going to come back and bite me in the ass
    # I don't remember if this is the correct way to do platform-independent paths
    return [x for x in os.listdir(os.path.dirname(__file__)) if '.gitignore' in x]

def generate_lang_names(files): 
    # NOTE: keep this separate because I'd like to have a command
    # that lists all the available langauge templates
    return [x.split('.')[0].lower() for x in files]

def generate_table():
    # NOTE: the expected result of this function is a dictionary that maps an all
    # lowercase language name to its respective file in the templates directory.
    # such that {'actionscript': 'Actionscript.gitignore', etc...}

    # NOTE: this _may_ come back to bite me if the files somehow get out-of-order
    return dict(zip(generate_lang_names(generate_files()), generate_files()))


if __name__ == '__main__':
    generate_table()
