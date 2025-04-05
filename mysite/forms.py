from django import forms
from .models import Report, ReportReply

# Create your forms here.


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['category', 'title', 'user_email', 'content']
        labels = {'category': 'نوع التقرير', 'title': 'عنوان التقرير', 'user_email': 'البريد الإلكتروني', 'content': 'محتوى التقرير'}


class UpdateReportStatusForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['status']


class ReportReplyForm(forms.ModelForm):
    class Meta:
        model = ReportReply
        fields = ['content']
        labels = {'content': 'محتوى الرد'}
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2})
        }


