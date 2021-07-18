# game_server: Install and configure a game's dedicated server instance

This role installs and configures a game's dedicated server instance.\
The role's prefix in the source code is **gs**.

Currently supported games are:
- Terraria
  - Launches as a systemd service through tmux on boot, on session `terraria`.
- Minecraft
  - Launches also as a systemd service through tmux on boot, on session `mc`.
- Starbound (TODO)

## Requirements

- git
- g++ and gcc compilers
- make
- tmux
- unzip
- ufw (Uncomplicated Firewall)
- iptables

All of these dependencies are installed by the role Global.\
This role also installs ZeroTier One and joins a network defined in a secret file, placed in this repo's global shared directory, specifically `/shared/private/secrets.yml`.

## Dependencies

There are no dependencies, but running the role Global is advisable prior to running this role, since it makes sure all the necessary dependencies are present.

## Role variables

### Global role variables:
- **gs_overwrite**: (bool | string) Decides whether or not an existing instance of the game's server will be overwritten if found.
  - Defaults to `false`, but can be set to the following values:
    - `false`: No overwriting will be done. Does nothing if the installation directory already exists.
    - `'soft'`: Soft overwriting. Appends an `_old_` and a unique timestamp to the installation directory, safely moving it elsewhere.
    - any other value: Hard overwriting. Deletes the installation directory if it exists.

- **gs_game**: (enum, string) Decides which game the server will host a server of. Currently supported values are (or will be):
  - `terraria`
  - `minecraft`
  - `starbound`

- **gs_zt_network**: (string) The ZeroTier network ID to join.
  - This is a secret variable placed on the dir `/private/secrets.yml`, relative to this repo's root.
  - This variable is optional, if no ID is specified, no "IP fetching" script will be launched and ZeroTier won't join any networks.

- **gs_install_zerotier**: (bool) Decides whether or not ZeroTier One will be installed. If this is false, the variable `gs_server_ip` **has** to be provided!

- **gs_server_ip**: (string) The server's IP to listen to. Automatically defined if ZeroTier is to be installed (and a network joined), else it must be defined manually.
  - If its value is set to `update` then it will skip the fail check for a valid server IP.
  - The `update` value is intended to update installs in an automated way.

### Terraria role variables:
- **gs_terraria_**: Prefix for the following variables:
  - `link`: (string) Link to the zipped dedicated server instance to install.
    - Defaults to Terraria's latest version at the time of running.
  - `install_dir`: (string) Absolute path to the server instance's installation directory. The worlds directory will be created on the exact same directory, save for a "_worlds" appended to the name.
    - Example: By default the path is `/home/vagrant/terraria`, so the worlds directory will be `/home/vagrant/terraria_worlds`.
  - `port`: (string | int) Port number to use, defaults to Terraria's default, 7777.
  - `world_name`: (string) The world name to use - the world will be saved in the .wld extension with that name too. Defaults to "Aurellia", because I like that name.
  - `autocreate_size`: (int) The world size to be autocreated with. Valid values:
    - `1`: Small world.
    - `2`: Medium world (default).
    - `3`: Large world.
  - `seed`: (string) The world seed. Defaults to the drunk world seed (05162020).
  - `difficulty`: (int) The difficulty. Valid values:
    - `0`: Normal.
    - `1`: Expert.
    - `2`: Master.
    - `3`: Journey (default).
  - `password`: (string) The server password. Defaults to 420, because memes.
  - `max_players`: (int) The maximum number of players allowed at a time. Defaults to Terraria's default, 8.
  - `motd`: (string) The server's message of the day. Defaults to a parody of Minecraft's default MOTD.
- As was mentioned at the top, the prefix for all of these is `gs_terraria_`, so for instance, to refer to the `link` variable, use `gs_terraria_link`.

### Minecraft role variables
- **gs_mc_**: Prefix for the following variables:
  - `link`: (string) A link to a server .jar file or a compressed archive containing a modded/plugin server install.
    - Defaults to Minecraft's latest vanilla server .jar at the time of running.
  - `install_dir`: (string) Absolute path to the server instance's installation directory. The world will be generated inside that directory.
  - `user`: (string) User to run the systemd service as. Defaults to `vagrant`.
  - `group`: (string) Group to run the systemd service as. Defaults to `vagrant`.
  - `ram`: (string) The amount of RAM to pass to the `-Xms` and `-Xmx` arguments. Defaults to `4G`.
  - `cfg`: (dict) Configuration file parameters to pass to the `server.properties` file. Each key is an entry in the vanilla config file.
    - The defaults are the same as the default values seen [here.](https://minecraft.fandom.com/wiki/Server.properties#Java_Edition_2)
    - Do note however that values containing dots, such as `query.port` should be referred to as having a dash instead in this variable.
    - For instance, to set the `query.port` value to `25575` instead, you'd set it as below:
    ```
    gs_mc_cfg:
      query-port: 25575
    ```

More role variables to come as the tasks for Starbound are developed.

## Additional notes
### Minecraft
- A directory named `minecraft.d` will be created inside the installation directory. This will contain the `ServerStart.sh` and `ServerStop.sh` scripts.
- If setting a custom link, you **will** have to properly set `ServerStart.sh` to point to whatever server .jar your custom install uses.
- The systemd service will not be enabled nor started in this case, and a `server_instructions.md` file will be written to your installation directory.
  - Please refer to that file if in doubt, as well as your custom install's README file.

## Example Playbook

    - hosts: servers
      roles:
        - role: global
          become: yes
        
        - role: game_server
          become: yes
          vars:
            gs_overwrite: yes
            gs_type: terraria
            gs_terraria_motd: "My Terraria dedicated server"
            gs_terraria:
              link: "https://terraria.org/dedicatedserver/restoflink/terraria-server-1412.zip"
              install_dir: /home/myuser/terraria-server
              port: 1234
              world_name: 'My HARDCORE world'
              autocreate_size: 1
              seed: for the worthy
              difficulty: 2
              password: thor
              max_players: 5
            
All of the vars can be omitted, in which case they will assume their defaults - with the notable exception of `gs_type`, which has no default.

## License

MIT License

## Author

It's a me, [Leonardo "Yuriel" Valim](mailto:emberbec@gmail.com)
