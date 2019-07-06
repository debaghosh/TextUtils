# I have created this file- Tanya


from django .http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('Home')
    #params={'name':'tanya','place':'moon'}, dictionaries used as the third argument
    return render(request, 'index.html')


def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    #Check check box values
    removepunc = request.POST.get('removepunc', 'off') #shows whether the check box is on or not
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=" "
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        params={'purpose':'Removed Punctuations','analyzed_text': analyze}
        #return render(request, 'analyze.html', params)
        djtext=analyze
    if(fullcaps=="on"):
        analyze= " "
        for char in djtext:
            analyze = analyze + char.upper()

        params={ 'purpose':'Capitalize text','analyzed_text': analyze}
        #return render(request, 'analyze.html', params)
        djtext = analyze

    if(newlineremover=="on"):
        analyze = " "
        for char in djtext:
            if char != "\n" and char !="\r" in djtext:
                analyze = analyze + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyze}
        #return render(request, 'analyze.html', params)
        djtext = analyze

    if (extraspaceremover == "on"):
        analyze = " "
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index + 1]==" "):
                analyze = analyze + char

        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyze}
        #return render(request, 'analyze.html', params)
        djtext = analyze

    if (charcount == "on"):

        count=0
        for char in djtext:
            if char != " ":
                count+=1
        analyze=count

        params = {'purpose': 'Count Characters', 'analyzed_text': analyze}
        #return render(request, 'analyze.html', params)
        djtext = analyze

    if(removepunc!="on" and fullcaps!="on" and extraspaceremover!="on" and newlineremover!="on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)



def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')
