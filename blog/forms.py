from django import forms
from .models import Comment, Post, User, Account


class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش'),
    )
    message = forms.CharField(widget=forms.Textarea, required=True)
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11, required=True)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError('شماره تلفن باید عدد باشد!')
            else:
                return phone


class CommentForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            if len(name) < 3:
                raise forms.ValidationError('نام کوتاه است !')
            else:
                return name

    class Meta:
        model = Comment
        fields = ['name', 'body']


# class PostForm(forms.Form):
#     author = forms.CharField(required=True, label='نام کاربری')
#     title = forms.CharField(max_length=250, required=True, label='موضوع')
#     description = forms.CharField(widget=forms.Textarea, required=True, label='متن')
#     # reading_time = forms.DateTimeField(label='زمان مطالعه')
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if title:
#             if len(title) > 250:
#                 raise forms.ValidationError('موضوع بسیار طولانی !')
#             else:
#                 return title
#
#     def clean_description(self):
#         description = self.cleaned_data['description']
#         if description:
#             if len(description) < 250:
#                 raise forms.ValidationError('متن پست بسیار کوتاه است !')
#             else:
#                 return description

    # def clean_author(self):
    #     author = self.cleaned_data['author']
    #     exists = User.objects.filter(username='author').exists()
    #     if exists:
    #         user = User.objects.get(username=author)
    #         return user
    #     else:
    #         raise forms.ValidationError('نام کاربری اشتباه است !')
    #


class PostForm(forms.ModelForm):
    image1 = forms.ImageField(label='تصویر اول')
    image2 = forms.ImageField(label='تصویر دوم')

    class Meta:
        model = Post
        fields = ['title', 'description', 'reading_time']


class SearchForm(forms.Form):
    query = forms.CharField()


# class LoginForm(forms.Form):
#     user_name = forms.CharField(max_length=250, required=True)
#     password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label='repeat password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('پسورد ها مطابقت ندارد!')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['date_of_birth', 'bio', 'job', 'photo']
