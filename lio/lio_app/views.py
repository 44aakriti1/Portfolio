from django.shortcuts import render, redirect
from .models import Project, Skill
from django.contrib import messages
import requests

def home_view(request):
    # Fetch data from your database
    manual_projects = Project.objects.all().order_by('-id')
    skills = Skill.objects.all()

    # Fetch GitHub Repos
    github_repos = []
    try:
        # Fetching your repos
        response = requests.get("https://api.github.com/users/44aakriti1/repos?sort=updated", timeout=5)
        if response.status_code == 200:
            github_repos = response.json()[:4] # Top 4 latest
    except:
        pass

    if request.method == "POST":
        # Simple logic for contact form
        messages.success(request, "✨ Your message has been sent to Aakriti!")
        return redirect('home')

    context = {
        'projects': manual_projects,
        'skills': skills,
        'repos': github_repos
    }
    return render(request, 'index.html', context)