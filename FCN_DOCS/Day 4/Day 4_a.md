### Day 4

Revision of all the topics till date was done :- 

#### TCP (Transmission Control Protocol)

TCP is a core protocol of the Internet Protocol Suite. It provides reliable, ordered, and error-checked delivery of data between applications running on hosts communicating via an IP network. Major features of TCP include:

- **Connection Establishment**: Uses a three-way handshake to establish a connection before data transfer.
- **Reliability**: Ensures data is delivered without errors and in the correct order.
- **Flow Control**: Manages the rate of data transmission between sender and receiver.
- **Congestion Control**: Prevents network congestion by adjusting the rate of data transmission.
- **Error Checking**: Uses checksums to verify data integrity.

TCP is widely used for applications that require reliable communication, such as web browsing (HTTP/HTTPS), email (SMTP), and file transfer (FTP).

#### UDP (User Datagram Protocol)

UDP is a simpler, connectionless protocol that is part of the Internet Protocol Suite. It provides a way for applications to send encapsulated raw IP datagrams without establishing a connection. Major features of UDP include:

- **Connectionless**: No need to establish a connection before data transfer.
- **Low Overhead**: Minimal protocol mechanism, resulting in lower latency.
- **Unreliable**: No guarantee of delivery, order, or error checking.
- **No Flow Control**: Does not manage the rate of data transmission.

UDP is suitable for applications where speed is critical and occasional data loss is acceptable, such as video streaming, online gaming, and VoIP (Voice over IP).


| Feature              | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
|----------------------|------------------------------------|------------------------------|
| **Connection Type**  | Connection-oriented (establishes a connection before data transfer) | Connectionless (no prior connection needed) |
| **Reliability**      | Reliable (ensures data is delivered in order and without errors) | Unreliable (no guarantee of delivery, order, or error checking) |
| **Error Checking**   | Uses checksum, acknowledgment, and retransmission | Uses checksum but no acknowledgment or retransmission |
| **Speed**           | Slower due to error checking and retransmission | Faster as it does not ensure delivery or ordering |
| **Overhead**        | High due to connection setup, error checking, and retransmission | Low as there is no connection setup or error correction |
| **Ordering of Data** | Ensures data arrives in the correct order | No order guarantee; data may arrive out of sequence |
| **Flow Control**     | Uses flow control (sliding window, congestion control) | No flow control |
| **Use Cases**       | Used for applications needing reliable communication (e.g., HTTP, FTP, Email) | Used for real-time applications where speed matters (e.g., VoIP, video streaming, gaming) |
| **Header Size**      | Larger (20-60 bytes) | Smaller (8 bytes) |



# PORT No. :  
    A protocol port number is a numerical identifier in networking used to specify a particular process or service on a device. When data is transmitted over a network, it is directed to a specific port number, which ensures that it reaches the correct application or service. For example, web traffic typically uses port 80 for HTTP and port 443 for HTTPS. Port numbers range from 0 to 65535 and are divided into three categories 

    1. **Well-Known Ports (1-1024):** Reserved for common services and protocols (e.g., HTTP, FTP, SMTP).
    2. **Registered Ports (1025-49151):** Assigned by IANA for specific services upon application.
    3. **Dynamic or Private Ports (49152-65535):** Used for private or temporary purposes, often assigned dynamically by the operating system.

    Understanding port numbers is crucial for network configuration, security, and troubleshooting.

        | Protocol | Port Number | Description |
        |----------|-------------|-------------|
        | HTTP     | 80          | HyperText Transfer Protocol, used for web traffic |
        | HTTPS    | 443         | HyperText Transfer Protocol Secure, used for secure web traffic |
        | FTP      | 21          | File Transfer Protocol, used for transferring files |
        | SMTP     | 25          | Simple Mail Transfer Protocol, used for sending emails |
        | IMAP     | 143         | Internet Message Access Protocol, used for retrieving emails |
        | POP3     | 110         | Post Office Protocol version 3, used for retrieving emails |
        | SSH      | 22          | Secure Shell, used for secure remote login and other secure network services |
        | DNS      | 53          | Domain Name System, used for resolving domain names to IP addresses |
        | Telnet   | 23          | Telnet protocol, used for unencrypted text communications |

