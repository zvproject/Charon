from itertools import islice
import glob
import os

def get_list_of_footer_social_links(path):
	source_list = []
	source = {}
	with open(path, "r") as file_footer_links:
		line_source = list(islice(file_footer_links, 3))
		n = len(line_source)
		while (n==3):
			source = {
				'name':line_source[0].strip().replace("_",""),
				'src':line_source[1].strip(),
				'href':line_source[2].strip(),
			}
			line_source = list(islice(file_footer_links, 3))
			n = len(line_source)
			source_list.append(source)
	return source_list

def get_projects(path):
	project_list = []
	file_names = glob.glob(os.path.join(path,"project_*"))
	print(os.path.join(path,"project_*"))
	for file_name in file_names:
		with open(file_name, "r") as project_file:
			project_info = {}
			for line in project_file:
				if ':' in line:
					(key, val) = line.split(':')
					project_info[str(key)] = val.strip()
				else:
					project_info[str(key)] += line.strip()
		project_list.append(project_info)
	return project_list

def get_art(path):
	file_names = glob.glob(os.path.join(path,"vz_art.*"))
	project_list = []
	for file_name in file_names:
		(key, name, formats) = file_name.split('.')
		project_info = {}
		project_info['Name'] = name.replace('_', ' ')
		project_info['ImageName'] = 'vz_art.'+name+'.'+formats
		project_list.append(project_info)
	return project_list

def get_text(path):
	with open(path,"r") as file_with_text:
		for line in file_with_text:
			text += line
	return text 

