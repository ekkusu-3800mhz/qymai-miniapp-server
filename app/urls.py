"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
import app.views.init_data as initData
import app.views.shop as shop
import app.views.queue as queue
import app.views.bot as bot


urlpatterns = [
    #path("init/", initData.InitData.as_view()),
    path("shop/list", shop.ShopList.as_view()),
    path("shop/info", shop.ShopInfo.as_view()),
    path("shop/cabinet", shop.CabinetInfo.as_view()),
    path("queue/list", queue.CabinetList.as_view()),
    path("queue/info", queue.CabinetInfo.as_view()),
    path("queue/update", queue.UpdatePlayer.as_view()),
    path("bot/queue/maimai", bot.MaimaiCabinetList.as_view()),
    path("bot/queue/chunithm", bot.ChunithmCabinetList.as_view()),
    path("bot/queue/update", bot.UpdatePlayer.as_view()),
]
