[app]

# (str) Title of your application
title = F9 Sovereign App

# (str) Package name
package.name = f9sovereign

# (str) Package domain (needed for android packaging)
package.domain = org.f9.sovereign

# (list) Source files to include (let it include python files and engines)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) List of inclusion & exclusion patterns in your project
source.include_patterns = assets/*,*.py

# (list) Application requirements
# طالما مشروعنا فيه بايثون وKivy وسيرفرات وأدوات، دي الحزم الأساسية للتجميع
requirements = python3,kivy,openssl,requests,urllib3,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Python main application
android.app_name = F9 Sovereign

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
bin_dir = ./bin
