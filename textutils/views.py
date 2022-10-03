# from django.shortcuts import render,HttpResponse


# def index(request):
#     return render(request,'index.html')

# def analyze(request):
#     #Get the text
#     djtext = request.POST.get('text', 'default')


#     # Check checkbox values
#     removepunc = request.POST.get('removepunc', 'off')
#     capsall = request.POST.get('capsall', 'off')
#     newlineremove = request.POST.get('newlineremove', 'off')
#     extraspaceremove = request.POST.get('extraspaceremove', 'off')


#     #Check which checkbox is on
#     if removepunc == "on":
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char

#         params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)

#     if(capsall=="on"):
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed + char.upper()

#         params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # Analyze the text
#         # return render(request, 'analyze.html', params)

#     if(extraspaceremove=="on"):
#         analyzed = ""
#         for index, char in enumerate(djtext):
#             if not(djtext[index] == " " and djtext[index+1]==" "):
#                 analyzed = analyzed + char

#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # Analyze the text
#         # return render(request, 'analyze.html', params)

#     if (newlineremove == "on"):
#         analyzed = ""
#         for char in djtext:
#             if char != "\n" and char!="\r":
#                 analyzed = analyzed + char
#             else:
#                 print("no")
#         print("pre", analyzed)
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

#     if(removepunc != "on" and newlineremove!="on" and extraspaceremove!="on" and capsall!="on"):
#         return HttpResponse("please select any operation and try again")

#     return render(request, 'analyze.html', params)











# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    capsall = request.POST.get('capsall', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    numberremover = request.POST.get('numberremover','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(capsall=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremove=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    
    if(removepunc != "on" and newlineremove!="on" and extraspaceremove!="on" and capsall!="on" and numberremover != "on"):
        # return HttpResponse("<h2>Please select any operation and try again!</h2>")
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')