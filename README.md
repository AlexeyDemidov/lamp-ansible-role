lamp
=========

Install OpsGenie Lamp

Role Variables
--------------

The role defines the following defaults:

- opsgenie_lamp_version: "3.1.4"
- opsgenie_api_url: "api.eu.opsgenie.com"
- opsgenie_api_key: "CHANGE_ME"
- lamp_bin_path: "/usr/local/bin/lamp"
- lamp_zip: "opsgenie-lamp_{{ opsgenie_lamp_version }}_linux_amd64.zip"

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: lamp }

License
-------

Copyright (C) 2024 Alex L. Demidov

BSD

Author Information
------------------

Alex L. Demidov <alexeydemidov@gmail.com> https://alexeydemidov.com
