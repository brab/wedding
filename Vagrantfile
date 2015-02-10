# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "trusty64"
  config.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "forwarded_port", guest: 5000, host: 5000,
      auto_correct: true
  config.vm.synced_folder ".", "/home/vagrant/wedding", nfs: true

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", 1024]
    vb.customize ["setextradata", :id, "VBoxInternal2/SharedFolderEnableSymlinksCreate/app", "1"]
  end

  config.vm.provision "puppet" do |puppet|
    puppet.manifests_path = "puppet"
    puppet.manifest_file  = "site.pp"
    puppet.module_path = "puppet/modules/"

    #puppet.options = "--verbose --debug"
  end
end
