Vagrant.configure("2") do |config|
  # Box base (misma para ambas máquinas)
  config.vm.box = "ubuntu/jammy64"

  # Carpeta compartida
  config.vm.synced_folder ".", "/vagrant"

  # Máquina web: Nginx
  config.vm.define "web" do |web|
    web.vm.hostname = "dataexplorer-web"
    web.vm.network "private_network", ip: "192.168.56.101"

    web.vm.provider "virtualbox" do |vb|
      vb.name = "DataExplorer-Web"
      vb.memory = 2048
      vb.cpus = 2
    end
  end

  # Máquina de monitoreo: Prometheus + Grafana
  config.vm.define "monitoring" do |monitoring|
    monitoring.vm.hostname = "dataexplorer-monitoring"
    monitoring.vm.network "private_network", ip: "192.168.56.102"

    monitoring.vm.provider "virtualbox" do |vb|
      vb.name = "DataExplorer-Monitoring"
      vb.memory = 4096
      vb.cpus = 2
    end
  end

  # Provisionamiento con Ansible desde el host (requiere Ansible instalado en la máquina host)
  # Ejecutará ansible/playbook.yml y Vagrant generará el inventario automáticamente
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/playbook.yml"
    ansible.verbose = true
  end
end
