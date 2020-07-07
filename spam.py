# in command line, run python spam.py
#this will not work because I removed the url of the page I messed with 


import requests 
import os 
import random 
import string 
import json 

url = 'hideen url so that nobody can see who I was messing with'
Session = requests.Session()

requests.post(url, data = {
    'et_pb_contact_name_1': 'Ur Mom', 
    'et_pb_contact_phone_1': '1232345',
    'et_pb_contact_company_name_1': 'adfg',
    'et_pb_contact_company_type_1': 'hfdg',
    'et_pb_contact_email_1': 'vsdf@gmail.com',
    'et_pb_contact_web_address_1': 'urmom.com',
    'et_pb_contact_information_1': 'heyo' ,
    'et_pb_contactform_submit_0': 'et_contact_proccess',
    # et_pb_contactform_validate_0': true',
    'et_pb_contact_captcha_0': '20'
    })

result = Session.post(url, data = {
    'et_pb_contact_name_1': 'Ur Mom', 
    'et_pb_contact_phone_1': '1232345',
    'et_pb_contact_company_name_1': 'adfg',
    'et_pb_contact_company_type_1': 'hfdg',
    'et_pb_contact_email_1': 'vsdf@gmail.com',
    'et_pb_contact_web_address_1': 'urmom.com',
    'et_pb_contact_information_1': 'heyo' ,
    'et_pb_contactform_submit_0': 'et_contact_proccess',
    'et_pb_contactform_validate_0':'',
    'et_pb_contact_captcha_0': '23',
    '_wpnonce-et-pb-contact-form-submitted': 'b8e419d0ff', 
    '_wp_http_referer': '/brand-registration/',
    'et_pb_contact_email_fields_0': '[{"field_id":"et_pb_contact_name_1","original_id":"name","required_mark":"required","field_type":"input","field_label":"Name"},{"field_id":"et_pb_contact_phone_1","original_id":"phone","required_mark":"required","field_type":"input","field_label":"Phone Number"},{"field_id":"et_pb_contact_company_name_1","original_id":"company_name","required_mark":"required","field_type":"input","field_label":"Company"},{"field_id":"et_pb_contact_company_type_1","original_id":"company_type","required_mark":"required","field_type":"input","field_label":"Type of Company"},{"field_id":"et_pb_contact_email_1","original_id":"email","required_mark":"required","field_type":"email","field_label":"Email Address"},{"field_id":"et_pb_contact_web_address_1","original_id":"web_address","required_mark":"required","field_type":"input","field_label":"Web Address"},{"field_id":"et_pb_contact_information_1","original_id":"information","required_mark":"required","field_type":"text","field_label":"Other Information"}]',
    'et_pb_contact_email_hidden_fields_0': [""]
    })


print(result.status_code)




