from django.shortcuts import render


def testhome(request):
	context = {}
	template = "donotuse.html"
	return render(request, template, context)
#from .forms import EmailForm
#from .models import Join
#
#def get_ip(request):
#    try:
#        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
#        if x_forward:
#            ip = x_forward.split(",")[0]
#        else:
#            ip = request.META.get("REMOTE_ADDR")
#    except:
#        ip = ""
#    return ip
#
#import uuid
#
#def get_ref_id():
#        red_id = str(uuid.uuid4())[:11].replace('-', '').lower()
#        try:
#            id_exists = Join.objects.get(ref_id=ref_id)
#            get_ref_id()
#        except:
#            return ref_id
#
#def home(request):
#    
#    form = EmailForm(request.POST or None)
#    if form.is_valid():
#        new_join = form.save(commit=False)
#        
#        email = form.cleaned_data['email']
#        new_join_old, created = Join.objects.get_or_create(email=email)
#        if created:
#            new_join_old.ref_id = get_ref_id()
#            new_join_old.ip_address = get_ip(request)
#            new_join_old.save()
#        
#
#        
#    context = { "form": form }
#    template = "home.html"
#    return render(request, template, context)