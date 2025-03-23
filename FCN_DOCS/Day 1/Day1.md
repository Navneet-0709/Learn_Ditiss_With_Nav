# Day 1
# Fundamentals of Computer Networks

* Why Do We Need Connectivity? *

    - Connectivity plays a vital role in today's digital world, enabling data communication, verbal communication, video sharing, and resource sharing across devices. The primary functionality of connectivity is resource sharing, allowing multiple users and devices to access shared resources efficiently.

    - In the 1990s, organizations transitioned from Novell NetWare to Windows-based systems. India alone had about 235 locations migrating to Windows.

* Cisco’s Role: * 
    - While Cisco is facing market challenges, it pioneered switches and routers.
    - It continues investing in R&D to innovate networking solutions.
    - Learning Cisco Router architecture and Cisco IOS is fundamental for network professionals.

* Evolution of Networking * 
    
    - Dumb Terminals & P2P Connections: Early computing relied on dumb terminals with limited processing power, connected via PAD (Packet Assembler/Disassembler) and modems.
    -Rise of Personal Computers (PCs): IBM’s open architecture allowed companies like Intel and Seagate to thrive, leading to affordable personal computers.
    - Early Computing: Initially, Floppy Disk Drives (FDDs) were used to transfer data between computers, which was inefficient and time-consuming.
    - Decentralized Computation Era: Computers were standalone systems with no interconnectivity.
    - Client-Server Technology: Centralized systems were introduced, where multiple users could connect to a single server.
    - Cloud Computing Era: Computing services were categorized into:
        - Infrastructure as a Service (IaaS) – Provides virtualized computing resources.
        - Software as a Service (SaaS) – Cloud-based applications like Office 365.
        - Platform as a Service (PaaS) – Provides a platform for application development.

After that, Cloud Computing, we know it already. 

* Later we got Hub-and-spoke Architecture, clients that were having problems they were able to connect to the server as the server were accessible across different locations
* Though, hub-and-spoke became the most popular choice for the Cloud Infrastructure.
* Client doesn’t connect directly to the other nodes (or say spokes) in the connection.
* The first level of Cloud Computation, Infrastructure as a service, providing virtual servers, scalalibility and flexiblity to adopt as you grow.
* Suppose a MS-Office, on every new version of the MS-Office, as they were to update it on all their systems, so Microsoft came up with Office 365, a cloud based application, providing SaaS.
* Office 365 represented the shift to cloud, where every application was delivered over the cloud.
* Then after that it was Platform as a Service. Where you get all different types of software and carry on with the job you have. 
* Now there is Communication as a service. 
* Some companies also offers the Security of the cloud. It is Security as a service, it is that before the data requested will travel through a inspection, firewalls, IDP (Intrusion Detection and Prevention), and then it will go to it requested destination.



*The question? Answer to whether we can share the micoprocessors? No we can’t*.

# Types of Networks

    - Networks are classified into Local Area Network (LAN) and Wide Area Network (WAN):

    - LAN: If the network is owned and managed internally, it is a LAN.

    - WAN: If the network relies on third-party ISPs, it is a WAN.

Additional network types include:

    PAN (Personal Area Network) – Used for personal devices.

    MAN (Metropolitan Area Network) – Covers a city.

    SAN (Storage Area Network) – Provides high-speed data access for multiple servers.

    VPN (Virtual Private Network) – Ensures secure data transfer over untrusted networks.

Ethernet and MAC Addressing

    - Ethernet: The most common networking technology, ranging from 10 Mbps to 100 Gbps.
    - MAC Address: A unique identifier assigned to network devices by IEEE.
    - CSMA/CD (Carrier Sense Multiple Access with Collision Detection):
        - Detects collisions and resends data using the backoff algorithm.
        - Prevents simultaneous data transmission to reduce data loss.

There are five Super ISPs, when you need to transfer to data over the long distance, you go and take services from the ISPs, then again have the another ISPs whom with they themselves are taking the service from.
* **Tata** has the 45% if shares that has acquired the teleglobe networks to lay down the optical fibre cables.
* A critical part of global infrastructure is **submarine cables**. These cable transfer data at extremely high speed, as it is **Terrabytes per seconds**, connnecting continents and nations.
* Our data is being transferred over sea, once it reaches the Destination, in our case New York, they have their own regional networks that are managed by their ISPs (probably Comcast, or Verizon)



* This uses RAID, Redundant Array of Inexpensive Disk, connecting storage devices to the Network.
* Instead of extracting specific data from each server, we created one single data center that allow the availability of resource to all the multiple servers, i.e., now you don't have to go for a specific server for specific data, instead, you can just go onto the single server that has all the resources.
* This also means that if one server is down, you can anyway access the data from the other servers, because there are multiple servers accessing the same data. So you are not dependent on same server to get data.

