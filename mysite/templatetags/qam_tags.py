from django import template
from django.utils.safestring import mark_safe
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import reverse

register = template.Library()


@register.simple_tag
def check_favorite(user, site):
    if user.favorites.filter(site=site).exists():
        return mark_safe('<span class="icon-[tabler--heart-filled]"></span>')
    else:
        return mark_safe('<span class="icon-[tabler--heart] self-center"></span>')


@register.simple_tag
def show_favorite(user, site):
    if not user.favorites.filter(site=site).exists():
        return mark_safe('hidden')


@register.simple_tag
def split_list(_list):
    return _list.split(',')


@register.filter
def filter_date(date):
    today = timezone.now().date()
    if date == today:
        return 'اليوم'
    elif date == today - timedelta(days=1):
        return 'الأمس'
    else:
        return date.strftime('%B %d, %Y')


@register.simple_tag
def report_checker(is_staff):
    if is_staff:
        return reverse('site:manager_reports')
    else:
        return reverse('site:user_reports')


@register.simple_tag
def convert_date(date):
    return date.strftime('%H:%M ,%Y-%m-%d')


@register.simple_tag
def report_status_badge(status):
    if status == 'تم حلها':
        return mark_safe('badge-success')
    elif status == 'قيد الإنتظار':
        return mark_safe('badge-warning')
    elif status == 'مغلق':
        return mark_safe('badge-error')
    else:
        return mark_safe('badge-info')
