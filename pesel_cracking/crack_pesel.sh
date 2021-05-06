
#method 1
hashcat -m 10600 -a 3 ekonto.hash "?d?d?d?d?d?d?d?d?d?d?d"
hashcat -m 10600 -a 3 -O ekonto.hash "?d?d?d?d?d?d?d?d?d?d?d"
hashcat -m 10600 -a 3 -O ekonto.hash pesel_mask1
hashcat -m 10600 -a 3 -O ekonto.hash pesel_mask2
hashcat -m 10600 -a 3 -O ekonto.hash pesel_mask3

hashcat -m 10600 -a 0 -O ekonto.hash out

 