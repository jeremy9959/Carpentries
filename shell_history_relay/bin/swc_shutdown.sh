#!/bin/bash -i
echo "stopping remote server"
ssh -p 23733 jet08013@1.tcp.ngrok.io "tmux -c bin/stop_swc_server.sh"
echo "killing fswatch process" $(cat /Users/swc/bin/fswatch.pid)
cat /Users/swc/bin/fswatch.pid | xargs -I{} kill -9 {}
rm /Users/swc/bin/fswatch.pid
