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
    #Path(f'{homedir}/log/ansible').mkdir(parents=True, exist_ok=True)
    log_path = "/var/log/ansible/deploy"  # trailing slashes might fuck this up
    req = request.get_json()

    try:
        vm_type = req.pop('type')
        vm_ip = req.pop('ip')
        if not isinstance(req['extras'], dict):
            raise Exception("Invalid extras element type")

    except Exception:
        return Response('{"response": "Wrongly formatted request"}', 400)

    req['extras']['global_vm_shortname'] = req['extras'].pop('desc')
    req['extras']['global_vm_hostname'] = req['extras'].pop('name')
    extra_vars = str(dumps(req['extras'])).replace('"', '\\"')

    ansible_command = "tmux send-keys -t autopshell "
    ansible_command += f"'ansible-playbook {homedir}/ansible/global.yml -i {vm_ip}, --tags \"{vm_type}\" --extra-vars \"{extra_vars}\" "
    ansible_command += f"| tee {log_path}/{req['extras']['global_vm_hostname']}-{datetime.now().isoformat()}.log' C-m"
    os.system(ansible_command)

    return jsonify({'response': 'Ansible command fired'})


@app.route('/getkey', methods=['GET'])
def get_public_key():
    with open(f'{homedir}/.ssh/ansible/id_ansible.pub', 'r') as pkfile:
        return jsonify({'publickey': pkfile.readline().rstrip()})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4960)

