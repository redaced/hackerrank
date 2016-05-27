read x
sum=0
for i in `seq 1 $x`;
do
	read y
	sum=`expr $sum + $y`
done
echo "scale=4; $sum/$x" | bc | xargs printf '%.3f'