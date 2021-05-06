@echo off
perl bin\pdf2john.pl %1 > temp\%1.hash
python2 bin\configgen.py %1 %2 %3
jtz1.9.0\run\john.exe --fork=4 --format=pdf --pot=temp\%1.pot --session=temp\%1.session --config=temp\%1.conf --extern=pesel temp\%1.hash
jtz1.9.0\run\john.exe --show --format=pdf --pot=temp\%1.pot temp\%1.hash

