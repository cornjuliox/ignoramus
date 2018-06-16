# About

I got tired of having to manually search for and download .gitignore files so I wrote this script.

Normally, I'd go here -> [here](https://github.com/github/gitignore) , find the relevant gitignore, click the filename, click on 'raw', copy-paste the file from my browser into a text editor, and save.

That's one too many steps for me. I'm hoping to get it down to a single command.

I considered 'pyignore', 'ignoregen', and 'genignore' as names for this script but they're all taken. So I picked 'ignoramus' for its uniqueness within the Python package space, not necessarily for its relevance.

# Usage
You need to install 'requests' for this to work. Then make script executable via `chmod a+x <script>`.

Then run the script like so `./get_gitignore <LANG_1> <LANG_2> ... <LANG_n>`

# How it Works
It sends a couple of API requests to https://gitignore.io, which does the actual generating of the gitignore.
You can specify multiple programming languages, and assuming that there are templates available on gitignore.io, they'll all be combined into a single, super-gitignore file that will be placed in the current directory.

# TODO
- grab click or something and turn it into a proper command line app.
- maybe turn this into a proper python package that can be installed via pip and run straightaway without having to deal with any of this installation bullshit.
- configurable output filename? maybe you want to name it something other than gitignore.
