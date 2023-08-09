import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.getcwd())+"\\config\\config.ini")

class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get('commonData', 'url')
        return url

    @staticmethod
    def get_password():
        password = config.get('commonData', 'password')
        return password

    @staticmethod
    def get_telephone():
        telephone = config.get('commonData', 'telephone')
        return telephone