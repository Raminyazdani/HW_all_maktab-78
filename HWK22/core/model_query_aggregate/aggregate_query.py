import json
from datetime import datetime
import bson
from hashlib import sha256

import pymongo.cursor


class AggregateQuery:

    def __init__(self, sort=None, currency=None, time_type=None, user=None, start_time=None, end_time=None):
        self.init_dict = {
            "sort": sort, "currency": currency, "time_type": time_type, "user": user, "start_time": start_time,
            "end_time": end_time}
        self.project = {"$project": {"key": "$createdAt", "value": "$amount", "_id": 0}}
        self.init_project = {
            "$project": {"_id": 0, "createdAt": {"$dateToParts": {"date": "$createdAt"}}, "amount": "$amount"}}

        if sort is None:
            sort = -1
            self.init_dict["sort"] = sort
        self.sort = {'$sort': {'createdAt': sort}}

        self.time_type = time_type
        if self.time_type == None:
            self.init_dict["time_type"] = "none"
            self.time_type = "none"

        self.user, self.match = user, {}
        if user is not None:
            self.match = {"$match": {"merchantId": user}}

        self.start_time = None
        if start_time is not None:
            time_capsule = ["0000", "1", "1", "0", "0", "0", "0"]
            if len(start_time) <= 4 and isinstance(start_time, str):
                start_time = [start_time]
            elif len(start_time) > 4 and isinstance(start_time, str):
                start_time = start_time.split(",")

            for item in start_time:
                time_capsule[start_time.index(item)] = item
            start_time = ",".join(time_capsule)
            self.init_dict["start_time"] = start_time
            self.start_time = datetime.strptime(start_time, "%Y,%m,%d,%H,%M,%S,%f")

        self.end_time = None
        if end_time is not None:
            time_capsule = ["0000", "1", "1", "0", "0", "0", "0"]
            if len(end_time) <= 4 and isinstance(end_time, str):
                end_time = [end_time]
            elif len(end_time) > 4 and isinstance(end_time, str):
                end_time = end_time.split(",")

            for item in end_time:
                time_capsule[end_time.index(item)] = item
            end_time = ",".join(time_capsule)
            self.init_dict["end_time"] = end_time
            self.end_time = datetime.strptime(end_time, "%Y,%m,%d,%H,%M,%S,%f")
        self.currency = "rial"
        if currency is not None:
            self.currency = currency
        self.init_dict["currency"] = self.currency

    def aggregate(self):
        result = []
        if self.user:
            match_user = {"$match": {"merchantId": bson.objectid.ObjectId(self.user)}}
            result.append(match_user)
        if self.start_time:
            match_start = {"$match": {"createdAt": {"$gte": self.start_time}}}
            result.append(match_start)
        if self.end_time:
            match_end = {"$match": {"createdAt": {"$lte": self.end_time}}}
            result.append(match_end)
        if self.time_type:
            if self.time_type != "week":
                result.append(self.init_project)

                time_type_dict = {"year": {"year": "$createdAt.year"},
                                  "month": {"year": "$createdAt.year", "month": "$createdAt.month"},
                                  "day": {"year": "$createdAt.year", "month": "$createdAt.month",
                                          "day": "$createdAt.day"},
                                  "none": {"year": "$createdAt.year", "month": "$createdAt.month",
                                           "day": "$createdAt.day", "hour": "$createdAt.hour",
                                           "minute": "$createdAt.minute",
                                           "second": "$createdAt.second",
                                           "millisecond": "$createdAt.millisecond"}
                                  }

                time_type_project = {"year": {"$concat": [{"$toString": "$_id.year"}]},
                                     "month": {
                                         "$concat": [{"$toString": "$_id.year"}, "-", {"$toString": "$_id.month"}]},
                                     "day": {
                                         "$concat": [{"$toString": "$_id.year"}, "-", {"$toString": "$_id.month"}, "-",
                                                     {"$toString": "$_id.day"}]},
                                     "none": {
                                         "$concat": [{"$toString": "$_id.year"}, "-", {"$toString": "$_id.month"}, "-",
                                                     {"$toString": "$_id.day"}, "-", {"$toString": "$_id.hour"}, "-",
                                                     {"$toString": "$_id.minute"}, "-",
                                                     {"$toString": "$_id.second"}, "-",
                                                     {"$toString": "$_id.millisecond"}]}
                                     }

                group = {"$group": {
                    "_id": time_type_dict[self.time_type],
                    "amount": {"$sum": "$amount"}}}
                result.append(group)

                projecting = {"$project": {"key": time_type_project[self.time_type], "value": "$amount", "_id": 0}}
                result.append(projecting)
            elif self.time_type == "week":
                group = {"$group": {
                    "_id": {"$week": "$createdAt"},
                    "amount": {"$sum": "$amount"}}}
                result.append(group)
                project = {"$project": {"key": "$_id", "value": "$amount", "_id": 0}}
                result.append(project)

        if self.currency == "toman":
            project = {"$project": {"key": 1, "value": {"$divide": ["$value", 10]}}}
            result.append(project)
        sort = {'$sort': {'key': 1}}
        result.append(sort)

        # if self.time_type == "year":
        #     group = {"$group": {
        #         "_id": {"year": {"$year": "$createdAt"}},
        #         "amount": {"$sum": "$amount"}}}
        #     result.append(group)
        #
        # elif self.time_type == "month":
        #     group = {"$group": {
        #         "_id": {"year": {"$year": "$createdAt"},
        #                 "month": {"$month": "$createdAt"}
        #                 },
        #         "amount": {"$sum": "$amount"}}}
        #     result.append(group)
        # elif self.time_type == "day":
        #
        #     group = {"$group": {
        #         "_id": {"year": {"$year": "$createdAt"},
        #                 "month": {"$month": "$createdAt"},
        #                 "day": {"$dateToParts": {"date": "$createdAt"}}
        #                 },
        #         "amount": {"$sum": "$amount"}}}
        #     result.append(group)
        #  project = {"$project": {"createdAt": "$_id", "amount": "$amount", "_id": 0}}
        # result.append(project)
        # result.append(self.sort)
        # result.append(self.project)

        return result

    def __str__(self):
        return str(self.init_dict)

    def dict_self(self):
        return self.init_dict

    def exec_query(self, col, col_cache):
        hash_id = sha256(str.encode(str(self.aggregate()))).hexdigest()
        data = col_cache.count_documents({"hash_id": hash_id})
        if data != 0:
            data = col_cache.find({"hash_id": hash_id})
            for record in data:
                return record["data"]
        data: pymongo.cursor.Cursor = col.aggregate(self.aggregate())
        col_cache.insert_one({"hash_id": hash_id, "data": list(data)})

        return self.exec_query(col, col_cache)
    # initializing flask app
