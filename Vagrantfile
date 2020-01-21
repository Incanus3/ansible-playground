# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANT_API_VERSION = '2'
VAGRANT_BRIDGE_DEV  = ENV.fetch('VAGRANT_BRIDGE_DEV', 'enp2s0')

Vagrant.configure(VAGRANT_API_VERSION) do |config|
  # config.vm.box = "ubuntu/bionic64"
  config.vm.box = 'generic/ubuntu1804'

  config.ssh.insert_key = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network 'public_network', dev: VAGRANT_BRIDGE_DEV

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder '.', '/vagrant', disabled: true

  config.vm.provider 'virtualbox' do |vb|
    vb.cpus         = 1
    vb.memory       = 512
    vb.linked_clone = true
  end

  config.vm.provider 'libvirt' do |lv|
    lv.cpus   = 1
    lv.memory = 512
  end

  config.vm.provision 'ansible' do |ansible|
    ansible.playbook           = 'playbook.yml'
    ansible.inventory_path     = 'hosts'
    ansible.compatibility_mode = '2.0'
    ansible.raw_arguments      = ["-e", "deploy_vars_file=deploy_vars.yml"]
  end

  config.vm.define "app1" do |app|
    app.vm.hostname = "orc-app1.test"
    app.vm.network :private_network, ip: "192.168.60.4"
  end

  config.vm.define "app2" do |app|
    app.vm.hostname = "orc-app2.test"
    app.vm.network :private_network, ip: "192.168.60.5"
  end

  config.vm.define "db1" do |db|
    db.vm.hostname = "orc-db.test"
    db.vm.network :private_network, ip: "192.168.60.6"
  end
end
