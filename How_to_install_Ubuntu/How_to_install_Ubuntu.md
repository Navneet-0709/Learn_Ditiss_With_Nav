# How to install Ubuntu as Dual Boot OS 

 - First take BAckuo of your Important Data 
 - To know your System Capabilities
 - Create a Swap Area
#       swap Area
            - Virtual Memory 
            - Exension of main memory(RAM)
            - When a computer is low on RAM, it temporarily moves data from RAM to a storage device like a hard drive or SSD. 
            - This frees up RAM so that the computer can run more programs at once. 
            - The OS manages virtual address spaces and assigns real memory to virtual memory.

 - we have to create ubuntu root partition 
 - before that we have to create a partition in our computer system to for ubuntu 
  #         how to do it 
                - click on start 
                - search disk management 
                -  can be done by shrinking the volume or by unallocating the free disk 
                
- turn off bitlocker 
- check whether the partition style is GPT or MBR
- check what booting style is UEFI Unified Extensible firware Interface or Legacy
    - by checking the EFI on disk 
    - or by clicking the system info - bios mode 
- boot the Machine and open the bios MAybe by clicking on function key depends on ur system eg - f1,f12,ESc,etc 
- check this on google
- open bios and open Hyper V i,e Virtualisation or VT-d
- Go to Boot menu
- turn off the secure boot 
- Set the boot option priority coz that will help us the most with which do we want to install 
- Change the Boot Device control to UEFI not to legacy 
- MAke a bootable Pendrive with UBUNTU LIVE ISO CD FILE 
- Now save the changes 
- and now boot the syystem it will automatically boot with the USB
- System is now booted and we have to start installing the system not try just install """ Kar na Chup chaaap ""
- Click on Normal Installation 
- check on install thisd party software
- Click on Something else 
- select the free space u created in the starting 
- give 2gb means 2048 mb as swap area 
- select the free space and type of new partition as primary 
- use as EXt4 journaling file system 
- boot as root
- Click on install and double check everything coz things can not be returned from here 
- Give all the names and Passwords 
- let the installation happen and reboot the suystem 


# In Short 
'''
1. - bitlocker off
2. - disk style basic
3. - unallocate space - 100gb
4. - delete drisk drive or shrink
5. - Partition style - gpt 
6. - Booting style - UEFI 
7. - reboot it and go to the bios 
8. - open bios and open Hyper V i,e Virtualisation or VT-d *Very Imp
9. - turn off the secure boot
10 - go to boot option priority and make usb as priority  
11 - Boot Device control to UEFI not to legacy 
12 - MAke a bootable Pendrive with UBUNTU LIVE ISO CD FILE 
13 - Now save the changes 
14 - and now boot the syystem it will automatically boot with the USB
15 - click enter and start installing ubuntu not on Try " Kar na Chup Chaaap try ku krna h "
16 - Normal Installation krlena zyada Pradhaan mat banna 
17 - install third party software waali sabse lambi line jo padhne ka mn nhi hoga usko check kr dena
18 - installation type me pehle do waale  nhi krne sab khatam ho jaayega 
19 - Click on Something else 
20 - select the free space u created in the starting 
21 - give 2gb means 2048 mb as swap area 
22 - click on free space 
23 - give type as ext4
24 - give names and password (PAssword daal dena Secuity ke ho)
25 - let the installation happen 
26 - After Installation reboot the System
27 - click on Ubuntu 
28 - beech ka nhi pata 
29 - jab aaye to ho gya tha install 
30 - fir sir ne thoda or gyaaan diya 
31. break of 30 min and now gyaaan ctnd 
'''

# Miscellenious 
-- Firmware are the programs which are fixed inside the hardwares 
-- they contains the basic device drivers
-- USB Controllers: - 
    UHCI    USB 1.0
    OHCI    USB 1.1
    EHCI Enhanced Host Controller Interface 2.0 
    XHCI extended Host Controller Interface 3.0 +0
-- diff between GPT and MBR
```
        *MBR                                                                     *GPT

    - Old Style Partitioning                            |   - mordern Partitioning      
    - MAX Disk Size = 2TB                               |   - MAX Disk size = 8ZB
    - MAX partitions =  4                               |   - MAx Parts = 128
    - All were Primary Partitions                       |   - Each PArtition is Assingned with a unique number 
    - For more partitions -                             |   - GUID - Globally Unique ID (GPT) 
       - you convert one as extended partition          |    
       - Can Create Multiple Logical PArtitions in it   |

```
-- diff between UEFI and Legacy
Boot/BIOS mmode - UEFI and LEGACY
```






```
# Hard disk name convention 
what is SD - SATA DISK 
        - two type of HArdDisk  
            - PATA HD - Parallel ATA
            - SATA HD - Serial ATA
ATA - AT Attachment 
AT - Advanced Technology 
NVME - Non Volatile Memory Express
first Computer 1980s IBM + MS
