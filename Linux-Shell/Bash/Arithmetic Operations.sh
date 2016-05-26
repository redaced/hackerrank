read x
echo "scale=4; $x" | bc | xargs printf '%.3f'