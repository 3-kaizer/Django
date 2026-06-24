try:
	from django.contrib import admin  # type: ignore
except Exception:  # Fallback for environments without Django available
	class _StubAdminSite:
		def register(self, *args, **kwargs):
			return None

	admin = _StubAdminSite()

# Register your models here.
