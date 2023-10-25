import threading


def tenant_db_from_the_request(request):
    hostname = request.headers.get("X-Tenant-Id")
    tenants_map = get_tenants_map()
    db = tenants_map.get(hostname)
    return db


def get_tenants_map():
    return {
        "one": "default",
        "two": "db_two",
        "three": "db_three",
        "four": "db_four",
        "five": "db_five",
        "six": "db_six",
        "seven": "db_seven",
        "eight": "db_eight",
        "nine": "db_nine",
        "ten": "db_ten",
    }


# ----------------------------------- #

Thread_Local = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = tenant_db_from_the_request(request)
        setattr(Thread_Local, "DB", db)
        response = self.get_response(request)
        return response


def get_current_db_name():
    return getattr(Thread_Local, "DB", None)


def set_db_for_router(db):
    setattr(Thread_Local, "DB", db)


# ----------------------------------- #


class TenantRouter:
    def db_for_read(self, model, **hints):
        return get_current_db_name()

    def db_for_write(self, model, **hints):
        return get_current_db_name()

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_syncdb(self, *args, **kwargs):
        return None

    def allow_migrate(self, *args, **kwargs):
        return None
