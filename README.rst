thales-hsm
==========

A role to manage Thales Hardware Security Module (HSM) client software.

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
     - /tmp/thales_client_install
     - Working directory in the target host.
   * - thales_client_gid
     - 42481
     - Group ID for the thales group.
   * - thales_client_uid
     - 42481
     - User ID for the thales user.
   * - thales_client_tarball_name
     - None
     - Filename for the Thales client software tarball.
   * - thales_client_tarball_location
     - None
     - Full URL where a copy of the client software tarball can be downloaded.
   * - thales_client_path
     - linux/libc6_11/amd64/nfast
     - Path to the client software directory inside the tarball
   * - thales_km_data_tarball_name
     - None
     - Filename for the KM Data tarball
   * - thales_km_data_location
     - None
     - Full URL where a copy of the KM Data tarball can be downloaded.
   * - thales_rfs_ip_address
     - None
     - IPv4 address for the Thales RFS host.
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
