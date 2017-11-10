from django.shortcuts import render
from .models import Display, Product, Artist, Image, Categorie


# Create your views here.
def store(request):
    display = Display.objects.all()
    products = Product.objects.all()

    artists = Artist.objects.all()
    images = Image.objects.all()
    categories = Categorie.objects.all()

    context = {
        "display": display,
        "products": products,
        "artists": artists,
        "categories": categories,
        "images": images
    }
    return render(request, 'store1.html', context)


def artistGalleryView(request, slug):
    artist_product = Artist.objects.filter(slug=slug)
    artist = Artist.objects.get(slug=slug)

    display = Display.objects.all()
    products = Product.objects.filter(artist=artist_product)

    context = {
        "artist_product": artist_product,
        "display": display,
        "products": products,
        "artist": artist,
    }
    return render(request, 'ArtistDetailView.html', context)


def DetailedView(request, slug):
    products = Product.objects.get(slug=slug)
    artist_details = Artist.objects.get(artist_name=products.artist)
    print(artist_details.email)
    context = {
        "artist_details":artist_details,
        "products": products
    }
    return render(request, 'DetailedView.html', context)
