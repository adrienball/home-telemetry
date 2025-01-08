# Notes
The `general.xml` file is an updated version of the same file provided by the deCONZ plugin, in which the following changes were made:

- The following attribute set was added to the `Simple Metering` cluster in order to handle TEMPO attributes:
```
<attribute-set id="0x0100" description="TOU Information Set">
  <attribute id="0x0100" name="Index HCHC/EJPHN/BBRHCJB, Current Summation Delivered (1)" type="u48" access="r" required="m"></attribute>
  <attribute id="0x0102" name="Index HCHP/EJPHPM/BBRHPJB, Current Summation Delivered(2)" type="u48" access="r" required="m"></attribute>
  <attribute id="0x0104" name="Index HCHP/EJPHN/BBRHCJW, Current Summation Delivered(2)" type="u48" access="r" required="m"></attribute>
  <attribute id="0x0106" name="Index HCHP/EJPHPM/BBRHPJW, Current Summation Delivered(2)" type="u48" access="r" required="m"></attribute>
  <attribute id="0x0108" name="Index HCHP/EJPHN/BBRHCJR, Current Summation Delivered(2)" type="u48" access="r" required="m"></attribute>
  <attribute id="0x010A" name="Index HCHP/EJPHPM/BBRHPJR, Current Summation Delivered(2)" type="u48" access="r" required="m"></attribute>
</attribute-set>
```

- The following cluster was added to handle CO2 measurement
```
    <cluster id="0x040D" name="Carbon dioxyde measurement">
      <description></description>
      <server>
        <attribute-set id="0x0000" description="Relative Carbon Dioxyde Information">
          <attribute id="0x0000" name="Measured Value" type="float" access="r" default="0" required="m"></attribute>
          <attribute id="0x0001" name="Min Measured Value" type="float" access="r" required="m"></attribute>
          <attribute id="0x0002" name="Max Measured Value" type="float" access="r" required="m"></attribute>
          <attribute id="0x0003" name="Tolerance" type="float" access="r" required="o"></attribute>
        </attribute-set>
      </server>
      <client>
      </client>
    </cluster>
```

This file is located in `/usr/share/deCONZ/zcl/general.xml`. 
As pointed out in the [deCONZ User Manual](https://www.dresden-elektronik.de/funk/software/deconz.html?file=files/dresden-elektronik/content/downloads/dokumente/funktechnik/deCONZ-BHB-en.pdf), 
in theory one should not update this file but rather provide additional custom XML files in order to extend the ZCLDB.