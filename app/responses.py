class Responses:
    @staticmethod
    def get(status_code, message, data, error):
        return {
            "status_code": status_code,
            "message": message,
            "data": data,
            "error": error
        }

responses = Responses()