# AD Value of Routing Protocols

Administrative Distance (AD) is a value used by routers to rank the trustworthiness of routing information received from different routing protocols. Here are the AD values for common routing protocols:
```
+------------------------+------------------------------+
| Routing Protocol       | Administrative Distance (AD) |
|------------------------+------------------------------|
| Directly connected     | 0                            |
| Static route           | 1                            |
| BGP (external)         | 20                           |
| EIGRP (internal)       | 90                           |
| IGRP                   | 100                          |
| OSPF                   | 110                          |
| IS-IS                  | 115                          |
| RIP                    | 120                          |
| EIGRP (external)       | 170                          |
| BGP (internal)         | 200                          |
| Unknown                | 255                          |
+------------------------+------------------------------+
```
```
+----------------------------+----------------------------+
| RIP v1                     | RIP v2                     |
+----------------------------+----------------------------+
| Class Full                 | Class Less                 |                
| FLSM                       | VLSM                       |
| Doesn't send SM            | sends SM                   |
| All 1ns BR 255.255.255.255 | 224.0.0.9                  |
| No Auth.                   | Authentication             |
| no compatible with v2      | Compatile with v1          |
+----------------------------+----------------------------+
```
```
+----------------------------+--------------------------------+
|Distance Vector (RIP)       | Link State (OSPF)              |
+----------------------------+--------------------------------+
|All 1s br 255.255.255.255   | 224.0.0.5 and 224.0.0.6        |
|whole table Update          | Hello, LSA, DD (database descp)|   
|Every 30 sec                | 10sec, 30sec, 30min            |
|One Routing table           | Routing table,                 |
|                            | -Link S Table,                 |
|                            | -neighbour table               |
|Routing Loop                | No loops                       |
|Support FLSm                | VLSM
|                            | Summarisation
|Bandwidth cOmsuming         |MEmory & Processing power consuming 
|works on HOPs               | 18^8Bandwidth = Cost
|Simlpe to Implement         | very Complex
|hops                        | 255*2^32 hops
|Small netowrks              | Medium to Large
|Belman and Ford             | Dijistra
+----------------------------+--------------------------------+
```
## OSPF Summarization
# Link State Routing 


