from django.shortcuts import render
from call import models as callmodels
from django.views.decorators.csrf import csrf_exempt
import requests
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
    lists = callmodels.call.objects.all()
    if 'data' in request.POST:
        is_private = request.POST['data']
        print(is_private)
        new_call = callmodels.call(
            gender_filter = is_private,
            state = "대기중"
        )
        new_call.save()
    else:
        is_private = False
    return render(request, "main.html", {'is_private':is_private,'lists':lists})
