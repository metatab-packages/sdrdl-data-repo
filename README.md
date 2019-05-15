# sdrdl-data-repo
Scripts and lists related to the old version of data.sandiegodata.org


Generate the datasets.jsonl file with:

     $ ckanapi dump datasets --all -O datasets.jsonl.gz -z -p 4 -r https://data.sandiegodata.org
     
     
Submit all of the packages to WP:

    $ cd non-mt-packages
    $ for i in `ls`; do mp wp -s testwp -p  $i; done