# TSP - Terminate and Stay Resident
TSR - Terminate and Stay Resident - Basically Background app in the current world 
A Terminate and Stay Resident (TSR) program is a type of computer program used in DOS operating systems that remains in memory after its execution has ended, allowing it to be quickly reactivated. This is similar to background applications in modern operating systems.


# Protocol Numbers

A protocol number is a numerical identifier assigned to each protocol in the network layer of the Internet Protocol Suite. These numbers are used to specify the protocol used in the data portion of the IP datagram. Here are some common protocol numbers:

| Protocol | Number | Description |
|----------|--------|-------------|
| ICMP     | 1      | Internet Control Message Protocol, used for error messages and operational information |
| IGMP     | 2      | Internet Group Management Protocol, used for managing multicast group memberships |
| TCP      | 6      | Transmission Control Protocol, used for reliable, ordered, and error-checked delivery of data |
| UDP      | 17     | User Datagram Protocol, used for simpler, connectionless communication |
| GRE      | 47     | Generic Routing Encapsulation, used for tunneling |
| ESP      | 50     | Encapsulating Security Payload,

```
# Layers And Numbers :- 
+------------------+-------------------------+------------------------+
| **Layer**        | **Identifier Used**      | **Example Values**     |
+------------------+-------------------------+------------------------+
| Application      | (No specific identifier)    | (HTTP, FTP, DNS, etc.) |
| Transport        | Port Number                 | TCP: 80 (HTTP), UDP: 53 (DNS) |
| Network          | Protocol Number, IP Address | ICMP: 1, TCP: 6, UDP: 17 | 
|                  |                             | IP: 192.168.1.1, IPv6: 2001:db8::1 |
| Data Link        | MAC Address                 | 00:1A:2B:3C:4D:5E      |
+------------------+-------------------------+------------------------+
```
# Session Layer

The Session Layer is the fifth layer in the OSI (Open Systems Interconnection) model. It is responsible for establishing, managing, and terminating sessions between two communicating devices. Key functions of the Session Layer include:

- **Session Establishment**: Sets up and synchronizes the session between the communicating devices.
- **Session Maintenance**: Manages the session by handling data exchange and keeping the session active.
- **Session Termination**: Properly closes the session to ensure that resources are released and data is not lost.
- **Dialog Control**: Manages the dialog between two devices, ensuring that data is properly synchronized and that both devices are in agreement on the state of the session.
- **Synchronization**: Provides checkpoints and recovery mechanisms to ensure that data can be accurately reconstructed in case of a failure.

The Session Layer is crucial for applications that require continuous data exchange, such as remote procedure calls (RPCs), video conferencing, and online gaming.


# Relation between Port ID and Session ID

Port ID identifies a specific process or service on a device, while Session ID uniquely identifies a session between two communicating devices. Both are used to manage and route data correctly in network communications.

# LLC and MAC Sublayers in DLL

The Data Link Layer (DLL) in the OSI model is divided into two sublayers: the Logical Link Control (LLC) sublayer and the Media Access Control (MAC) sublayer. Each sublayer has distinct responsibilities in managing data transmission over a network.

## Logical Link Control (LLC) Sublayer

The LLC sublayer is responsible for identifying and encapsulating network layer protocols, and controlling error checking and frame synchronization. Key functions of the LLC sublayer include:

- **Multiplexing**: Allows multiple network protocols to coexist within a multipoint network and be transported over the same network medium.
- **Flow Control**: Manages the rate of data transmission between devices to prevent overwhelming the receiver.
- **Error Control**: Detects and corrects errors that may occur in the data link layer.

## Media Access Control (MAC) Sublayer

The MAC sublayer is responsible for controlling how devices on a network gain access to the medium and permission to transmit data. Key functions of the MAC sublayer include:

