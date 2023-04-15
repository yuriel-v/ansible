# global: Yurielnet template setup role

This role configures fresh CentOS and Ubuntu installs into proper templates for yurielnet.
- The following essentials are installed:
  - gcc
  - make
  - tar
  - zip
  - unzip
  - iptables
  - tmux
  - wget
- On Ubuntu:
  - ufw
  - g++
- On CentOS:
  - gcc-c++ (a.k.a. g++)
  - bind-utils (for the dig command)

IPv6 is also disabled at grub level by this role, and Python 3.9 is installed as well.

## Requirements

None.

## Dependencies

None.

## Role variables

- (string) `global_vm_hostname`: The machine's hostname. Yurielnet's standard is `"vmXXX"`, with each `X` being a number, ranging from 001 to 999.
- (string) `global_vm_shortname`: A human readable, short name for the machine's terminal prompt. Overridden by the role `clone`.

## Example Playbook
```
- hosts: servers
  roles:
    - role: global
      become: yes
      vars:
        global_vm_hostname: vm000
        global_vm_shortname: Test VM
```
## License

MIT License

## Author

It's a me, [Leonardo "Yuriel" Valim](mailto:emberbec@gmail.com)
