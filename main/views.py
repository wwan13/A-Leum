from django.shortcuts import render,get_object_or_404,redirect
from call import models as callmodels
from django.views.decorators.csrf import csrf_exempt
import requests
import random
# , serial


# # Create your views here.
# @csrf_exempt
# def home(request):
#     #URL = 'http://127.0.0.1:8000/' 


#     # ser = serial.Serial("/dev/cu.usbmodem141301", 9600)

#     # print('아두이노 연결 성공')

#     # while True:
#     #     res = None

#     #     try:
#     #         if ser.readable():
#     #         res = ser.readline()
#     #         print(res)
#     #         data = {'data':res}
#     #         #response = requests.post(URL, data=data)


#     #     except serial.serialutil.SerialException:
#     #         print("아두이노 연결 실패")
#     #         break


#     #print(request.POST['date'])
#     return render(request,'main.html')


@csrf_exempt
def home(request):
    file = open('main/textfiles/address.txt', mode='rt', encoding='utf-8')
    addresses = file.readlines()
    randon_index = random.randrange(0,len(addresses))
    my_address = addresses[randon_index]
    lists = callmodels.call.objects.filter(state="대기중")
    if 'data' in request.POST:
        is_private = request.POST['data']
        print(is_private)
        new_call = callmodels.call(
            gender_filter = is_private,
            state = "대기중",
            address = my_address
        )
        new_call.save()
    else:
        is_private = False
    return render(request, "main.html", {'is_private':is_private,'lists':lists})

def get_connect(request,call_id):
    call = get_object_or_404(callmodels.call,pk=call_id)
    call.state = "완료"
    call.save()
    return redirect('')
