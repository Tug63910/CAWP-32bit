from setuptools import find_packages, setup

setup(
	name='CAWPr',
	version='1.0.0'
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'flask',
		'python-dotenv',
		'scrapy',
		'html2text',
		'google-cloud-storage',
		'beautifulsoup4',
		'psycopg2',
	],
)
