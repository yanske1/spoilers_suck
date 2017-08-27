import requests
import base64

image_paths = ['jon_snow/jon-snow.jpg', 'jon_snow/jon-snow1.jpg', 'jon_snow/jon-snow2.jpg']
base_url = 'https://api.kairos.com/'
auth_headers = {
        'app_id': '4f9705ff',
        'app_key': 'cb6c0e9a44490714b616a3cb2c0cc803'
    }

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

def detect_face(url=None, file=None, additional_args={}):
    payload = build_payload(url, file, additional_args)
    response = requests.post(base_url+'detect', json = payload, headers = auth_headers)
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

def build_payload(url, file, additional_args):
    if file is not None:
        image = extract_base64_content(file)
    else:
        image = url
    
    required_fields = {
        'image': image
    }

    return dict(required_fields, **additional_args)

def extract_base64_content(image_path):
    with open(image_path, 'rb') as fp:
        return base64.b64encode(fp.read()).decode('ascii')

#print enroll_face(file=image_paths[1], subject_id='Jon Snow', gallery_name='1')

print recognize_face(file=image_paths[2], gallery_name='1')
