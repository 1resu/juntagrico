from juntagrico.entity.subs import SubscriptionPart
from juntagrico.util.models import q_activated, q_cancelled, q_isactive, q_deactivated


class SubscriptionPartDao:

    @staticmethod
    def get_canceled_for_subscription(subscription):
        return SubscriptionPart.objects.filter(subscription=subscription).filter(q_cancelled())

    @staticmethod
    def get_waiting_for_subscription(subscription):
        return SubscriptionPart.objects.filter(subscription=subscription).filter(~q_activated())

    @staticmethod
    def all_active_extrasubscritions():
        return SubscriptionPart.objects.filter(type__size__product__is_extra=True).filter(q_isactive())

    @staticmethod
    def future_extrasubscriptions():
        return SubscriptionPart.objects.filter(type__size__product__is_extra=True)\
            .filter(~q_cancelled() & ~q_deactivated()).filter(deactivation_date=None)

    @staticmethod
    def waiting_extra_subs():
        return SubscriptionPart.objects.filter(type__size__product__is_extra=True).filter(~q_activated())

    @staticmethod
    def canceled_extra_subs():
        return SubscriptionPart.objects.filter(type__size__product__is_extra=True).filter(q_cancelled() & ~q_deactivated())
