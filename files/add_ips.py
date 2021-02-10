#!/usr/bin/python3
#
# Copyright 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
import os
import sys


def write_new_conf(directory, addresses):
    """Write a new Thales HSM configuration file

    This function reads a file called `config` in the given directory,
    adds the given list of addresses to the [hs_clients] section and
    writes the result in the `config.new` file.

    If an existing `config.new` file is found, it is backed up as
    `config.new.X` where X is the next available integer starting from
    zero.

    For example, given addresses=['192.168.24.10'], a new client config
    entry will be added to the config file including the client delimiter
    (-----) and other required options:

        syntax-version=1
        [server_settings]

        # --- snip ---

        [hs_clients]
        addr=EXISTING_IP_ADDRESS
        clientperm=priv
        keyhash=0000000000000000000000000000000000000000
        esn=
        timelimit=86400
        datalimit=8388608
        -----
        addr=192.168.24.10
        clientperm=priv
        keyhash=0000000000000000000000000000000000000000
        esn=
        timelimit=86400
        datalimit=8388608

        # --- snip ---

    Although the file looks a lot like an ini, we're not able to use
    configparse due to the required syntax-version declaration,
    the ----- delimiters, and the reused config options for every client
    entry.

    """
    # parse config file into 3 sections
    before_config = list()
    client_config = list()
    after_config = list()

    conf = os.path.join(directory, 'config')

    with open(conf) as f:
        lines = f.readlines()

    for line in lines:
        if after_config:
            after_config.append(line)
            continue
        if "[hs_clients]" in line:
            client_config.append(line)
            continue
        if client_config:
            if line.startswith('['):
                after_config.append(line)
            else:
                client_config.append(line)
            continue
        before_config.append(line)

    # move trailing empty lines from client config to after config
    while client_config[-1] == '\n':
        after_config.insert(0, client_config.pop())

    # list configured adresses
    configured_ips = list()
    for line in client_config:
        if line.startswith("addr"):
            configured_ips.append(line.strip('\n').split('=')[1])

    # skip addresses that have already been configured
    new_ips = list()
    for addr in addresses:
        if addr in configured_ips:
            continue
        new_ips.append(addr)

    if not new_ips:
        # nothing to do
        sys.exit(0)

    new_entries = list()
    for addr in new_ips:
        new_entries += [
            '-----\n',
            'addr={}\n'.format(addr),
            'clientperm=priv\n',
            'keyhash=0000000000000000000000000000000000000000\n',
            'esn=\n',
            'timelimit=86400\n',
            'datalimit=8388608\n',
        ]

    new_conf = os.path.join(directory, 'config.new')

    if os.path.exists(new_conf):
        next = 0
        while os.path.exists(os.path.join(directory,
                             ('config.new.' + str(next)))):
            next += 1
        os.rename(new_conf,
                  os.path.join(directory, ('config.new.' + str(next))))

    with open(new_conf, 'w') as f:
        for line in (before_config + client_config +
                     new_entries + after_config):
            f.write(line)
    sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config-dir", help="Path to the directory that "
                                             "contains the config file.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--ips", nargs="+",
                       help="One or more IP addresses to be added "
                            "to the config file.")
    group.add_argument("--file", help="Path to file containing IP addresses "
                                      "to be added to the config file.")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            ips = f.readlines()
        ips = [ip.strip('\n') for ip in ips]
    else:
        ips = args.ips

    write_new_conf(args.config_dir, ips)
