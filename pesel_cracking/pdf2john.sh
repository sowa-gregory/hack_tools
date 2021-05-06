perl tools/pdf2john.pl "$1" | cut -d":" -f2 | tee temp/"$1".hash

