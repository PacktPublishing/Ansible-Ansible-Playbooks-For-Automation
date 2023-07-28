#!/bin/bash
ansible ${1} -m ansible.builtin.yum -a 'name=httpd state=present'   -b
