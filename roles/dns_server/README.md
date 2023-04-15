# dns_server: Installing a BIND9 DNS server

This role configures a CentOS or Ubuntu machine as a DNS server master or slave instance.

## Requirements

The machine must ideally be a template previously configured by the role `clone`. That is not a hard requirement however.

## Dependencies

None.

## Role variables

- (string) `dns_server_type`: Defines the type of instance to be configured, either a `"master"` or a `"slave"` instance. Defaults to `"slave"`.
- (string) `dns_server_zone`: Defines the zone to be configured. Defaults to `"yuriel.net"`.
- (string) `dns_server_reverse_zone`: Defines the reverse zone to be configured. Defaults to `"16.172.in-addr.arpa"`.
- (string) `dns_server_master_ns_name`: Defines the record name of the master NS instance, mapped along with `dns_server_zone`, such that the record name will be `"{{ dns_server_master_ns_name }}.{{ dns_server_zone }}"`. Defaults to `"ldap"`, the default record being `"ldap.yuriel.net"`.
- (dict/map) `dns_server_records`: Defines the default records to be written to the zone. See `defaults/main.yml` for the default.

## Example Playbook
```
- hosts: servers
  roles:
    - role: dns_server
      become: yes
      vars:
        dns_server_type: master
        dns_server_zone: example.com
        dns_server_reverse_zone: 10.in-addr.arpa
        dns_server_master_ns_name: ns1
        dns_server_records:
          # Add NS record: 'example.com. IN NS ns1.example.com.'
          - domain: example.com.
            ttl: ""
            type: NS
            address: ns1.example.com.

          # Add A record: 'ns1 86400 IN A 10.0.0.2'
          - domain: ns1
            ttl: "86400"
            type: A
            address: 10.0.0.2
```
## License

MIT License

## Author

It's a me, [Leonardo "Yuriel" Valim](mailto:emberbec@gmail.com)
