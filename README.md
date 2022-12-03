# NOID
No Idea - WPA2 packet deauth and injection POC for KCCIS Access Point [SKCIS2]

# NOID exploit explanation

NOID (NO IDea) is an exploit discovered by  the GNAA on November 21, involving the school's WiFi system.

# Why is the GNAA releasing this?
NOID is nearly obsolete now, judging by the school's recent actions to improve WiFi infrastructure. Two access points remain vulnerable to NOID, but the main one switched to a better security protocol, therefore negating most of our methods. Furthermore, TCP-SYN ACK protocols seem to have been buffed in WPA3.

# Kindergarten Explanation

What NOID does is it allows for malicious users and individuals to reroute internet traffic and disconnect (kill) users off of an access point. NOID does this using `pcap`, an open source traffic analysis library. Then, once we have done the complex stuff, and we do a simple network scan to reveal the local MAC addresses of any user, we can kill any user off of the network or reroute network traffic to any website.

# Detailed Explanation
NOID relies on the `deauth` packet. As WPA/2 relies on an encryption key for secure traffic (we call this a 4-way handshake protocol) between multiple nodes, by reinstating an lower yield key with negative int to invoke a deauthenticate packet to a MAC addeess, we.can obtain a handshake key. After that we reuse the same lower yield key and it will refeesh the keystream and in this case, decrypt any SYN-ACK protocol (TCP or UDP). NOID's primary "offensive" force is nicknamed `SLURPR`. Slurpr's primary use is invoke the deauth packet and fire it to a target. Obviously this itself already constitutes to a Denial Of Service attack, however if we want to snoop and modify or spoof DNS or do packet injection, we will have to meddle with the WPA2 keystream itself. Since, we have access fo the new refreshed keystream, we can use it to decrypt and alter TCP SYN-ACK protocols, and inject new packets. One such example is abuse a Newline Injection attack, to alter HTTP headers and send them to any desired website.
The school utilizes a GCMP keystream protocol, which **is** vulnerable to NOID. 

# Components
NOID utilizes a frontend, middleware and backend component.
The frontend is a simple Python interface for sending attacks (SLURPR).The POC code is only found in the backend.
The middleware nicknamed Axon, is as it's name implies, a MAC address and HWID randomizer/spoofer. It also uses a large array of user agents and fake HTTP headers for further testing.
The exploit itself is a modification of a KRACK attack, however it is less intricate and does not require heavy amounts of presets. 
Furthermore, LevelDB, being ran in Lua, utilizes LuaJIT for runtime. Just In Time compilation although is very fast, does not help with refreshing connections. So we do not recommend using `jit`. 
We recommend using either a JSON file or a metatable for storing information, as BoltDB and LevelDB is clearly overkill for such a small project.

# Recorded Info

Currently, both databases now amount to around 2.9 GB each, with over 9,601 lines.
