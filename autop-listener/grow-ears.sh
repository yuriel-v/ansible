tmux new -d -s autop
tmux new -d -s autopshell
tmux send-keys -t autop "source $HOME/autop-listener/bin/activate" C-m
tmux send-keys -t autop "python3 $HOME/ansible/autop-listener/autop-listener.py" C-m
