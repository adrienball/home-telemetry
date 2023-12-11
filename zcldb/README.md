The `general.xml` file is an updated version of the same file provided by the deCONZ plugin, in which the following 
attribute set was added to the `Simple Metering` cluster in order to handle TEMPO attributes:
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