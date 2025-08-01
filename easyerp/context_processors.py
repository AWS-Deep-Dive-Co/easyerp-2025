# Context processors for EasyERP
from .version import VERSION, BUILD_DATE, BUILD_NUMBER, DESCRIPTION, AUTHOR

def version_info(request):
    """Make version information available in all templates"""
    return {
        'app_version': VERSION,
        'app_build_date': BUILD_DATE,
        'app_build_number': BUILD_NUMBER,
        'app_description': DESCRIPTION,
        'app_author': AUTHOR,
    }
