from flask_restplus import fields

from rest_flask.api import API

DEFAULT_CNT = 10

predict_query = API.parser()
predict_model = API.model(
    "Prediction",
    {
        "user_id": fields.Integer(
            required=True,
            description="user ID for which the recommendation should be made",
        ),
        "category_ids": fields.List(
            fields.Integer,
            required=False,
            default=list(),
            description="categories to search from them",
        ),
        "cnt": fields.Integer(
            required=False,
            default=DEFAULT_CNT,
            description="number of SKU-s to recommend",
        ),
    },
)

predict_query.add_argument(
    "user_id",
    required=True,
    type=int,
    help="user ID for which the recommendation should be made",
)
predict_query.add_argument(
    "category_ids",
    required=False,
    type=int,
    action="split",
    help="categories to search from them",
    default=list(),
)
predict_query.add_argument(
    "cnt",
    type=int,
    required=False,
    help="number of SKU-s to recommend",
    default=DEFAULT_CNT,
)

predict_result = API.model(
    "PredictResult",
    {
        "value_1": fields.Integer(required=True, description="info about value"),
        "value_2": fields.Integer(required=True, description="info about value"),
    },
)

result_predict = API.model(
    "ResultRecommended",
    {
        "user_id": fields.Integer(
            required=True,
            description="user ID for which the recommendation should be made ",
        ),
        "predict": fields.Nested(predict_result, required=True),
        "category_ids": fields.List(
            fields.Integer,
            required=True,
            description="categories to search from them",
            min_items=0,
        ),
        "cnt": fields.Integer(
            required=True,
            description="number of SKU-s to recommend",
            default=DEFAULT_CNT,
        ),
    },
)
good_response_recommended_sku = API.model(
    "GoodResponsePrediction",
    {
        "status": fields.String(required=True, default="Success"),
        "data": fields.Nested(result_predict),
    },
)
