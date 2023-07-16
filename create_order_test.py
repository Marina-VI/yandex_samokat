import sender_stand_request
import data

def send_order_request():
    return sender_stand_request.create_order(data.order_data)

def get_track_number():
    return sender_stand_request.currently_track(send_order_request())

def get_order():
    return sender_stand_request.order_info(get_track_number())

#Старт тестов

def test_user_send_order():
    send_request = send_order_request()

    assert send_request.status_code == 201

def test_track_number_created():
    track_number = get_track_number()

    assert isinstance(track_number, (int, float)), "Ответ получен в не верном формате"

def test_view_user_order():
    order_info = get_order()

    assert order_info.status_code == 200


