from itertools import islice

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
