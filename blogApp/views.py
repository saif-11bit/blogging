from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from .models import Blog, Contact, Subscriber, Crousal, UserProfile
from .forms import ContactForm, SubscribeForm
# from django.core.paginator import Paginator



class IndexView(View):

	def get(self, *args, **kwargs):
		form = SubscribeForm()
		context = {
			'blogs': Blog.objects.all()[:8],
			'crousal1': Crousal.objects.first(),
			'crousal2': Crousal.objects.filter()[1:2].get(),
			'crousal3': Crousal.objects.filter()[2:3].get(),
			'form': form,
			'user': UserProfile.objects.first()
		}
		return render(self.request, 'index.html', context)

	def post(self, *args, **kwargs):
		form = SubscribeForm(self.request.POST or None)
		if form.is_valid():
			email = form.cleaned_data['email']
			subscriber = Subscriber.objects.create(email=email)
			return redirect('blogApp:index')


class BlogView(ListView):

	model = Blog
	paginate_by = 10
	template_name = 'blog.html'
	context_object_name = 'blogs'
	


class BlogDetail(DetailView):
	model = Blog
	context_object_name = 'blog_details'
	template_name = 'blogdetails.html'
	


class ContactView(View):
	def get(self, *args, **kwargs):
		form = ContactForm()
		context = {
			'form': form
		}
		return render(self.request, 'contact.html', context)

	def post(self, *args, **kwargs):
		form = ContactForm(self.request.POST or None)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			message = form.cleaned_data['message']

			contact = Contact.objects.create(name=name,email=email,phone=phone,message=message)
			# contact.save()


			return redirect('blogApp:index')