- **Addressing**: Uses MAC addresses to uniquely identify devices on a network.
- **Access Control**: Determines when a device can access the network medium to send data, using protocols such as CSMA/CD (Carrier Sense Multiple Access with Collision Detection) and CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance).
- **Frame Delimiting**: Defines the start and end of a frame, ensuring that data is properly framed for transmission.

The LLC and MAC sublayers work together to ensure reliable and efficient data transmission over a network, with the LLC sublayer managing logical link control and the MAC sublayer managing access to the physical medium.


### Frame Encapsulation in the OSI Model

Frame encapsulation is the process of adding headers and trailers to data as it moves down the layers of the OSI (Open Systems Interconnection) model. Each layer adds its own specific information to ensure proper data transmission and delivery. Here is a table that illustrates how a frame gets encapsulated layer by layer in the OSI model:

| **OSI Layer**       | **Encapsulation Unit** | **Header/Trailer Added** | **Description** |
|---------------------|------------------------|--------------------------|-----------------|
| Application Layer   | Data                   | None                     | User data is created and prepared for transmission. |
| Presentation Layer  | Data                   | None                     | Data is translated, encrypted, or compressed. |
| Session Layer       | Data                   | None                     | Sessions are established, managed, and terminated. |
| Transport Layer     | Segment                | Header                   | Transport layer header (e.g., TCP/UDP header) is added. |
| Network Layer       | Packet                 | Header                   | Network layer header (e.g., IP header) is added. |
| Data Link Layer     | Frame                  | Header and Trailer       | Data link layer header and trailer (e.g., MAC address, frame check sequence) are added. |
| Physical Layer      | Bits                   | None                     | Data is converted to bits and transmitted over the physical medium. |

Each layer's encapsulation unit becomes the payload for the next layer, ensuring that all necessary information is included for successful communication between devices on a network.


### Co-Axial Cable

Co-axial cables are a type of electrical cable consisting of a central conductor, an insulating layer, a metallic shield, and an outer insulating layer. They are used for transmitting high-frequency signals with low loss. There are two main types of co-axial cables:

- **Thinnet (10Base2)**: 
    - Also known as Cheapernet.
    - Maximum segment length of 185 meters.
    - Used for short-distance communication.
    - Easier to install and more flexible than Thicknet.

- **Thicknet (10Base5)**:
    - Also known as Standard Ethernet.
    - Maximum segment length of 500 meters.
    - Used for long-distance communication.
    - More rigid and harder to install compared to Thinnet.

### UTP & STP Cables

Unshielded Twisted Pair (UTP) and Shielded Twisted Pair (STP) cables are types of twisted pair cables used for networking. They consist of pairs of wires twisted together to reduce electromagnetic interference.

- **UTP (Unshielded Twisted Pair)**:
    - No additional shielding.
    - More susceptible to electromagnetic interference.
    - Commonly used in Ethernet networks.
    - Categories range from Cat 1 to Cat 8, with higher categories supporting higher data rates.

- **STP (Shielded Twisted Pair)**:
    - Includes additional shielding to reduce interference.
    - More expensive and harder to install than UTP.
    - Used in environments with high electromagnetic interference.

#### Categories of UTP Cable

- **Cat 1**: Used for voice communication (telephone wires).
- **Cat 2**: Supports data rates up to 4 Mbps, used in token ring networks.
- **Cat 3**: Supports data rates up to 10 Mbps, used in early Ethernet networks.
- **Cat 4**: Supports data rates up to 16 Mbps, used in token ring networks.
- **Cat 5**: Supports data rates up to 100 Mbps, used in Ethernet networks. (Current generation)
- **Cat 5e**: Enhanced version of Cat 5, supports data rates up to 1 Gbps.
- **Cat 6**: Supports data rates up to 10 Gbps, used in Ethernet networks.
- **Cat 6a**: Enhanced version of Cat 6, supports data rates up to 10 Gbps over longer distances.
- **Cat 7**: Supports data rates up to 10 Gbps, used in Ethernet networks with additional shielding.
- **Cat 8**: Supports data rates up to 40 Gbps, used in data centers.

