import requests


class PicPay(object):

    _URL = "https://appws.picpay.com/ecommerce/public/"

    def __init__(self, x_picpay_token, x_seller_token):
        self._x_picpay_token = x_picpay_token
        self._x_seller_token = x_seller_token

    def _get_url(self, path):
        return f"{self._URL}{path}"

    def _get_headers(self):
        return dict(
            "x-picpay-token"=x_picpay_token,
            "x-seller-token"=x_seller_token
        )