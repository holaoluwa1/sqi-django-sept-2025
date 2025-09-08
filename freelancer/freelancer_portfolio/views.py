from django.shortcuts import render

# Create your views here.



def services(request):
    services = ["Web Development", "App Development", "SEO Optimization", "UI/UX Design"]
    return render(request, "freelancer_portfolio/services.html", {"services": services})


def testimonials(request):
    testimonials = {
        "Alice": "Fantastic work! Highly recommend.",
        "Bob": "Delivered my project on time and exceeded expectations.",
        "Charlie": "Very professional and detail-oriented."
    }
    return render(request, "freelancer_portfolio/testimonials.html", {"testimonials": testimonials})

def pricing(request):
    prices = {
        "Web Development": "$500",
        "App Development": "$800",
        "SEO Optimization": "$300",
        "UI/UX Design": "$400"
    }
    return render(request, "freelancer_portfolio/pricing.html", {"prices": prices})


def blog(request):
    blogs = [
        {"title": "How to Scale Your Website", "content": "Tips and tricks to scale effectively."},
        {"title": "Why SEO Still Matters", "content": "SEO is crucial for visibility and growth."}
    ]
    return render(request, "freelancer_portfolio/blog.html", {"blogs": blogs})


def case_studies(request):
    case_studies = [
        {"project": "E-commerce Store", "result": "Increased sales by 40%"},
        {"project": "Startup Website", "result": "Generated 1,000+ signups in 3 months"}
    ]
    return render(request, "freelancer_portfolio/case_studies.html", {"case_studies": case_studies})