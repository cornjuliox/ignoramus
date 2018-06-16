# About
I got tired of having to manually search for and download .gitignore files so I wrote this script.

I normally pull them from [here](https://github.com/github/gitignore) but that's several steps too many
for me. 

# Usage
You need to install 'requests' for this to work. Then make script executable via `chmod a+x <script>`.

Then run the script like so `./get_gitignore <LANG_1> <LANG_2> ... <LANG_n>`

# How it Works
It sends a couple of API requests to https://gitignore.io, which does the actual generating of the gitignore.
You can specify multiple programming languages, and assuming that there are templates available on gitignore.io, they'll all be combined into a single, super-gitignore file that will be placed in the current directory.

# TODO
- maybe turn this into a proper python package that can be installed via pip and run straightaway without having to deal with any of this installation bullshit.
