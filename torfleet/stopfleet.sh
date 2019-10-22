kill $(ps aux | grep 'NewCircuitPeriod' | awk '{print $2}')
kill $(ps aux | grep 'torproxy' | awk '{print $2}')
rm log/*