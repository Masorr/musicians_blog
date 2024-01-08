from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Post, Comment, Profile
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:'blog.post',

    **Context**
    ``post``
        An instance of :model:'blog.Post'.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
    **Template:**
    :template:'blog/post_detail_html'
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = User.objects.get(id=request.user.id)
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete a comment.

    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        The comment to be deleted.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def profile_list(request):
    '''
    Renders a list of user profiles excluding the logged-in user.

    **Context**
    ``profiles``
        QuerySet of profiles excluding the logged-in user, and ordering them.
    ``profile_count``
        The count of profiles excluding the logged-in user.

    **Template:**
    :template:'blog/profile_list.html'
    '''
    profiles = (
        Profile.objects
        .exclude(user=request.user)
        .order_by('user__username')
    )
    profile_count = Profile.objects.exclude(user=request.user).count()
    return render(
        request, 'blog/profile_list.html',
        {'profiles': profiles, "profile_count": profile_count},
    )


def profile(request, pk):
    '''
    Renders the user profile page based on the user's authentication status.

    **Context**
    ``profile``
        The user profile based on the primary key (pk).

    **Template:**
    :template:'blog/profile.html'

    Parameters:
    - request (HttpRequest) = The HTTP request object.
    - pk (int) = The primary key of the user profile to be displayed.
    '''
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=pk)

        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
                messages.error(request, f'You have unfollowed {profile} ')
            elif action == "follow":
                current_user_profile.follows.add(profile)
                messages.success(request, f'You are now following {profile} ')
            current_user_profile.save()

        return render(request, 'blog/profile.html', {'profile': profile})

    messages.success(request, ('You must be logged in to view this profile'))
    return redirect('home')
