# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANT_API_VERSION = '2'
VAGRANT_BRIDGE_DEV  = ENV.fetch('VAGRANT_BRIDGE_DEV', 'enp2s0')

Vagrant.configure(VAGRANT_API_VERSION) do |config|
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

  config.ssh.insert_key = false

  config.vm.box = 'generic/ubuntu1804'
  config.vm.synced_folder '.', '/vagrant', disabled: true

  # config.vm.provider 'virtualbox' do |vb|
  #   vb.cpus         = 1
  #   vb.memory       = 512
  #   vb.linked_clone = true

  #   vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  #   vb.customize ["modifyvm", :id, "--ioapic",              "on"]
  # end

  config.vm.provider 'libvirt' do |lv|
    lv.cpus   = 1
    lv.memory = 512

    # lv.storage :file, size: '2G', bus: 'scsi'
  end

  config.vm.define "app1" do |app1|
    app1.vm.hostname = "app1.test"

    app1.vm.network :private_network, ip: "192.168.60.11"
  end

  config.vm.define "app2" do |app2|
    app2.vm.hostname = "app2.test"

    app2.vm.network :private_network, ip: "192.168.60.12"
  end

  config.vm.define "db1" do |db1|
    db1.vm.hostname = "db1.test"

    db1.vm.network :private_network, ip: "192.168.60.21"
  end

  config.vm.define "db2" do |db2|
    db2.vm.hostname = "db2.test"

    db2.vm.network :private_network, ip: "192.168.60.22"
  end

  config.vm.define "db3" do |db3|
    db3.vm.hostname = "db3.test"

    db3.vm.network :private_network, ip: "192.168.60.23"
  end
end
