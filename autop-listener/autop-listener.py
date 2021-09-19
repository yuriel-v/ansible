import os
from pathlib import Path
from datetime import datetime
from json import dumps

import flask as fsk
from flask import request, jsonify, Response

app = fsk.Flask(__name__)
app.config['DEBUG'] = False
homedir = os.getenv('HOME')

@app.route('/provision', methods=['POST'])
def auto_provision():
    Path(f'{homedir}/log/ansible').mkdir(parents=True, exist_ok=True)
    req = request.get_json()

    try:
        vm_type = req.pop('type')
        vm_ip = req.pop('ip')
        vm_name = req.pop('name')
        vm_desc = req.pop('desc')
    except Exception:
        return Response('{"response": "Wrongly formatted request"}', 400)

    req["global_vm_shortname"] = vm_desc
    req["global_vm_hostname"] = vm_name
    extra_vars = str(dumps(req)).replace('"', '\\"')

    ansible_command = "tmux send-keys -t autopshell "
    ansible_command += f"'ansible-playbook {homedir}/ansible/global.yml -i {vm_ip}, --tags \"{vm_type}\" --extra-vars \"{extra_vars}\" "
    ansible_command += f"| tee {homedir}/log/ansible/{vm_name}-{datetime.now().isoformat()}.log' C-m"
    os.system(ansible_command)

    return jsonify({'response': 'Ansible command fired'})


@app.route('/getkey', methods=['GET'])
def get_public_key():
    with open(f'{homedir}/.ssh/ansible/id_ansible.pub', 'r') as pkfile:
        return jsonify({'publickey': pkfile.readline().rstrip()})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4960)

