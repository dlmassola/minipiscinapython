from django.shortcuts import render
import random

def generate_shades():
    shades = [
        '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        for _ in range(4)
    ]
    return shades

def table(request):
    shades = generate_shades()
    
    step = 255 / 50
    
    context = {
        'shades': shades,
        "range": [
            "{:02X}".format(int(i * step)) for i in range(50)
        ]
    }
    return render(request, 'ex03/table.html', context)