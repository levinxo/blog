#!/usr/bin/env bash

#add disqus_identifier to posts
for f in `ls content/2*`;
do
    head -n 7 $f | grep "disqus_identifier: "
    if [ $? -eq 1 ];then
        date_ori=`head -n 6 $f | grep "Date: "`
        date=${date_ori#Date: }
        date=`echo $date | sed -e 's/-//g' -e 's/ //g' -e 's/://g'`
        
        sed "s/Date: .*/${date_ori}newlinelinenewdisqus_identifier: ${date}/" $f | sed 's/newlinelinenew/\
/' > $f.new
        mv $f.new $f
    fi
done

#make publish
rm -rf output/
make publish
cp -r output/* webroot/ && rm -rf output/

