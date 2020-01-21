#!/bin/sh
deploy_vars_file="${DEPLOY_VARS_FILE:-deploy_vars.yml}"
host_inventory="${INVENTORY_FILE:-hosts}"
playbook="${PLAYBOOK:-playbook.yml}"

ansible-playbook -i "$host_inventory" -e deploy_vars_file="$deploy_vars_file" $@ "$playbook"
