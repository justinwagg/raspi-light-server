import os

class Config:
	# Flask form key
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-yes-two-hello-wireless'

	# Mysql credentials
	MYSQL_USER = os.environ.get('MYSQL_USER')
	MYSQL_PASS = os.environ.get('MYSQL_PASS')
