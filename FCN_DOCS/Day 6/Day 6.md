# Cisco Commands and Concepts

## 1. Setting Hostname
```cisco
hostname HOSTNAME
```
- **Purpose**: Sets the name of the device (router/switch) to identify it in the network.
- **Example**:
  ```cisco
  Router(config)# hostname Sunbeam
  Sunbeam(config)#
  ```

---

## 2. Password Protection in Cisco Devices
### User Mode Passwords
- `console 0` (con 0) → Secures access via the console port.
- `auxiliary 0` (aux 0) → Secures access via the auxiliary port (used for remote access via modem).
- `virtual terminal lines (vty 0 4)` → Secures remote access via Telnet/SSH.

### Privilege Mode Passwords
- `enable secret <password>` → Encrypts the password using MD5 for security.

---

## 3. Viewing Configurations
```cisco
show running-config
```
- Displays the current running configuration stored in RAM.

```cisco
show startup-config
```
- Displays the saved configuration stored in **NVRAM** (used after a reboot).

---

## 4. Copying Configurations
```cisco
copy source destination
```
- Copies configuration files between different locations.

Examples:
```cisco
copy running-config startup-config
```
- Saves the running configuration to **NVRAM**.

```cisco
copy startup-config running-config
```
- Loads the startup configuration into the current running configuration.

```cisco
copy running-config startup-config overwrite startup-config
```
- Overwrites the existing startup configuration with the current running configuration.

---

## 5. Encrypting Passwords
```cisco
service password-encryption
```
- Encrypts all plain-text passwords stored in the configuration.

To disable:
```cisco
no service password-encryption
```

---

## 6. Configuring Console Access
```cisco
line con 0
exec-timeout 0 30
logging synchronous
```
- `exec-timeout 0 30`: Sets the timeout to 30 seconds.
- `logging synchronous`: Prevents log messages from interrupting input.

---

## 7. Configuring Interfaces
```cisco
interface gigabitethernet 0/0
no shutdown
shutdown
ip address 172.16.10.1 255.255.255.0
```
- `no shutdown`: Activates the interface.
- `shutdown`: Disables the interface.
- `ip address`: Assigns an IP to the interface.

---

## 8. Viewing System Information
```cisco
show version
```
- Displays hardware and software information.
- Configuration register (default `0x2102`).

```cisco
show flash
```
- Displays IOS filenames stored in Flash memory.

```cisco
show interfaces
```
- Displays physical and data link layer details.

```cisco
show ip interface brief
```
- Shows summary of IP interfaces.

```cisco
show protocols
```
- Displays protocol status.

---

## 9. Memory Types
| Memory Type | Description |
|------------|-------------|
| **DRAM (Dynamic RAM)** | Stores the running configuration and routing tables. Data in DRAM is lost when the router is powered off or restarted. |
| **NVRAM (Non-Volatile RAM)** | Stores the startup configuration. It retains data even after a reboot, ensuring settings persist. |
| **Flash Memory** | Stores the IOS (Internetwork Operating System) image. It is non-volatile, meaning it keeps the IOS even when the device is restarted. Flash can be erased and rewritten when upgrading the IOS. |
| **ROM (Read-Only Memory)** | Contains a minimal IOS version (ROMMON) used for system recovery. ROM stores the bootloader, which helps initialize hardware and software. |

---

## 10. Password Recovery Steps
1. Restart the router and press `Ctrl + Break`.
2. Enter ROMMON mode: `boot# set ios-conf = 0x2142`.
3. Save and restart: `boot# save`.
4. Router asks for setup (answer `No`).
5. Enter privileged mode: `router>en`.
6. Copy startup to running-config: `router# copy start run`.
7. Enter configuration mode: `router# config t`.
8. Reset the password: `router(config)# enable secret new_password`.
9. Restore configuration register: `router(config)# config-reg 0x2102`.
10. Save the configuration: `router# copy run start`.

---

## 11. Cisco Discovery Protocol (CDP)
```cisco
show cdp neighbors
show cdp neighbors details
```
- Shows connected Cisco devices.

### Disabling CDP
```cisco
no cdp run
```
- Disables CDP globally.

```cisco
interface g0/0
no cdp enable
```
- Disables CDP on a specific interface.

---

## 12. User Management
```cisco
show users
```
- Displays connected users.

```cisco
clear line <line_number>
```
- Disconnects a user.

```cisco
show sessions
```
- Displays active sessions.

To switch sessions: `Shift + Ctrl + 6`, then `x`.

---

## 13. Static Hostname Assignments
```cisco
ip host b 172.xx.xx.xx
ip host c 172.xx.xx.xx
ip host d 172.xx.xx.xx
```
- Assigns static hostnames to IPs.

---

## 14. Configuring DNS Server
```cisco
conf t
ip name-server <DNS_IP>
ip domain-lookup
ip domain-name sunbeam.com
```
- Configures domain name and DNS settings.

To disable domain lookup:
```cisco
no ip domain-lookup
```

---

## 15. Backup and Restore Configuration
### Backup to TFTP
```cisco
copy flash tftp
copy running-config tftp
copy startup-config tftp
```
- Backs up configuration files to a TFTP server.

### Restore from TFTP
```cisco
copy tftp flash
copy tftp running-config
copy tftp startup-config
```
- Restores configuration files from a TFTP server.

---

## Conclusion
This guide covers essential Cisco commands and their explanations. Mastering these commands will help in managing Cisco devices efficiently.


``` 
      //\\            //      //\\      \\            //          
     //  \\          //      //  \\      \\          //                            
    //    \\        //      //    \\      \\        //                         
   //      \\      //      //      \\      \\      //                   
  //        \\    //      //        \\      \\    //                     
 //          \\  //      //          \\      \\  //                    
//            \\//      //            \\      \\//              
```

