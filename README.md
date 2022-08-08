# Ansible
This is a repository of roles and playbooks used by Ansible in my yurielnet. \
More information on the infrastructure itself can be found [here](https://github.com/yuriel-v/yurielnet).

## Roles

### global

Global provisioning role. Not much to it, just default configurations for all machines. \
[More information.](roles/global/README.md)

### dev_master

Provisioning role for a desktop development VM. \
[More information.](roles/dev_master/README.md)

### game_server

Provisioning role for a game server. Currently implemented servers:
- Terraria
- Minecraft (vanilla and modded)

Games to be supported in the future:
- Starbound (unlikely)
- Factorio
- Satisfactory

[More information.](roles/game_server/README.md)

### mysql_install

A still-not-implemented provisioning role for a basic MySQL server VM.

## License

MIT License

## Author

It's a me, [Leonardo "Yuriel" Valim](mailto:emberbec@gmail.com)
