from django.contrib import admin
from tapmenuapp.models import (
    Restaurant,
    RestaurantImage,
    RestaurantAddress,
    RestaurantMenuImage,
    Category,
    Item,
    ItemImage,
)


class TimeBaseModelAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated')
    list_filter = ('created', 'updated')
    readonly_fields = ('created', 'updated')


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 0


class RestaurantAddressInline(admin.TabularInline):
    model = RestaurantAddress
    extra = 1


class RestaurantMenuImageInline(admin.TabularInline):
    model = RestaurantMenuImage
    extra = 0


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


class RestaurantAdmin(TimeBaseModelAdmin):
    list_display = ('name', 'subdomain', 'show_menu')
    list_filter = ('show_menu',) + TimeBaseModelAdmin.list_filter
    search_fields = ('name', 'subdomain', 'one_liner', 'phone', 'email', 'website')
    inlines = [
        RestaurantImageInline,
        RestaurantAddressInline,
        RestaurantMenuImageInline,
        CategoryInline,
    ]


class RestaurantImageAdmin(TimeBaseModelAdmin):
    list_display = ('restaurant', 'image')
    search_fields = ('restaurant__name', 'restaurant__subdomain',)


class RestaurantAddressAdmin(TimeBaseModelAdmin):
    list_display = ('restaurant', 'street', 'city', 'state', 'zip')
    search_fields = ('restaurant', 'street', 'city', 'state', 'zip')


class RestaurantMenuImageAdmin(TimeBaseModelAdmin):
    list_display = ('restaurant', 'image')
    search_fields = ('restaurant', 'image')


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0


class CategoryAdmin(TimeBaseModelAdmin):
    list_display = ('name', 'restaurant')
    list_filter = ('restaurant',) + TimeBaseModelAdmin.list_filter
    search_fields = ('name', 'description', 'restaurant')
    inlines = (ItemInline,)


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 0


class ItemAdmin(TimeBaseModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',) + TimeBaseModelAdmin.list_filter
    search_fields = ('name', 'description', 'category')
    inlines = (ItemImageInline,)


class ItemImageAdmin(TimeBaseModelAdmin):
    list_display = ('item', 'image')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantImage, RestaurantImageAdmin)
admin.site.register(RestaurantAddress, RestaurantAddressAdmin)
admin.site.register(RestaurantMenuImage, RestaurantMenuImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
