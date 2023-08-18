from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myblog.accounts"


    def ready(self):
        import myblog.accounts.signals

    