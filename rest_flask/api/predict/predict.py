from flask import request
from flask_restplus import Resource

from apps import DICT_MODELS
from rest_flask.api import API, bad_response_model
from rest_flask.utils import bad_response, good_response

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
        data = predict_query.parse_args()
        model = DICT_MODELS.get("lgbm")
        if not model:
            code = 401
            response = bad_response(
                code=code, title="Server Error", detail="Not exist model fot predict"
            )
        else:
            response = data
        return good_response(response), code

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
        model = DICT_MODELS.get("random")
        if not model:
            code = 401
            response = bad_response(
                code=code, title="Server Error", detail="Not exist model fot predict"
            )
        else:
            response = request.json
        return good_response(response), code
