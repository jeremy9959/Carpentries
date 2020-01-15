#!/bin/bash
ssh -t -p 23733 jet08013@1.tcp.ngrok.io "tmux -c ~/bin/start_swc_server.sh"
(fswatch -0 ~/code & echo $! >&3) 3> ~/bin/fswatch.pid | xargs -0 -I{} ~/code/bin/log2md_2.sh {} &
echo "done"
