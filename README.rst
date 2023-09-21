thales-hsm
==========

This is a role to manage the client software for Entrust nShield Connect
Hardware Security Modules (HSMs).

This repo uses the "Thales" name for historical reasons:

At the time when this repository was created nShield HSMs were owned by Thales.
Since then, the nShield line of HSMs have gone through some ownership changes,
including nCipher for some time, and currently Entrust.

If you are looking for the ansible role to manage client software for
Thales Luna Network HSMs you can find it here:

https://opendev.org/openstack/ansible-role-lunasa-hsm

Role Variables
--------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Name
     - Default Value
     - Description
   * - thales_install_client
     - false
     - Whether the role should install the client software on the target host.
   * - thales_configure_rfs
     - false
     - Whether the role should execute the RFS configuration tasks.
   * - thales_client_working_dir
     - /tmp/security_world_install
     - Working directory in the target host.
   * - thales_client_gid
     - 42481
     - Group ID for the nfast group.
   * - thales_client_uid
     - 42481
     - User ID for the nfast user.
   * - security_world_iso_zip_url
     - None
     - URL location of the Security World ISO ZIP file.
   * - thales_client_tarball_location
     - None
     - DEPRECATED: Use security_world_iso_zip_url instead.
   * - thales_rfs_ip_address
     - None
     - IPv4 address for the RFS host.
   * - thales_client_ips
     - None
     - Whitespace separated list of IP addresses to be added to RFS config.
   * - thales_bootstrap_client_ip
     - None
     - Bootstrap client IP address.  This IP will be allowed to update RFS
       server.
   * - nshield_hsms
     - None
     - List of one or more HSM devices


Requirements
------------

 - ansible >= 2.4
 - Security World Software v13.4.4 ISO ZIP file - The ISO file in ZIP format as
   provided by Entrust.  This should be hosted in an HTTPS server that can be
   accessed from the target host.
