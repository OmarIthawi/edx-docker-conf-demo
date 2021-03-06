from ..devstack import *

# Load module store settings from config files
update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)

# Set uploaded media file path
MEDIA_ROOT = "/openedx/data/uploads/"

# Deactivate forums
FEATURES['ENABLE_DISCUSSION_SERVICE'] = False

FEATURES.update({
    'AUTOMATIC_AUTH_FOR_TESTING': False,
    'ENABLE_COURSEWARE_SEARCH': False,
    'ENABLE_COURSE_DISCOVERY': False,
    'ENABLE_DASHBOARD_SEARCH': False,
    'ENABLE_DISCUSSION_SERVICE': False,
    'SHOW_HEADER_LANGUAGE_SELECTOR': False
})

SEARCH_ENGINE = "search.tests.mock_search_engine.MockSearchEngine"

# Activate dev_env for logging, otherwise rsyslog is required (but it is
# not available in docker).
LOGGING = get_logger_config(LOG_DIR,
                            logging_env=ENV_TOKENS['LOGGING_ENV'],
                            debug=False,
                            dev_env=True,
                            service_variant=SERVICE_VARIANT)

# Create folders if necessary
import os
for folder in [LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE]:
    if not os.path.exists(folder):
        os.makedirs(folder)
