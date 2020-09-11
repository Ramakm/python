import xml.etree.ElementTree as ET
data = ''' <person>
    <name> chuck</name>
    <phone type=intl"> 192873744</phone>
    <email hide ='yes'/>
</person>'''
parser = ET.XMLParser(encoding="utf-8")
tree = ET.fromstring(data)
print("Name:", tree.find('name').text)
print("Attr:",tree.find('eamil').get('hide'))


