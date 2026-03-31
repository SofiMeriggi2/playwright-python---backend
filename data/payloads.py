class Payloads:

    @staticmethod
    def new_booking() -> dict:
        return {
            "firstname": "Sofi",
            "lastname": "QA",
            "totalprice": 150,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-06-01",
                "checkout": "2025-06-05"
            },
            "additionalneeds": "Breakfast"
        }

    @staticmethod
    def updated_booking() -> dict:
        return {
            "firstname": "Sofi",
            "lastname": "Updated",
            "totalprice": 200,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2025-07-01",
                "checkout": "2025-07-10"
            },
            "additionalneeds": "Lunch"
        }

    @staticmethod
    def partial_update() -> dict:
        return {
            "firstname": "SofiPatch",
            "totalprice": 999
        }