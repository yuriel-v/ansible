# Ansible
This is a repository of roles and playbooks used by Ansible in my own home's infrastructure. \
More information on the infrastructure itself can be found [here](https://github.com/yuriel-v/Infrastructure).

---

## Roles

### global

Global provisioning role. Not much to it, just default configurations for all machines. \
[More information.](roles/global/README.md)

### dev_master

Provisioning role for a desktop development VM.
[More information.](roles/dev_master/README.md)

### game_server

Provisioning role for a game server. Currently implemented servers:
- Terraria

Games to be supported in the future:
- Minecraft (vanilla and modded)
- Starbound

[More information.](roles/game_server/README.md)

### mysql_install

A still-not-implemented provisioning role for a basic MySQL server VM.

## License

MIT License

## Author

It's a me, [Leonardo "Yuriel" Valim](mailto:emberbec@gmail.com)