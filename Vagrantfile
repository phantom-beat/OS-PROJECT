Vagrant.configure("2") do |config|
  # Box base
  config.vm.box = "ubuntu/jammy64"
  config.vm.hostname = "dataexplorer"

  # Red privada (para acceso local)
  config.vm.network "private_network", ip: "192.168.56.99"

  # Carpeta compartida
  config.vm.synced_folder ".", "/vagrant"

  # Configuración de VirtualBox
  config.vm.provider "virtualbox" do |vb|
    vb.name = "DataExplorer-Ubuntu"
    vb.memory = 4096
    vb.cpus = 2
  end

  # Provisionamiento con Ansible Local
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "/vagrant/ansible/playbook.yml"
    ansible.verbose = "v"
  end
end