|Distance Vector |Link State|
|----------------|----------|
|Sends Entire packets, that is one of the biggest disadvantage of the **RIP**, as every 30 sec the whole routing table isbeing send to the neighbour router | In **Link State**, there are three components, First, **Hello Message**, that sends only packet ensuring *everything is alright*, and next is **LSA**, that sends any new changes occured in network topology, another is **DD (Database Discription)** that contain the routing table which is send every **30mins**|
| In RIP, there us **routing with rumours**, meaning router connected to each other telling the next router that there is a change, it is possible though that info is not accurate, refer to [split horizon](../day7/day7.md#split-horizon)| Here in OSPF, there is **Neighbour Table** as well as **Link State** table, so it only listens to the one that is directly connected to the network on which the decision is to be made|
|It works with **Metric = Hops (max 15)** | But it works with **distance = 10⁸/Bandwidth**, and there is no Hop count limitation in the link state routing|
|RIP is used in small network as it can't be implemented obvisouly for major networks, because it can' reach to network that has more than 15 hops | But OSPF can contains large tables and very huge number of Routing tables as it isn't limited by any hop count
|RIP consumes **Bandwidth**, it's a kind of recurring cost| OSPF consumes **Memory** as it has to contain larg routiung table and consumes **Power**|
|RIP is very simple to implement| OSPF us very complex and a proper planning is required as there is hierarchical adressing|
|**Belmann & ford** ALgorithm| **(SPF) Dijikstra** Algorithm|   

OSPF (Open Shortest Path First) is a link-state routing protocol used to find the best path for data exchange. Summarization in OSPF is the process of consolidating multiple routes into a single summary route to reduce the size of the routing table and improve efficiency.

### Types of OSPF Summarization

1. **Inter-Area Summarization**: This occurs on Area Border Routers (ABRs) and summarizes routes between different OSPF areas.
2. **External Route Summarization**: This occurs on Autonomous System Boundary Routers (ASBRs) and summarizes external routes injected into the OSPF domain.

#### `Hello` message

`Hello` messages are sent in order to ensure the network about the presence of the routers, it basically establishes the relationship between the two routers, such that the routers are able to build a connection between themselves.

#### LSA (Link State Advertisement)

Link-state Advertisement annouces or updates the next or connected routers about the updates to any network topology, as it could be router going **down** and getting **up**.

#### DD (Database Distribution)

Database Distribution is where the routing table shared with all the routers, maintaining the identical record throughout the network topology.  

### Neighbour table & Link state table

![alt text](link-state.png)

OSPF contains a **Neighbour table**, meaning *who am I connected to* and another is **Link state** table contains *who is connected to whom*. Neighbour table has to first establish a relationship with the router next to it, and stores the relationship with the next routers to it, over which there is Link state which contains the routing table of all the links connected in the network. 

The link state and neighbour table match the entries over the any decision that is requored to be made regarding any netwrok, say if router `X` is down, it will check from whom the update is comming, such that, if it is not directly comming from the one connected directly, it would leave the update and will not listen to it.

### Example

**OSPF** is a hierarchical routing protocol and has **Root Summarization**, as if there are like 200 branches and any updates from any of the branches will occur, there won't be 200 updates on each branch getting forwarded to the **Main branch**, instead there will be only on update getting transfered to the main branch from the **ABR** connected to singleton branch, similarly, there will one transfer to update from another **ABR**.  

![alt text](asbr.png)

### Example of Inter-Area Summarization

Consider an OSPF network with the following subnets in Area 1:
- 10.1.1.0/24
- 10.1.2.0/24
- 10.1.3.0/24

These can be summarized into a single route:
- 10.1.0.0/22

To configure summarization on an ABR, use the following command in the OSPF router configuration mode:
```plaintext
area 1 range 10.1.0.0 255.255.252.0
```

### Example of External Route Summarization

Consider an ASBR injecting the following external routes into OSPF:
- 192.168.1.0/24
- 192.168.2.0/24
- 192.168.3.0/24

These can be summarized into a single route:
- 192.168.0.0/22

To configure summarization on an ASBR, use the following command in the OSPF router configuration mode:
```plaintext
summary-address 192.168.0.0 255.255.252.0
```

Summarization helps in reducing the size of the routing table, which in turn reduces the amount of memory and CPU resources required by the router.
```
                             +--------------------+
                             |    ASBR - Delhi    |
                             +--------------------+        
                               /      |     \    
                              /       |      \           
                             /        |       \      
                            /         |        \          
                           /          |         \
                          /           |          \   
                         /            |           \  
                        /             |            \         
                       /              |             \                             
                      /               |              \       
                     /                |               \              
                    /                 |                \             
                   /                  |                 \            
                  /                   |                  \           
                 /                    |                   \          
                /                     |                    \           
            +----------------+ +----------------+ +----------------+
            | Backbone Router| | Backbone Router| | Backbone Router|
            |     Mumbai     | |    Chennai     | |   Bangalore    |
            +----------------+ +----------------+ +----------------+
                  |
            +------------------------------------------------------------+
            |                      |                           |         |
            | +----------------+  +----------------+  +----------------+ |
            | | Internal Router|  | Internal Router|  | Internal Router| |
            | |     Pune       |  |    Nashik      |  |    Satara      | |
            | +----------------+  +----------------+  +----------------+ |
```

1. Backbone Area (Area 0):
The backbone area is the core of an OSPF (Open Shortest Path First) network. It is designated as Area 0.
All other areas must connect to the backbone area, either directly or through a virtual link.
It is responsible for distributing routing information between different areas.

2. Normal Area:
A normal area is any OSPF area that is not a special type of area like a stub, totally stub, or NSSA.
It can have multiple routers and networks within it.
It can receive and send routing information to other areas and the backbone area.

3.Stub Area:
A stub area is an OSPF area that does not receive external routes (routes from outside the OSPF autonomous system).
Instead, it uses a default route to reach external networks.
This reduces the size of the routing table and the amount of routing information exchanged.

4. Totally Stub Area:
A totally stub area is a more restrictive version of a stub area.
It does not receive external routes or summary routes from other areas.
It only receives a default route to reach all destinations outside the area.
This further reduces the size of the routing table and the amount of routing information exchanged.

5. NSSA (Not-So-Stubby Area):
An NSSA is a type of OSPF area that allows limited external routing information.
It can import external routes into the OSPF autonomous system but does not receive external routes from other areas.
This allows for some flexibility in routing while still reducing the size of the routing table.
These concepts are essential for understanding how OSPF manages routing information and optimizes network performance.


# commands for OSPF
router(config)# router ospf 10
router(config)# network networkadress wildcard area number 
router(config)# network 172.16.10.0 0.0.0.255 area 0




#### Backbone Area

OSPF uses area to divide the network and therefore these large networks are divided into areas. `area0` is the main area to which all the areas are connected to. It sends and allocates all the IPs to the other areas connected. 

#### Normal Area



#### Stub Areas

There are **stub areas**, the branch router will not be having any router of the 

#### Totally Stub Area

#### No-so-stubby Area

# Working of OSPF

OSPF broadcast its LSA (Link state Advertisements) to all the routers in the area, making sure that each router has now developed the same routing table as of network. These LSA information is organised in **LSDB (Link State Database)**.

LSA constains **Router-ID**, **Neighbour-ID**, and **Cost**. In order to establish relationship with the neighbour there need to be sending and recieving *hello* messages, so in OSPF the messages are multicasted on `224.0.0.5` to all the OSPF routers. 

#### Init/Attempt

#### Two way
![alt text](router-id.png)

#### Ex-start

#### Exchange

#### Loading

#### Full


# Configuring OSPF 

Yo can configure the **OSPF** using `router ospf` *process id*, where you can choose the process id and the netowrk command can configured using `network` *subnet* *wildcard-mask* *area* *area-id*. 

*You might ask what is the use of wildcard mask?* Basically **Wildcard mask** improves your flexibility, which allows you to pickup the speicifc nuymber of IPs within the subnet, 




![alt text](loopback-address.png)

In OSPF the **router-id** is priority is assigned based on the **highest of the physical interfaces**. If three are three interface on router, the one will be selected which is the highest of all interface. 

If that interface is down, there could possible scenario where there could be **unreachablility** to that network as it will show that there is no network connection, and network is **down**. Therefore we need to consider configruing the **Loopback address**.

**Loopback** addresses are virtual as it will not affect the overall network once any interface (the one that is highest) has gone **down**. Refer to [working of OSPF](#working-of-ospf) to learn how the relationship is build between the routers. 

#### Configuring the Looback IP

Loopback IP is configured using the **Host-mask**, meaning configure the loopback using `int lo0`, then enter the interface and configure the loopback IP using `ip address 1.1.1.1 255.255.255.255` and `no shut` oto open the interface, here `255.255.255.255` is called the **Host-mask**, as this is how you configure loopback, it tells router that there is network by 1.1.1.1 which is the only IP in the whole network, i.e., `255.255.255.255`.


###  DR (Designated Router) and BDR (backup designated Router)

DR and BDR are the router to wwhich every update will reach out ebfore them getting emshed into the networks, as it would only create the routing loop in order to make the update. 

![alt text](dr-bdr.png)

If you want to make the cahnge in the currect DR and BDR, then either you can go and implement the **highest** loopback address on the router and **second highest** address on the BDR. Thus, all the routers are set on **default priority** and this you can goand change the priority.

*How it handles the recieve and send of the updates?* Basically the **DR** will recieve the update first and after it will send it through `224.0.0.5` to every other OSPF router in the network, but remember the updated are send to the DR and BDR through **`224.0.0.6`**. 

|Priority | Route-ID|
|---------|---------|
|1|5.5.5.5|
|1|4.4.4.4|
|1|3.3.3.3|
|1|2.2.2.2|
|1|1.1.1.1|

Remember that, once the highest router-id disappears, there will be elections for the BDR, such that the BDR will itself become the DR, after it doesn't find any **DR**. This is called Non-Preemption of the DR and BDR.

Once the there will be any new entry, there won't be any change, only that if the DR isn't available, BDR will become the next DR.

# EIGRP


| EIGRP     |OSPF            |
|-----------|----------------|
|Using `224.0.0.10` to multicast the addresses to the EIGRP routers| Using `224.0.0.5` to send updates to routers and `224.0.0.6` for send updates to the **DR** and **BDR**|
|Initially there are only two packets - *Hello*, *Updates* | There are - *Hello*, LSA, DD|
|It uses **RTP (Reliable Transport Protocol)**, works on Transport layer ensure end-to-end connection and retransmission if necessary| |
|In EIGRP calculation, total of five parameteres, **Bandwidth**, **Delay**, **Load**, **Reliability**, and **MTU (Maximum Transmission Unit)** are used| There are only one parameter, i.e., **Bandwidth**|
|Uses **PDM (Protocol Dependent Modules)** which makes it versatile to adopt any network layer protocol and EIGRP will work on that| |
|**Unequal Cost Load balancing**, meaning it will not take the ideal path but the metrices of what it will calculate, unlike the **RIP** which will send equal packets on both the links without metering the traffic and reliability of the path, EIGRP does opposite to RIP, it take notes via it metrices and then distribute data accordingly| |
|Timer for **EIGRP**, it's 5 - 60sec (**1.54Mbps**)|Timer is of 40 sec| 

### Configuration of the EIGRP

COnfigure the RIGRP routing using `router eigrp` *process-id* and then `network` *sub-network*

-  It is also called **Hybrid Routing Protocol**

One feature is called **Auto Summarization**. It 





