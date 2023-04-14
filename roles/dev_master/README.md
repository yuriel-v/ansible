# dev_master: Development environment base install, Ubuntu/Linux Mint version

This role configures a development master machine, that is, a machine used to develop just about any kind of application you work with.
By default, this role installs the following:

- Visual Studio Code
- Insomnia
- GitKraken
- AdoptOpenJDK 11 Hotspot
- Maven

Optionally, x11vnc can be installed for VNC support, if needed.

## Requirements

The only requirement is that the target OS must be Ubuntu or Linux Mint.

## Dependencies

None.

## Role variables

- (boolean) `devinstall_add_lxde`: Installs the lxde GUI environment. Defaults to `true` if the machine in question is a Ubuntu installation.
- (boolean) `devinstall_skiptovscode`: If true, only installs the VSCode extensions. Default `false`.
- (string) `devinstall_remdesk`: Case insensitive, chooses which type of remote access protocol to be installed, between `"rdp"` and `"vnc"`. Any other value will not install either. Default value is `"none"`.

## Example Playbook
```
- hosts: servers
  roles:
    - role: dev_master
      become: yes
      vars:
        devinstall_add_lxde: false
        devinstall_skiptovscode: false
        devinstall_remdesk: rdp
```
## License

MIT License

## Author

It's a me, [Leonardo "Yuriel" Valim](mailto:emberbec@gmail.com)
