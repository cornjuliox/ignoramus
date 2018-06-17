# About
I got tired of having to manually search for and download .gitignore files so I wrote this script.

Normally, I'd go here -> [here](https://github.com/github/gitignore) , find the relevant gitignore, click the filename, click on 'raw', copy-paste the file from my browser into a text editor, and save.

That's one too many steps for me. I'm hoping to get it down to a single command.

# Usage
`python ignoramus.py <subcommand> <options> <arguments>` following installation.

## Subcommands:
### `available`
`python ignoramus.py available` - lists all available language templates
`python ignoramus.py --help OR python ignoramus.py <subcommand> --help` - shows help message, either for the program or the subcommand.

### `generate`
`python ignoramus.py generate --output=foobar <language>`- Generates a .gitignore file based on the programming language specified.

| Option Name | Description | Default | 
|---|---|---|
| `--output` | lets you specify the name of the output file. Default is set to .gitignore | `output=.gitignore`

| Argument Name | Description | 
|---|---|
| <language> | specifies the name of the template to use. Valid names are any one of the names output by the `available subcommand |
