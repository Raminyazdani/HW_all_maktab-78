import datetime
import json
from core.model_query_aggregate.aggregate_query import AggregateQuery
from core.utils.initial_model import col as col_primary
from core.utils.initial_model import col_cache as col_secondary
import os

from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api, reqparse

x = AggregateQuery(sort=1, time_type="week", start_time=("2021", "2"), end_time=("2022"))

data = x.exec_query(col_primary, col_secondary)

# print(AggregateQuery().aggregate())
# data = col.aggregate(AggregateQuery().aggregate())
# print(*data, sep="\n")

# try:
#     client = MongoClient()
# try:    mongo_cond=False
#            /{file_name}#               print( add data to database)print("Could not initialize Mongo client
#        nt")

#   initializing flask api
app = Flask(__name__)

# try:
#     app = Flask(__name__)
# except:
#     app_cond=False
#     print("Could not initializing flask app")

#  initializing flask api
api = Api(app)


# if app_cond==True:
#     try:
#         api = Api(app)
#     except:
#         api_cond=False
#         print("Could not initialize flask api")

@app.route('/')
def index():  # put application's code here
    return render_template('home.html')


transacrion_args = reqparse.RequestParser()
transacrion_args.add_argument("user", type=str, help="merchant_id is not correct", required=False, default=None)
transacrion_args.add_argument("sort", type=str, help="sort only -1/1", required=False, choices=["1", "-1"],
                              default=None)
transacrion_args.add_argument("currency", type=str, help="currency only rial/toman", required=False,
                              choices=["rial", "toman"], default=None)
transacrion_args.add_argument("time_type", type=str, help="only none,year,month,week,day", required=False, default=None)
transacrion_args.add_argument("start_time", type=str,
                              help="starting time format yyyy-mm-dd-h-m-s-ms or nothing from beggining", required=False,
                              default=None)
transacrion_args.add_argument("end_time", type=str,
                              help="starting time format yyyy-mm-dd-h-m-s-ms or nothing from beggining", required=False,
                              default=None)


class Data(Resource):
    def get(self):
        x = AggregateQuery()
        data = x.exec_query(col_primary, col_secondary)
        print(data)
        return jsonify(data)

    def post(self):
        # req = request.get_json(force=True)
        # print(req)
        # datas = request.form.keys()
        # print(datas)
        # return datas
        data_req = transacrion_args.parse_args()

        if data_req["end_time"] is not None:
            if "-" in data_req["end_time"]:
                data_req["end_time"] = data_req["end_time"].replace("-", ",")
        if data_req["start_time"] is not None:
            if "-" in data_req["start_time"]:
                data_req["start_time"] = data_req["start_time"].replace("-", ",")

        x = AggregateQuery(**data_req)
        data = x.exec_query(col_primary, col_secondary)
        print(data)
        return jsonify(data)


api.add_resource(Data, "/transaction/")

if __name__ == '__main__':
    app.run(debug=True)
