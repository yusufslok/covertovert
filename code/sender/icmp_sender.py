from scapy.all import IP, ICMP, send

destination_ip = "172.18.0.2"

packet = IP(dst=destination_ip, ttl=1) / ICMP()

print("Sending ICMP packet with TTL=1")
send(packet)