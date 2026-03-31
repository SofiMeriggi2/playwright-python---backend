from playwright.sync_api import APIRequestContext, APIResponse


class BookingClient:

    def __init__(self, context: APIRequestContext):
        self.context = context

    def get_all_bookings(self) -> APIResponse:
        return self.context.get("/booking")

    def get_booking(self, booking_id: int) -> APIResponse:
        return self.context.get(
            f"/booking/{booking_id}",
            headers={"Accept": "application/json"}
        )

    def create_booking(self, payload: dict) -> APIResponse:
        return self.context.post(
            "/booking",
            headers={"Content-Type": "application/json"},
            data=payload
        )

    def update_booking(self, booking_id: int, payload: dict, token: str) -> APIResponse:
        return self.context.put(
            f"/booking/{booking_id}",
            headers={
                "Content-Type": "application/json",
                "Cookie": f"token={token}"
            },
            data=payload
        )

    def partial_update_booking(self, booking_id: int, payload: dict, token: str) -> APIResponse:
        return self.context.patch(
            f"/booking/{booking_id}",
            headers={
                "Content-Type": "application/json",
                "Cookie": f"token={token}"
            },
            data=payload
        )

    def delete_booking(self, booking_id: int, token: str) -> APIResponse:
        return self.context.delete(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"}
        )