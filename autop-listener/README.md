# autop-listener

This is a simple Flask listener for automatic provisioning. \
It'll listen to incoming requests on port 4960 and fire Ansible 
at the caller, according to the parameters.

This **REQUIRES** that the host have Ansible's public key added! To get it, visit the endpoint `/getkey` on a GET method.

## Request body format
Method: POST
Endpoint: /provision
```json
{
    "ip": "172.16.0.1",
    "type": "general",
    "extras": {
        "name": "vm123",
        "desc": "Test VM",
        "role_param1": "asdf",
        "role_param2": "qwerty"
    }
}
```

This will launch an Ansible command with the following format:
`ansible-playbook global.yml -i [ip], --tags [type], --extra-vars "{'global_vm_shortname': '[extras.desc]', 'global_vm_hostname': '[extras.name]', 'role_param1': [extras.role_param1], 'role_param2': [extras.role_param2]}"`
