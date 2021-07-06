from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from .forms import *
import random

# Create your views here.



def index(request):
    return render(request, 'index.html')

def bingo_list(request):
    bingo = {
        "b_list" : ['B1', 'B2' ,'B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','B16','B17','B18', 'B19' ,'B20'],
        "i_list" : ['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','I14','I15','I16','I17','I18','I19','I20'],
        "n_list" : ['N1','N2','N3','N4','N5','N6','N7','N8','N9','N10','N11','N12','N13','N14','N15','N16','N17','N18','N19','N20'],
        "g_list" : ['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16','G17','G18','G19','G20'],
        "o_list" : ['O1','O2','O3','O4','O5','O6','O7','O8','O9','O10','O11','O12','O13','O14','O15','O16','O17','O18','O19','O20'],
    }
    return render(request, bingo_list)

def bingo(request):
    return render(request, 'bingo.html')

def char(request):
    form = CharacterForm()
    character = Character.objects.create(
        name=request.POST['name'],
        affiliation=request.POST['affiliation'],
        char_pic=request.POST['char_pic'],
        char_desc=request.POST['char_desc'],
        char_quotes=request.POST['char_quotes'],
    )
    return redirect(f"/bingo/")

# gridSize = 5
# minNum = 1  # Minimum number for each column
# maxNum = 20  # Max number for each column
# cards = 2  # Two cards made for now

# allCards = []  # List of all cards generated
# randRange = range(minNum, maxNum+1)  # Might want maxNum = 20
# for h in range(cards):  # Generates cards
#     newCard = []  # New card that will be filled in
#     # Loop through each column (B, I, N, G, O usually)
#     for i in range(gridSize):
#         # Generate numbers for that column
#         # Generate 5 (or gridSize) random numbers
#         newCard.append(random.sample(randRange, gridSize))
#     allCards.append(newCard)  # Add this newly generated card

# print(allCards)
