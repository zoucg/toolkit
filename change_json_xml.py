import json
import xml.dom.minidom
import os

def get_label(json_file_path):
    with open(json_file_path) as f:
        dict = json.load(f)


        return dict

def creat_xml(xml_path, label):
    im_height = label['imageHeight']
    im_width = label['imageWidth']

    doc = xml.dom.minidom.Document()
    root = doc.createElement('anotation')
    doc.appendChild(root)

    node_floder = doc.createElement('folder')
    node_floder.appendChild(doc.createTextNode('VOC2007'))

    node_filename = doc.createElement('filename')
    node_filename.appendChild(doc.createTextNode(label['imagePath']))

    node_source = doc.createElement('source')
    node_database = doc.createElement('database')
    node_database.appendChild(doc.createTextNode('The VOC2007 Dotadataset'))
    node_anotation = doc.createElement('anotation')
    node_anotation.appendChild(doc.createTextNode('PASCAL VOC2007'))
    node_image = doc.createElement('image')
    node_image.appendChild(doc.createTextNode('fickrid'))
    node_fickrid = doc.createElement('fickrid')
    node_fickrid.appendChild(doc.createTextNode('341012865'))

    node_source.appendChild(node_database)
    node_source.appendChild(node_anotation)
    node_source.appendChild(node_image)
    node_source.appendChild(node_fickrid)

    node_ownner = doc.createElement('ownner')
    node_frick = doc.createElement('fickrid')
    node_frick.appendChild(doc.createTextNode('zoucg'))
    node_name = doc.createElement('name')
    node_name.appendChild(doc.createTextNode('zoucg'))
    node_ownner.appendChild(node_fickrid)
    node_ownner.appendChild(node_name)

    node_size = doc.createElement('size')
    node_width = doc.createElement('width')
    node_width.appendChild(doc.createTextNode(str(im_width)))
    node_height = doc.createElement('height')
    node_height.appendChild(doc.createTextNode(str(im_height)))
    node_depth = doc.createElement('depth')
    node_depth.appendChild(doc.createTextNode(str(3)))
    node_size.appendChild(node_width)
    node_size.appendChild(node_height)
    node_size.appendChild(node_depth)

    node_segment = doc.createElement('segmented')
    node_segment.appendChild(doc.createTextNode('0'))

    root.appendChild(node_floder)
    root.appendChild(node_filename)
    root.appendChild(node_source)
    root.appendChild(node_ownner)
    root.appendChild(node_size)
    root.appendChild(node_segment)

    for b in label['shapes']:
        print(b)
        node_object = doc.createElement('object')

        node_name1 = doc.createElement('name')
        node_name1.appendChild(doc.createTextNode(b['label']))
        node_pose = doc.createElement('pose')
        node_pose.appendChild(doc.createTextNode('left'))
        node_truncated = doc.createElement('truncated')
        node_truncated.appendChild(doc.createTextNode('0'))
        node_diffcult = doc.createElement('difficult')
        node_diffcult.appendChild(doc.createTextNode('0'))

        node_bndbox = doc.createElement('bndbox')
        node_x0 = doc.createElement('xmin')
        node_x0.appendChild(doc.createTextNode(str(b['points'][0][0])))
        node_y0 = doc.createElement('ymin')
        node_y0.appendChild(doc.createTextNode(str(b['points'][0][1])))
        node_x1 = doc.createElement('xmax')
        node_x1.appendChild(doc.createTextNode(str(b['points'][1][0])))
        node_y1 = doc.createElement('ymax')
        node_y1.appendChild(doc.createTextNode(str(b['points'][1][1])))
        # node_x2 = doc.createElement('x2')
        # node_x2.appendChild(doc.createTextNode(b['object_box'][4]))
        # node_y2 = doc.createElement('y2')
        # node_y2.appendChild(doc.createTextNode(b['object_box'][5]))
        # node_x3 = doc.createElement('x3')
        # node_x3.appendChild(doc.createTextNode(b['object_box'][6]))
        # node_y3 = doc.createElement('y3')
        # node_y3.appendChild(doc.createTextNode(b['object_box'][7]))
        node_bndbox.appendChild(node_x0)
        node_bndbox.appendChild(node_y0)
        node_bndbox.appendChild(node_x1)
        node_bndbox.appendChild(node_y1)
        # node_bndbox.appendChild(node_x2)
        # node_bndbox.appendChild(node_y2)
        # node_bndbox.appendChild(node_x3)
        # node_bndbox.appendChild(node_y3)

        node_object.appendChild(node_name1)
        node_object.appendChild(node_pose)
        node_object.appendChild(node_truncated)
        node_object.appendChild(node_diffcult)
        node_object.appendChild(node_bndbox)

        root.appendChild(node_object)

    with open(xml_path, 'w') as xf:
        doc.writexml(xf, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


def main():
    label_dir = 'D:\zoucg\data\前视800x800 原始'
    xml_dir = 'D:\zoucg\data\\xml'
    json_file = os.listdir(label_dir)
    json_file = [fi for fi in json_file if fi.endswith('json')]

    for ji in json_file:
        xml_name = ji[:-4] + 'xml'
        json_path = os.path.join(label_dir, ji)
        label = get_label(json_path)
        xml_path = os.path.join(xml_dir, xml_name)
        creat_xml(xml_path, label)

main()
