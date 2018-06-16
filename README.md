# About This Project
I think a lot of us have considered starting a blog at some point, but stuff like Wordpress doesn't really fit the workflow of the average programmer. I know it didn't really fit -my- workflow.

Static site generators like Jekyll are a closer fit, but have their limits. 

What I liked most about Jeykll (more specifically, Github Pages) was how nicely it integrated with a git-based workflow - commits to the master branch triggered an update of the site so I didn't really have to leave the terminal, which is where I spent most of my time anyways.

What I didn't like about Jekyll was how there's no easy way to include a commenting system. (A blog without comments isn't really a blog) [https://blog.codinghorror.com/a-blog-without-comments-is-not-a-blog/]. I realize that this isn't really Jekyll's fault, but rather a limitation of static sites in general.

So I guess the whole point of this project is to come up with a programmer-friendly blogging system, i.e one that would allow submissions and updates through git and has built-in support for comments.

A few notes:
- This definitely won't be a static site. The requirement for comment support, and all that it entails, makes it impossible for this to be a static site. Whether the site ends up being server-side rendered, or an SPA with very minimal theming (see below) hasn't been decided yet.
- Definitely allow github based submissions/updates.
	- The idea here is to copy the way Jekyll does it; set the app up to watch a branch on a repo, and whenever it's committed to, we create/update/delete posts in the database.
	- Jekyll has a `_drafts` folder that I'd like to copy.
		- One thing I disliked about the whole setup was how you had to manually put a date on all your posts. Automatically putting a date on posts is pretty much a basic-bitch feature of any CMS, and its absence here is rather noticable.
		- This goes for both `created at` and `updated at` stamps.
- Support for comments! Threaded is better, but I suppose I could start with 'vanilla' comments.
	- I haven't figured out how to handle moderation, but I suppose this is a problem I can handle another day.
	- I also haven't figured out how to handle spam.
	- I haven't figured out how to handle user auth and shit either.
	- I haven't even figured out how to handle storing threaded comments in the database either.
	- Jesus there's a lot to do.

