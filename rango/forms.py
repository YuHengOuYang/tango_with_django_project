#这个页面所有的东西都是要呈现在page上的表格
from django import forms
from rango.models import Page,Category
from django.contrib.auth.models import User
from rango.models import UserProfile



class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
            help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)#事实上这里的代码统统都是override

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)#指定category的name属性将被包含在表格里

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH,help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,help_text="Please enter the URL of the page.")
    #url = forms.URLField(max_length=Page.URL_MAX_LENGTH,help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):#override clean function 
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
                url = f'http://{url}'
                cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values; we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)#因为category是外键，我们不希望它被修改，就排除掉
        # or specify the fields to include (don't include the category field).
        #fields = ('title', 'url', 'views')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)#指定显示这三个，有意思的是上面还对要显示的field做了定义

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)