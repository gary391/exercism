import xml.etree.ElementTree as ET
import json
xml_string = '<?xml version="1.0"?>\n<locationRequest xmlns="urn:ietf:params:xml:ns:geopriv:held" responseTime="emergencyRouting"><locationType exact="false">geodetic locationURI</locationType><device xmlns="urn:ietf:params:xml:ns:geopriv:held:id"><uri>{"sip_headers":"Via:SIP/2.0/TCP 10.14.14.100;branch=z9hG4bKBroadWorks.-1i2d6pu-10.13.137.244V5060-0-241517110-1545988651-1716322468971-\\r\\nFrom:\\"MEM2 security-desk\\"&lt;sip:+16628519794@amazon.com;user=phone;isup-oli=0&gt;;tag=1545988651-1716322468971-\\r\\nTo:&lt;sip:911@10.13.137.244;user=phone&gt;\\r\\nCall-ID:BW1614289712105241779933246@10.14.14.100\\r\\nCSeq:241517110 INVITE\\r\\nContact:&lt;sip:10.14.14.100;transport=tcp&gt;\\r\\nP-Asserted-Identity:\\"MEM2 security-desk\\"&lt;sip:+16628519794@amazon.com;user=phone&gt;\\r\\nPrivacy:none\\r\\nP-Access-Network-Info:unknown\\r\\nSupported:100rel\\r\\nP-Early-Media:supported\\r\\nAllow:ACK,BYE,CANCEL,INFO,INVITE,OPTIONS,PRACK,REFER,NOTIFY,UPDATE\\r\\nX-BroadWorks-DNC:network-address=\\"sip:+16628519794@amazon.com;user=phone\\";user-id=\\"security-desk@amazon.com\\";sc-user-class=\\"Unclassified\\";sc-priority=21\\r\\nX-BroadWorks-Correlation-Info:73d04786-6c7d-440e-887a-3c334e77629b\\r\\nAccept:application/btbc-session-info,application/media_control+xml,application/sdp,application/x-broadworks-call-center+xml,multipart/mixed,application/x-broadworks-conference-info+xml\\r\\nUser-Agent: PolycomVVX-VVX_150-UA/6.4.1.2280_482567164887\\r\\nP-Private-Network-Indication: 10.229.5.114\\r\\nMax-Forwards:40\\r\\nContent-Type:application/sdp\\r\\nContent-Length:292","mac_ip":"482567164887@10.14.14.100"}</uri></device></locationRequest>\n'
root = ET.fromstring(xml_string)

element1 = root.find("element1")
if element1 is not None:
    print(element1.text) # Output: value1
    print(type(element1.text)) # Output: value1
    uri_text = element1.text
    print(uri_text)
    try:
        uri_json = json.loads(uri_text)
    except Exception as e:
        print(e)
element3 = root.find("element3")
if element3 is not None:
    print(element3.text)
else:
    print("Element 'element3' not found.") # Output: Element 'element3' not found.