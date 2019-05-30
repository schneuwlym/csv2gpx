#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import csv
import datetime
import os
import re
from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='    ')


def is_valid_file(file_):
    if not os.path.exists(file_) or type(file_) is not str:
        parser.error('The file %s does not exist!' % file_)
    return file_


def dms2dd(dms):
    tmp = re.findall('(\d+)°([\d\.]+)\'([\d\.]+)\"?([NSWE]{1})', dms)[0]
    dd = int(tmp[0]) + float(tmp[1])/60 + float(tmp[2])/3600
    if tmp[3].upper() in ['S', 'W']:
        dd = -dd
    return "{0:.6f}".format(dd)


def dm2dd(dm):
    tmp = re.findall('(\d+)°([\d\.]+)\'?([NSWE]{1})', dm)[0]
    dd = int(tmp[0]) + float(tmp[1])/60
    if tmp[2].upper() in ['S', 'W']:
        dd = -dd
    return "{0:.6f}".format(dd)


co_format = ['DD', 'DM', 'DMS']


parser = argparse.ArgumentParser(prog='csv2gpx', description='Convert a CSV GPS track into a gpx track')
parser.add_argument('--author', dest='author', type=str, default=None, help='Set the author tag in metadata')
parser.add_argument('--url', dest='url', type=str, default=None, help='Set the url tag in metadata')
parser.add_argument('--file', dest='file', type=is_valid_file, required=True, help='CSV file path')
parser.add_argument('--output', dest='output', type=str, required=True, help='output GPX file')
parser.add_argument('--delimiter', dest='delimiter', type=str, default=',', help='CSV field delimiter')
parser.add_argument('--co-format', dest='format', type=str, default=co_format[0], choices=co_format,
                    help='Change the coordinate format. DD=decimal degrees / DMS=degrees minutes seconds')

args = parser.parse_args()

gpx = Element('gpx')
gpx.set('xmlns', 'http://www.topografix.com/GPX/1/1')
gpx.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
gpx.set('creator', 'csv2gpx')
gpx.set('version', '1.1')
gpx.set('xsi:schemaLocation', 'http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd')

if args.author or args.url:
    metadata = SubElement(gpx, 'metadata')
    if args.author:
        author = SubElement(metadata, 'author')
        author_name = SubElement(author, 'name')
        author_name.text = args.author
    if args.url:
        url = SubElement(metadata, 'link')
        url.set('href', args.url)

with open(args.file, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=args.delimiter)
    trk = None
    trk_name = None
    for row in csv_reader:
        if trk is None or trk_name.text != row['track_name']:
            trk = SubElement(gpx, 'trk')
            trk_name = SubElement(trk, 'name')
            trk_name.text = row['track_name']
            trk_desc = SubElement(trk, 'desc')
            trk_desc.text = row['track_description']
            trk_trkseg = SubElement(trk, 'trkseg')
        trk_trkseg_trkpt = SubElement(trk_trkseg, 'trkpt')
        if args.format == 'DD':
            trk_trkseg_trkpt.set('lat', row['latitude'])
            trk_trkseg_trkpt.set('lon', row['longitude'])
        elif args.format == 'DM':
            trk_trkseg_trkpt.set('lat', dm2dd(row['latitude']))
            trk_trkseg_trkpt.set('lon', dm2dd(row['longitude']))
        elif args.format == 'DMS':
            trk_trkseg_trkpt.set('lat', dms2dd(row['latitude']))
            trk_trkseg_trkpt.set('lon', dms2dd(row['longitude']))
        time = SubElement(trk_trkseg_trkpt, 'time')
        t = datetime.datetime.strptime('{date} {time}'.format(date=row['date'], time=row['time']), '%d.%m.%Y %H:%M:%S')
        cstTimeDelta = datetime.timedelta(hours=int(row['time_delta']))
        tzObject = datetime.timezone(cstTimeDelta)
        t = t.replace(tzinfo=tzObject)
        time.text = t.isoformat()

with open(args.output, mode='w') as output_file:
    output_file.write(prettify(gpx))

print(prettify(gpx))