The coating mechanism of Shielded Twisted Pair (STP) cables involves several layers designed to reduce electromagnetic interference (EMI) and crosstalk. Here's a breakdown of the components:

Individual Pair Shielding: Each pair of wires within the cable is wrapped in a foil shield. This helps to prevent interference between the pairs.

Overall Shielding: In addition to the individual pair shielding, the entire bundle of twisted pairs is wrapped in an additional layer of shielding. This can be either a foil shield or a braided shield, providing an extra layer of protection against external EMI.

Outer Jacket: The entire cable is then encased in an outer jacket, typically made of PVC or another durable material. This outer layer protects the internal components from physical damage and environmental factors.

The combination of these shielding layers makes STP cables more effective at reducing interference compared to Unshielded Twisted Pair (UTP) cables. However, this also makes STP cables more expensive and harder to install due to their increased thickness and rigidity.
*
BaseBand is half Duplex
Broadband is full duplex *

### Straight-Through and Crossover Cables

Straight-through and crossover cables are types of Ethernet cables used for different networking purposes. Understanding their differences and use cases is essential for setting up a network correctly.

#### Straight-Through Cable

A straight-through cable is used to connect different types of devices. The wiring on both ends of the cable follows the same standard (either T568A or T568B). This type of cable is commonly used for:

- Connecting a computer to a network switch or hub.
- Connecting a router to a network switch or hub.
- Connecting a computer to a router.

#### Crossover Cable

A crossover cable is used to connect similar types of devices directly. The wiring on one end of the cable follows the T568A standard, while the other end follows the T568B standard. This type of cable is commonly used for:

- Connecting two computers directly.
- Connecting two network switches or hubs directly.
- Connecting two routers directly.

#### Wiring Standards

- **T568A**:                                    - **T568B**: 
    - Pin 1: White/Green                            - Pin 1: White/Orange
    - Pin 2: Green                                   - Pin 2: Orange
    - Pin 3: White/Orange                            - Pin 3: White/Green
    - Pin 4: Blue                                    - Pin 4: Blue   
    - Pin 5: White/Blue                              - Pin 5: White/Blue   
    - Pin 6: Orange                                  - Pin 6: Green  
    - Pin 7: White/Brown                             - Pin 7: White/Brown   
    - Pin 8: Brown                                   - Pin 8: Brown   

#### Use Cases

- **Straight-Through Cable**:                   - **Crossover Cable**:     
    - Computer to Switch/Hub                            - Computer to Computer
    - Router to Switch/Hub                              - Switch to Switch
    - Computer to Router                                - Router to Router    

Choosing the correct type of cable ensures proper communication between devices and helps maintain network efficiency.

### PuTTY and Console Port on the Router for Configuration

#### PuTTY

PuTTY is a free and open-source terminal emulator, serial console, and network file transfer application. It supports various network protocols, including SSH, Telnet, rlogin, and raw socket connection. PuTTY is widely used for remote access to servers and network devices.

Key features of PuTTY include:

- **SSH Support**: Provides secure remote login and command execution.
- **Telnet Support**: Allows connection to devices using the Telnet protocol.
- **Serial Console**: Enables connection to devices via serial ports.
- **Session Management**: Saves and manages multiple session configurations.
- **Customizable Interface**: Offers various settings for appearance, behavior, and connection options.

#### Console Port on the Router

The console port on a router is a physical interface used for direct local management and configuration of the device. It allows network administrators to connect to the router using a console cable and a terminal emulator like PuTTY.

Key points about the console port:

- **Direct Access**: Provides direct access to the router's command-line interface (CLI) for initial configuration and troubleshooting.
- **No Network Dependency**: Does not rely on network connectivity, making it useful for out-of-band management.
- **Serial Connection**: Typically uses an RJ-45 or DB-9 connector for serial communication.

#### Configuring a Router Using PuTTY and Console Port

