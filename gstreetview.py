import google_streetview.api
import csv
import pandas as pd

parm = []
fields = ["id","lat","lon","tag_number"]

def download_street_view_image():
	df = pd.read_csv('./data/pole_feature.csv',usecols=fields)
	print(df)
	return df
			# parm.append({
			# 	'size': '640x640', # max 640x640 pixels
			# 	'location': f'{row[0]},{row[1]}',
			# 	'heading': '151.78',
			# 	'yaw': '-0.76',
			# 	'key': 'your_dev_key'
			# })

def get_parm():
	return parm