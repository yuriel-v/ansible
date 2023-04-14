# clone: Generic post-cloning setup role

This role configures basic aspects of any newly provisioned machine.

## Requirements

It's only required that the machine in question be a clone of a template previously configured by the role `global`.

## Dependencies

None.

## Role variables

No modifiable variables have been defined.

## Example Playbook
```
- hosts: servers
  roles:
    - role: clone
      become: yes
```

## License

MIT License

## Author

It's a me, [Leonardo "Yuriel" Valim](mailto:emberbec@gmail.com)
