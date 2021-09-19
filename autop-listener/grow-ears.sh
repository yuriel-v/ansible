tmux new -d -s autop
tmux new -d -s autopshell
tmux send-keys -t autop "source /home/vagrant/autop-listener/bin/activate" C-m
tmux send-keys -t autop "python3 /home/vagrant/ansible/autop-listener/autop-listener.py" C-m
