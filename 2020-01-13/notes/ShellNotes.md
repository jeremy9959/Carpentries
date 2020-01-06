Make sure to download the data-shell.zip
file and put it on the Desktop

https://swcarpentry.github.io/shell-novice/data/data-shell.zip (it's on the etherpad now)


## Navigation 

- Root directory
- Directory hierarchy
- Home directory
- Compare windows and UNIX

## commands and options

- Three key navigation commands

```bash
cd # change directory
ls # list directory
pwd # list directory
```


```bash
ls
ls -F
ls -l
ls -a
```

- Getting help

```bash
ls --help # if that works
man ls # paging through the manual pages
```

- Changing directories

```bash
pwd
ls
cd
cd ..
ls .
cd ~
cd ~/Desktop
```

## Creating files and directories

- the *nano* editor to create a file

```bash
mkdir directory # create a directory
```

- file names and extensions 
    extensions usually indicate file type
    .txt, .pdf, .tex, .csv
    names explain the content
    
## Moving (renaming) and copying

```bash
cp file1 file2 # overwrites file2, leaves file1
mv file1 file2 # overwrites file2, removes file 1
cp file1 directory # copies file1 into directory, leaves file1 alone
mv file1 directory # moves file1 into directory, file1 is gone from original location
mv directory1 directory2 # renames directory, contents unchanged
```

## Deleting files

```bash
rm file # deletes file. IRREVERSIBLE
rm -i file # asks for confirmation
rm directory # error: won't remove directory
rm -r directory # removes contents. DANGER DANGER DANGER
```

#### deleting a directory

```bash
rmdir directory # removes directory - must be empty
```

## Wildcards

```bash
ls *.txt # list all .txt files
ls a* # list files beginning with a
ls *data* # list all files with data in the name
```

**EXERCISES: SOCRATIVE 1-7 work here.**

## Pipes and filters

- Standard input and output
- pipes

```bash
cat file
less file
wc file
wc -l file
wc -c file
wc -l *.pdb > lengths.txt # redirect output
sort file
sort -n file
```

- in the molecules directory

```bash
wc -l *.pdb > lengths.txt
sort -n lengths.txt
sort -n lengths.txt > sorted-lengths.txt
head -n 1 sorted-lengths.txt
```

- Beware of redirection over the same file

**SOCRATIVE 8-10 work here**

## Pipes
 
| chains standard in to standard out

```bash
wc -l *.pdb | sort -n
wc -l *.pdb | sort -n | head -n 1
```

**SOCRATIVE 11 works here**

More on pipes
go to the north-pacific-gyre/2012-07-03 directory

```bash
wc -l *.txt
wc -l *.txt | sort -n | head -n 5
```

Notice that one file is 60 lines shorter.

```bash
wc -l *.txt | sort -n | tail -n 5
```

shows that none are longer than 300 lines

```bash
ls *Z.txt
```

finds files with Z in their name.

## Loops

```bash
for file in basilisk.dat minotar.dat
do
head -n 2 \\file | tail -n 1
done
```


Pay attention to the  prompt!

## Variables

- the \\ means "value of"

```bash
x='hello'
echo \\x
```

```bash
for file in *.txt
do
cp \\file new-\\file
done
```

- using echo to test your loop

```bash
for file in *.txt
do
echo "cp \\file new-\\file"
done
```

## spaces in file names

SOCRATIVE 12-14

# Shell Scripts

Create a file with a sequence of commands
in nano with extension .sh

In molecules directory create a file
with the command
```bash
head -n 15 "\\1" | tail -n 5
```

This will show lines 10-15 of your file.

To run it use
```bash
bash middle.sh octane.pdb
```
A command to sort files by length; call 
it sorted.sh

```bash
wc -l "\\@" | sort -n
```

Then 
```bash
bash sorted.sh *.pdb ../creatures/*.dat
```

sorts all the files by length.

**SOCRATIVE 15**

## grep