1. **Connect the Console Cable**: Connect one end of the console cable to the router's console port and the other end to the serial port on your computer (or use a USB-to-serial adapter if needed).

2. **Launch PuTTY**: Open PuTTY on your computer.

3. **Configure the Connection**:
    - Select "Serial" as the connection type.
    - Enter the appropriate serial line (e.g., COM1, COM2) and set the speed (usually 9600 baud).
    - Click "Open" to start the session.

4. **Access the CLI**: Once connected, you will see the router's CLI prompt. You can now enter commands to configure and manage the router.

5. **Save Configuration**: After making changes, save the configuration to ensure it persists after a reboot.

Using PuTTY and the console port is an essential method for configuring and managing routers, especially during initial setup or when network access is unavailable.


# DOD Model 
–The DoD (Department of Defense) Model, also called the TCP/IP Model, was created for reliable communication across networks. Unlike the OSI model (7 layers), it has only 4 layers and serves as the backbone of modern networking.

1. Application/Process Layer
This is where users interact with network services. It includes applications and protocols that allow communication, data transfer, and remote access.
🔹 Functions:
    Provides an interface for applications to communicate over the network.
    Ensures proper data formatting and service handling.
🔹 Protocols Used:
    HTTP/HTTPS – Web browsing
    FTP – File transfers
    DNS – Converts domain names to IP addresses
    DHCP – Assigns IP addresses dynamically
    SSH/Telnet – Remote access
    POP3
    Imap
    SMTP

2. Host-to-Host (Transport) Layer
    Ensures reliable or best-effort communication between devices by managing connections and data flow.
🔹 Functions:
    Provides error detection and flow control.
    Uses either reliable (TCP) or unreliable (UDP) transmission.
🔹 Protocols Used:
    TCP (Transmission Control Protocol) – Reliable, connection-oriented communication.
    UDP (User Datagram Protocol) – Fast, connectionless, and used where speed matters (e.g., VoIP, gaming).

3. Internet Layer
This layer ensures data packets are routed across networks, much like the OSI model’s Network Layer (Layer 3).
    🔹Functions:
        Assigns IP addresses to devices.
        Determines the best route for data transmission.
    🔹Protocols Used:
        IP (Internet Protocol) – Addressing and packet delivery.
        ICMP (Internet Control Message Protocol) – Error reporting (used in ping).
        ARP (Address Resolution Protocol) – Resolves IP to MAC addresses.
        RARP (Reverse ARP) – Resolves MAC to IP addresses.
        Bootp
        Proxy ARP

4. Network Access (Physical) Layer
Handles the physical transmission of data between devices and detects errors in transmission.
🔹 Functions:   
    Manages the physical connection between devices (cables, wireless, etc.).
    Detects and corrects transmission errors.
🔹 Components Used:
    Ethernet, Wi-Fi, Fiber Optics – Physical connectivity.
    MAC (Media Access Control) Addresses – Unique hardware identifiers

# *NEtwork LAyer Protocols*

### ARP (Address Resolution Protocol)

    ARP is a protocol used to map an IP address to a physical machine address (MAC address) that is recognized in the local network. It is essential for the proper functioning of IP networking. Key features of ARP include:

    - **IP to MAC Mapping**: Resolves IP addresses to MAC addresses.
    - **Broadcast Request**: Sends a broadcast request to all devices on the network to find the MAC address corresponding to an IP address.
    - **ARP Cache**: Stores recently resolved IP-to-MAC address mappings to reduce network traffic.

### RARP (Reverse Address Resolution Protocol)

    RARP is a protocol used to map a physical machine address (MAC address) to an IP address. It is used primarily by diskless workstations to determine their IP address at boot time. Key features of RARP include:

    - **MAC to IP Mapping**: Resolves MAC addresses to IP addresses.
    - **Server-Based**: Requires a RARP server to respond to requests from clients.
    - **Initialization**: Used during the boot process of diskless workstations.