Let’s see what is WAN, let’s talk about **Ethernet** and **TokenRing**. You won’t see TokenRing netowrks, mostly Ethernet. 

* IEEE maintains Ethernet standards, and it is an open Technology and anyone can use it.
* It goes from 10Mbps to 100Gbps.
* IBM didn’t thought how visionary the production into the PC or say the PC-DOS was, much profitable, they lost again.
* Ethernet has 10Mbps, which is Metro E, 100Mbps, which is PPPoE, 1Gbps, which is LRE (long range ethernet), then, 10Gbps, which is WLAN.


How Ethernet works? Understand how the data is being transferd, it takes that co-axial cable in order to send data. When a machine is sending data, other machine on the same cable used to recieve it till the conversation comes to end, as it won't accept another streamline of data. Ethernet technology uses **Collision detection**, which detects the data collision and resends the data using **backoff algorithm**.

So, that’s why there was set of rules, or say protocols that was developed by IEEE, they developed **CSMA/CD**.

# Collision Detection and Frame Structure
    Ethernet Collision Detection:
        If multiple devices send data at the same time, a collision occurs.
        The backoff algorithm ensures devices wait before resending data.
    Frame Header and CRC (Cyclic Redundancy Check):
        CRC detects errors in transmitted data.
        Ensures data integrity by recalculating CRC at the destination.

* Basically, CSMA/CD listens to any ongoing transmission of data before sending another data.
* When a device wants to send data, it first listens to see if the network is busy. If the network is clear, it sends the data. 
* However, if two devices sending data simultaneously, a **collision** occurs, and the data is scrambled. Each device then waits a random amount of time before trying again. This is managed by the **backoff algorithm**.

* Every machine has it ’s own backoff timer, and the NIC (with unique identifier).
* All the machines will back off, if there is coliison, they will anyway backoff. This is called **backoff alogithm**, every machine is suppose to wait till the **backoff timer**.
* If the machines shares the same collision domain, then there will be **backoff timer** that will prevent the device from sending data, thus the device has to wait before the channel starts listening again.
* So a machine has to wait for the random amount of time in order to send the data.


Evolution of Network Infrastructure
    Migration from Novel NetWare to Windows (1990s):
        Organizations moved towards Windows-based network solutions.

    Cisco's Contribution:
        Introduced routers and switches to improve networking.
        Investment in R&D continues to advance network security and performance.

VPNs and Secure Communication
    Virtual Private Networks (VPNs):
        Securely connect remote users to networks.
        Use IPSec, OpenVPN protocols with AES/DES encryption.

Storage and Data Access
    Storage Area Network (SAN):
        Provides centralized storage for multiple servers.
        Uses RAID (Redundant Array of Inexpensive Disks) for redundancy.

Data Transmission Challenges
    Electromagnetic Interference (EMI) and Radio Frequency Interference (RFI):
        Can alter data during transmission.
    
    MTU (Maximum Transmission Unit):
        Defines the maximum size of a data frame (64 to 1518 bytes).


Let’s see Unicaset and Braodcast:

* The unicast works as if  two ends are to be communicated
* Another sis BraodCast address, themmachine will see if the mac cddress it not changing, then it said be rereciveving the data.

Once the machine that were communicating , the probability of remaining machine i the waiting state, that number increases, when there are more number of machine. If there are more mahcines, the more backoff timer, the more there will be more, so you can imaginetha tthe more machin will be ther, ther more ther will be wastage of speed, say if the speed is 100Mbps, then say if 100Mbps is wasted. 
In this case there is also a limit of getting redialed, that is avaliability of the media will be the problem, these two drawbacks of the using the ethernet. So it is important to note that the availability ofthe media doesn’t come to a limitation.

* Electromagnetic Interference, this is what makes the changes to the data during the transmission of data. Because this strong magnetic fields changes the bits and bytes of the data, 1 may become 0, 0 may become 1. Same with RFI.
* Second is the siglnals might be weak, due to this, this can cause a problem in bits of data.
* So what does the CRC does? A CRC is going to be mismatch if there is going to be some happering during the transmission of data. So on the destination the calculation of the CRC is recalculated.
* MTU, Maximum transmission units. 
* The frame size could vary between 64 to 1518 bytes.
* Remember that all the calculation happens in the NIC, as it has nothing to do with the Operating system as such or with the processor.


# Key Abbreviations

    - OUI – Organizationally Unique Identifier
    - CSMA/CD – Carrier Sense Multiple Access with Collision Detection
    - MAC – Media Access Control
    - IaaS – Infrastructure as a Service
    - SaaS – Software as a Service
    - PaaS – Platform as a Service
    - IEEE – Institute of Electrical and Electronics Engineers
    - LAN – Local Area Network
    - WAN – Wide Area Network

