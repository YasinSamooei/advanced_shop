from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib import messages

# local
from .forms import ContactForm


class ContactView(CreateView):
    template_name = "contact/contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request, messages.SUCCESS, "your message is successfully saved!"
        )
        return redirect("contact:contact")
