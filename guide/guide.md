# Setting up a workshop website

## Prerequisites

These notes will walk through the process of setting up a website for a carpentries
workshop.  To do this successfully, you need:

1. a [github](https://github.com) account.
2. to be comfortable working at the command line to edit text files using `nano`
or another editor such as `vscode`, `vim` or `emacs`, or using a graphical text editor like `sublime`, `textmate`, or `notepad++`
3. to have a basic understanding of `git` including the commands `git status`, `git add`, `git branch`,
`git checkout`, `git commit`, `git push` and `git pull`.
4. to be a member of the [Carpentries at UConn](https://github.com/carpentries-uconn)
organization.  If you have a [github](https://github.com) account, 
contact [Tim Moore](mailto:timothy.e.moore@uconn.edu) and ask to be added to this organization. 

## Overview

The website construction process takes advantage of the ability to publish web pages out of a 
[github](https://github.com) repository.  There are a number of ways to do this, but the
one employed here relies on a special `gh-pages`
branch in the repository which [github](https://github.com) treats as the source code for a website.

In broad outline, you will be:

- creating a new repository inside the [UConn Carpentries repository](https://github.com/carpentries-uconn/) named `YYYY-MM-DD-UConn` that includes a set of template files taken from the software carpentries.

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


### Step 2: Clone the repository to your local machine

It is possible to edit the files we will need to change directly on the [github](https://github.com) website,
but I think it is more convenient to clone the repository and work on your local machine.  

1.  Using the command shell on your computer, navigate to a directory where you wish to locate the repository.
For example (you may have a different preferred location, so this is just for illustration):

```
$ mkdir Carpentries
$ cd Carpentries
```

Now clone the repository:

```
$ git clone https://github.com/uconn-carpentries/YYYY-MM-DD-UConn.git
Cloning into 'YYYY-MM-DD-UConn'...
remote: Enumerating objects: 242, done.
remote: Counting objects: 100% (242/242), done.
remote: Compressing objects: 100% (235/235), done.
remote: Total 242 (delta 23), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (242/242), 2.21 MiB | 10.94 MiB/s, done.
Resolving deltas: 100% (23/23), done.
$
```
This will create a subdirectory called `YYYY-MM-DD-UConn` which contains (copies of) the files for creating the website.

### Step 3: Edit the _config.yml file


1. Change into the `YYYY-MM-DD-UConn` directory and list the files, looking for the file called `_config.yml`:

```
$ cd YYYY-MM-DD-UConn
$ ls
assets/  data/           _extras/  _includes/  aio.md    CODE_OF_CONDUCT.md  CONTRIBUTING.md  index.md    README.md 
bin/     _episodes/      fig/      _layouts/   AUTHORS   CONDUCT.md          Gemfile          LICENSE.md  requirements.txt
code/    _episodes_rmd/  files/    setup/      CITATION  _config.yml         getsql.sh        Makefile
```

2. This is the first file that we need to edit. Open it with a text editor.
It is written in a very simple language called YAML.  Lines with `#`
are comments and contain explanatory text.  Otherwise, the file contains declarations of the form

```yaml
key: value
```

and it is these keys that we wish to edit. In fact, there is probably only one line that we need to change --
the line for the workshop title. Using `nano`, for example, open the file and scroll down to the
line

```
title: "Workshop Title"
```

Then replace "Workshop Title" with the title of your workshop.

**Note:** This step assumes you are teaching a *Software Carpentry* workshop.  If you are teaching a *Data
Carpentry* workshop, then you need to make other changes to this file beyond those described here. In particular,
you will need to:

- set the value for the `carpentry` key to "dc"
- set the "curriculum" to the appropriate value ("dc-ecology", "dc-genomics", "dc-socsci","dc-geospatial", or possibly others)
- set the "flavor" to "r" or "python"

See [this web page](https://carpentries.github.io/workshop-template/customization/index.html) for more details.

If you are teaching a *software carpentry workshop*, confirm that the line with the key `carpentry` is set to `swc`:

```
carpentry: "swc"
```

[Here is a movie of this step](./EditYaml.html)

3.  Commit these changes to the repository and push them to the remote repository.

```
$ git status
On branch gh-pages
Your branch is up to date with 'origin/gh-pages'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   _config.yml

no changes added to commit (use "git add" and/or "git commit -a")
$ git commit -am 'Updated _config.yml file'
git commit -am 'Updated _config.yml file'
[gh-pages f847aea] Updated _config.yml file
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push
Username for 'https://github.com': (your userid)
Password for 'https://jeremy9959@github.com': (your password)
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 334 bytes | 334.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/carpentries-uconn/YYYY-MM-DD-UConn.git
   1d9f535..f847aea  gh-pages -> gh-pages
```

4. To see that it worked, go to the developing workshop page (which should be at `carpentries-uconn.github.io/YYYY-MM-DD-UConn`) and see that the workshop title is changed!

### Step 4: Edit the Webpage (index.md)

1. First, check that your website works by going to `https://carpentries-uconn.github.io/YYYY-MM-DD-UConn/`, where YYYY-MM-DD correspond to your workshop. It's easy to break the webpage, and difficult to debug, so make incremental changes, checking to make sure your website still works each time.

2. At the top right of your repository page just below the tabs. click on the Edit button. Add the workshop website link there. This makes it convenient to get to the website from your repository. 

3. Open index.md in the root folder of the repository in a text editor. At the top, in the block of yaml encapsulated with `---` (see step 3 above), you'll be filling in the workshop-specific information. Follow the guide [here](https://carpentries.github.io/workshop-template/customization/index.html#home-page-indexmd-data-in-the-yaml-header) carefully. **Be especially careful to close quotes, and follow formatting guidelines, or the website will break**. Of particular note:
   * `venue` should always be `"University of Connecticut"`
   * `address` should be the address of the building on campus for physical workshops. See [online workshop configuration](https://carpentries.github.io/workshop-template/customization/index.html#for-online-workshops) for online options.
   * `country` will always be `"us"`
   * `language` will generally be `"en"`
   * `collaborative_notes` Add the link to the etherpad, without quotes. Generally, this should use the same name as the workshop website, but at pad.carpentries.org. For example: `collaborative_notes: https://pad.carpentries.org/2020-05-01-UConn-online`. The etherpad will be created by The Carpentries when you visit the link. 
   * `eventbrite` **TODO, figure out how we're doing registration as an organization**
      
### Step 5: Customizing Workshop Website Sections

3. Customize the section templates of the website to your workshop, in the `_includes` folder, especially schedule.html, syllabus.html, and setup.html (see [customizing templates](https://carpentries.github.io/workshop-template/customization/index.html#home-page-schedule-and-syllabus). **Be very careful to make sure that all html tags are closed** (e.g. `<div>` and `</div>`). Otherwise, you'll break the website.
   * For schedule, set the start and end times for each day and tailor breaks to your curriculum. It's wise to start half an hour early the first day to deal with setup issues and late arrivals, so that you can start teaching on time. It's also nice to put in the name of the person teaching each section. Make sure to leave wrap-up time at the end for post-workshop survey and promoting the carpentries.
   * For syllabus, comment out the portions you won't be teaching, using html comments at the beginning and end of the blocks (`<!--` and `-->`). Be careful to not include extra lines when doing this that results in `<div>` tags not being closed.
   * For setup, comment out the portions of software setup that aren't relevant to your teaching. Note that the git setup section may be required to install nano for Windows users.
   * Advanced users can make their own template sections (e.g., for [post-workshop resources](https://github.com/carpentries-uconn/2020-05-01-UConn-online/blob/gh-pages/_includes/swc/resources.html)). These get added to index.md using a line like `include swc/resources.html`. 
   
### Step 6: Set Up the Etherpad

It's helpful to spend a bit of time doing some thoughtful setup of the etherpad before the workshop. This is especially useful in getting things going quickly and smoothly at the beginning. A good model for a workshop etherpad from a past workshop is [here](https://pad.carpentries.org/2019-01-10-UCONN).

1. Add a section on what learners should do when they first get to the workshop. Suggestions
   * Get a nametag and stickies, sign in
   * Go to the workshop website, and open this etherpad (collaborative notes link)
   * Name yourself in the etherpad in the top right corner where it says Enter your name
   * Introduce yourself in the introductions section
   * Install the software and packages
   * Take the pre-workshop survey
   * Open up tabs for things like Socrative

2. Add a section for introductions for instructors, helpers, and learners

3. Add links for Socrative (along with the room name), downloading data, and perhaps a synced version of the instructor's script to follow along with. 

### Troubleshooting

* If there is a problem building the files used to generate the website, then the previous version of the website will stay live. Sometimes it will take a few minutes for your changes to be built, so be patient. You can check the status of your website's build by going to the commit history. Green checkmarks beside the time since commit mean that the build was successful. A red X means that the build failed. A yellow circle denotes build in progress. 

* If a build fails, first compare the changes for that commit with the previous version and look for obvious errors that you can fix. Failing that, try rolling back the commit. 

* Finally, the software carpentry repository includes a makefile tool to check files for some syntax errors and tell you where the problem is. Sometimes, this is helpful. You can run it using `make workshop-check` (requires python to be installed). There are some additional undocumented testing tools in the makefile as well. 
