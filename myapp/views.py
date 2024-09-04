from django.shortcuts import render

# Create your views here.



def index(request):
    
    return render(request,'index.html')

def index_2(request):
    return render(request,'index-2.html')

def index_4(request):
    return render(request,'index-4.html')

def portfolio(request):
    return render(request,'portfolio.html')

def portfolio_2(request):
    return render(request,'portfolio-2.html')

def portfolio_3(request):
    return render(request,'portfolio-3.html')

def portfolio_mesonary(request):
    return render(request,'portfolio-mesonary.html')
    

def portfolio_details(request):
    return render(request,'portfolio-details.html')

def about(request):
    return render(request,'about.html')

def about_me(request):
    return render(request,'about-me.html')

def job(request):
    return render(request,'job.html')

def job_details(request):
    return render(request,'job-details.html')

def product(request):
    return render(request,'product.html')

def product_details(request):
    return render(request,'product-details.html')


def service_1(request):
    return render(request,'service-1.html')


def service_2(request):
    return render(request,'service-2.html')

def service_3(request):
    return render(request,'service-3.html')
    
def service_4(request):
    return render(request,'service-4.html')

def service_details(request):
    return render(request,'service-details.html')

def testimonial(request):
    return render(request,'testimonial.html')

def price(request):
    return render(request,'price.html')

def faq(request):
    return render(request,'faq.html')

def login(request):
    return render(request,"login.html")

def registration(request):
    return render(request,"registration.html")

def e_404(request):
    return render(request,"404.html")

def blog(request):
    return render(request,"blog.html")

def blog_grid_1(request):
    return render(request,"blog-grid-1.html")

def blog_grid_2(request):
    return render(request,"blog-grid-2.html")

def blog_grid_3(request):
    return render(request,"blog-grid-3.html")

def blog_details(request):
    return render(request,"blog-details.html")

def contact(request):
    return render(request,"contact.html")
        
    