### BOOTP (Bootstrap Protocol)

    BOOTP is a protocol used to automatically assign an IP address to network devices during the boot process. It is a predecessor to DHCP and provides additional configuration information. Key features of BOOTP include:

    - **IP Address Assignment**: Automatically assigns IP addresses to devices.
    - **Configuration Information**: Provides additional configuration information such as the default gateway and subnet mask.
    - **Static Allocation**: Uses a static allocation of IP addresses, where each device is assigned a specific IP address based on its MAC address.
    - **Relay Agents**: Supports relay agents to forward BOOTP requests across different networks.

    BOOTP is still used in some legacy systems but has largely been replaced by DHCP for dynamic IP address allocation.

### Proxy ARP (Proxy Address Resolution Protocol)

    Proxy ARP is a technique used to enable devices on a network to communicate with each other even if they are on different subnets. It allows a router to respond to ARP requests on behalf of another device, effectively making the devices appear to be on the same subnet. Key features of Proxy ARP include:

    - **ARP Request Handling**: The router responds to ARP requests intended for devices on a different subnet.
    - **Transparent Communication**: Enables seamless communication between devices without requiring changes to their IP configuration.
    - **Network Segmentation**: Useful in scenarios where network segmentation is needed but devices must still communicate as if they are on the same subnet.

    Proxy ARP can be useful in certain network configurations but may introduce security risks and increased ARP traffic, so it should be used with caution.

    ### ICMP (Internet Control Message Protocol)

    ICMP is a network layer protocol used for error reporting and diagnostic functions in IP networks. It is an integral part of the Internet Protocol Suite and is primarily used by network devices, like routers, to send error messages and operational information. Key features of ICMP include:

    - **Error Reporting**: Communicates network-level errors, such as unreachable hosts or network congestion.
    - **Echo Requests and Replies**: Used by the `ping` command to test connectivity between devices.
    - **Time Exceeded Messages**: Indicates that a packet has been discarded because it exceeded its time-to-live (TTL).
    - **Destination Unreachable Messages**: Informs the sender that a destination is unreachable for various reasons (e.g., network, host, protocol, or port unreachable).

    ICMP is essential for network troubleshooting and management, providing valuable information about the status and health of the network.

    | Message Type           | Description                                      |
    |------------------------|--------------------------------------------------|
    | Echo Request (Type 8)  | Sent to request an ICMP Echo Reply (ping request)|
    | Echo Reply (Type 0)    | Sent in response to an ICMP Echo Request (ping reply)|
    | Destination Unreachable (Type 3) | Indicates that a destination is unreachable|
    | Time Exceeded (Type 11)| Indicates that a packet's TTL has expired        |
    | Redirect (Type 5)      | Informs a host of a better route for a destination|

    ICMP messages are encapsulated within IP packets and are used by network administrators to diagnose and resolve network issues effectively.

### Ping and Traceroute

#### Ping

    Ping is a network utility used to test the reachability of a host on an IP network and measure the round-trip time for messages sent from the originating host to a destination computer. It uses the ICMP Echo Request and Echo Reply messages.

    Key features of Ping include:

    - **Connectivity Test**: Checks if a host is reachable.
    - **Round-Trip Time**: Measures the time it takes for a packet to travel to the destination and back.
    - **Packet Loss**: Identifies if any packets are lost during transmission.
    - **TTL (Time to Live)**: Shows the number of hops the packet can take before being discarded.

    Example usage:
    ```sh
    ping www.example.com
    ```

#### Traceroute

    Traceroute is a network diagnostic tool used to track the path that packets take from the source to the destination. It helps identify the route and measure transit delays of packets across an IP network.

    Key features of Traceroute include:

    - **Path Discovery**: Identifies each hop along the route to the destination.
    - **Transit Delays**: Measures the time taken for packets to reach each hop.
    - **TTL Manipulation**: Uses increasing TTL values to discover each successive hop.

    Example usage:
    ```sh
    traceroute www.example.com
    ```

    Both Ping and Traceroute are essential tools for network troubleshooting and performance analysis, providing insights into connectivity and routing issues.
