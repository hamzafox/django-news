from django.http import HttpRequest, HttpResponse


# GET Request to get all articles
def all_topics(request):
    s = request.GET.get('sort')
    if s == None or s == '' or s not in ('recent', 'rated'):
        s = 'recent'
    
    if s == 'rated':
        pass
    elif s == 'recent':
        pass
    else:
        pass

    return HttpResponse('Index Page: List Topics here sorted by most %s' % (s))


# GET Request to get an article by ID
def topic_detail(request, id=0):
    return HttpResponse('Get a Topic with ID = %d' % (id))


# POST Request to submit a Topic
def topic_submit(request):
    if request.method == 'POST':
        return HttpResponse('Submit a new Topic')
    else:
        return HttpResponse('Wrong method')

# POST Request to upvote a Topic
def topic_upvote(request, id=0):
    if request.method == 'POST':
        return HttpResponse('Upvote a Topic with ID = %d' % (id))
    else:
        return HttpResponse('Wrong method')


# POST Request to comment on a Topic
def topic_comment(request, id=0):
    if request.method == 'POST':
        return HttpResponse('Comment on Topic with ID = %d' % (id))
    else:
        return HttpResponse('Wrong method')
