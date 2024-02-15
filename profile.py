import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
node = request.RawPC("node")
#node.hardware_type = 'c240g5'
node.hardware_type = 'd8545'

node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD"
# node.routable_control_ip = "true"

#Install Packages
node.addService(rspec.Execute(shell="/bin/sh", command="sudo add-apt-repository ppa:graphics-drivers/ppa"))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install -y ubuntu-drivers-common"))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo apt install -y nvidia-driver-535'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo curl -OJL https://raw.githubusercontent.com/JarrettTrapani/CloudLab/main/RamBot.py'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo apt install -y python3-pip'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo pip install transformers'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo pip install accelerate'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo pip install bitsandbytes'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo pip install sentencepiece'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo pip install protobuf'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo cp /local/repository/RamBot.py /users/JTrap'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo python RamBot.py'))

# node.addService(rspec.Execute(shell="/bin/sh", command='sudo reboot'))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
