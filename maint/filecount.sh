#! /usr/bin

# get previous count
prev_count=$(cat filecount)
# echo $prev_count
curr_count=$(find ~/public_html -type f | wc -l)
# echo $curr_count
if [ $prev_count != $curr_count ] 	
then
	msg="Previous count $prev_count, current count $curr_count"
	echo $msg | mail -s "Bluehost File Count Alert" dsikar@gmail.com
fi

# Save current count
find ~/public_html -type f | wc -l >> ~/public_html/filecount
