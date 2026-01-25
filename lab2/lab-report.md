# Grabed Lab 2
## Process
1. Assign policy for the "Canada Central" region
![Assign policy 1](./images/Screenshot%20(485).png)
![Assign policy 2](./images/Screenshot%20(489).png)
2. Try to create a VM in another region
![Create VM](./images/Screenshot%20(487).png)
I changed the region in the policy and the test because our subscription does not allow us to create ressouce in Canada Central
![Assign policy East US 2](./images/Screenshot%20(488).png)
![Assign policy East US 2](./images/Screenshot%20(489).png)
3. Try to create a VM in the region
![Create VM](./images/Screenshot%20(490).png)
![Create VM](./images/Screenshot%20(491).png)
![Create VM](./images/Screenshot%20(492).png)
4. Create the subnets
![Create subnet 1](./images/Screenshot%20(493).png)
![Create subnet 2](./images/Screenshot%20(494).png)
![Create subnet 3](./images/Screenshot%20(495).png)
5. Create the NSG rules
![Create NSG rules 1](./images/Screenshot%20(496).png)
![Create NSG rules 2](./images/Screenshot%20(497).png)
![Create NSG rules, Outbounds](./images/Screenshot%20(498).png)
![Create NSG rules, Outbounds](./images/Screenshot%20(499).png)
![Create NSG rules, inbounds](./images/Screenshot%20(500).png)
6. Create storage account
![Create storage account 1](./images/Screenshot%20(501).png)
![Create storage account 2](./images/Screenshot%20(502).png)
7. Create file share
![Create file share](./images/Screenshot%20(503).png)
8. Create vm-private in the private subnet
![Create vm-private 1](./images/Screenshot%20(504).png)
![Create vm-private 2](./images/Screenshot%20(505).png)
9. Connect to the vm-private via bastion and try to connect to the file share. It worked
![Connect to file share 1](./images/Screenshot%20(506).png)
10. Create vm-public in the public subnet
![Create vm-public 1](./images/Screenshot%20(507).png)
![Create vm-public 2](./images/Screenshot%20(508).png)
11. Connect to the vm-public via bastion and try to connect to the file share. It failed
![Connect to file share 2](./images/Screenshot%20(509).png)
This means that the policy block every connection from other endpoints than the private one.
12. I deleted the resources
![Delete resources](./images/Screenshot%20(510).png)


## Analysis and observations
1. Policy Enforcement: The policy successfully restricted resource creation out of the specified region, demonstrating effective governance over resource deployment.
2. Network Security: The NSG rules effectively controlled access to the VMs, allowing only the private subnet to connect to the file share, which enhances security.
3. Connectivity Testing: The successful and failed connection attempts to the file share provided clear evidence of the policy and NSG rules in action, validating their configurations.

## Cleanup confirmation 
![Delete resources](./images/Screenshot%20(511).png)