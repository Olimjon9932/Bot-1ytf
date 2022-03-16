from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from  .guruh_bilan_ishlash import Guruh
from  .Gr_bilan import Guruh2
if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(Guruh)
    dp.filters_factory.bind(Guruh2)