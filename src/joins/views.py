from django.conf import settings
from django.shortcuts import render, render_to_response, HttpResponseRedirect, Http404
from aPI import run_query
from aPItwo import run_tagging
from stanfordParse import stan_Parse
from resultsStats import run_stats
from django.http import HttpResponse
from django.template import RequestContext
import os


# Create your views here.
from .forms import JoinForm #, EmailForm 
from .models import Join


def search(request):
    context = RequestContext(request)
    result_list = {}
    print type(result_list)

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)
            
    bASE_DIR = os.path.dirname(os.path.dirname(__file__))
    hOME_DIRS = (
    #BASE_DIR+'/templates/',
    os.path.join(bASE_DIR, 'templates', 'home.html'),
    )
    
    #print result_list
    
    #for result in result_list:
    #    print result.summary
        # result['link']
        #print result.summary
        #print type(result_list)
    
    if 'query' in locals():
        presenttitle = result_list[0].get("title")
        senttitle = str(presenttitle)
        #print type(senttitle)
        tagging_result = run_tagging(senttitle) #sends to aPItwo.py to tag the words
        
        parseing_result = stan_Parse(presenttitle)
        
        stats_result = run_stats(result_list)

    
    #print type(result_list)
    
    #return render_to_response('test.html', {'results2': results2}, context_instance = context)
    #return render(request, 'test.html', {'results2': results2} )
    return result_list

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip


#str(user_id)[:11].replace('-', '').lower()
import uuid

def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	#ref_id = '9f16a22615'
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id



def share(request, ref_id):
	#print ref_id
	try:
		join_obj = Join.objects.get(ref_id=ref_id)
		friends_referred = Join.objects.filter(friend=join_obj)
		count = join_obj.referral.all().count()
		ref_url = settings.SHARE_URL + str(join_obj.ref_id)

		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
		template = "share.html"
		return render(request, template, context)
	except:
		raise Http404



def home(request):
	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
	except:
		obj = None

	form = JoinForm(request.POST or None)
	#form = SearchForm(request.POST or None)
        #print form()
        #print form.is_valid()
        
        #test = search(request)
        #print test
        results3 = search(request)
        
        #print test
        
        if form.is_valid():
            new_join = form.save(commit=False)
            search_string = form.cleaned_data['search_string']
            print form.cleaned_data["search_string"]
            new_join_old, created = Join.objects.get_or_create(search_string=search_string)
            
            print new_join_old, created
            if created:
                    new_join_old.ref_id = get_ref_id()
                    # add our friend who referred us to our join model or a related
                    if not obj == None:
                            new_join_old.friend = obj
                    new_join_old.ip_address = get_ip(request)
                    new_join_old.save()
            
            #print all "friends" that joined as a result of main sharer email
            #print Join.objects.filter(friend=obj).count()
            #print obj.referral.all().count()

            #redirect here
            
            return HttpResponseRedirect("/%s" %(new_join_old.ref_id))

	context = {"form": form}
	template = "home.html"
	return render(request, template, {"results3": results3, "form": form})