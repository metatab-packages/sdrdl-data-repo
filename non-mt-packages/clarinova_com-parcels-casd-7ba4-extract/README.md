Parcels, linked to communities and groups by land use. (more...)

San Diego County parcels, from the SANGIS.org shape files, with improved data structure. 

Images
======

The Images zip file includes raster maps, two for each incorporated city, with the Assessor's tax zone -- from the asr\_zone field in the original SANGIS files -- assigned to 10m square cells. Since there are no parcels for roads and other areas, there are two versions of each image. The '-base' version is rasterized directly from the parcels, and has no data over roads and other areas that have an asr_zone of 0.  The '-infill' version fills in cells that have a value of 0 in the '-base' version with the value of the nearest non-zero cell. These files are particularly useful for use with point data that is assigned to streets, where there otherwise would be no values. 


City, District and Community Codes
===================================

In the source datasets ( not included in the repository, but available in the the databundle library ) Four of the fields use custom codes to identify geographic regions: 

  * neighborhood/nbrhood
  * community
  * council
  * city

These fields use [Clarinova Place Codes](https://sandiegodata.atlassian.net/wiki/display/SDD/Clarinova+Place+Codes), 6 character codes that are designed to be memorable and unambiguous. See the [place codes Google spreadsheet](https://docs.google.com/a/clarinova.com/spreadsheet/ccc?key=0AhnSJoCKXnSUdE1SMXVDYzBGYjVXX3kwUkRBUi1NaHc#gid=0) for a list all of the codes. 



Citation
=========

*Name of file*, extracted from clarinova.com-parcels-casd-7ba4. San Diego Regional Data Library. 2013-07-18 http://sandiegodata.org


Terms
=======================

This data is released under the following terms and conditions. [See the SDRDL Disclaimers and Limitations web page for complete details.](http://www.sandiegodata.org/get-data/data-disclaimers-and-limitations/)

This data is based on data from SANGIS, which is subject to its own terms and conditions. See the [SANGIS Legal Notice for details](http://www.sangis.org/Legal_Notice.htm). 

This data is based on data from SANDAG, which is subject to its own terms and conditions. See the [SANDAG Legal Notice for details](http://rdw.sandag.org/m). 




