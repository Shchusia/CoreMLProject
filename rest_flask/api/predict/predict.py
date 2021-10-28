from flask import request
from flask_restplus import Resource

from rest_flask.api import API, bad_response_model
from rest_flask.utils import good_response  # , bad_response

from .serializers import good_response_recommended_sku, predict_model, predict_query

predict_ns = API.namespace("predict", description="Api to predict.")


@predict_ns.route("/predict", endpoint="predict")
class PredictionModel(Resource):
    @API.expect(predict_query)
    @API.response(200, "Success", good_response_recommended_sku)
    @API.response(502, "Internal Server Error", bad_response_model)
    @API.header("filial_id", "filial_id", required=False)
    def get(self):
        """

        :return:
        """
        code = 200
        # response = dict()
        data = predict_query.parse_args()
        # bad = bad_response_model()
        return good_response(data), code

    @API.expect(predict_model)
    @API.response(200, "Success", good_response_recommended_sku)
    @API.response(502, "Internal Server Error", bad_response_model)
    @API.header("filial_id", "filial_id", required=False)
    def post(self):
        """

        :return:
        """
        code = 200
        # response = dict()
        # data = predict_model
        print(request.json)
        # print(help(predict_model))
        return good_response(request.json), code
