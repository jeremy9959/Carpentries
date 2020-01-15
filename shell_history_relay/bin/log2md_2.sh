#!/bin/bash
cp /Users/swc/code/bin/top.md /tmp/latest.md
awk 'BEGIN {print "\n```bash";} {print $0;} END {print "```\n";}' $1 >> /tmp/latest.md 
rsync -e 'ssh -p 23733' /tmp/latest.md jet08013@1.tcp.ngrok.io:swc/index.md
echo $1 >> /tmp/fswatch.log
