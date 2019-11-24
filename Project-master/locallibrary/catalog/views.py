from django.shortcuts import render

import csv
import pandas as pd

# Create your views here.

def post_list(request):
    return render(request, 'post_list.html', {})


def koty(request):
    print('About')
    return render(request, 'koty.html', {})



def analiza(request):
    return render(request, 'analiza.html', {})

def zdj(request):
    original = cv2.imread("dog.jpg")
    duplicate = cv2.imread("images/dog2.jpg")
    if original.shape == duplicate.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    cv2.imshow("Original", original)
    cv2.imshow("Duplicate", duplicate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
