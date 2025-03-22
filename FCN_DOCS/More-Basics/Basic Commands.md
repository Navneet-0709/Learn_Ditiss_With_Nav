# Cisco Packet Tracer
Some basic Things to remeber :- 
        - Prompt for every configuration is very much important
        - to make changes to any of the configuration in router you have to be in configuration prompt
            :- router(config)#


# Task :- to setup the hostname of the router
    router# config t
    router(config)# hostname [hostname]
    [hostname](config)#

# Task :- To set Password to all the Lines (con , aux , vty)
..first enter to the config prompt
    router(config)# line con 0
    router(config)# password cisco
    router(config)# login
    router(config)# exit

    router(config)# line aux 0
    router(config)# password cisco
    router(config)# login
    router(config)# exit
    
    router(config)# line vty 0 4
    router(config)# password cisco
    router(config)# login
    router(config)# exit


# Task :- To set Password to the router
    router(config)# enable secret Cisco

# Task :- To see the runnng configuration and startup configuration
    router# show runn
[or]  router# show running-configuration

    router# show start
[or]  router# show startup-configuration

# Task :- To save the running configuration to the tartup configuation:-

    router# copy runn start
[or]  router# copy running-configuration startup-configuration     

# Task :- To give the ip addresses to the interfaces
    
    router(config)# interface g0/_
    router(config-if)# no shut      //(to make the link up)
    router(config-if)# ip address xxx.xxx.xxx.xxx [Subnet_Mask]
    router(config-if)# exit
    router(config)# exit
    router#

# Task :- To see the neighbours and connected ips
    Cicso Discovery Protocol : - 
        router# show cdp neighbors
        router# show cdp neighbors details

# Task :- disable Cicso Discovery Protocol :- 
        router# no cdp run    
    

# Task :- To encrypt the passwords 
    router(config)# service passwords-encryption 

# Task :- To disable the encrypt passwords service
    router(config)# no service passwords-encryption

# Task :- To set the executive timeout to console line
    router(config)# line con 0
    router(config-line)# exec-timeout min sec

# Task :- To see the Information of a particular Interface
    router# show int g0/_
# Task :- To see the Information of Interfaces
    router# show ip interface 
# Task :- To see the Information of Interfaces in detail
    router# show ip interface brief
# Task :- To see the Information of protocols
    router# show protocols

# Task :- To recover the forgotten password 
    
        1 -- restart (ctrl + break)
        2 -- boot# set ios-conf = 0x2142
        3 -- boot# save 
        4 -- restart 
        5 -- ssrtup y/n
        6 -- router>en
        7 -- router# copy start run
        8 -- router# config t
        9 -- router(config)# en secret new_password
        10 -- router(config)# config-reg 0x2102
mostimp 11 -- router# copy run start

# Task :- Static Assingment of Host for Telnet by name
 
    router(config)#ip host b 172 .xx.xx.xx
    router(config)#ip host c 172 .xx.xx.xx
    router(config)#ip host d 172 .xx.xx.xx

# Task :- To turn of the DNS lookup 
    router(config)# no ip domain-lookup 


# Task:-  BAckup and Restoring in routers (configuration and ios)

BAckup :- 
        router# copy flash tftp 
                      start
                      runn
        
        router# tftp ip ?
        router# source file ?
        router# dest file ?
        
restore :- 
        router# copy tftp    flash 
                        start
                        runn
        
        router# tftp ip ?
        router# source file ?
        router# dest file ?

# Task :- To configure Static Routes to a router 

    router(Config)# ip route destination_subnet Subnet_mask Next_hop

# Task :- To configure RIP Routing PRotocol 
    
    router(config)# router rip
    router(config)# network [NetworkAddress]1
    router(config)# network [NetworkAddress]2
