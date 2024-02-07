import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
# Create a XenVM
node = request.RawPC("node")
node.hardware_type = 'c240g5'
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD"
node.routable_control_ip = "true"

#Install Packages
node.addService(rspec.Execute(shell="/bin/sh", command="sudo add-apt-repository ppa:graphics-drivers/ppa"))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt update"))
node.addService(rspec.Execute(shell="/bin/sh", command="sudo apt install ubuntu-drivers-common"))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo apt install nvidia-driver-535'))
node.addService(rspec.Execute(shell="/bin/sh", command='sudo reboot'))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
