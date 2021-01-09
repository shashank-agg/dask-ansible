## Starting a dask cluster using Ansible

### One time setup:

1. Install required dependencies on all the nodes (python3, pip3, dask, distributed)
2. Run a dask scheduler anywhere, and paste it's IP in the `hosts` file
3. Install ansible on your local machine (https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu)
4. If using keys to SSH into the nodes, paste the username and the keyfile path in the `hosts` file. 
5. If using username & password to SSH into the nodes, generate a key instead:

Generate ssh key using:
`ssh-keygen`

Copy key to server:
`ssh-copy-id -i <key_name_from_above> <node-address>` (for each node in the cluster)

Paste this key's details into ansible (as in step 4)


### Specify cluster info in the `hosts` file 
`hosts` is the ansible inventory file. Here you should specify all the nodes in your cluster, and other arguments.

### Test if ansible is able to communicate with all nodes:
`ansible -i hosts all -m ping`

### Start the cluster
`ansible-playbook -i hosts cluster-start.yml`

### Test the cluster
`python3 test-cluster.py` (after replacing the scheduler IP inside)  to run a test task

### Stop the cluster (stops all the workers on all the nodes)
`ansible-playbook -i hosts cluster-stop.yml `
