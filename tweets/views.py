from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Tweet
from .forms import TweetForm
from django.urls import reverse_lazy, reverse
from cloudinary.forms import cl_init_js_callbacks
# make ypur views here


def index(request):
    form = TweetForm(request.POST, request.FILES)
    # if the method is POST
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
    # if the form is valid
        if form.is_valid():

            # yes,save
            form.save()
        # Redirect to home
            return HttpResponseRedirect('/')

        else:

            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())

    tweets = Tweet.objects.all().order_by('-created_at')[:20]
    return render(request, 'tweets.html', {'tweets': tweets, 'form': form})


def delete(request, tweet_id):
    # find post
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.delete()
    return HttpResponseRedirect('/')


def edit(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)

    if request.method == 'POST':
        print("hello world")
        form = TweetForm(request.POST, request.FILES, instance=tweet)
    # if the form is valid
        if form.is_valid():

            # yes,save
            form.save()
        # Redirect to home
            return HttpResponseRedirect('/')

        else:

            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())
    return render(request, 'edit.html', {'tweet': tweet})


def LikeView(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    new_value = tweet.likes + 1
    tweet.likes = new_value
    tweet.save()
    return HttpResponseRedirect('/')
