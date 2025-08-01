from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')   

def analyze(request):
    djtext = request.POST.get('text', 'default')
    
    # Check CheckBox Values
    removepunc = request.POST.get('removepunc', 'off')
    caps = request.POST.get('fullcaps', 'off')
    nlinerem = request.POST.get('newlinerem', 'off')
    extraspacerem = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charactercount', 'off')
    sample = djtext
    
    # Check which Checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        for i in sample:
            if i not in punctuations:
                analyzed += i
            else:
                continue
        
        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed }
        djtext = analyzed
    
    if caps == "on":
        analyzed = ""
        
        for i in djtext:
            if i.isalpha():
                analyzed += i.upper()
            else:
                analyzed += i
                
        params =  {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed }
        djtext = analyzed
    
    if nlinerem == "on":
        analyzed = ""
        
        for i in djtext:
            if i == '/n' or i == '/r':
                continue
            else:
                analyzed += i
                
                        
        params =  {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed }
        djtext = analyzed
    
    if extraspacerem == "on":
        analyzed = ""
        
        for idx, char in enumerate(djtext):
            if djtext[idx] == " " and djtext[idx + 1] == " ":
                continue
            else:
                analyzed += char
                
        params =  {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed }
        djtext = analyzed
    
    if charcount == "on":
        count = 0
        
        for ch in djtext:
            if ch.isalpha():
                count += 1
                
        params =  {'purpose' : 'Removed Punctuations', 'analyzed_text' : count }
        djtext = analyzed

    if sample == djtext:
         return HttpResponse("Please Choose a valid operation to Continue")     
    else:
         return render(request, 'analyze.html', params)

