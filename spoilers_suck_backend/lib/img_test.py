import requests
import base64

base_url = 'https://api.kairos.com/'
auth_headers = {
        'app_id': '4f9705ff',
        'app_key': 'cb6c0e9a44490714b616a3cb2c0cc803'
    }
    
gallery_const = '1'

def recognize_face(gallery_name, url = None, file = None, additional_args={}):
    payload = build_recognize_payload(gallery_name, url, file,additional_args)
    response = requests.post(base_url+'recognize', json=payload, headers = auth_headers)
    json_response = response.json()

    return json_response

def enroll_face(subject_id, gallery_name, url=None, file = None, base64_image_contents=None, multiple_faces = False, additional_args={}):
    payload = build_enroll_payload(subject_id, gallery_name,url, file, base64_image_contents,multiple_faces, additional_args)
    response = requests.post(base_url+'enroll', json=payload, headers = auth_headers)
    json_response = response.json()

    return json_response

def build_recognize_payload(gallery_name, url, file, additional_args):
    if file is not None:
        image = extract_base64_content(file)
    else:
        image = url
    
    required_fields = {
        'image': image,
        'gallery_name': gallery_name
    }

    return dict(required_fields, **additional_args)

def build_enroll_payload(subject_id, gallery_name, url, file, imgframe, multiple_faces, additional_args):
    if imgframe is not None:
        image = imgframe
    elif file is not None:
        image = extract_base64_content(file)
    else:
        image = url

    required_fields = {
        'image': image,
        'subject_id': subject_id,
        'gallery_name': gallery_name,
        'multiple_faces': multiple_faces
    }

    return dict(required_fields, **additional_args)

def extract_base64_content(image_path):
    with open(image_path, 'rb') as fp:
        return base64.b64encode(fp.read()).decode('ascii')

#add the following data to gallery name
#print enroll_face(file='jon_snow/jon-snow1.jpg', subject_id='Jon Snow', gallery_name='1')
#print enroll_face(file='arya_stark/arya-stark' + str(i)+'.jpg', subject_id='Arya Stark', gallery_name='1')
#print enroll_face(file='cersei_lannister/cersei-lanister' + str(i)+'.jpg', subject_id='Arya Stark', gallery_name='1')
#print enroll_face(file='daenerys_targaryen/daenerys-targaryen' + str(i)+'.jpg', subject_id='Arya Stark', gallery_name='1')
#print enroll_face(file='gregor_clegane/gregor-clegane' + str(i)+'.jpg', subject_id='Arya Stark', gallery_name='1')
#print enroll_face(file='sansa_stark/sansa-stark' + str(i)+'.jpg', subject_id='Arya Stark', gallery_name='1')
#print enroll_face(file='tyrion_lannister/tyrion_lannister' + str(i)+'.jpg', subject_id='Arya Stark', gallery_name='1')


#print recognize_face(url='http://pixel.nymag.com/imgs/daily/vulture/2015/09/15/15-kit-harington-got-snow.w529.h529.jpg', gallery_name='1')
