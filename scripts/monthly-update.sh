timestamp=$(date --iso-8601=seconds)
ansible-playbook /home/vagrant/ansible/run_update.yml -i /home/vagrant/ansible/inv > "/var/log/ansible/update/${timestamp}.log" 2>"/var/log/ansible/update/${timestamp}.errlog"
