from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ReportForm, ReportReplyForm, UpdateReportStatusForm
from .models import Site, Course, Report, ReportReply
from django.core.mail import send_mail
# Create your views here.


def index(request):
    top_sites = Site.objects.all().order_by("-favorites")

    paginator = Paginator(top_sites, 8)
    try:
        top_sites = paginator.page(1)
    except EmptyPage:
        top_sites = paginator.page(paginator.num_pages)

    context = {
        "top_sites": top_sites
    }

    return render(request, 'mysite/index.html', context)


def sites_list(request):
    sites = Site.objects.all().order_by("-addedAt")

    site_name = request.GET.get("site_name")

    if site_name != '' and site_name is not None:
        sites = sites.filter(name__icontains=site_name)

    paginator = Paginator(sites, 12)
    page = request.GET.get('page')
    try:
        sites = paginator.page(page)
    except PageNotAnInteger:
        sites = paginator.page(1)
    except EmptyPage:
        sites = paginator.page(paginator.num_pages)

    return render(request, 'mysite/sites_list.html', {"sites": sites})


def contact(request):
    form = ReportForm(request.POST or None)
    if request.user.is_authenticated:
        form = ReportForm(request.POST or None, initial={'user_email': request.user.email})
        form.instance.user = request.user

    if form.is_valid():
        form.save()
        return redirect('site:index')

    return render(request, 'mysite/contact.html', {"form": form})


def site_info(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    courses = Course.objects.filter(site=site)
    paginator = Paginator(courses, 6)
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(request, 'mysite/site_info.html', {"site": site, "courses": courses})


@login_required()
def favorites(request):
    sites = Site.objects.all()

    site_name = request.GET.get("site_name")

    if site_name != '' and site_name is not None:
        sites = sites.filter(name__icontains=site_name)

    favorites = request.user.favorites.all()
    paginator = Paginator(favorites, 12)
    page = request.GET.get('page')
    try:
        favorites = paginator.page(page)
    except PageNotAnInteger:
        favorites = paginator.page(1)
    except EmptyPage:
        favorites = paginator.page(paginator.num_pages)

    return render(request, 'mysite/favorites.html', {"sites": sites, "favorites": favorites})


@login_required()
def toggle_favorite(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    favorite, created = request.user.favorites.get_or_create(user=request.user, site=site)

    if not created:
        favorite.delete()
        is_favorite = False
    else:
        is_favorite = True

    return JsonResponse({"is_favorite": is_favorite, "fav_count": site.favorite_by.count()})


@login_required()
def manager_reports(request):
    if request.user.is_staff:
        manager_reports_list = Report.objects.all()
        paginator = Paginator(manager_reports_list, 12)
        page = request.GET.get('page')
        try:
            manager_reports_list = paginator.page(page)
        except PageNotAnInteger:
            manager_reports_list = paginator.page(1)
        except EmptyPage:
            manager_reports_list = paginator.page(paginator.num_pages)

        return render(request, 'mysite/manager_reports_list.html', {"reports": manager_reports_list, "title": "إدارة التقارير"})
    else:
        return redirect('site:reports')


@login_required()
def user_reports(request):
    user_reports_list = Report.objects.filter(user=request.user)
    paginator = Paginator(user_reports_list, 12)
    page = request.GET.get('page')
    try:
        user_reports_list = paginator.page(page)
    except PageNotAnInteger:
        user_reports_list = paginator.page(1)
    except EmptyPage:
        user_reports_list = paginator.page(paginator.num_pages)

    return render(request, 'mysite/user_reports_list.html', {"reports": user_reports_list, "title": "تقاريري"})


@login_required()
def report_info(request, report_id):
    report = Report.objects.get(pk=report_id)
    replies = ReportReply.objects.filter(report=report)
    if request.method == 'POST':
        # change status form section
        status_form = UpdateReportStatusForm(request.POST, instance=report)
        if status_form.is_valid():
            status_form.save()
            return redirect('site:report_info', report_id=report_id)
        # reply form section
        reply_form = ReportReplyForm(request.POST)
        if reply_form.is_valid():
            reply_form.instance.user = request.user
            reply_form.instance.user_email = request.user.email
            reply_form.instance.report = report
            reply_form.save()
            return redirect('site:report_info', report_id=report_id)
    else:
        # reset both forms on load
        reply_form = ReportReplyForm()
        status_form = UpdateReportStatusForm(instance=report)

    return render(request, 'mysite/report_info.html', {"report": report, "replies": replies, "reply_form": reply_form,
                                                       "status_form": status_form})


