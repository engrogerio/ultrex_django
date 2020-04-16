from django.contrib import admin
from trade.models import Trade 


class DeployMixin:
    def deploy(self, request, queryset):
        # deploy the trade on the server
        for trade in queryset:
            trade.deploy()
            
        rows_updated = queryset.count()

        if rows_updated == 1:
            message_bit = "1 trade was"
        else:
            message_bit = "%s trades were" % rows_updated
        self.message_user(request, "%s deployed." % message_bit)

        #return response

    deploy.short_description = "Deploy the trades"
    
class TradeAdmin(admin.ModelAdmin, DeployMixin): 
    actions = ['deploy']
    list_display = ('id', 'asset', 'amount', 'action', 'duration', 'martingale',
    'martingale_factor', 'start_datetime', 'status')
    readonly_fields = ['status']
    #search_fields = ['asset',]
    list_filter = ['status', 'asset', ]

admin.site.register(Trade, TradeAdmin)



#['amount', 'asset', 'action', 'duration', 'martingale',
#'martingale_factor', 'start_datetime', 'status']