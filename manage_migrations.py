import logging
from peewee_migrate import Router
from .backend.open_webui.apps.webui.internal.db import db

log = logging.getLogger(__name__)

def create_migration(name):
    migrate_dir = "open_webui/apps/webui/internal/migrations"
    router = Router(db, migrate_dir=migrate_dir)
    router.create(name)

def run_migrations():
    migrate_dir = "open_webui/apps/webui/internal/migrations"
    router = Router(db, migrate_dir=migrate_dir)
    router.run()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python manage_migrations.py <create|migrate> [migration_name]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "create":
        if len(sys.argv) < 3:
            print("Usage: python manage_migrations.py create <migration_name>")
            sys.exit(1)
        migration_name = sys.argv[2]
        create_migration(migration_name)
    elif command == "migrate":
        run_migrations()
    else:
        print("Unknown command")
        sys.exit(1)