# Setting up a workshop website

## Prerequisites

These notes will walk through the process of setting up a website for a carpentries
workshop.  To do this successfully, you need:

1. a [github](https://github.com) account.
2. to be comfortable working at the command line to edit text files using `nano`
or another editor such as `vscode`, `vim` or `emacs`.
3. to have a basic understanding of `git` including the commands `git status`, `git add`, `git branch`,
`git checkout`, `git commit`, `git push` and `git pull`.
4. to be a member of the [Carpentries at UConn](https://github.com/carpentries-uconn)
organization.  If you have a [github](https://github.com) account, 
contact [Tim Moore](mailto:timothy.e.moore@uconn.edu) and ask to be added to this organization. 

## Overview


The website construction process takes advantage of the ability to publish web pages out of a 
[github](https://github.com) repository.  There are a number of ways to do this, but the
one employed here relies on a special `gh-pages`
branch in the repository which [github](https://github.com)treats as the source code for a website.

In broad outline, you will be:

- creating a new repository inside the [UConn Carpentries repository(https://github.com/carpentries-uconn/) named `YYYY-MM-DD-UConn` that includes a set of template files taken from the software carpentries.

- editing some of the template files so that the website will show the correct location, date, and
curriculum.

- updating the repository with these edited files to publish it.  

This may be an iterative process as you work out the bugs.

Before diving in to the technicalities, let's 
look at an example.  We taught a Carpentries workshop on May 1, 2020.  The
website for that workshop is located in the repository [https://github.com/carpentries-uconn/2020-05-01-UConn-online](https://github.com/carpentries-uconn/2020-05-01-UConn-online).  Follow that link and
make sure that the `Branch:` selector is set to gh-pages.  You will see the all of the files
that constitute the source code for the workshop's page.

[Github](https://github.com) publishes this page at the link [https://carpentries-uconn.github.io/2020-05-01-Uconn-online](https://carpentries-uconn.github.io/2020-05-01-Uconn-online).  

So to recap, when we create a new workshop page, we will create a repository 
`https://github.com/carpentries-uconn/YYYY-MM-DD-UConn` with a branch called `gh-pages`.  The
information in that branch will get published at `https://github.com/carpentries-uconn.github.io/YYYY-MM-DD-Uconn`.

Many of the complications in this process arise from the fact that instead of being a straightforward
collection of `html` or `markdown` files, the site is written in a templating language called `jekyll` which is then processed into its final form.  This makes the site look nice, but complicates the setup process.
We will *not* be explaining `jekyll` in these notes, except insofar as is needed to do the bare minimum
of configuration of the final website. 

To learn more about the infrastructure, you can read about [GitHub Pages](https://pages.github.com/)
and [jekyll](https://jekyllrb.com/docs/github-pages/).

## SWC Instructions

The SWC documentation for this process is located in three places:

- [The Template Repository](https://github.com/carpentries/workshop-template)
- The webpage [Customizing Your Website](https://carpentries.github.io/workshop-template/customization/index.html)
- [Design Notes](https://carpentries.github.io/workshop-template/design/index.html)

Essentially we will be working through the process outlined in the first two of these files.

## The process

### Step 1: Create the Repository

1.  Log in to [github](https://github.com).
2.  Got to the [Carpentries Workshop Template](https://github.com/carpentries/workshop-template).
3.  Click on the `Use this template` button, make sure you create the repository in the 
[Carpentries-uconn](https://github.com/carpentries-uconn) organization, and name it 
YYYY-MM-DD-UConn for the year, month, and day it will be offered.

[Click here for a movie of this process](./MakeTemplate.html)





