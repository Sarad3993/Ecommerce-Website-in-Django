from django.shortcuts import render
# for class based views we have to import View
from django.views.generic.base import View
from .models import *


# Function based view 
def contact(request):
    inform = {}  # empty dictionary
    inform['information'] = Information.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        info = Contact.objects.create(
            name=name,
            subject=subject,
            email=email,
            message=message
        )
        info.save()
    return render(request, 'contact.html', inform)



# Till now we created function based views
# now let's create class based views to render the templates
# sano sano app ko lagi chi function based use hunxa(yesma inherit garna mildaina yesko main disadvantage) tara thulo thulo app jasma query haru dherai use hunxa tesma class based view better hunxa (cuz class based view ma OOP use garna painxa)
# there are three types of generic views:  view, detail view(dictionary ko aadhar ma data aayera basxa), list view(list ko aadhar ma data aayera basxa)
# teen ota generic view madhya euta lai chi inherit garnai parxa main class based view ma


# Yo muniko class based view chi value matra declare garna ho
class BaseView(View):  # inheriting generic view
    template_views = {}  # creating empty dictionary
# euta arko kura edi maile yo dictionary aru xuttai different class based view ma use garna chahe bhane majale use garna sakinxa simply by inheriting like as below ( aba tala nai her na dictionary ta BaseView class ko ho ni but use bhako xa HomeView maa)
# yo dictionary each and every time multiple thau ma majale use garna sakixna

# VVI note: edi yo BaseView class lai aru class haru le inherit garxan bhane ta pratyak class ma jj query haru define bhako xa; tyo queries haru chi sabai page le use garna paune bho


# Yo muniko class based view chi html page(in this case index.html) ma gayera value lai view garauna ho
# tesko lagi BaseView class lai yaa inherit garna parxa:
# inherit garna ko main readon chi tyo template_views bhanne dictionary lai aba yaa ma use garxu k
# yesari duita class based view banara garyo bhane code chi nikai xoto hunxa k

class HomeView(BaseView):
    # aba request argument handle garna ko lagi euta get() function banauna parxa
    # request hami user le patahune ho certain content malai access garna paryo hai ; malai tyo content de bhanera; ani tyo request ko  badla ma server le response pathauxa ani tespaxi we are able to see the content of the webpage

    # junsukai view hos request chi jaile ni chinxa
    def get(self,request):  # self parameter is a instance of  class; it represents objects of that class

        # aba hami (query or context variable) haru banam  (bhannale le paila python ma instance varibales banautheu ni ho tei bhanna khojya khas ma)
        # class based view ko lagi chi khali agadi self add garde pugyo aru sab same as function based views
        # here query is written in the form of key : value pair
        # for eg: 'items' is a key jasma Item.objects.all() bhanne value (bhayebhar ko sab item bhanna khojya) gayera basxa
        # yaa naya naya key haru add gardai janu bhaneko mathi ko dictionary bhitra add hudai janu ho ;
        # jaile in templates ma loop lauda use hune bhaneko dictionary ko key or context variable ho ;  

        self.template_views['items'] = Item.objects.all()
        self.template_views['categories'] = Category.objects.all()
        self.template_views['subcategories'] = Subcategory.objects.all()
        self.template_views['slider'] = Slider.objects.all()
        self.template_views['ads'] = Ad.objects.all()
        self.template_views['special_offers'] = Item.objects.filter(special_offer = True)
        # yo filter bhanne function through hami le chaheko anusar ko filtration garna milxa 
        # aba maile models.py ma ta special_offers by default False banako xu tara yaa k garxu bhane tyo special_offers lai True banaidinxu jasle garda special_offers True bhako product matra filter bhayera tya template ma dekhinxa out of all items added 
        # Actual kaam kasari garxa bhane Item bhanne database ma bhako table ma gayera herxa k; ani jun jun item ko special_offers = True xa tyo table ma tyo tyo item lai matra tyo template ma dekhaune kaam garxa 
        

        # aba yo bhaye bhar ko query haru kaa render garne ta bhanda index.html ma render garne ; for that we have to pass that dictionary as an argument
        return render(request, 'index.html', self.template_views)


# Create a new class based view for quick view items: 
# Dictionary xuttai banairana pardaina ; sidai BaseView class lai inherit gardine ; this is the advantage of creating class based views  
class ItemView(BaseView):
    def get(self,request,slug):
        self.template_views['view_items'] = Item.objects.filter(slug=slug)
        # aba jun slug ko value urls ma gako xa tesko item view garna parne xa hamilai ; so we can use filter function for that
        # yo filter function  ma use bhako pailo slug chi mathi url maa as a id aayeko slug ho bhane paxadi ko slug chi item ko database ma bhako slug ho
        # ra yedi yo slug value match bhayesi matra tyo product ko info view garau bhaneko 
        return render(request,'single.html',self.template_views)
        
