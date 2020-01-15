#!/bin/bash -i
~/ngrok http -hostname=server.jeremy9959.net 4000 &
echo "$!" > ~/bin/swc_ngrok.pids
cd ~/swc
bundle exec jekyll serve 2>&1 > ~/bin/jekyll.log &
echo "$!" >> ~/bin/swc_ngrok.pids
