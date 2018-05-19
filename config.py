import os

class Config:
	# Flask form key
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-yes-two-hello-wireless'

	# Mysql credentials
