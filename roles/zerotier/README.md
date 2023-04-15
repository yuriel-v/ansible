# zerotier: Installs ZeroTier One VPN

This role installs ZeroTier One VPN. This role will NOT install it should another installation already be present.

## Requirements

The machine must ideally be a template previously configured by the role `clone`. That is not a hard requirement however.

## Dependencies

None.

## Role variables

- (string) `zt_network`: An existing ZeroTier network to join upon a successful installation. If not provided, no networks will be joined.

## Example Playbook
```
- hosts: servers
  roles:
    - role: zerotier
      become: yes
      vars:
        zt_network: 0abc123ztnw
```
## License

MIT License

## Author

It's a me, [Leonardo "Yuriel" Valim](mailto:emberbec@gmail.com)
